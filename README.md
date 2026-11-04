# jcm.

My small static professional website. Plain HTML, CSS and JavaScript, with no build dependencies.

## Structure

- `site/index.html`: homepage, styles and interactions.
- `site/cv/index.html`: redirect to the CV PDF.
- `site/cv/Jonathan-Carson-McGeary-CV.pdf`: tagged CV download.
- `site/favicon.svg` and `site/favicon-dark.svg`: theme aware favicons.

## Updating the CV

Edit `scripts/cv-source.html`, then run `python3 scripts/export-cv-pdf.py` with LibreOffice's `soffice` command on your PATH. Check the regenerated PDF's layout and tag order before committing it.

## Deployment

GitHub Actions deploys `site/` to GitHub Pages on pushes to `main`.
