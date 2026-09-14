// Local-only admin dashboard for the portfolio repo.
// No dependencies beyond Node's stdlib — binds to 127.0.0.1 only.
const http = require('http');
const fs = require('fs/promises');
const path = require('path');
const { execFile } = require('child_process');

const REPO_ROOT = path.resolve(__dirname, '..', '..');
const CONFIG_PATH = path.join(REPO_ROOT, 'config.toml');
const BIO_PATH = path.join(REPO_ROOT, 'content', 'bio.md');
const RESUME_PATH = path.join(REPO_ROOT, 'content', 'resume.md');
const PROJECTS_DIR = path.join(REPO_ROOT, 'content', 'projects');
const PUBLIC_DIR = path.join(__dirname, 'public');
const PORT = process.env.PORT || 4321;

function run(cmd, args, cwd = REPO_ROOT) {
  return new Promise((resolve) => {
    execFile(cmd, args, { cwd, maxBuffer: 10 * 1024 * 1024 }, (err, stdout, stderr) => {
      resolve({ ok: !err, code: err ? err.code : 0, stdout: stdout || '', stderr: stderr || '' });
    });
  });
}

function splitFrontmatter(raw) {
  const m = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!m) return { frontmatter: '', body: raw };
  return { frontmatter: m[1], body: m[2] };
}

function parseFrontmatterFields(fm) {
  const fields = {};
  for (const line of fm.split(/\r?\n/)) {
    const m = line.match(/^(\w+):\s*(.*)$/);
    if (!m) continue;
    let val = m[2].trim();
    if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
    fields[m[1]] = val;
  }
  return fields;
}

function toSlug(title) {
  return title.toLowerCase().trim()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '') || 'untitled';
}

async function getSubtitle() {
  const raw = await fs.readFile(CONFIG_PATH, 'utf8');
  const m = raw.match(/^subtitle = "((?:[^"\\]|\\.)*)"/m);
  return m ? m[1].replace(/\\"/g, '"') : '';
}

async function setSubtitle(newSubtitle) {
  const raw = await fs.readFile(CONFIG_PATH, 'utf8');
  const escaped = String(newSubtitle).replace(/\\/g, '\\\\').replace(/"/g, '\\"');
  const updated = raw.replace(/^subtitle = "(?:[^"\\]|\\.)*"/m, `subtitle = "${escaped}"`);
  await fs.writeFile(CONFIG_PATH, updated, 'utf8');
}

async function listProjects() {
  const files = (await fs.readdir(PROJECTS_DIR)).filter(f => f.endsWith('.md') && f !== '_index.md');
  const projects = [];
  for (const file of files) {
    const raw = await fs.readFile(path.join(PROJECTS_DIR, file), 'utf8');
    const { frontmatter, body } = splitFrontmatter(raw);
    const fields = parseFrontmatterFields(frontmatter);
    projects.push({
      slug: file.replace(/\.md$/, ''),
      title: fields.title || '',
      summary: fields.summary || '',
      date: fields.date || '',
      body: body.trim(),
    });
  }
  projects.sort((a, b) => (a.date < b.date ? 1 : -1));
  return projects;
}

async function saveProject({ slug, title, summary, date, body }) {
  const finalSlug = slug || toSlug(title);
  const fm = [
    '---',
    `title: "${String(title).replace(/"/g, '\\"')}"`,
    `summary: "${String(summary).replace(/"/g, '\\"')}"`,
    `date: ${date || new Date().toISOString().slice(0, 10)}`,
    '---',
    '',
  ].join('\n');
  await fs.writeFile(path.join(PROJECTS_DIR, `${finalSlug}.md`), fm + body.trim() + '\n', 'utf8');
  return finalSlug;
}

async function deleteProject(slug) {
  const p = path.join(PROJECTS_DIR, `${slug}.md`);
  await fs.unlink(p);
}

async function gitStatus() {
  const [status, branch] = await Promise.all([
    run('git', ['status', '--porcelain']),
    run('git', ['rev-parse', '--abbrev-ref', 'HEAD']),
  ]);
  return {
    branch: branch.stdout.trim(),
    changes: status.stdout.split('\n').filter(Boolean),
  };
}

const routes = {
  'GET /api/data': async () => {
    const [subtitle, bioRaw, resumeRaw, projects, git] = await Promise.all([
      getSubtitle(),
      fs.readFile(BIO_PATH, 'utf8'),
      fs.readFile(RESUME_PATH, 'utf8'),
      listProjects(),
      gitStatus(),
    ]);
    const bio = splitFrontmatter(bioRaw);
    return { subtitle, bioBody: bio.body.trim(), resumeRaw, projects, git };
  },
  'POST /api/subtitle': async (body) => {
    await setSubtitle(body.subtitle);
    return { ok: true };
  },
  'POST /api/bio': async (body) => {
    const raw = await fs.readFile(BIO_PATH, 'utf8');
    const { frontmatter } = splitFrontmatter(raw);
    const updated = `---\n${frontmatter}\n---\n\n${body.body.trim()}\n`;
    await fs.writeFile(BIO_PATH, updated, 'utf8');
    return { ok: true };
  },
  'POST /api/resume': async (body) => {
    await fs.writeFile(RESUME_PATH, body.raw, 'utf8');
    return { ok: true };
  },
  'POST /api/projects': async (body) => {
    const slug = await saveProject(body);
    return { ok: true, slug };
  },
  'POST /api/projects/delete': async (body) => {
    await deleteProject(body.slug);
    return { ok: true };
  },
  'POST /api/git/commit': async (body) => {
    await run('git', ['add', '-A']);
    const msg = (body.message || '').trim() || 'Update portfolio content';
    const res = await run('git', ['commit', '-m', msg]);
    return { ok: res.ok, output: res.stdout + res.stderr };
  },
  'POST /api/git/push': async () => {
    const res = await run('git', ['push']);
    return { ok: res.ok, output: res.stdout + res.stderr };
  },
};

const MIME = { '.html': 'text/html', '.js': 'application/javascript', '.css': 'text/css' };

async function serveStatic(req, res) {
  let filePath = req.url === '/' ? '/index.html' : req.url;
  filePath = path.join(PUBLIC_DIR, filePath);
  if (!filePath.startsWith(PUBLIC_DIR)) { res.writeHead(403); res.end(); return; }
  try {
    const data = await fs.readFile(filePath);
    const ext = path.extname(filePath);
    res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
    res.end(data);
  } catch {
    res.writeHead(404);
    res.end('Not found');
  }
}

const server = http.createServer(async (req, res) => {
  const key = `${req.method} ${req.url.split('?')[0]}`;
  const handler = routes[key];
  if (!handler) return serveStatic(req, res);

  let body = {};
  if (req.method === 'POST') {
    const chunks = [];
    for await (const chunk of req) chunks.push(chunk);
    try { body = JSON.parse(Buffer.concat(chunks).toString('utf8') || '{}'); } catch { body = {}; }
  }
  try {
    const result = await handler(body);
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(result));
  } catch (err) {
    res.writeHead(500, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ ok: false, error: err.message }));
  }
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`Portfolio dashboard running at http://127.0.0.1:${PORT}`);
});
