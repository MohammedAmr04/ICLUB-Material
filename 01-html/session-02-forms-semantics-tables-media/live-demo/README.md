# Session 2 — Live Demo

Live-coding plan for the session. Build the skeleton live, then fill each
section as you teach the matching topic.

## Running order

| Step | Topic | What you build live |
| --- | --- | --- |
| 1 | Semantics & Structure | The page skeleton: `header`, `nav`, `main`, `footer`, and empty sections |
| 2 | Forms & Inputs | The registration form inside `#register` |
| 3 | Form Controls | Add the radio group, the select, and the textarea |
| 4 | Tables | The schedule table inside `#courses` |
| 5 | Audio & Video | The audio and video players inside `#media` |

Open [`starter/index.html`](./starter/index.html) — it has the head and the
landmarks with empty sections. Fill it as you go. Compare against
[`finished/index.html`](./finished/index.html) at the end.

## Teaching notes

- **Type, do not paste.** Students follow the keystrokes, not the finished file.
- Demonstrate native validation by submitting the form with a required field empty.
- Open DevTools → Accessibility to show the landmarks appear as you add them.
- Keep the session on HTML: mention CSS and JS only when they come up.
- Before the session, drop real files into `media/` (see its README) or the
  players will show the fallback content on purpose — which is a good demo too.

## File map

```text
live-demo/
├── starter/index.html    # skeleton to build into
├── finished/index.html   # the completed page
└── media/
    ├── lesson-en.vtt     # valid WebVTT captions
    └── README.md         # which binary files to drop in
```
