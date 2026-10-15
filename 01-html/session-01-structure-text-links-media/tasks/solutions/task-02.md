# Task 02 — Explanation (head vs body)

**What belongs in `<head>` vs `<body>`:** the `<head>` holds metadata — instructions *about* the document that the browser, search engines, and social networks read but never draw on the page. The `<body>` holds everything the visitor actually sees and interacts with. Rule of thumb: if you can see it, it goes in the body; if it only affects how the page is loaded, described, or styled, it goes in the head.

**Three head tags:**

- `<meta charset="UTF-8">` — declares the character encoding, so non-Latin text (including Arabic) renders correctly instead of as garbage.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` — tells mobile browsers to use the device width, instead of rendering the desktop layout zoomed out.
- `<title>` — the document title, shown in the browser tab, used for bookmarks, and often used as the headline of a search result.

See [`task-02.html`](./task-02.html) for the code.
