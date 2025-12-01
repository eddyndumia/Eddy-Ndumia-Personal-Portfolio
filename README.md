# Personal Website / Portfolio

Personal portfolio built with Hugo + PaperMod theme. (I like to keep things simple)

## Pages
- Home (profile + intro)
- Projects
- Bio
- Resume (PDF viewer) -- this is actually a native reader
- Blog

## Local Development

```bash
# Clone and setup
git clone <repo-url>
cd personal-site
git submodule update --init --recursive

# Run locally
hugo server -D
```

## Production Build

```bash
hugo --minify
```

## Cloudflare Pages Deployment

- Build command: `hugo`
- Output directory: `public`
- Hugo version: Latest