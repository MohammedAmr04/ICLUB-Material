# Session 2 — Sizing, Display, Box Model, Position & Visual Chrome

**Duration**: ~5 hours — **Goal**: control the size, placement, and visual chrome of every element precisely, with typography and effects in place.

**Display format**: each topic has **Slides** (bullets for the slide), **Code** (shown on screen / demoed live), and **Talk track** (what the instructor says out loud). This mirrors the deck format used by the HTML track: bullets become `slide_content`, code becomes `slide_code`, and the talk track becomes `notes=`.

> **Note**: colors and backgrounds were covered in Session 1. This session assumes you already know colour models, tokens, and gradients.

---

## 1. Fonts

### Slides

- **`font-family`** takes a list of fonts — browsers use the first one it finds
- The **system font stack** (`system-ui`, `-apple-system`, `Segoe UI`, `Roboto`, …) matches the OS and costs nothing to load
- **Fallback fonts**: always end the stack with a generic (`sans-serif`, `serif`, `monospace`) so you never render nothing
- **`@font-face`** defines your own font from a file; pair it with **`font-display`**
  - `swap` — show fallback immediately, swap in the web font when ready (best default)
  - `optional` — use the font only if it loads within ~100ms
  - `block` — invisible text for up to 3s (bad for user experience)
- **Web fonts from a CDN** cost bandwidth and render-blocking risk; self-host when you can
- **Variable fonts**: one file carries a whole weight range — `font-weight: 100 900;`
- Local vs web fonts: local/system for speed and offline, web fonts for brand identity

### Code

```css
/* system stack: free, fast, native */
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
    Arial, sans-serif;
}

/* self-hosted web font */
@font-face {
  font-family: "Inter";
  src: url("fonts/inter.woff2") format("woff2");
  font-weight: 100 900; /* variable font range */
  font-display: swap;
}

h1 {
  font-family: "Inter", system-ui, sans-serif;
  font-weight: 700;
}
```

```text
font-display values:  swap (default) · optional · block · fallback
                      ↑ swap after paint          ↑ longest wait
```

### Talk track

> Start with the system stack. It is what most production sites use for body text — no download, no layout shift, looks correct on every OS. Show DevTools Network with "Disable cache" to prove web fonts block first paint.
>
> `font-display: swap` is the one setting to remember. `block` leaves blank text for up to three seconds — a real accessibility and retention cost. The WOFF2 format is the modern default: smaller than TTF/WOFF.
>
> Variable fonts deserve thirty seconds: one file, a `font-weight` range instead of ten separate files. Perfect for headings that step in weight.

---

## 2. Text

### Slides

- **Type scale** — sizes follow a ratio (`1.2` modular scale): `0.75rem`, `0.875rem`, `1rem`, `1.25rem`, `1.5rem`, `2rem`
- **`line-height`** — prefer a **unitless multiplier** (`1.6`) over `px`; it scales with `font-size`
- **`font-weight`** (`100`–`900` or `normal`/`bold`), **`font-style`** (`italic`), **`font-stretch`**
- **`letter-spacing`** — negative tightens headlines; positive improves small-caps/labels
- **`text-transform`** — `uppercase`/`lowercase`/`capitalize` (don't type in caps)
- **`text-align`**, **`text-indent`**
- **`white-space`**, **`word-break`**, **`overflow-wrap`** — wrapping and overflow control
- Truncating: one line with `text-overflow: ellipsis` (+ `white-space: nowrap` + `overflow: hidden`), multiple lines with `-webkit-line-clamp`
- **`text-wrap: balance`** (headlines) and **`text-wrap: pretty`** (paragraphs) — modern line-breaking
- **`::marker`** — restyle list bullets/numbers
- **`writing-mode`** — horizontal/vertical text (brief)

### Code

```css
:root {
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.25rem;
  --text-xl: 1.5rem;
  --text-2xl: 2rem;
}

h1 {
  font-size: var(--text-2xl);
  line-height: 1.15; /* unitless: scales with font-size */
  letter-spacing: -0.02em;
  text-wrap: balance;
}

p {
  font-size: var(--text-base);
  line-height: 1.6;
  text-wrap: pretty;
}

.label {
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

/* one-line truncation */
.truncate {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* multi-line clamp */
.clamp {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* long-word safety */
.wrap {
  overflow-wrap: break-word; /* or word-break: break-word */
}

/* list marker styling */
li::marker {
  color: var(--color-brand);
  font-weight: 700;
}
```

### Talk track

> The type scale is a system, not a list of random numbers. Pick a ratio and apply it once — every heading and paragraph then shares a rhythm. Show two pages side by side: one with scattered `17px`, `19px`, `21px`; one on a scale. The difference is felt before it is explained.
>
> `line-height: 1.6` (unitless) is the default you should reach for. `line-height: 24px` breaks when font size changes. Unitless multiplies the font size, so it always stays proportional.
>
> Truncation is the daily skill: cards, table cells, nav items. `text-overflow: ellipsis` needs all three of `nowrap`, `hidden`, and the ellipsis — missing one and nothing happens. For descriptions, `-webkit-line-clamp` gives a clean three-line cut with `…`.
>
> `text-wrap: balance` on headlines makes them much more attractive — quick live demo by toggling it in DevTools.

---

## 3. Opacity, Filters & Icons

### Slides

- **`opacity: 0`** — makes the **whole element and its children** transparent (still occupies space, still clickable if not paired with `visibility`)
- Prefer **`rgba()` / slash notation** when you want only the *background* faded, not the text
- **`filter`** — `blur()`, `grayscale()`, `sepia()`, `brightness()`, `contrast()`, `hue-rotate()`, `saturate()`, `drop-shadow()`
- Filters compose left→right; `drop-shadow` follows alpha, `box-shadow` does not
- **`backdrop-filter`** — blurs what is *behind* the element (glass effect) — heavy on GPU, use sparingly
- Applying filters on `:hover` for feedback
- **Icons**: inline SVG (styable, accessible, no font) vs icon fonts (legacy) vs icon libraries
- Styling SVG: `fill`, `stroke`, `stroke-width`, `currentColor` inherits from `color`

### Code

```css
/* only the card fades */
.card {
  background: rgb(255 255 255 / 0.7); /* rgba works too */
}

/* the whole box incl. text fades */
.card-faded {
  opacity: 0.4;
}

/* filters */
.thumb {
  filter: grayscale(100%);
  transition: filter 0.2s ease;
}
.thumb:hover {
  filter: grayscale(0); /* colour on hover */
}

.glass {
  background: rgb(255 255 255 / 0.6);
  backdrop-filter: blur(8px);
}

/* SVG icons inherit text colour */
.icon {
  fill: currentColor;
  width: 1.25rem;
  height: 1.25rem;
}

.icon:hover {
  filter: brightness(1.1);
}
```

```html
<button class="btn" aria-label="Close">
  <svg class="icon" viewBox="0 0 24 24" aria-hidden="true">
    <path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" fill="none" />
  </svg>
  <span>Close</span>
</button>
```

### Talk track

> The classic mistake: `opacity: 0` to hide a background, but the button label goes invisible too. Make the distinction explicit — **`opacity` affects everything; `rgba()` on the background only affects the background**.
>
> `filter: grayscale(100%)` to `grayscale(0)` on hover is one of the most-used effects in card galleries — costs nothing, always readable. `drop-shadow` versus `box-shadow` matters for transparent PNGs/SVGs: `drop-shadow` follows the alpha shape; `box-shadow` draws a rectangle.
>
> `backdrop-filter` demos well but note the performance cost on low-end phones — it forces a backdrop repaint every frame. Use it for a sticky nav, not for every card.
>
> Icons: prefer **inline SVG**. It inherits `currentColor` (so it matches the button text automatically) and is fully accessible with `aria-hidden` plus a text label. Icon fonts date from 2014 and have accessibility and loading problems.

---

## 4. Sizing

### Slides

- **`width` / `height`** — but `height` is often the wrong tool; let content decide
- **`min-width` / `max-width`, `min-height` / `max-height`** — guard rails
- Content-based sizing keywords: **`auto`**, **`fit-content`**, **`min-content`**, **`max-content`**
  - `max-content` — as wide as the longest unbreakable line
  - `min-content` — as narrow as the longest word (no wrapping beyond that)
  - `fit-content` — grow to content, but respect the container
- **`aspect-ratio: 16 / 9`** — reserves the box before the image loads; replaces height hacks
- **Shorthand order matters**: `margin: top right bottom left` (clockwise) — `margin: 10px 20px` = top/bottom 10, left/right 20

### Code

```css
.card {
  width: 320px;
  max-width: 100%; /* never wider than its parent */
}

.media {
  aspect-ratio: 16 / 9;
  width: 100%;
  object-fit: cover;
}

.actions {
  display: flex;
  gap: 0.5rem;
  width: fit-content;
}

.quote {
  width: min-content; /* shrinks to the longest word */
}
```

```text
width keywords:  auto        — normal flow behaviour
                 fit-content  — grow to content, capped by container
                 max-content  — longest line, no wrapping
                 min-content  — longest word, forces wrapping
```

### Talk track

> The message: **let content size itself where you can**. Fixed `height` on a text card breaks the moment someone zooms to 200% — a WCAG failure. Use `max-width` + `aspect-ratio` instead.
>
> `fit-content` in a flex row is the clean way to keep a button group from stretching. Demo `min-content` on a paragraph: it collapses to the longest word — useful for sidebar labels, dangerous for body copy.
>
> Shorthand order is a common exam question. Say the mnemonic out loud: **top, right, bottom, left** (clockwise from 12 o'clock).

---

## 5. Display

### Slides

- **`display: block`** — full width, starts a new line (`div`, `p`, `h1`)
- **`display: inline`** — flows inside text, ignores width/height (`span`, `a`, `strong`)
- **`display: inline-block`** — inline flow **but** respects width/height and margins
- **`display: flex` / `inline-flex`**, **`display: grid` / `inline-grid`** — layout engines (Session 5 goes deep)
- **`display: none`** — removed from layout entirely (no space, not read by screen readers)
- **`visibility: hidden`** — occupies space, invisible, not announced
- **`opacity: 0`** — occupies space, invisible, but **still focusable/clickable** and read by some tools
- When a `div` becomes a flex/grid container, its **direct children** become flex/grid items

### Code

```css
a { display: inline; }

.tag {
  display: inline-block;
  padding: 0.25rem 0.5rem; /* works because inline-block honours box */
}

.row {
  display: flex;
  gap: 1rem;
}

/* three ways to hide */
.hide-none { display: none; }        /* gone from layout */
.hide-vis  { visibility: hidden; }   /* space kept */
.hide-fade { opacity: 0; }           /* space kept, still clickable */
```

```html
<p>
  An <a href="#">inline link</a> stays in the sentence,
  but a <span class="tag">tag</span> can have padding.
</p>
<div class="row"><div>Item</div><div>Item</div></div>
```

### Talk track

> Use the DevTools element picker to show `display: inline` ignoring `width` — this is one of the top beginner bugs ("my link won't get bigger").
>
> The three "hide" values are an interview favourite. Drive it home with a use case each: **`display: none`** for toggling menus, **`visibility: hidden`** when you must reserve space (skeleton loading), **`opacity: 0`** only for fade transitions — and remember it stays clickable, so add `pointer-events: none` or use `display`.
>
> Introduce flex/grid here as "containers" but don't go deep — that is Session 5. Just make the mental model stick: parent gets `display: flex`, children become items automatically.

---

## 6. The Box Model

### Slides

- Every element is a box: **content → padding → border → margin**
- **content** = text/image area; **padding** = inside space; **border** = the edge; **margin** = outside space (transparent)
- **`box-sizing: content-box`** (default): `width` = content only, padding/border add on top
- **`box-sizing: border-box`**: `width` includes padding + border — **predictable sizing**, set it globally
- The DevTools box-model overlay shows each layer with its colour
- **Margin collapsing**: adjacent vertical margins merge into one (the larger wins), and parent/child margins collapse
- Fix collapsing with: padding/border on the parent, `flex`/`grid` children, or `overflow: hidden`

### Code

```css
/* the global reset everyone ships */
*,
*::before,
*::after {
  box-sizing: border-box;
}

.card {
  width: 320px;          /* with border-box: total box = 320px */
  padding: 1rem;
  border: 1px solid #e2e8f0;
  margin-block-end: 2rem;
}

/* prevent margin collapse: give the parent a "fence" */
.parent {
  overflow: hidden; /* or padding, border, display: flow-root */
}
```

```text
content-box:  width(300) + padding(32) + border(2) = 334px total
border-box:   width(300)  → total is 300, content shrinks
```

### Talk track

> This is the slide that fixes half the bugs students hit. Draw the two boxes on the board: content-box balloons past the parent, border-box stays inside. Then say the rule they will use for the rest of the course: **set `box-sizing: border-box` globally in the reset**.
>
> Show the DevTools overlay (Elements → Computed → box model) — the colour-coded rings make padding vs margin unmistakable. Have students put their mouse over each ring live.
>
> Margin collapsing is the other classic surprise: two paragraphs with `margin: 1rem 0` show 1rem, not 2rem, between them. It is *by design*. Demonstrate `display: flow-root` as the modern fix (cleaner than `overflow: hidden`, which creates a scroll container).

---

## 7. Position

### Slides

- **`position: static`** — default; normal flow, ignores `top/right/bottom/left`
- **`position: relative`** — stays in flow, offsets shift it visually (space stays where it was)
- **`position: absolute`** — out of flow; positioned relative to the **nearest positioned ancestor** (or the initial containing block)
- **`position: fixed`** — relative to the **viewport**, stays on scroll
- **`position: sticky`** — hybrid: acts `relative` until its threshold is hit, then `fixed`
  - Needs `top`/`bottom` **and** a scrollable ancestor, and no `overflow: hidden` on parents
- **Stacking context** — elements with `position` + `z-index`, plus `transform`, `filter`, `opacity < 1`, etc.
- **`z-index`** only competes **within the same stacking context** — `z-index: 9999` can still lose to a parent's context
- `transform` and `filter` accidentally create stacking contexts — a very common bug source

### Code

```css
.badge { position: relative; }
.badge span { position: absolute; top: -0.5rem; right: -0.5rem; }

.tooltip { position: absolute; left: 50%; transform: translateX(-50%); }

.navbar {
  position: sticky;
  top: 0;
  z-index: 10;
  background: white;
}

.modal-backdrop { position: fixed; inset: 0; background: rgb(0 0 0 / 0.5); }
```

```html
<div class="parent" style="position: relative">
  <div class="child" style="position: absolute; top: 0; right: 0">X</div>
</div>
```

### Talk track

> Anchor the five values in use cases, not definitions: **static** = normal, **relative** = small nudges + anchor for children, **absolute** = badges/overlays, **fixed** = sticky bars/modals, **sticky** = headers that pin.
>
> The containing-block rule for `absolute` is the single hardest concept here: it looks at the **nearest ancestor with a position other than static**, not necessarily the direct parent. If nothing is positioned, it escapes to the viewport. Demo by removing `position: relative` from the parent and watching the badge fly to the page corner.
>
> On stacking: the classic "my dropdown is behind the hero" bug. Explain that `z-index: 9999` fails because the element lives inside a parent that created its own stacking context (often via `transform` or `opacity`). Fix is at the ancestor level. This is worth spending real minutes on — students hit it for years.

---

## 8. Border, Shadows & Overflow

### Slides

- **`border`** shorthand: `width style colour` — styles: `solid`, `dashed`, `dotted`, `double`, `none`
- Per-side: `border-top`, `border-inline-start` (logical, RTL-safe)
- **`border-radius`** — round corners; elliptical with two values `border-radius: 50% / 25%`
- **`outline`** vs **`border`**: outline draws *outside* the box and **does not affect layout** — use for focus rings with **`outline-offset`**
- **`:focus-within`** — style a group when any child receives focus (forms, cards with inputs)
- **`box-shadow`**: `offset-x offset-y blur spread color`; multiple via commas; **`inset`** for inner shadows
- **`drop-shadow`** (filter) for transparent PNGs/SVGs — follows alpha shape
- **`overflow`**: `visible`, `hidden`, `scroll`, `auto`, plus `overflow-x`/`overflow-y`; **`scroll-behavior: smooth`**
- **`clip-path`** — clip an element to a shape (circle, polygon, inset)

### Code

```css
.card {
  border: 1px solid #e2e8f0;
  border-radius: 0.75rem;
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  overflow: hidden; /* clips children to the radius */
}

.card:hover {
  box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.12);
}

/* focus ring that never shifts layout */
button:focus-visible {
  outline: 2px solid var(--color-brand);
  outline-offset: 2px;
}

/* group focus */
.form-row:focus-within {
  background: #f8fafc;
}

/* smooth anchor scrolling */
html {
  scroll-behavior: smooth;
}

/* clip to a shape */
.hero {
  clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);
}
```

```text
box-shadow: h-offset v-offset blur spread color  (optional "inset")
            0            4px   6px  -1px  rgb(...)
```

### Talk track

> **Never remove outlines** — restyle them. `outline` does not take layout space, so it is the perfect focus indicator; `outline-offset` separates it from the border. If you must use a border ring, keep `:focus-visible` so mouse users aren't annoyed but keyboard users always see focus.
>
> Shadows: teach the *feel*, not the numbers. Small blur + small offset = subtle card; larger blur + bigger offset = elevated/hover. Show the same card at rest and hover — that delta is how elevation reads.
>
> `overflow: hidden` on the card is what makes children respect `border-radius` — otherwise a background image pokes out of the rounded corners. But warn: `overflow: hidden` on a parent **breaks `position: sticky`** for descendants — show that bug live.
>
> `clip-path` is the one-line way to do angled hero sections. Keep it brief; it previews transforms (Session 4).

---

## Recap / Checkpoints

- **Fonts**: system stack by default; `@font-face` + `font-display: swap` for web fonts; variable fonts for weight ranges
- **Text**: build a **type scale** as tokens; unitless `line-height`; `text-wrap: balance`/`pretty`; truncation with `ellipsis` or `-webkit-line-clamp`
- **Opacity vs `rgba`**: `opacity` fades everything; `rgba()`/slash fades only the background
- **Filters**: `grayscale`/`blur`/`drop-shadow` on hover for cheap feedback; `backdrop-filter` sparingly; inline SVG icons with `currentColor`
- **Sizing**: `max-width`, `aspect-ratio`, `fit-content`; shorthand order = **top right bottom left**
- **Display**: block vs inline vs inline-block; `none` vs `visibility: hidden` vs `opacity: 0`
- **Box model**: content → padding → border → margin; ship `box-sizing: border-box` globally; margin collapsing and its fixes
- **Position**: static, relative, absolute (nearest *positioned* ancestor), fixed, sticky (+ its requirements)
- **Stacking**: `z-index` wins only inside one stacking context; `transform`/`filter`/`opacity` create contexts
- **Border & shadow**: outline for focus (`outline-offset`), never deleted; `box-shadow` for elevation; `overflow: hidden` clips to radius but breaks `sticky`

---

## Mini Project

Build a **profile card** page combining this session:

- A card with `border`, `border-radius`, and layered `box-shadow`
- Correct spacing using `padding` + `margin` with `box-sizing: border-box` globally
- `aspect-ratio` image (no fixed height), truncated description with `text-overflow: ellipsis` or line clamp
- A sticky header using `position: sticky`
- A badge pinned with `position: absolute`
- Hover elevation (shadow change) and a `:focus-visible` outline
- Text on a **type scale** with unitless `line-height`

Keep it **without copying** the complete example from Session 1 — this one must stand on the box model and positioning you just learned.
