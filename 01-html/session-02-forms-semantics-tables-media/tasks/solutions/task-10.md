# Task 10 — Concept questions (answers)

1. **`id` vs `name`** — `id` identifies an element inside the document (used by labels, CSS, and anchors). `name` identifies the field in the submitted data: the browser sends `name=value` pairs.

2. **Why connect a `<label>` to an input** — it explains what the field is for, and it makes the text clickable/tappable to focus the control. Screen readers announce the label with the field. The connection is `for` on the label matching `id` on the control.

3. **Radio vs checkbox** — radios select exactly one option in a group (options that share a `name`); checkboxes are independent, so the user can pick zero, one, or many.

4. **GET vs POST** — GET places the data in the URL query string, suited to searches and safe for bookmarking; POST sends the data in the request body, suited to creating or changing data. POST does not encrypt by itself — HTTPS is still required, and neither replaces server-side validation.

5. **Why `<main>` is useful** — it marks the page's primary content as a landmark, so assistive technology and keyboard users can jump straight to it. There should normally be only one per page.

6. **Why not lay out pages with tables** — tables describe relationships between data in rows and columns. Using them for layout produces huge, hard-to-maintain markup that misleads screen readers and search engines. CSS (Flexbox/Grid) is the right tool for layout.

7. **`<th>` vs `<td>`** — `<th>` is a header cell that labels a row or column (with `scope`); `<td>` is an ordinary data cell.

8. **Why `controls` matters** — without it, the browser renders no UI for the media, so the user cannot play, pause, or seek. `controls` gives the native, keyboard-accessible player UI.

9. **What `<source>` does** — it offers one media file/format for the browser to choose from. Listing several lets the browser pick the first format it can play.

10. **What a `.vtt` file is** — a WebVTT text file holding timed captions/subtitles. It starts with `WEBVTT` and contains cues of the form `hh:mm:ss.mmm --> hh:mm:ss.mmm` followed by the text.
