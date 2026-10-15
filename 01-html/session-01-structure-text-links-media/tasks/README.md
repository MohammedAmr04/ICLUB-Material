# Session 1 — Tasks

Exercises for **HTML Session 1 — Structure, Text, Links & Media**.

Each task maps to a topic in `../content.md`. Work through them in order — they build toward the Personal Profile Page.

| # | Task | Topic | Type |
| --- | --- | --- | --- |
| 01 | Pick the right element | How HTML Works | Written |
| 02 | Minimal document from memory | Document Structure | Code |
| 03 | Fix the syntax | Tags, Elements & Attributes | Code |
| 04 | Mark up plain text | Text Content | Code |
| 05 | Build a nav + special links | Links | Code |
| 06 | Resolve the paths | Paths & File Structure | Written / Code |
| 07 | Images done right | Images | Code |
| 08 | Lists in three flavours | Lists | Code |
| 09 | Fix three broken documents | Whole session | Debugging |

Reference solutions live in [`solutions/`](./solutions/).

## How to submit

- Put each task in its own file, e.g. `task-02.html`.
- **Every file must carry the mandatory head**: `<meta charset="UTF-8">`, the viewport meta, a non-empty `<title>`, and `lang` on `<html>`. No exceptions — a file without these is not submission-ready.
- Run every HTML file through the [W3C validator](https://validator.w3.org/#validate_by_input) before submitting.
- Zero validator errors is the bar for every code task.

---

## Task 01 — Pick the right element

For each description, write the element you would reach for. Then write one sentence explaining why.

1. The name of the site, at the top of every page.
2. A quote from a customer.
3. The main navigation links.
4. A short aside that is related but not essential.
5. A paragraph of body copy.
6. A word inside a sentence that is important.
7. A clickable phone number.

**Acceptance**: every answer is a semantic element, not `div` or `span`.

---

## Task 02 — Minimal document from memory

Without looking at the notes, write a complete, valid HTML5 document that:

- declares the doctype
- sets the language to English
- sets the text direction to left-to-right
- declares UTF-8
- declares the viewport for mobile
- has a page title of `My First Page`
- has one `h1` that says `Hello, HTML`
- has one paragraph of your choice

Then, in a sentence each, explain: **what belongs in `<head>` vs `<body>`, and why.** Name at least three tags that live in the head and what each one does.

**Deliverable**: `task-02.html`

**Acceptance**: passes the W3C validator with zero errors; `charset` is present.

---

## Task 03 — Fix the syntax

The snippet below has **six** mistakes. Fix all of them.

```html
<html>
  <body>
    <img src="cat.jpg"></img>
    <input type=text name=email>
    <p>This is <b>bold</b> and <I>italic</I>
    <hr>
    <A href="/about">About</A>
  </body>
</html>
```

**Deliverable**: `task-03.html`

**Acceptance**: no void element has a closing tag; every attribute value is quoted; elements are lowercase; the unclosed `<p>` is closed.

---

## Task 04 — Mark up plain text

Turn the following plain text into correct HTML. Choose headings, paragraphs, and inline formatting yourself.

```text
Ahmed's Coffee Guide

Ahmed has been roasting coffee since 2010. He says the water temperature matters more than the bean.

Brewing notes

Always use a 1 to 16 ratio. This is critical, not optional.
The grind should be consistent.

The cost is 80 EGP per bag, including tax.

Ahmed's favourite tool is the Hario V60.
```

**Deliverable**: `task-04.html`

**Acceptance**: one `h1`; heading levels never skip; `strong` used for the genuinely important statement; `small` used for the tax note; no `<br>` used to fake paragraph spacing.

---

## Task 05 — Build a nav + special links

Create a small page with:

1. A `<nav>` containing a list of four links (use `#` fragments for now).
2. One link to `https://developer.mozilla.org` that opens in a new tab, done safely.
3. A `mailto:` link.
4. A `tel:` link.
5. A fragment link that jumps to a section further down the page.

**Deliverable**: `task-05.html`

**Acceptance**: external new-tab link has `rel="noopener noreferrer"`; no link uses an empty `href` as a fake button.

---

## Task 06 — Resolve the paths

Given this project tree:

```text
shop/
├── index.html
├── contact/
│   └── index.html
└── assets/
    ├── css/site.css
    └── img/logo.png
```

Write the correct relative `src` or `href` **for each file below**:

1. `shop/index.html` linking to `site.css`.
2. `shop/index.html` loading `logo.png`.
3. `shop/contact/index.html` linking back to the homepage.
4. `shop/contact/index.html` loading `logo.png`.

Then answer: why would `href="/assets/css/site.css"` be a problem if this site were hosted in a subfolder like `example.com/shop/`?

**Deliverable**: `task-06.md` (or a `.html` file with the answers in a `<pre>`).

**Acceptance**: paths use `./` and `../` correctly; the written answer mentions that a leading `/` points at the domain root, not the project root.

---

## Task 07 — Images done right

Add four images to a page:

1. A meaningful photo with real alt text, plus `width` and `height`.
2. A purely decorative divider with the correct `alt`.
3. An image below the fold with lazy loading.
4. A responsive image using `srcset` and `sizes`.

**Deliverable**: `task-07.html` (placeholder file names are fine).

**Acceptance**: the decorative image uses `alt=""`, not a missing attribute; the meaningful image alt describes the image, not the word "image"; `srcset` has at least two candidates with `w` descriptors.

---

## Task 08 — Lists in three flavours

1. An unordered list of five groceries, with a nested sub-list under one item.
2. An ordered list that starts at `5` and counts **down**.
3. A description list defining three terms of your choice.
4. A `<nav>` that contains a list of links.

**Deliverable**: `task-08.html`

**Acceptance**: nested lists are inside the parent `<li>`; the ordered list uses `start` and `reversed`; nav links are wrapped in a list.

---

## Task 09 — Fix three broken documents

Three documents are broken in different ways. Find and fix every issue.

### Document A

```html
<!DOCTYPE html>
<html>
  <head><title>Broken A</title></head>
  <body>
    <h1>Welcome</h1>
    <h3>Skipped a level</h3>
  </body>
</html>
```

### Document B

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Broken B</title>
  </head>
  <body>
    <img src="team.jpg">
    <a href="https://example.com" target="_blank">Our team</a>
  </body>
</html>
```

### Document C

```html
<!DOCTYPE html>
<html lang="en">
  <head><meta charset="UTF-8"><title>Broken C</title></head>
  <body>
    <p>First line<br><br>Second line, spaced with breaks.</p>
    <ul><li>Item</li><ul><li>Nested outside its parent</li></ul></ul>
  </body>
</html>
```

**Deliverable**: `task-09-a.html`, `task-09-b.html`, `task-09-c.html`

**Acceptance**: A has a correct heading order; B has alt text and a safe external link; C uses block elements instead of `<br><br>` and nests the sub-list inside its parent `<li>`.
