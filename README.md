# ndumia.netlify.app

My site. Projects, bio, resume and a blog. Hugo with the PaperMod theme, restyled to stay out of the way.

A few things I added on top: the resume reads right in the page (PDF.js, works on phones), posts have emoji reactions, and people can subscribe to get new posts by email.

```bash
git submodule update --init --recursive
hugo server -D
```

Deploys to GitHub Pages on every push, plus a daily rebuild at 6am Nairobi so posts dated ahead go live on their day. After a deploy, `tools/notify_subscribers.py` emails Buttondown subscribers about any new post. It needs `buttondownUser` in `config.toml` and a `BUTTONDOWN_API_KEY` repo secret, and skips quietly without them.

The resume PDF comes from `static/files/generate_resume.py`.
