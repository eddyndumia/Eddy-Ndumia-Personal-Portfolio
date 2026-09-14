async function api(path, body) {
  const res = await fetch(path, body ? {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  } : undefined);
  return res.json();
}

function flash(el, text, ok = true) {
  el.textContent = text;
  el.style.color = ok ? '#2f8f2f' : '#c0392b';
  setTimeout(() => { el.textContent = ''; }, 2500);
}

const projectsList = document.getElementById('projects-list');
const projectTemplate = document.getElementById('project-template');

function renderProject(p) {
  const node = projectTemplate.content.cloneNode(true);
  const root = node.querySelector('.project');
  root.dataset.slug = p.slug || '';
  root.querySelector('.p-title').value = p.title || '';
  root.querySelector('.p-date').value = p.date || '';
  root.querySelector('.p-summary').value = p.summary || '';
  root.querySelector('.p-body').value = p.body || '';

  root.querySelector('.p-save').addEventListener('click', async () => {
    const payload = {
      slug: root.dataset.slug || undefined,
      title: root.querySelector('.p-title').value,
      date: root.querySelector('.p-date').value,
      summary: root.querySelector('.p-summary').value,
      body: root.querySelector('.p-body').value,
    };
    const result = await api('/api/projects', payload);
    if (result.ok) {
      root.dataset.slug = result.slug;
      flash(root.querySelector('.p-status'), 'Saved');
    } else {
      flash(root.querySelector('.p-status'), 'Error', false);
    }
  });

  root.querySelector('.p-delete').addEventListener('click', async () => {
    if (!root.dataset.slug) { root.remove(); return; }
    if (!confirm(`Delete project "${root.querySelector('.p-title').value}"?`)) return;
    const result = await api('/api/projects/delete', { slug: root.dataset.slug });
    if (result.ok) root.remove();
  });

  projectsList.appendChild(node);
}

document.getElementById('add-project').addEventListener('click', () => {
  renderProject({ slug: '', title: '', date: new Date().toISOString().slice(0, 10), summary: '', body: '' });
});

async function loadAll() {
  const data = await api('/api/data');
  document.getElementById('subtitle').value = data.subtitle || '';
  document.getElementById('bio').value = data.bioBody || '';
  document.getElementById('resume').value = data.resumeRaw || '';

  projectsList.innerHTML = '';
  (data.projects || []).forEach(renderProject);

  renderGit(data.git);
}

function renderGit(git) {
  document.getElementById('git-summary').textContent =
    `branch: ${git.branch} — ${git.changes.length} uncommitted change(s)`;
  document.getElementById('changes-list').textContent =
    git.changes.length ? git.changes.join('\n') : '(clean)';
}

document.querySelectorAll('button[data-save]').forEach((btn) => {
  btn.addEventListener('click', async () => {
    const key = btn.dataset.save;
    const statusEl = document.getElementById(`status-${key}`);
    let result;
    if (key === 'subtitle') {
      result = await api('/api/subtitle', { subtitle: document.getElementById('subtitle').value });
    } else if (key === 'bio') {
      result = await api('/api/bio', { body: document.getElementById('bio').value });
    } else if (key === 'resume') {
      result = await api('/api/resume', { raw: document.getElementById('resume').value });
    }
    flash(statusEl, result.ok ? 'Saved' : 'Error', result.ok);
    const data = await api('/api/data');
    renderGit(data.git);
  });
});

document.getElementById('refresh-btn').addEventListener('click', loadAll);

document.getElementById('commit-btn').addEventListener('click', async () => {
  const message = document.getElementById('commit-message').value;
  const result = await api('/api/git/commit', { message });
  document.getElementById('git-output').textContent = result.output || (result.ok ? 'Committed' : 'Nothing to commit');
  const data = await api('/api/data');
  renderGit(data.git);
});

document.getElementById('push-btn').addEventListener('click', async () => {
  if (!confirm('Push committed changes to the remote now?')) return;
  const result = await api('/api/git/push');
  document.getElementById('git-output').textContent = result.output || (result.ok ? 'Pushed' : 'Push failed');
});

loadAll();
