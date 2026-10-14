# jcm.

A small static professional website for Jonathan Carson-McGeary. Plain HTML, CSS and JavaScript, with no build dependencies.

## Structure

- `site/index.html`: homepage, styles and interactions.
- `site/cv/index.html`: browser PDF viewer.
- `site/cv/Jonathan-Carson-McGeary-CV.pdf`: the single published CV PDF. Replace this file to update the CV.
- `site/favicon.svg` and `site/favicon-dark.svg`: theme-aware favicons.

## Local preview

Run `python3 -m http.server 8765 --directory site`, then open http://localhost:8765.

## Deployment

GitHub Actions deploys `site/` to GitHub Pages on pushes to `main`. You can also run the workflow manually. In repository Settings → Pages, select GitHub Actions as the source.

A custom domain can be configured in Pages settings. Verify ownership and enable HTTPS; preserve your email DNS records. No custom domain is configured in this repository yet.

Only public website assets belong here. Working notes and private source material are excluded.
