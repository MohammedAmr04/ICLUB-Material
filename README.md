# ICLUB — Material

Front-end bootcamp curricula, split into four tracks that build on each other.

| Track | Sessions | Level | Capstone |
| --- | --- | --- | --- |
| [01 — HTML](./01-html.md) | 2 | Beginner | Restaurant Menu & Order Page |
| [02 — CSS + Tailwind](./02-css.md) | 7 | Beginner | GameZone Landing Page — twice |
| [03 — JavaScript](./03-javascript.md) | 4 | Beginner | Products Manager |
| [04 — React](./04-react.md) | 7 | Intermediate | AdminHub dashboard |

**Total**: 20 sessions · roughly 115 hours

------------------------------------------------------------------------

## Coverage

Required content is marked by omission: anything not under
`### Optional Extensions` is required. The list below is the summary of what
each track guarantees, and what it deliberately leaves open.

| Area | Required | Optional |
| --- | --- | --- |
| HTML | semantics, forms, tables, media, entities, bidi, ARIA essentials | Web Components, `<dialog>`, Microdata, advanced SEO |
| CSS | cascade, box model, position, typography, colors, animation, Flex, Grid, variables, dark mode, responsive, container queries, RTL, `@supports` | view transitions, anchor positioning, `content-visibility` |
| Tailwind | setup, the working set, variants, responsive, `@theme`, `cn()` | custom plugins, container query depth, v3→v4 migration |
| JavaScript | language, data, `Map`/`Set`, regex, closures, async, browser APIs, modules, npm, security, tests | generators, `BigInt`, service workers, WebSockets |
| React | refs, portals, state, effects, hooks, Context, routing, forms, validation, server state, auth lifecycle, performance, CWV, a11y, testing | React 19 `use()`, `useSyncExternalStore`, React Compiler, MSW, E2E |

------------------------------------------------------------------------

## Order

Each track assumes the previous one is done. The chain is not optional:

```text
HTML → CSS + Tailwind → JavaScript → React
                    └─ service contract ─┘
```

The JavaScript track delivers a **service contract** that the React track
depends on. Do not start React without it working.

Tailwind lives inside the CSS track as a single session, not as its own track —
it is a productivity tool, not a separate mental model. Students who already
use Tailwind may skip Session 7 of that track.

------------------------------------------------------------------------

## Structure of every track

- **Prerequisites** — what you need before session one
- **Table of contents** — jump to any session
- **Sessions** — duration, goal, topics, live coding, homework, project work
- **Final Deliverables** — everything a student must have at the end
- **Assessment** — how the capstone is graded

------------------------------------------------------------------------

## Conventions

-   Top-level headings are sessions; `##` are sections; `###` group topics
-   `---` separates sessions
-   **Everything under `## Topics` is required.** Anything under
    `### Optional Extensions` is a bonus and is excluded from the assessment
    unless that track's Assessment section says otherwise
-   Homework is a small isolated exercise; Project Work is cumulative and feeds
    the capstone
-   A topic marked as a deliverable (the service contract) is a hard dependency
    for the next track
-   Sessions longer than 5 hours carry a pacing note about where to split
-   A capstone rebuilt twice (CSS then Tailwind) ends with a written
    comparison — that comparison is the graded part
