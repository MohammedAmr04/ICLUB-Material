# Session 2 — Forms, Semantics, Tables & Media

**Duration**: ~6 hours — **Goal**: build forms, meaningful page structure, and data-rich content — then ship the capstone.

**Display format**: each topic has **Slides** (bullets for the slide), **Code** (shown on screen / demoed live), and **Talk track** (what the instructor says out loud). This mirrors the `build_html.py` deck: bullets become `slide_content`, code becomes `slide_code`, and the talk track becomes `notes=`.

> **Mandatory head** (from Session 1): every full document in this session carries `<meta charset="UTF-8">`, the viewport meta, a non-empty `<title>`, and `lang` on `<html>`. Snippets that are fragments are labelled as such.

> **Important framing for the whole session**: HTML creates structure and built-in browser behaviour. A form will not save or send data to a real system unless its `action` points to a working backend (or JavaScript handles submission). Browser-side validation improves usability but never replaces server-side validation.

---

## 1. Forms & Inputs

### Slides

- A `<form>` **collects information** from a user and groups the controls submitted together
- The main element is `<form>`; the controls are `<input>`, `<textarea>`, `<select>`, and `<button>`
- Key attributes: `action` (where data goes), `method` (`get` / `post`), `name` (the submitted key), `id` (links a label)
- `required` asks the browser to enforce a value before submission
- `placeholder` is a hint — it is **not** a label
- Common input types cover most data: `text`, `email`, `password`, `number`, `tel`, `url`, `date`, `radio`, `checkbox`, `file`, `range`, `submit`, `reset`
- Extra attributes: `min`, `max`, `step`, `minlength`, `maxlength`, `pattern`, `checked`, `multiple`, `accept`, `autocomplete`
- `get` puts data in the URL; `post` sends it in the request body

### Code

Input types at a glance (fragment):

```html
<input type="text"     name="name"  />
<input type="email"    name="email" />
<input type="password" name="pw" />
<input type="number"   name="age" min="10" max="100" />
<input type="tel"      name="phone" />
<input type="url"      name="site" />
<input type="date"     name="dob" />
<input type="radio"    name="format" value="online" />
<input type="checkbox" name="terms" />
<input type="file"     name="cv" accept=".pdf" multiple />
<input type="range"    name="volume" min="0" max="10" />
<input type="submit"   value="Send" />
```

Full registration form (complete document — mandatory head included):

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Registration Form</title>
  </head>
  <body>
    <main>
      <h1>Course Registration</h1>

      <form action="/register" method="post">
        <div>
          <label for="full-name">Full name</label>
          <input
            type="text"
            id="full-name"
            name="fullName"
            autocomplete="name"
            required
            minlength="3"
          />
        </div>

        <div>
          <label for="email">Email</label>
          <input type="email" id="email" name="email" autocomplete="email" required />
        </div>

        <div>
          <label for="age">Age</label>
          <input type="number" id="age" name="age" min="10" max="100" />
        </div>

        <fieldset>
          <legend>Preferred learning format</legend>
          <label>
            <input type="radio" name="format" value="online" required />
            Online
          </label>
          <label>
            <input type="radio" name="format" value="onsite" />
            On-site
          </label>
        </fieldset>

        <div>
          <label for="track">Choose a track</label>
          <select id="track" name="track" required>
            <option value="">-- Choose one --</option>
            <option value="frontend">Front-end</option>
            <option value="backend">Back-end</option>
            <option value="uiux">UI/UX</option>
          </select>
        </div>

        <div>
          <label for="notes">Additional notes</label>
          <textarea id="notes" name="notes" rows="4"></textarea>
        </div>

        <label>
          <input type="checkbox" name="terms" required />
          I agree to the terms
        </label>

        <button type="submit">Register</button>
      </form>
    </main>
  </body>
</html>
```

### Talk track

> Walk the registration form and make five points out loud:
> 1. `<form>` groups the controls that get submitted together.
> 2. `label[for]` **must** match the control's `id` — this is the one accessibility rule that matters most.
> 3. `name`, not `id`, is what becomes the submitted field name. `id` identifies an element in the document; `name` identifies the data.
> 4. Radio options for one question **share the same `name`** — that is what makes them mutually exclusive.
> 5. `required`, `min`, and `minlength` are the browser's built-in validation; leave a required field empty live and let the browser complain.
>
> Be blunt about `/register`: it is an example endpoint. With no backend route, nothing is actually saved. Do not let students think HTML alone submits data anywhere.
>
> GET vs POST: GET is for searches where the query belongs in the URL; never put passwords or sensitive data in GET. POST is for creating or changing data — but POST does **not** encrypt anything, you still need HTTPS, and neither method replaces server-side validation or authorization.

---

## 2. Form Controls

### Slides

- Form controls are the interactive fields users type in or select from
- `<input>` — many types of short or specialized data
- `<textarea>` — multi-line text
- `<select>` + `<option>` — drop-down list
- `<button>` — an actionable button
- `<fieldset>` + `<legend>` — group related controls and name the group
- `<datalist>` — suggestions for a text input
- `<output>` — the result of a calculation or user action
- **Good practice**: every control gets a visible label; use the input type that fits the data; group radios and related checkboxes; never use placeholder as the only label
- `disabled` controls are **not submitted**; `readonly` controls **are** submitted
- `button type="button"` is for a button that must not submit the form

### Code

Several controls together (fragment):

```html
<form>
  <label for="search">Search courses</label>
  <input type="search" id="search" name="q" list="course-options" />

  <datalist id="course-options">
    <option value="HTML"></option>
    <option value="CSS"></option>
    <option value="JavaScript"></option>
  </datalist>

  <label for="level">Level</label>
  <select id="level" name="level">
    <option value="beginner">Beginner</option>
    <option value="intermediate">Intermediate</option>
    <option value="advanced">Advanced</option>
  </select>

  <button type="submit">Search</button>
  <button type="button">Clear</button>
</form>
```

### Talk track

> The whole topic is really one idea: **match the control to the data**. `tel` gives a numeric keypad on mobile; `email` gets basic format checking; `date` gets a picker. Choosing right is most of the accessibility work.
>
> `datalist` is a suggestion list, not a constraint — the browser still lets the user type anything. Contrast that with `<select>`, which restricts.
>
> `disabled` vs `readonly` is a favourite interview question: disabled fields are skipped on submit and unreachable by keyboard; readonly fields are read, submitted, and focusable. Pick based on whether the value should be sent.
>
> Close on the security line: front-end validation is a convenience for honest users, not a security control. A determined user can bypass everything in the browser.

---

## 3. Semantics & Structure

### Slides

- Semantic HTML means choosing elements for their **meaning**, not their default look
- It helps **four audiences**: browsers, search engines, screen readers, and other developers
- Structural elements: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`
- Rich content elements: `<figure>` + `<figcaption>`, `<address>`, `<time>`
- `<main>` is the primary content — normally **one per page**
- `<article>` stands on its own; `<section>` is a thematic grouping, usually with a heading
- `<div>` is a generic container — fine when nothing more meaningful fits; `<span>` is its inline cousin
- Never pick an element because it "looks right" — CSS controls presentation
- **Common mistake**: `<div>` for everything, or headings used only to make text larger

### Code

A semantic page (complete document — mandatory head included):

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Learn Web Development</title>
  </head>
  <body>
    <header>
      <p>Web Academy</p>
      <nav aria-label="Main navigation">
        <ul>
          <li><a href="#courses">Courses</a></li>
          <li><a href="#about">About</a></li>
        </ul>
      </nav>
    </header>

    <main>
      <section id="courses">
        <h1>Learn Web Development</h1>
        <p>Start with HTML, then continue to CSS and JavaScript.</p>

        <article>
          <h2>HTML Basics</h2>
          <p>Learn how to structure web content.</p>
        </article>
      </section>

      <aside>
        <h2>Tip</h2>
        <p>Practice each example in a separate HTML file.</p>
      </aside>
    </main>

    <footer>
      <address>Contact: <a href="mailto:hello@example.com">hello@example.com</a></address>
    </footer>
  </body>
</html>
```

### Talk track

> Frame the "three audiences" — browsers, screen readers, search engines — and add the fourth: the developer who inherits the page. A page built from `<div>` and `<span>` gives all four nothing to work with.
>
> Open the accessibility tree in DevTools on a semantic page, then on a div-soup page. The landmarks (`banner`, `navigation`, `main`, `contentinfo`) appear and disappear. That demo lands better than any slide.
>
> `article` vs `section` — the test is "could this stand alone?" A blog post, a product card: `article`. A themed cluster of related content with a heading: `section`. If neither clearly fits, a `div` with a class is honest.
>
> Warn about the opposite sin too: nothing wrong with a `div` when there is no meaning to convey. Semantic HTML does not mean "no divs ever".

---

## 4. Tables

### Slides

- Use a table only for **tabular data** — rows and columns of related values
- Never use a table to lay out a whole page — that is CSS's job (Flexbox / Grid)
- Elements: `<table>`, `<caption>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th>`, `<td>`
- `<caption>` names the table — always worth adding when it helps
- `scope="col"` / `scope="row"` tell assistive tech which cells a header describes
- `colspan` and `rowspan` make a cell span multiple columns or rows — use only when the data needs it
- Use `<th>` for headers, not bolded `<td>`s
- HTML alone does not make a wide table mobile-friendly — that needs a scroll container or responsive CSS

### Code

A class schedule (fragment, shown inside a page body):

```html
<table>
  <caption>Weekly Web Development Schedule</caption>

  <thead>
    <tr>
      <th scope="col">Day</th>
      <th scope="col">Topic</th>
      <th scope="col">Duration</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <th scope="row">Saturday</th>
      <td>HTML Forms</td>
      <td>60 minutes</td>
    </tr>
    <tr>
      <th scope="row">Sunday</th>
      <td>HTML Tables</td>
      <td>45 minutes</td>
    </tr>
    <tr>
      <th scope="row">Monday</th>
      <td>Audio and Video</td>
      <td>45 minutes</td>
    </tr>
  </tbody>

  <tfoot>
    <tr>
      <th scope="row" colspan="2">Total learning time</th>
      <td>150 minutes</td>
    </tr>
  </tfoot>
</table>
```

### Talk track

> The one rule that matters: **tables are for data, not layout**. If a student has ever seen a 2005-era site built from nested tables, this is why that is a red flag.
>
> The `scope` attribute is invisible but big: without it, a screen reader reading a cell has to guess whether "45 minutes" is under Day or Topic. `scope` removes the guess.
>
> Walk `thead` / `tbody` / `tfoot` as a way to group rows — it also gives you stable CSS hooks later, so you never need a class on every cell.
>
> Finish on the honesty note: the table renders fine on desktop and breaks on a phone. HTML gave you the structure; making it responsive is a CSS job we do in the next track.

---

## 5. Audio & Video

### Slides

- HTML has native `<audio>` and `<video>` — no plugins needed
- `<audio>` attributes: `controls`, `autoplay` (browsers usually block it, especially with sound), `loop`, `muted`, `preload` (a hint only)
- `<video>` adds: `width`, `height`, `poster` (image before playback)
- `<source>` offers the same media in several formats so the browser picks one it can play
- `<track kind="captions">` attaches captions / subtitles from a `.vtt` file (WebVTT with timestamps)
- **Captions** include dialogue and relevant sounds; **subtitles** are usually a translation — provide a transcript for important audio-only content
- Always provide a fallback inside the element for browsers that cannot play it
- Use visible `controls` unless you build an accessible alternative
- For a hosted video (e.g. YouTube), use the platform's **Share → Embed** `<iframe>` with a `title`

### Code

Audio (fragment), with sources and fallback:

```html
<figure>
  <figcaption>Listen to the lesson introduction</figcaption>

  <audio controls>
    <source src="media/intro.mp3" type="audio/mpeg" />
    <source src="media/intro.wav" type="audio/wav" />
    <p>Your browser cannot play this audio.
      <a href="media/intro.mp3">Download the audio</a>.</p>
  </audio>
</figure>
```

Video with multiple sources and a captions track (fragment):

```html
<figure>
  <video controls width="640" poster="media/lesson-poster.jpg">
    <source src="media/lesson.mp4" type="video/mp4" />
    <source src="media/lesson.webm" type="video/webm" />

    <track
      kind="captions"
      src="media/lesson-en.vtt"
      srclang="en"
      label="English"
      default
    />

    <p>Your browser does not support HTML video.
      <a href="media/lesson.mp4">Download the video</a>.</p>
  </video>

  <figcaption>Introduction to HTML</figcaption>
</figure>
```

Embedding a hosted video (fragment):

```html
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  title="HTML lesson video"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen>
</iframe>
```

### Talk track

> Start with why this exists at all: before HTML5 you needed Flash to play media. Now `<video>` and `<audio>` are built in.
>
> The `<source>` pattern is progressive enhancement: list formats from best to most compatible; the browser takes the first it can play. That is also why the fallback paragraph inside the element matters — it is what an old browser shows.
>
> The `poster` attribute saves you from an ugly black box before playback — worth calling out because students forget it.
>
> Captions vs subtitles is a distinction students mix up: captions also carry sound cues ("[door slams]"), subtitles are usually a translation. Both come from a `.vtt` file, which must be valid WebVTT with timestamps.
>
> For a YouTube video, do not hand-write the iframe — use Share → Embed. Point out the `title` (screen-reader label), `allowfullscreen`, and `referrerpolicy`. And remind them third-party embeds have a performance cost.

---

## 6. Good to know

Extra material worth a mention if time allows. Not part of the core assessment.

### 6.1 Form Validation & UX

- Native constraint validation is free: `required`, `type`, `pattern`, `min`/`max`, `minlength`/`maxlength`
- Style invalid fields with `:user-invalid` (only after the user interacts) rather than `:invalid`
- Write **specific, readable** error messages — not "invalid input"
- Attach help text and errors with `aria-describedby` so screen readers announce them
- Group radios semantically with a `<fieldset>`/`<legend>`, not by visual proximity

### 6.2 Embedding (`<iframe>`)

- `<iframe>` embeds another page: maps, videos, third-party widgets
- Always give it a `title` (accessibility)
- `sandbox`, `allow`, `referrerpolicy`, and `loading="lazy"` control and protect the embed
- `<embed>` and `object` exist but should be avoided — prefer `iframe` or native elements
- Third-party embeds cost performance; load them lazily

### 6.3 Quality

- Validate markup with the W3C validator — zero errors
- Read HTML out loud as a debugging technique: if it does not read as a clear outline, the structure is weak
- SEO essentials: one `h1`, a meta description, meaningful link text
- Optional: structured data with `application/ld+json`
- Check keyboard navigation and focus order in a static page

### Talk track

> Keep this section light — it is "here is what exists" rather than a deep dive. The two things worth 60 seconds each: `:user-invalid` (do not shout at the user while they are still typing) and `aria-describedby` (connect the error message to the field). If you are short on time, drop this entire section — the correct cut is Tables, then Good-to-know, never Forms.

---

## 7. Topics to search

Point students here and move on. These are named, not taught.

- **ARIA: the essentials** — first rule: do not use ARIA when a semantic element exists. Covers roles, implicit landmark roles, live regions (`aria-live`, `role="alert"`), `aria-labelledby` / `aria-describedby`, `aria-expanded`, `aria-current`, `aria-hidden`, `aria-modal`.
- **Optional extensions** — the native `<dialog>` element and `showModal()`, the `popover` attribute with `popovertarget`, form-associated custom elements, advanced SEO (`canonical`, `robots.txt`, sitemaps, `hreflang`), and advanced ARIA (live-region politeness debugging, ARIA Authoring Practices patterns).

### Talk track

> Say the first rule of ARIA out loud, once: **no ARIA is better than bad ARIA**. It sends the right signal — reach for real elements first. Then tell them exactly where to look when they need the rest.

---

## Recap / Checkpoints

- A form groups controls; `name` is the submitted key, `id` links the label
- Match the control to the data; radios share a `name`; `disabled` is not submitted, `readonly` is
- Semantic elements give browsers, search engines, and screen readers meaning — `main` once per page
- Tables are for data only, with `<caption>`, `<th>`, and `scope`
- Audio/video use `controls`, `<source>` for formats, `<track>` for captions, and fallback content
- **Good to know**: native validation, `iframe` embedding, validator + SEO
- **To search**: ARIA essentials and the optional extensions
- Every full document still carries the mandatory head
