# Session 1 — Structure, Text, Links & Media

**Duration**: ~5 hours — **Goal**: write a complete, valid, accessible page from memory and navigate it correctly.

**Display format**: each topic has **Slides** (bullets for the slide), **Code** (shown on screen / demoed live), and **Talk track** (what the instructor says out loud). This mirrors the `build_html.py` deck: bullets become `slide_content`, code becomes `slide_code`, and the talk track becomes `notes=`.

---

## 1. How HTML Works

### Slides

- HTML is a **vocabulary for describing what a thing is**, not what it looks like
- The browser reads HTML and builds a **tree of objects** (the DOM), then paints that tree
- `<h1>` means "this is the main heading" — not "this is 32px bold"
- CSS answers *how does it look*; HTML answers *what is it*
- Get this backwards and you end up styling paragraphs because you could not find a heading element
- **Fault-tolerant**: parse errors are recoverable — wrong elements are not

### Code

```text
  .html  →  parse  →  DOM tree  →  render  →  layout  →  paint
  bytes      tokens      objects     boxes      positions  pixels
```

```html
<!-- The browser fixes this and gives you a page you did not design -->
<h1>My Page
<p>Welcome
```

### Mandatory head — every file starts with this

> **This is slide 1 of the session.** Every HTML file you write from now on — exercises, homework, projects, demos — must contain this head. No exceptions.

- **`<meta charset="UTF-8">`** — encoding. Without it, Arabic and emoji break.
- **`<meta name="viewport" content="width=device-width, initial-scale=1.0">`** — mobile. Without it, phones show a zoomed-out desktop layout.
- **`<title>`** — the tab, the bookmark, the search headline. Never leave it empty.
- **`lang` on `<html>`** — screen-reader pronunciation and hyphenation.
- These four are the **minimum viable head**. Everything else is an upgrade you add later.

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Page title goes here</title>
</head>
```

> **Rule for the whole course:** a document without `charset`, viewport, and a non-empty `<title>` is not submission-ready. The validator and the assessment both check for it.

### Talk track

> The most common beginner bug is reaching for a `<div>` because "I need it big and bold", instead of an `<h1>`. We frame the whole session around meaning-first, styling-second.
>
> Analogy: HTML is the **label on a shipping box**, not the paint colour. Nobody at the warehouse cares what colour the box is; they care that it says FRAGILE in the right place.
>
> Only explain the flow diagram this far — students do not need script blocking or the critical rendering path yet. The takeaway is the last line: HTML is fault-tolerant, which is a blessing while learning and a curse when shipping. A typo does not error, it just gives you something else. That is exactly why the W3C validator is part of the assessment.
>
> Close the first slide on the **mandatory head**: charset, viewport, title, and `lang`. Say it explicitly — every file they hand in for the rest of the course must carry these. We will unpack each one under Document Structure, but the rule starts here.

---

## 2. Document Structure

### Slides

- `<!DOCTYPE html>` must be the **first line** — it puts the browser in standards mode
- Three required parts: `<html>`, `<head>` (metadata), `<body>` (visible content)
- **`<head>` is for the browser; `<body>` is for the human** — this one idea explains the split
- Root attributes: `lang` (language) and `dir` (text direction — `ltr` / `rtl`)
- The `<head>` holds machine-readable information: character encoding, viewport, title, description, icons, stylesheets, preloads
- The `<body>` holds everything the visitor actually sees and interacts with
- `<meta charset="UTF-8">`, the viewport meta, and `<title>` are the three head tags you cannot ship without
- `<link>`, `<style>`, `<script>`, `<base>`, and `<noscript>` also live in the head
- Parent / child relationships — nested elements form a tree

### Head vs Body — what goes where

- **`<head>`** — *metadata*. Nothing here is drawn on the page. It tells the browser, search engines, and social networks about the document before a single pixel is painted.
  - Character encoding, the viewport, the title, the description, icons, stylesheets, scripts, and resource hints
- **`<body>`** — *content*. Every element the user sees, reads, clicks, or focuses lives here.
  - Headings, paragraphs, images, links, lists, forms, and the landmarks (`header`, `nav`, `main`, `footer`)
- Rule of thumb: **if you can see it, it belongs in the body.** If it only affects how the page is loaded, described, or styled, it belongs in the head.

### Inside `<head>` — the tags in detail

| Tag | What it does | Why it matters |
| --- | --- | --- |
| `<title>` | The document title | Browser tab, bookmark name, search-result headline. **Required.** |
| `<meta charset="UTF-8">` | Declares the character encoding | Without it, non-Latin text and Arabic can render as garbage. Must be early in the head. |
| `<meta name="viewport" ...>` | Sets the viewport for mobile | Without it, phones render the desktop layout zoomed out. **Required for mobile.** |
| `<meta name="description" ...>` | A short page summary | Search engines may use it as the snippet under your result. |
| `<meta name="author" ...>` | Who wrote the page | Lightweight attribution metadata. |
| `<meta property="og:*">` | Open Graph tags | Control the title, description, and image when the link is shared on social media. |
| `<link rel="stylesheet">` | Attaches an external CSS file | How styles get into the page. |
| `<link rel="icon">` | The favicon | The little image in the browser tab. |
| `<link rel="preconnect">` / `preload` | Resource hints | Start connecting to, or fetching, critical resources earlier. |
| `<base href="...">` | Sets a base URL for all relative links | Powerful and almost always the wrong tool — fix the folder structure instead. |
| `<style>` | Inline CSS for the page | Convenient in demos, a maintenance problem in real projects. |
| `<script defer>` | JavaScript for the page | Usually in the head with `defer` so it runs after the DOM is parsed. |
| `<noscript>` | Fallback content | Shown when JavaScript is disabled. Graceful degradation. |

### Code

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <!-- ---- metadata: for the browser, never drawn on the page ---- -->
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="A short summary of the page." />
    <meta name="author" content="Nour Hassan" />
    <meta property="og:title" content="My Page" />
    <meta property="og:image" content="https://example.com/preview.png" />
    <title>My Page</title>
    <link rel="icon" href="favicon.ico" />
    <link rel="stylesheet" href="styles.css" />
    <link rel="preconnect" href="https://fonts.example.com" />
    <script src="app.js" defer></script>
    <noscript>This site needs JavaScript enabled.</noscript>
  </head>
  <body>
    <!-- ---- content: everything the visitor sees ---- -->
    <header>
      <h1>Hello</h1>
      <nav>
        <ul>
          <li><a href="#about">About</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <p>This is the part of the document a human actually reads.</p>
    </main>
  </body>
</html>
```

### Talk track

> Walk the skeleton slowly, and make the **head/body split** the anchor. Say it plainly: the head is a set of instructions *about* the page, the body is the page. Nothing in the head is ever painted — if a student puts an `<h1>` in the head, the browser will not show it, and that surprise teaches the split better than any slide.
>
> `<!DOCTYPE html>` is not a tag, it is a mode switch — forget it and the browser falls back to quirks mode.
>
> In the head, drill the three non-negotiables: **`charset`** (or Arabic and emoji break), **viewport** (or mobile is unusable), and **`title`** (or your tab and search result are blank). Everything else — description, Open Graph, icons, preloads — is an improvement you add once the basics are right.
>
> `lang` and `dir` are the two attributes people skip and later regret: `lang` drives screen-reader pronunciation and hyphenation, `dir` is what makes Arabic pages lay out right.
>
> `<base>` — if a student reaches for it, ask what problem it solves; the answer is almost always "fix the folder structure instead".
>
> `<script>` in the head: mention `defer` so it runs after the DOM is parsed. We go deeper on ordering when we reach JavaScript — for now, `defer` is the safe default.

---

## 3. Tags, Elements & Attributes

### Slides

- **Tag** = the markup (`<p>`), **element** = opening tag + content + closing tag, **content** = what is between
- **Void elements** have no closing tag: `img`, `br`, `hr`, `input`, `meta`, `link`
- Attribute syntax: `name="value"` — always quote the value
- **Boolean attributes** need no value: `required`, `disabled`, `checked`
- Case sensitivity: write everything **lowercase** — HTML is forgiving, XHTML-style habits are not

### Code

```html
<!-- element = opening tag + content + closing tag -->
<p>Hello, world.</p>

<!-- void elements: no closing tag -->
<img src="cat.jpg" alt="A cat" />
<br />
<input type="text" name="email" />

<!-- boolean attributes -->
<input type="checkbox" checked />
<button disabled>Can't click me</button>
```

### Talk track

> The tag-vs-element distinction trips people up in interviews and in reading spec language. Use the shipping-box analogy again: the tag is the label template, the element is the whole box.
>
> Void elements: if a student writes `<img></img>`, the browser survives it but the validator complains. Better to learn it right first.

---

## 4. Text Content

### Slides

- Comments `<!-- -->` — for notes to yourself, not for hiding code
- Headings `<h1>`–`<h6>` form an **outline**; use one `h1`, never skip levels for styling
- Paragraphs `<p>` — inline content only, no block elements inside
- `<br>` vs `&nbsp;` vs a new block element — each means something different
- Formatting: `<strong>` (importance), `<em>` (stress), `<small>`, `<mark>`, `<del>`
- `<pre>` and `<code>` for code and preserved whitespace
- `<abbr>`, `<cite>`, `<q>`, `<dfn>` for references and definitions

### Code

```html
<h1>Main heading</h1>
<h2>Section</h2>
<h3>Subsection</h3>

<p>A paragraph with <strong>important</strong> and <em>emphasised</em> text.</p>

<p>The price is 100&nbsp;EGP <small>(including tax)</small>.</p>

<pre><code>const x = 1;</code></pre>

<p><abbr title="HyperText Markup Language">HTML</abbr> is <dfn>markup</dfn>.</p>
```

### Talk track

> The heading outline is the single easiest accessibility win. Open the accessibility tree in DevTools and show that the headings literally become a navigable list — skip a level and the outline breaks.
>
> `<b>` and `<i>` are not wrong, but they carry no meaning. `<strong>` and `<em>` do. Prefer meaning.

---

## 5. Links

### Slides

- The `href` attribute — the whole point of the web
- **Absolute** vs **relative** paths
- Internal links and fragment links (`#id`) for same-page navigation
- `target="_blank"` — always pair with `rel="noopener noreferrer"` (security + performance)
- Special schemes: `mailto:`, `tel:`, `sms:`
- The `download` attribute
- The **"fake link" anti-pattern**: a `<div>` or `<a href="#">` that looks clickable but is not

### Code

```html
<!-- absolute -->
<a href="https://example.com/about">About</a>

<!-- relative -->
<a href="./about.html">About</a>
<a href="../index.html">Home</a>

<!-- fragment / same page -->
<a href="#pricing">Jump to pricing</a>

<!-- new tab, done safely -->
<a href="https://example.com" target="_blank" rel="noopener noreferrer">External</a>

<!-- special schemes -->
<a href="mailto:hi@example.com">Email us</a>
<a href="tel:+201234567890">Call us</a>

<!-- download -->
<a href="menu.pdf" download>Download the menu</a>
```

### Talk track

> Lead with `target="_blank"` security: without `rel="noopener"`, the opened page gets a handle on `window.opener` and can redirect your tab. Modern browsers mostly protect you, but write it anyway — it is cheap and correct.
>
> The fake-link anti-pattern is everywhere in student code. A link that goes nowhere is worse than no link: screen readers announce it, keyboards tab to it, and nothing happens.

---

## 6. Paths & File Structure

### Slides

- `./` = this folder, `../` = one folder up
- **Absolute paths from the project root** (`/style.css`) break when the site is not at the domain root
- Relative paths keep the project portable
- Recommended folder structure: one `assets/` for images/css/js
- `index.html` is the default document the server serves

### Code

```text
project/
├── index.html
├── about/
│   └── team.html
├── assets/
│   ├── css/style.css
│   └── img/logo.png
```

```html
<!-- from project/index.html -->
<img src="assets/img/logo.png" alt="Logo" />
<a href="about/team.html">Team</a>

<!-- from project/about/team.html -->
<img src="../assets/img/logo.png" alt="Logo" />
<a href="../index.html">Home</a>
```

### Talk track

> Draw the tree on the board and trace `../` out loud, one folder at a time. This is the topic where visual learners suddenly get it.
>
> Rule of thumb: **never start a path with `/`** unless you know the site is served from the domain root. Relative paths travel with the project.

---

## 7. Images

### Slides

- `<img>` and the **required `alt`**
- Meaningful alt text vs **decorative** images (`alt=""`)
- `width` and `height` — how they prevent layout shift
- `loading="lazy"` and `decoding="async"`
- `srcset` + `sizes` for responsive images
- `<picture>` — when it beats `srcset` alone (art direction / format fallback)
- Formats: JPEG, PNG, WebP, AVIF, SVG
- Inline SVG vs an image file

### Code

```html
<img src="cat.jpg" alt="A grey cat asleep on a keyboard" width="640" height="480" />

<!-- decorative: empty alt, no announcement -->
<img src="divider.svg" alt="" />

<!-- lazy loading below the fold -->
<img src="photo.jpg" alt="Team offsite" loading="lazy" decoding="async" />

<!-- responsive -->
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="Team offsite"
/>

<!-- art direction / modern format with fallback -->
<picture>
  <source srcset="photo.avif" type="image/avif" />
  <source srcset="photo.webp" type="image/webp" />
  <img src="photo.jpg" alt="Team offsite" />
</picture>
```

### Talk track

> Alt text is the most important line in this session. Two failure modes: **missing alt** (screen reader reads the filename) and **useless alt** ("image of a cat" instead of "a grey cat asleep on a keyboard").
>
> Decorative images get `alt=""` — an empty string, not a missing attribute. That tells the screen reader to skip it entirely.
>
> `width` and `height` are not for sizing — they let the browser reserve space before the image loads, which is how you avoid layout shift.

---

## 8. Lists

### Slides

- `<ul>` for unordered, `<ol>` for ordered — plus `start`, `reversed`, `value`
- Nested lists — indentation comes for free
- Description lists `<dl>`, `<dt>`, `<dd>`
- A list is often the right element for **navigation**

### Code

```html
<ul>
  <li>Flour</li>
  <li>Sugar
    <ul>
      <li>Brown</li>
      <li>White</li>
    </ul>
  </li>
</ul>

<ol start="3" reversed>
  <li>Third</li>
  <li>Second</li>
  <li>First</li>
</ol>

<dl>
  <dt>HTML</dt>
  <dd>The structure of a page.</dd>
  <dt>CSS</dt>
  <dd>The presentation of a page.</dd>
</dl>
```

### Talk track

> Show that a `<nav>` is really a list of links — that is why `<ul>` inside `<nav>` is the standard pattern, and why we do not reach for `<div>` there.
>
> Nested lists are a great first taste of the tree idea from topic 2.

---

## Recap / Checkpoints

- HTML describes **meaning**, CSS describes **appearance**
- A valid document has a doctype, `<html lang dir>`, `<head>`, and `<body>`
- `<head>` = instructions for the browser (charset, viewport, title, links, scripts); `<body>` = what the human sees
- The three head tags you cannot ship without: `charset`, viewport, and `<title>`
- **Mandatory in every file, no exceptions**: `charset`, viewport, non-empty `<title>`, and `lang` on `<html>`
- Use semantic elements for text; one `h1`, no skipped levels
- Links: relative paths, safe `target="_blank"`, no fake links
- Images: always `alt`, empty alt when decorative
- Lists are structure, not just bullets
