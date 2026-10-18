# Session 2 — Tasks

Exercises for **CSS Session 2 — Sizing, Display, Box Model, Position & Visual Chrome**.

## Task 1 — Fonts & Type Scale

Build a text page that:

- Uses the system font stack
- Defines a modular type scale as `:root` tokens (`--text-xs` … `--text-2xl`)
- Applies a variable font with `@font-face` + `font-display: swap` (or explain why you would)

## Task 2 — Text Controls

Given a long heading and a card description:

- Balance the heading with `text-wrap: balance`
- Truncate the description to one line with `text-overflow: ellipsis` **and** to three lines with `-webkit-line-clamp`
- Use unitless `line-height` everywhere
- Restyle a list's bullets with `::marker`

## Task 3 — Opacity, Filters & Icons

- Fade **only the background** of a card (not its text) using an alpha colour
- Hide an element fully with `opacity: 0` and explain the difference
- Add a `grayscale(100%)` → `grayscale(0)` hover transition on an image
- Build a button with an inline SVG icon using `currentColor`

## Task 4 — Sizing & Display

- Size a card with `width`, `max-width: 100%`, and `aspect-ratio: 16 / 9` image (no fixed height)
- Use `fit-content` on a button group so it doesn't stretch
- Show the three ways to hide an element and when each is correct
- Make a `span` behave like a box with `inline-block`

## Task 5 — Box Model & Position

- Ship the global `box-sizing: border-box` reset
- Fix a margin-collapsing gap two ways (`display: flow-root` and a fence)
- Pin a badge with `position: absolute` inside a `position: relative` parent
- Build a `position: sticky` header that survives page scroll

## Task 6 — Border, Shadows & Overflow

- Give a card `border`, `border-radius`, and a two-layer `box-shadow`; elevate it on hover
- Add a `:focus-visible` outline with `outline-offset` (never remove focus rings)
- Clip a child image to the card's rounded corners with `overflow: hidden`
- Clip a hero with `clip-path` and note what `overflow: hidden` does to `position: sticky`

## Mini Project

**Profile card** — card with border/shadow/hover elevation, `aspect-ratio` image, truncated text, sticky header, absolute badge, type scale, and visible focus states. Build it **without copying** the Session 1 example.
