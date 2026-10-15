# Session 1 — Fundamentals, Cascade & Selectors

**Duration**: 4 hours — **Goal**: understand how the browser resolves conflicting styles, and style a page without touching layout.

**Display format**: each topic has **Slides** (bullets for the slide), **Code** (shown on screen / demoed live), and **Talk track** (what the instructor says out loud). This mirrors the deck format used by the HTML track: bullets become `slide_content`, code becomes `slide_code`, and the talk track becomes `notes=`.

---

## 1. How CSS Works

### Slides

- **CSS (Cascading Style Sheets)** is the language that styles and lays out HTML elements
- HTML describes **what a thing is**; CSS describes **how it looks**
- `<h1>` means "this is the main heading" — CSS decides its colour, size, font, and spacing
- When the browser loads a page it: reads the HTML → builds the structure → reads the CSS rules → matches selectors to elements → applies the styles → paints the result
- The matching step is the whole game — a rule that matches nothing does nothing
- **Every browser ships a user-agent stylesheet** — CSS you never wrote, applied by default
- That is why an unstyled `<h1>` is already big and bold, and why a **reset** exists

### Ways to add CSS — and why external wins

| Method | Where it lives | Use it when |
| --- | --- | --- |
| **Inline** | `style="..."` on the element | A one-off quick test. Avoid — it mixes meaning with appearance. |
| **Internal** | a `<style>` block in `<head>` | Styles that genuinely belong to a single page. |
| **External** | a separate `.css` file via `<link>` | **Almost always.** One source of truth, cached, reusable, maintainable. |

### A minimal reset we use for the whole course

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

* {
  margin: 0;
}

body {
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}
```

### Code

```text
  HTML  →  parse  →  DOM tree
                     ↓
  CSS   →  parse  →  rule list
                     ↓
          match selectors to elements
                     ↓
          resolve the cascade (who wins?)
                     ↓
          compute layout  →  paint pixels
```

```html
<!-- external stylesheet: the default choice -->
<head>
  <link rel="stylesheet" href="styles.css" />
</head>
```

```css
/* styles.css */
h1 {
  color: #0047ff;
  font-size: 2.5rem;
}
```

### Talk track

> The most common beginner confusion is styling paragraphs by hand because they could not find the right heading element. Frame the session meaning-first, appearance-second: you pick the correct HTML element, then you style it.
>
> Analogy: HTML is the **label on the shipping box**; CSS is the paint colour. The warehouse cares about the label. The paint is decoration.
>
> Spend a moment on the **user-agent stylesheet**. Students assume a blank page is truly blank. Turn on DevTools, select an `<h1>`, and show the grey "user agent stylesheet" rules. That single reveal explains resets, margin collapsing surprises, and half the "why is there a gap" questions for the rest of the course.
>
> Land the rule early: **we write an external `styles.css`**. Inline styles are for quick demos only. Internal `<style>` is acceptable for a single self-contained page.

---

## 2. Syntax

### Slides

- A CSS rule = **selector** + **declaration block**
- A declaration = **property** + `:` + **value** + `;`
- The semicolon separates declarations — forget it and the next line breaks
- Write one declaration per line: readable diffs, sane blame
- **Comments** `/* ... */` document intent or temporarily disable a rule
- What the HTML side looks like: `<link rel="stylesheet" href="styles.css" />`

### Code

```css
selector {
  property: value;
}
```

```css
/* a type selector styling every paragraph */
p {
  color: #333;
  font-size: 1.125rem;
  line-height: 1.6;
}
```

```html
<head>
  <link rel="stylesheet" href="styles.css" />
</head>
```

```css
/* section banners make long files navigable */
/* =======================================
   HEADER
   ======================================= */
```

### Talk track

> This slide is muscle memory. By the end of the session `selector { property: value; }` should be automatic — do not move on until it is.
>
> Point out the two silent failures: a **missing semicolon** kills the declaration after it, and a **typo in a property name** is simply ignored. CSS never errors at you; it fails quietly. That is why the DevTools Styles panel is not optional — it is the debugger.
>
> Contrast with HTML's fault tolerance from the previous track. Same philosophy, different failure surface: HTML recovers into a different page, CSS just drops the rule.

---

## 3. Selectors

### Slides

- A selector decides **which elements** a rule applies to
- Type, class (`.`), ID (`#`), and universal (`*`)
- Grouping with commas — one rule, many selectors
- Combinators: descendant (space), child (`>`), adjacent sibling (`+`)
- Attribute selectors: `[type="text"]`, `[data-state="open"]`
- Pseudo-classes for **state**: `:hover`, `:focus-visible`, `:disabled`, `:first-child`, `:nth-child()`
- Pseudo-elements for **parts of an element**: `::before`, `::after`, `::placeholder`, `::selection`
- **Specificity** decides the winner when two rules match the same element

### Which selector to reach for

| Selector | Example | Meaning |
| --- | --- | --- |
| Type | `p` | Every `<p>` |
| Class | `.title` | Every element with `class="title"` — reusable |
| ID | `#header` | The one element with `id="header"` — unique per page |
| Universal | `*` | Every element (reset, debug) |
| Group | `h1, h2, p` | All of the listed selectors |
| Descendant | `div p` | Any `<p>` inside a `<div>`, at any depth |
| Child | `div > p` | Only `<p>` that is a **direct** child of `<div>` |
| Adjacent sibling | `h1 + p` | The `<p>` immediately after an `<h1>` |
| Attribute | `input[type="text"]` | Elements matching the attribute condition |

### Code

```html
<h1 id="main-title" class="title">My Website</h1>
<p class="description">First paragraph.</p>
<p class="description">Second paragraph.</p>

<div>
  <p>Selected by `div p` and by `div > p`.</p>
  <section>
    <p>Selected by `div p` only — not a direct child.</p>
  </section>
</div>

<input type="text" />
<input type="password" />
```

```css
/* type */
p {
  color: #333;
}

/* class — reusable on many elements */
.description {
  color: #666;
}

/* id — unique per page */
#main-title {
  color: #0047ff;
}

/* universal — reset */
* {
  margin: 0;
}

/* grouping */
h1,
h2,
p {
  font-family: system-ui, sans-serif;
}

/* descendant vs child */
div p {
  color: green;
}
div > p {
  font-weight: 700;
}

/* adjacent sibling */
h1 + p {
  margin-block-start: 0.5rem;
}

/* attribute */
input[type="text"] {
  border: 1px solid #999;
}

/* pseudo-class */
a:hover {
  text-decoration: underline;
}
button:focus-visible {
  outline: 2px solid #0047ff;
  outline-offset: 2px;
}
li:nth-child(odd) {
  background: #f5f5f5;
}

/* pseudo-element */
.description::before {
  content: "→ ";
  color: #0047ff;
}
```

### Talk track

> Start with the three everyone meets first — type, class, ID — then make the class/ID distinction a rule they repeat: **classes are for reusing a style, IDs are for uniquely naming a thing**. Prefer classes in CSS; IDs belong to links (`#section`) and JavaScript hooks.
>
> The descendant vs child distinction is where eyes glaze over. Draw the nested `<div> > <section> > <p>` on the board and trace which `<p>` each selector catches. The contrast is the point: descendant matches at any depth, child matches one level only.
>
> `:focus-visible` deserves a sentence: it shows the focus ring for keyboard users without flashing it on mouse clicks. Removing focus outlines entirely is an accessibility bug — restyle them, never delete them.
>
> `::before` / `::after` need `content` or they render nothing. The most common mistake is forgetting `content`.

---

## 4. The Cascade & Specificity

### Slides

- The **cascade** is the algorithm that resolves conflicting declarations
- When two rules set the same property on the same element, something has to win
- Order of resolution: **origin & importance** → **specificity** → **source order**
- **Specificity** is a score for a selector, written as three components `(id, class, type)`
- Type and pseudo-elements count as 1 in the last slot; class, attribute, and pseudo-class count as 1 in the middle; ID counts in the first
- `*` and combinators add **nothing** to specificity
- Equal specificity → the rule that comes **later** in the stylesheet wins
- `!important` overrides everything — and is almost always a symptom, not a solution

### Specificity worked step by step

| Selector | (id, class, type) | Score |
| --- | --- | --- |
| `p` | (0, 0, 1) | 1 |
| `.description` | (0, 1, 0) | 10 |
| `p.description` | (0, 1, 1) | 11 |
| `#main-title` | (1, 0, 0) | 100 |
| `div p` | (0, 0, 2) | 2 |
| `a:hover` | (0, 1, 1) | 11 |
| `input[type="text"]` | (0, 1, 1) | 11 |
| `ul li:nth-child(2)` | (0, 1, 2) | 12 |

### Code

```html
<p id="lead" class="intro">Which colour am I?</p>
```

```css
p {
  color: black;
} /* (0,0,1) */

.intro {
  color: green;
} /* (0,1,0) — wins over the type selector */

p.intro {
  color: orange;
} /* (0,1,1) — wins over .intro alone */

#lead {
  color: blue;
} /* (1,0,0) — wins over everything so far */

p {
  color: red;
} /* (0,0,1), later — loses to all of the above */
```

```css
/* !important: the escape hatch you should almost never open */
.intro {
  color: purple !important;
} /* now nothing without !important can beat it */
```

### Talk track

> This is the topic the session is named after, and the one students get wrong for months. Do not memorise a mysterious score — make the mental model explicit: **count IDs, then classes/attributes/pseudo-classes, then types/pseudo-elements**, compare left to right.
>
> Run six short "who wins?" predictions on the board and reveal the answer each time. The act of predicting is what makes it stick — a list of numbers on a slide never does.
>
> Source order matters only on a tie. Keep saying it: *specificity first, source order to break ties*.
>
> End on `!important` with a warning, not an endorsement. If you find yourself reaching for it, the stylesheet has an architecture problem, not a specificity problem. Keep specificity **low and flat** — mostly single classes — and you will rarely fight the cascade at all.

---

## 5. Inheritance

### Slides

- **Inheritance** passes some property values from a parent element down to its children
- Not all properties inherit — text properties usually do, box properties usually do not
- Commonly **inherited**: `color`, `font-family`, `font-size`, `line-height`, `text-align`
- Commonly **not inherited**: `margin`, `padding`, `border`, `width`, `height`, `background`, `background-color`
- The `inherit` keyword forces a property to take its parent's computed value
- `initial` resets a property to its spec default; `unset` means "inherit if it normally would, otherwise initial"
- Inheritance happens **before** the cascade resolves the final value — it is the fallback, not the winner

### Code

```html
<div class="parent">
  <p>I inherit the colour.</p>
  <p class="child">I override it.</p>
</div>
```

```css
.parent {
  color: #0047ff;
  font-family: system-ui, sans-serif;
}

/* colour and font-family inherit down automatically
   margin, padding, and border do not */
p {
  margin-block: 0.5rem;
}

.child {
  color: inherit; /* take the parent's colour explicitly */
}
```

```css
/* comparison of the three keywords */
.reset-to-default {
  color: initial; /* the spec default, not the parent's value */
}

.follow-the-parent {
  color: unset; /* inherit, because color normally inherits */
}
```

### Talk track

> The clean way to teach this: inheritance is a property of the **text**, and text flows. Colour, font, and line-height cascade down because the child is made of text too. Box properties do not, because a child's margin is its own.
>
> Open DevTools and show the "Inherited from `<div>`" section on a child element — it makes the invisible visible.
>
> The `inherit` keyword is mostly used to **undo** a browser default. The classic case is a `<button>` or form control: the user-agent sets `font-family` and `font-size`, so the button text does not match the page. `button { font: inherit; }` fixes it. Show that live.
>
> Do not confuse inheritance with the cascade. Inheritance supplies a value when nothing declares one; the cascade decides between declarations that do. Different mechanisms, common mix-up.

---

## 6. Units

### Slides

- **Absolute**: `px` (and print units `pt`, `cm`, `in`) — a fixed size regardless of context
- **Relative**: `rem`, `em`, `%`, `ch`, and viewport units `vw`, `vh`, `vmin`, `vmax`
- `rem` = relative to the **root** font size (`html`). Predictable, the default choice for spacing.
- `em` = relative to the **element's own** font size. Compounds when nested — powerful and dangerous
- `%` for width/height is relative to the containing block; for `font-size` it is relative to the parent
- Viewport units size to the window — great for heroes, easy to overuse
- `clamp(min, preferred, max)`, `min()`, and `max()` create fluid values with no media query
- **Rule of thumb: spacing in `rem`, type usually in `rem`, avoid `px` for anything meant to scale**

### Code

```text
  1rem  = the root font size      (16px by default)
  1em   = this element's font size
  1vw   = 1% of the viewport width
  1vh   = 1% of the viewport height
  1ch   = the width of the "0" glyph
```

```css
html {
  font-size: 100%; /* keep the user's setting — do not hard-set 16px */
}

h1 {
  font-size: 2.5rem; /* 2.5 × root, regardless of the parent */
}

p {
  font-size: 1rem;
  margin-block: 1rem; /* rem, so the rhythm is consistent */
}

/* em compounds: a nested .box doubles its padding */
.box {
  font-size: 1.25em;
  padding: 1em; /* = its own font size */
}

/* fluid hero text with no media query */
.hero-title {
  font-size: clamp(1.75rem, 4vw + 1rem, 3.5rem);
}

.card {
  width: min(100%, 32rem);
  max-width: max(20rem, 60vw);
}
```

### Talk track

> The `rem` vs `em` question is the one to nail. Say it plainly: **`rem` looks at the root, `em` looks at the current element's font size** — and nesting `em` multiplies. Draw a nested box and show the padding doubling. Then give the rule: default to `rem` for spacing and type, reach for `em` only when you deliberately want a value to scale with its own text (buttons, icon spacing).
>
> Never set `html { font-size: 10px }` to make the maths easy — you break the user's zoom preference. Keep the root at `100%`.
>
> `clamp()` is the highlight: one line replaces a stack of breakpoints for fluid type. Show the hero title resizing as you drag the window — no media query in sight. This is a preview of the responsiveness session.

---

## 7. Colors & Backgrounds

### Slides

- **Named colours** — `red`, `blue`, `rebeccapurple` — readable, limited
- **HEX** — `#rrggbb`, and the short form `#rgb` when each pair repeats
- **`rgb()`** — channels `0`–`255`; **`rgba()`** adds alpha from `0` to `1`
- **`hsl()`** — hue `0`–`360`, saturation and lightness in `%`; the easiest model to reason about
- **`oklch()`** — the modern, perceptually uniform model; lightness, chroma, hue
- Alpha can now live in any model: `rgb(0 0 0 / 0.5)`, `hsl(220 90% 56% / 0.4)`
- **`background-color`** sets the fill colour behind content and padding
- **`background-image`**, `background-repeat`, `background-position`, `background-size`, `background-attachment`, `background-clip`, `background-origin` draw/manipulate background layers
- The **`background` shorthand** sets multiple background properties in one line (order matters in edge cases; keep readable)
- Gradients: `linear-gradient()`, `radial-gradient()`, `conic-gradient()`, `repeating-linear-gradient()` create images without files
- Multiple backgrounds: comma-separated layers (first is on top)
- Transparency: prefer `rgba()`/slash notation over `opacity` when you want to fade only the background
- Two colours to use with care: contrast matters — **WCAG AA** wants ~4.5:1 for body text
- Turn raw values into **tokens** (custom properties) so the palette has one source of truth

### The same colour, five ways

| Model | Value | Notes |
| --- | --- | --- |
| Named | `red` | Readable, but only ~140 names exist |
| HEX | `#ff0000` | Short form `#f00` |
| RGB | `rgb(255 0 0)` | Channels 0–255 |
| RGBA | `rgba(255 0 0, 0.5)` | RGB plus alpha |
| HSL | `hsl(0 100% 50%)` | Hue, saturation, lightness |
| OKLCH | `oklch(0.63 0.26 29)` | Perceptually uniform |

### Code

```css
/* named */
p {
  color: red;
}

/* hex, long and short */
.card {
  border-color: #ff0000;
  background: #fff;
}

/* rgb / rgba */
.overlay {
  background: rgba(0, 0, 0, 0.5); /* 50% black veil */
}

/* hsl — easy to derive shades by moving lightness */
.button {
  background: hsl(220 90% 56%);
}
.button:hover {
  background: hsl(220 90% 48%);
}

/* backgrounds: solid, gradient, image, multiple layers, attachment */
.hero {
  background-color: #0047ff;
  background-image: linear-gradient(135deg, #0047ff 0%, #0ea5e9 100%);
}

.cover {
  background-image: url("assets/placeholder.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed; /* keep image fixed while scrolling */
}

.banner {
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.7), transparent),
    url("assets/placeholder.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.pattern {
  background-image: repeating-linear-gradient(45deg, #eee 0 10px, #fff 10px 20px);
  background-repeat: repeat;
}

.text-clip {
  background-image: linear-gradient(90deg, #0047ff, #0ea5e9);
  -webkit-background-clip: text;
  color: transparent;
}

/* oklch — same idea, perceptually even */
.badge {
  background: oklch(0.72 0.18 145);
}
```

```css
/* colour tokens: define once, use everywhere */
:root {
  --color-ink: oklch(0.25 0.02 260);
  --color-brand: hsl(220 90% 56%);
  --color-brand-strong: hsl(220 90% 46%);
  --color-muted: #64748b;
}

body {
  color: var(--color-ink);
}

a {
  color: var(--color-brand);
}
```

### Talk track

> Keep the format list short and opinionated. Students do not need every syntax — they need to know **HEX, `rgb`/`rgba`, and `hsl`**, and to have heard of `oklch` as where the platform is heading. HSL is worth emphasising because deriving a hover shade is just a lightness tweak — show it live rather than explaining it.
>
> Alpha is the practical bit: `rgba()` (or the slash syntax `rgb(0 0 0 / 0.5)`) is how you make an overlay that dims an image without hiding it. For backgrounds, prefer fading only the background layer (a translucent colour or gradient) instead of `opacity` on the whole element — `opacity` affects text and children too.
>
> **Backgrounds:** `background-color` fills the box; `background-image` sits on top. With comma-separated values you can stack multiple backgrounds. `background-size: cover` fills the area without distortion; `background-position: center` keeps the focal point visible; `background-attachment: fixed` creates a parallax-like effect but can be costly on mobile — demo it and note performance. `background-clip: text` lets you put gradients inside text (with `color: transparent`). `background-origin` controls how the image is positioned relative to padding/border/content boxes.
>
> The `background` shorthand resets unspecified values, so be explicit when combining multiple layers. `linear-gradient()` is the one to know first — show a two-stop gradient live and watch it animate between stops in DevTools. Also introduce `repeating-linear-gradient()` for simple patterns.
>
> Finish on contrast, because it is an accessibility requirement, not a taste call. Pull up a contrast checker, test the brand colour on white and on the dark ink, and show a pair that fails AA. The fix is usually a darker shade of the same hue — which is exactly why you build a **token ramp** instead of scattering random hexes.
>
> That token idea (`:root { --color-brand: ... }`) is the seed of the theming session. Plant it now; we harvest it later.

---

## Complete Example

A small page that combines units, cascade, inheritance, and colour tokens.

### HTML

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CSS Example</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <div class="container">
      <h1>Welcome</h1>
      <p class="lead">This is a CSS example.</p>
      <button>Click me</button>
    </div>
  </body>
</html>
```

### CSS

```css
/* ---- tokens: one source of truth for colour ---- */
:root {
  --color-ink: oklch(0.25 0.02 260);
  --color-body: rgb(80 80 80);
  --color-brand: #0066ff;
  --space-1: 1rem;
  --space-2: 1.5rem;
}

/* ---- reset ---- */
*,
*::before,
*::after {
  box-sizing: border-box;
}
* {
  margin: 0;
}

/* ---- layout + inheritance: colour flows down ---- */
body {
  font-family: system-ui, sans-serif;
  line-height: 1.6;
  color: var(--color-ink);
  padding: var(--space-2);
}

.container {
  max-width: 40rem;
  margin-inline: auto;
  text-align: center;
}

/* ---- elements ---- */
h1 {
  font-size: 2.25rem; /* rem: scales with the root */
  color: var(--color-brand);
  margin-block-end: var(--space-1);
}

.lead {
  color: var(--color-body);
  margin-block-end: var(--space-2);
}

/* subtle background to show background-color */
body {
  background-color: #fafafa;
}

/* button does not inherit text styles by default — force it */
button {
  font: inherit;
  background: var(--color-brand);
  color: white;
  border: 0;
  border-radius: 0.5rem;
  padding: 0.75rem 1.25rem;
  cursor: pointer;
}

button:hover {
  background: hsl(220 90% 46%);
}
```

This example combines several concepts from the session:

- External stylesheet + a minimal reset
- Class and element selectors, and specificity in action (`body` colour vs `.lead` colour)
- Inheritance (`font-family` and `line-height` flow down; the button opts back in with `font: inherit`)
- `rem` for type and spacing, `%` / `max-width` for layout
- Colour tokens, HEX, `rgb()`, `hsl()`, and `oklch()`
- A `:hover` state

---

## Recap / Checkpoints

- CSS describes **appearance**; HTML describes **meaning**
- Write **external** stylesheets; keep inline styles for demos only
- Rule anatomy: `selector { property: value; }` — a missing semicolon breaks the next line, a typo fails silently
- Selectors: type, class, ID, universal, grouping, combinators (` `, `>`), attributes, pseudo-classes, and pseudo-elements
- Prefer **classes** for styling, IDs for links and hooks; keep focus styles visible with `:focus-visible`
- The **cascade** resolves conflicts in this order: origin & importance → **specificity** → source order
- Specificity is `(id, class, type)` — count left to right; keep it flat and avoid `!important`
- **Inheritance** supplies values for text properties to descendants; box properties do not inherit — use `inherit`/`initial`/`unset` deliberately
- Units: default to **`rem`** for spacing and type; `em` compounds; `clamp()` gives you fluid values for free
- Colours & backgrounds: know named, HEX, `rgb()`/`rgba()`, `hsl()`, and be aware of `oklch()`; know `background-color`, `background-image`, `background-size`, `background-position`, `background-repeat`, `background-attachment`, `background-clip`, `background-origin`, `background` shorthand, `linear-gradient()`, `radial-gradient()`, `conic-gradient()`, `repeating-linear-gradient()`, and multiple backgrounds; check **contrast (WCAG AA)** and build a **token ramp** instead of scattering hexes

### Mini Project

Build a simple personal profile page containing:

- A profile heading and a short description
- A profile section and a button
- At least three different selector types
- A colour palette written as `:root` tokens, plus a `:hover` state
- An external `styles.css` and a minimal reset

Try to build it **without copying the complete example above**.
