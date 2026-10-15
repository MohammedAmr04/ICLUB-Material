# Task 06 — Solutions

1. `shop/index.html` → `assets/css/site.css`
2. `shop/index.html` → `assets/img/logo.png`
3. `shop/contact/index.html` → `../index.html`
4. `shop/contact/index.html` → `../assets/img/logo.png`

## Why `/assets/css/site.css` is a problem

A leading `/` means **the root of the domain**, not the root of the project. If
the site is hosted at `example.com/shop/`, then `/assets/css/site.css` resolves
to `example.com/assets/css/site.css` — one level too high — and the stylesheet
404s.

Relative paths (`assets/...`, `../index.html`) travel with the project, so they
keep working no matter where the folder is deployed.
