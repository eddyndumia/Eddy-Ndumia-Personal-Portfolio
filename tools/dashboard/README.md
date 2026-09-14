# Portfolio Dashboard

A small local-only admin tool for editing this site's content and pushing
changes, without hand-editing markdown/TOML or typing git commands.

No dependencies — plain Node.js stdlib. Never exposed beyond your machine
(binds to 127.0.0.1 only).

## Run it

```bash
cd tools/dashboard
node server.js
```

Then open http://127.0.0.1:4321

## What it does

- **About** — edit the homepage profile subtitle and the full `/bio/` page.
- **Projects** — add, edit, or delete entries under `/projects/`.
- **Resume page** — edit the raw markdown behind `/resume/` (the PDF embed).
- **Push** — shows `git status`, lets you commit with a message, and push to
  the remote — all from the browser instead of the terminal.

This tool itself lives under `tools/` and is never picked up by the Hugo
build (`hugo` only reads `content/`, `layouts/`, `static/`, `themes/`,
`config.toml`), so it ships with the repo but never appears on the live site.
