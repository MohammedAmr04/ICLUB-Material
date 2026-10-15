# Session 2 — Tasks

Exercises for **HTML Session 2 — Forms, Semantics, Tables & Media**.

Each task maps to a topic in `../content.md`. Tasks 1–4 build the forms skill, 5 the semantics, 6 the tables, 7–8 the media, and Task 9 is the capstone that combines everything.

| # | Task | Topic | Type |
| --- | --- | --- | --- |
| 01 | Label every control | Forms & Inputs | Code |
| 02 | Build the registration form | Forms & Inputs | Code |
| 03 | Match the control to the data | Form Controls | Code |
| 04 | Radio groups and `name` | Form Controls | Code |
| 05 | Refactor the div soup | Semantics & Structure | Code |
| 06 | Build a data table | Tables | Code |
| 07 | Audio with fallback | Audio & Video | Code |
| 08 | Video with captions | Audio & Video | Code |
| 09 | Combined mini-project (capstone) | All | Code |
| 10 | Concept questions | All | Written |

Reference solutions live in [`solutions/`](./solutions/).

## How to submit

- Put each task in its own file, e.g. `task-02.html`.
- **Every full document must carry the mandatory head**: `<meta charset="UTF-8">`, the viewport meta, a non-empty `<title>`, and `lang` on `<html>`.
- Run every HTML file through the [W3C validator](https://validator.w3.org/#validate_by_input) before submitting.
- Zero validator errors is the bar for every code task.

---

## Task 01 — Label every control

Build a small search bar with three controls: a text search field, a `<select>` for category, and a submit button. Every control must have a **visible** `<label>` connected by `for`/`id`. Do **not** use placeholder text as the only label.

**Deliverable**: `task-01.html`

**Acceptance**: each label's `for` matches an existing `id`; no control relies on `placeholder` for its name; clicking a label focuses its control.

---

## Task 02 — Build the registration form

Build a registration form with these fields, all labelled:

- full name (text, `autocomplete="name"`, required, min length 3)
- email (email type, `autocomplete="email"`, required)
- age (number, min 10, max 100)
- preferred format (two radios: Online / On-site, sharing a `name`, one required)
- track (select with a disabled placeholder option and three real options, required)
- notes (textarea, 4 rows)
- terms (checkbox, required)

Group the radios in a `<fieldset>` with a `<legend>`. End with a submit button.

**Deliverable**: `task-02.html`

**Acceptance**: every control is labelled; radios share a `name`; `action` and `method` are set; leaving a required field empty blocks submission.

---

## Task 03 — Match the control to the data

For each piece of data, choose the input `type` and one extra attribute that improves the experience. Write one sentence explaining the choice.

1. An email address
2. A phone number
3. A date of birth
4. A website URL
5. A quantity between 1 and 20
6. A password
7. A profile photo upload that accepts only images

Then build one small form containing all seven.

**Deliverable**: `task-03.html`

**Acceptance**: each field uses the semantically correct type (not `text` everywhere); the phone field does not pretend to validate with `pattern` unless you explain it; the file field has `accept`.

---

## Task 04 — Radio groups and `name`

You are building a quiz with two questions, each with three options.

1. Write the markup using radio buttons.
2. Explain in a comment why the two questions must use **different** `name` values.
3. Add a checkbox group ("choose all that apply") and explain why checkboxes differ from radios.

**Deliverable**: `task-04.html`

**Acceptance**: each question is its own radio group; selecting one option in a question deselects the others in that question only; the comment correctly explains `name` grouping.

---

## Task 05 — Refactor the div soup

The page below is built entirely from `<div>`. Rewrite it using semantic elements and add a `main` landmark. Keep every piece of text.

```html
<div class="page">
  <div class="top">
    <p>Web Academy</p>
    <div class="menu">
      <a href="#courses">Courses</a>
      <a href="#about">About</a>
    </div>
  </div>
  <div class="content">
    <div id="courses">
      <h1>Learn Web Development</h1>
      <p>Start with HTML, then CSS and JavaScript.</p>
      <div class="post">
        <h2>HTML Basics</h2>
        <p>Learn how to structure web content.</p>
      </div>
    </div>
    <div class="tip">
      <h2>Tip</h2>
      <p>Practice each example in a separate file.</p>
    </div>
  </div>
  <div class="bottom">
    <p>Contact: hello@example.com</p>
  </div>
</div>
```

**Deliverable**: `task-05.html`

**Acceptance**: uses `header`, `nav`, `main`, `footer`, `article`, `aside`; the nav is a list of links; exactly one `main`; no text is lost.

---

## Task 06 — Build a data table

Build a table of your weekly study schedule with columns **Day**, **Topic**, **Duration**. Requirements:

- a `<caption>`
- `<thead>` with `<th scope="col">`
- `<tbody>` with row headers using `<th scope="row">`
- a `<tfoot>` with a total row using `colspan`

**Deliverable**: `task-06.html`

**Acceptance**: headers use `<th>`, not bold `<td>`; every header has a `scope`; the total row spans two columns; the table is wrapped so a wide layout can scroll later.

---

## Task 07 — Audio with fallback

Add an audio player for a lesson introduction.

1. Use `<audio>` with visible `controls`.
2. Provide two `<source>` elements in different formats.
3. Add fallback content with a download link for browsers that cannot play it.
4. Wrap it in a `<figure>` with a `<figcaption>`.

**Deliverable**: `task-07.html` (a `media/` folder with placeholder files is fine)

**Acceptance**: `controls` is present; there are at least two `<source>`s with `type`; fallback content is inside the element; a caption describes the audio.

---

## Task 08 — Video with captions

Add a video player.

1. Use `<video>` with `controls`, `width`, and a `poster`.
2. Provide two `<source>` formats.
3. Add a `<track kind="captions">` pointing at a valid `.vtt` file.
4. Add fallback content and a `<figcaption>`.

Then write the `.vtt` file with at least three correctly timed cues.

**Deliverable**: `task-08.html` and `media/lesson-en.vtt`

**Acceptance**: the `.vtt` starts with `WEBVTT`, uses `hh:mm:ss.mmm --> hh:mm:ss.mmm` cues, and loads with no console error; the video has `controls` and a `poster`.

---

## Task 09 — Combined mini-project (capstone)

Build one page, `index.html`, that includes:

1. A semantic `header`, `nav`, `main`, and `footer`.
2. A registration form (name, email, a radio group, a dropdown, a notes field, a submit button).
3. A table showing three course sessions.
4. An audio player for an introduction.
5. A video player with `controls` and a captions/subtitle track.

Suggested structure:

```text
html-session-2/
├── index.html
└── media/
    ├── intro.mp3
    ├── lesson.mp4
    ├── lesson.webm
    ├── lesson-poster.jpg
    └── lesson-en.vtt
```

**Deliverable**: the folder above.

**Acceptance** — all must hold:

- [ ] Every form control has a label.
- [ ] Radio options for one question share the same `name`.
- [ ] Required fields and basic validation work.
- [ ] The form endpoint is clearly identified as a demo if no backend exists.
- [ ] The page uses semantic elements appropriately.
- [ ] The table has a caption and meaningful headers.
- [ ] Audio and video show controls.
- [ ] Media file paths are correct.
- [ ] Subtitles/captions load from a valid `.vtt` file.
- [ ] The page can be navigated with a keyboard.
- [ ] The document passes the W3C validator with zero errors.

---

## Task 10 — Concept questions

Answer in your own words. One short paragraph each.

1. What is the difference between `id` and `name` in a form control?
2. Why should a `<label>` be connected to an input?
3. When should you use radio buttons instead of checkboxes?
4. What is the difference between `GET` and `POST`?
5. Why is a `<main>` element useful?
6. Why should tables not be used for whole-page layout?
7. What is the difference between `<th>` and `<td>`?
8. Why is the `controls` attribute useful for audio and video?
9. What does `<source>` do?
10. What is a `.vtt` file used for?

**Deliverable**: `task-10.md`
