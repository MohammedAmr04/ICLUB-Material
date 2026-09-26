# CSS + Tailwind Bootcamp (7 Sessions)

- **Level**: Beginner
- **Sessions**: 7 (6 CSS + 1 Tailwind)
- **Final Project**: GameZone Landing Page — built twice, once in CSS and once
  in Tailwind
- **Previous Track**: [HTML Bootcamp](./01-html.md)
- **Next Track**: [JavaScript Bootcamp](./03-javascript.md)

------------------------------------------------------------------------

## Prerequisites

-   Completed the [HTML Bootcamp](./01-html.md)
-   Can write semantic HTML without help
-   The DevTools Elements panel is familiar

## Sessions

-   [Session 1 — Fundamentals, Cascade & Selectors](#session-1--fundamentals-cascade--selectors)
-   [Session 2 — The Box Model, Display & Position](#session-2--the-box-model-display--position)
-   [Session 3 — Typography, Colors & Backgrounds](#session-3--typography-colors--backgrounds)
-   [Session 4 — Transforms, Transitions & Animation](#session-4--transforms-transitions--animation)
-   [Session 5 — Flexbox & Grid](#session-5--flexbox--grid)
-   [Session 6 — Variables, Theming & Responsive Design](#session-6--variables-theming--responsive-design)
-   [Session 7 — Tailwind](#session-7--tailwind)
-   [Final Deliverables](#final-deliverables)
-   [Assessment](#assessment)

> **Core vs optional**: every topic under `## Topics` is required. Anything
> under `### Optional Extensions` is a bonus — it will not appear in the
> assessment unless stated otherwise.

> **Why Tailwind is one session here**: it is a productivity tool, not a new
> mental model. Everything it does — spacing, layout, hierarchy, state
> handling, responsiveness — was already taught in Sessions 1–6. Session 7 maps
> those concepts onto utility classes. If you already use Tailwind at work, you
> can skip it and go straight to the JavaScript track.

> **Version note**: Session 7 is written against **Tailwind CSS v4** (CSS-first
> configuration, `@import "tailwindcss"`, `@theme`). v3 used a JavaScript config
> file and `@tailwind base/components/utilities`. The setup steps differ
> completely between the two — verify the installed version first.

------------------------------------------------------------------------

# Session 1 — Fundamentals, Cascade & Selectors

**Duration**: 4 hours — **Goal**: understand how the browser resolves conflicting
styles, and style a page without touching layout.

## Topics

### How CSS Works

-   What CSS is and the problem it solves
-   Inline vs internal vs external stylesheets, and why external wins
-   Browser defaults and the user-agent stylesheet
-   A minimal reset and `box-sizing: border-box` globally
-   Inspecting and live-editing styles in DevTools

### Syntax

-   Rule structure: selector, block, property, value
-   Multi-value shorthands and what they expand to
-   Comments `/* */` and section banners
-   `styles.css` and how to link it

### Selectors

-   Universal `*`, type, class, ID
-   Grouping with commas
-   Descendant, child (`>`), and adjacent sibling (`+`) combinators
-   Attribute selectors: `[data-x]`, `[type="text"]`
-   Pseudo-classes: `:hover`, `:focus-visible`, `:disabled`, `:first-child`,
    `:nth-child()`
-   Pseudo-elements: `::before`, `::after`, `::placeholder`, `::selection`
-   Specificity calculated step by step
-   `!important` and the cascade order of origins
-   `@supports` feature queries — how to use a new feature safely without
    breaking older browsers

### Inheritance

-   Which properties inherit and which do not
-   The initial value, the inherited value, and the cascade
-   When `inherit`, `initial`, and `unset` are the right answer

### Units

-   Absolute: `px`, `pt`, `cm`
-   Relative: `rem`, `em`, `%`
-   `rem` vs `em` and when each is correct
-   Viewport units: `vw`, `vh`, `vmin`, `vmax`
-   `clamp()`, `min()`, `max()` for fluid values
-   Why spacing should almost always use `rem`

### Colors

-   Named, `hex`, `rgb()`, `rgba()`, `hsl()`
-   Modern `oklch()` and why it is easier to reason about
-   The custom-property shorthand for brand colors
-   Contrast ratios and WCAG AA

## Live Coding

-   Restyle a page from the HTML track using only the DevTools inspector
-   Predict the winner of six specificity battles, then verify

## Homework

-   **Typography Practice**: a text-heavy page with a type scale, a spacing
    rhythm, and a consistent ramp

------------------------------------------------------------------------

# Session 2 — The Box Model, Display & Position

**Duration**: 5 hours — **Goal**: control the size and placement of every
element precisely.

## Topics

### The Box Model

-   Content, padding, border, margin
-   The DevTools box-model overlay
-   `box-sizing: border-box` as the default
-   Margin collapsing and how to prevent it

### Sizing

-   `width`, `height`, and when `height` is the wrong tool
-   `min-width` / `max-width` and `min-height` / `max-height`
-   Content-based sizing: `auto`, `fit-content`, `min-content`, `max-content`
-   `aspect-ratio` instead of height hacks
-   Shorthand order: `margin: 10px 20px` and friends

### Display

-   `block`, `inline`, `inline-block`, `inline-flex`, `inline-grid`
-   `display: none` vs `visibility: hidden` vs `opacity: 0`
-   When a `div` becomes a flex or grid container

### Position

-   The five values: `static`, `relative`, `absolute`, `fixed`, `sticky`
-   `sticky` and the conditions it needs
-   Positioning relative to which ancestor
-   Absolute positioning with no positioned parent
-   Stacking context and `z-index`
-   `z-index: 9999` and why it never works
-   How `transform` and `filter` create a stacking context by accident

### Borders, Shadows & Overflow

-   `border` shorthand and per-side borders
-   `border-style` values
-   `border-radius`, including elliptical corners
-   `outline` vs `border` for focus styles, and `outline-offset`
-   `:focus-within` for styling a group when any child has focus
-   `box-shadow` with spread, multiple shadows, and inset
-   `drop-shadow` for transparent PNGs
-   `overflow`, `overflow-x`, and `scroll-behavior`
-   Clipping with `clip-path`

## Live Coding

-   Center an element four different ways
-   Build a tooltip with `absolute` and a dropdown with `fixed`

## Homework

-   **Card Gallery**: six cards with shadows, hover elevation, and a sticky
    header

## Project Work

-   **Profile Card**: your info and image with correct spacing, a reset, and a
    hover effect — using `box-sizing`, `position`, and `box-shadow` only

------------------------------------------------------------------------

# Session 3 — Typography, Colors & Backgrounds

**Duration**: 4 hours — **Goal**: control type and colour with a deliberate
system.

## Topics

### Fonts

-   `font-family` and the system font stack
-   Fallback fonts and `font-display`
-   `@font-face` and self-hosting
-   Web fonts from a CDN and their performance cost
-   Variable fonts and the `font-weight` range
-   Local vs web fonts, and when each is right

### Text

-   `font-size` with a type scale
-   `line-height` as a unitless multiplier vs a length
-   `font-weight`, `font-style`, `font-stretch`
-   `letter-spacing` and readability
-   `text-transform` vs typing in caps
-   `text-align`, `text-indent`
-   `white-space`, `word-break`, `overflow-wrap`
-   Truncating one line and multiple lines with `-webkit-line-clamp`
-   `text-wrap: balance` and `text-wrap: pretty` for headlines and body copy
-   `::marker` for styling list bullets and numbers
-   `writing-mode` (brief)

### Color Systems

-   Contrast ratios checked in DevTools
-   Building 5–8 semantic tokens instead of 20 random hex values
-   `color-mix()` for deriving shades
-   `currentColor`

### Backgrounds

-   `background-color`, `background-image`
-   `background-size`, `-position`, `-repeat`
-   The `background` shorthand and what it resets
-   `linear-gradient`, `radial-gradient`, `conic-gradient`
-   Repeating gradients for patterns without an image
-   Multiple backgrounds and their stacking order
-   `background-clip: text`

### Opacity, Filters & Icons

-   `opacity` vs `rgba()` vs a translucent token
-   `filter`: `blur`, `grayscale`, `sepia`, `brightness`, `contrast`
-   `backdrop-filter` and its stacking-context side effect
-   Applying filters on hover
-   Icons: inline SVG vs icon font vs an icon library
-   Styling SVG with `fill`, `stroke`, and CSS inside it

## Live Coding

-   Rebuild a type scale from a design screenshot
-   Match three gradients and verify the contrast ratio of each

## Homework

-   **Hero Section**: a landing hero with a layered gradient, a clipped shape,
    and a type scale

## Project Work

-   **Favorite Movie Showcase (part 1)**: structure, type scale, color tokens,
    and backgrounds — no animation yet

------------------------------------------------------------------------

# Session 4 — Transforms, Transitions & Animation

**Duration**: 4 hours — **Goal**: add motion that communicates, plus the
accessibility rules that come with it.

## Topics

### Transforms

-   `transform` with `translate`, `scale`, `rotate`, `skew`
-   Multiple functions and why order matters
-   `transform-origin`
-   `translate` vs `margin` / `left`
-   2D vs 3D: `perspective`, `rotateX/Y`, `translateZ`, `backface-visibility`

### Transitions

-   The `transition` shorthand and its four parts
-   Which properties can and cannot be animated
-   Animating `transform` and `opacity` for performance
-   Multiple transitions
-   `cubic-bezier()`, `linear()`, `steps()`
-   Entrance, hover, and exit states with `transition-delay`

### Keyframe Animation

-   `@keyframes` with percentages or `from` / `to`
-   The `animation` shorthand and the longhands
-   `animation-iteration-count` and `animation-direction`
-   `animation-fill-mode` and why it matters
-   Multiple animations and `animation-composition`
-   `animation-play-state`

### Motion Design & Accessibility

-   Easing: why `ease-in-out` feels natural
-   Duration guidelines (roughly 150–300ms for UI feedback)
-   `prefers-reduced-motion` and a real fallback
-   When not to animate at all
-   `will-change` and why you must not apply it everywhere
-   `@starting-style` and `transition-behavior: allow-discrete` for entrance and
    exit animations without a class toggle
-   Scroll-driven animation with `animation-timeline: view()` and
    `scroll()` — the native alternative to `IntersectionObserver`
-   `requestAnimationFrame` and the 16.7ms frame budget, from the JS side

### Optional Extensions

-   Cross-document and same-document view transitions:
    `@view-transition` and `view-transition-name`
-   Anchor positioning: `anchor-name` and `position-anchor`
-   `interpolate-size` and `calc-size()` for animating intrinsic sizes
-   `field-sizing: content` for auto-sizing form controls
-   `overscroll-behavior` and scroll chaining control

## Live Coding

-   Animate a card on hover: lift, shadow, and image zoom
-   Add a keyframe intro that respects `prefers-reduced-motion`

## Homework

-   **Animated Profile Card**: entrance animation, hover state, and a skeleton
    shimmer

## Project Work

-   **Favorite Movie Showcase (final)**: the page from Session 3 plus entrance
    animations, hover transitions, a poster zoom, and a reduced-motion
    fallback

------------------------------------------------------------------------

# Session 5 — Flexbox & Grid

**Duration**: 6 hours — **Goal**: master both layout systems and know which one
to reach for.

> This is the longest CSS session. If you are running short, take Flexbox here
> and Grid in the first hour of Session 6.

## Topics

### The Flex Model

-   Flex container, flex items, main axis, cross axis
-   The mental model: one dimension, distributed along an axis

### Direction & Wrapping

-   `flex-direction` and the reverse values
-   `flex-wrap` and `flex-flow`

### Distribution & Alignment

-   `justify-content`, `align-items`, `align-content`, `align-self`
-   `place-content`
-   `gap`, `row-gap`, `column-gap` and why it beats margins

### Sizing in Flex

-   `flex-grow`, `flex-shrink`, `flex-basis`, and the `flex` shorthand
-   `flex: 1` vs `flex: 1 1 0` vs `flex: auto`
-   `min-width: 0` and the overflow bug everyone hits
-   `order` and when not to use it

### Flex Patterns

-   Perfect centering
-   A navbar with a pushed item
-   A media object (image + text)
-   An equal-width wrapping card row

### The Grid Model

-   Grid container, items, tracks, lines, explicit vs implicit
-   `grid-template-columns` / `rows`, `fr`, `repeat()`, `minmax()`
-   `auto` vs `1fr` vs `minmax(0, 1fr)`
-   The `repeat(auto-fill, minmax(...))` pattern
-   `auto-flow`, `grid-column`, `grid-row`, and `span`
-   `justify-items`, `align-items`, `place-items`, `place-self`
-   Named lines and `grid-template-areas`
-   `subgrid` (note) and nested grids
-   Overlapping items for hero layouts

### Choosing

-   Grid vs Flex: a decision rule
-   Grid for page and section layout, Flex for components and alignment
-   Refactoring one into the other and explaining the difference

## Live Coding

-   Recreate three common headers with Flexbox only
-   Fix the classic `overflow` inside a flex item bug
-   Build a photo gallery with `auto-fill` and zero media queries

## Homework

-   **Dashboard Grid**: a stats row, a chart area, and a sidebar that stays
    fixed while content scrolls

------------------------------------------------------------------------

# Session 6 — Variables, Theming & Responsive Design

**Duration**: 6 hours — **Goal**: write CSS that scales, themes cleanly, and
survives every screen.

> The variables and theming half can move into Session 7 if you need the room.

## Topics

### Custom Properties

-   Declaring and using variables with `var()`
-   Fallback values inside `var()`
-   Scope: `:root` vs a scoped selector
-   Inheriting variables
-   Theming by overriding variables on one element
-   `@property` for typed, animatable custom properties

### The Cascade, Revisited

-   `@layer` and the layer order
-   When layers beat specificity
-   Layers as base / components / utilities
-   Keeping specificity flat

### Advanced Selectors

-   `:is()`, `:where()`, `:not()`
-   `:has()` and relational selectors
-   Nesting and `&`
-   Native CSS nesting and its support story

### Dark Mode

-   `prefers-color-scheme`
-   A manual toggle via `data-theme` on the root
-   Why you swap tokens and never write a second set of rules
-   `light-dark()` and the CSS-only alternative to a JS toggle
-   Persisting the choice and avoiding a flash of the wrong theme
-   The `color-scheme` property

### Conventions

-   BEM vs utility-first vs a hybrid, and the trade-offs
-   Naming that survives refactoring
-   Reusable component CSS
-   `@media print` essentials
-   When a preprocessor or build tool is worth it
-   `!important` as a symptom

### Responsive Strategy

-   Responsive vs adaptive vs fluid
-   Mobile-first vs desktop-first, and why mobile-first scales better
-   Content-driven breakpoints, not device-driven ones
-   Resilience: what happens when a heading wraps to four lines

### Media Queries

-   `@media` syntax: `screen`, `print`, features
-   `min-width` over `max-width`
-   Range syntax `(width >= 48rem)`
-   Logical operators, and `,` vs `and`

### Responsive Units

-   `%` vs `fr` vs `auto`
-   `vw` / `vh` and the scrollbar problem
-   `dvh`, `svh`, `lvh` and mobile browser chrome
-   `ch`
-   Fluid typography with `clamp()`

### Images & Media

-   `srcset`, `sizes`, and `<picture>` art direction
-   `width` / `height` to prevent layout shift
-   `loading="lazy"` and `fetchpriority`
-   `image-set()` for background images
-   `aspect-ratio` boxes for media

### Scroll Behaviour & RTL

-   `scroll-behavior: smooth` and the `prefers-reduced-motion` guard
-   `scroll-snap-type` and `scroll-snap-align` for galleries and carousels
-   `scroll-margin-top` and `scroll-padding-top` so anchor targets are not
    hidden under a sticky header
-   Logical properties: `margin-inline`, `padding-inline`, `inset-inline`,
    `border-inline-start` and the rest
-   Why logical properties are the only sane way to support `dir="rtl"`
-   Testing an RTL layout with `dir="rtl"` in DevTools

### Container Queries

-   Why viewport queries are not always the right tool
-   `container-type`, `container-name`, `@container`
-   Container query units: `cqw`, `cqi`, `cqb`, `cqmin`
-   A reusable card that sizes itself

### Accessibility & Testing

-   `prefers-reduced-motion`, `prefers-color-scheme`, `prefers-contrast`
-   `pointer` vs `hover` queries for touch
-   Zoom and text-size resilience
-   Device mode in DevTools
-   Testing on a real phone, and why DevTools lies
-   The 320px and 4K sanity checks

### Optional Extensions

-   `content-visibility` and CSS containment for long pages
-   `contain-intrinsic-size` and avoiding layout shift with `content-visibility`
-   Page Transitions API vs view transitions
-   `@media print` taken seriously: a real print stylesheet

## Live Coding

-   Convert a page of hard-coded colors into tokens, then add dark mode in
    under ten lines of new CSS
-   Take a fixed-width layout and make it fluid with no media query
-   Turn a component into a container-query component

## Homework

-   **Themed Component Kit**: a card, a button set, and a badge driven by
    tokens, with a working light/dark toggle
-   **Responsive Portfolio**: a page that survives 320px to 2560px

## Project Work

-   **GameZone Landing Page — version 1, hand-written CSS**
    -   Four sections: Home, Characters, Features, Gallery
    -   Navbar with a mobile menu and an active-link state
    -   Hero with a call to action
    -   Gallery built with Grid and responsive images
    -   Dark mode toggle driven by custom properties
    -   Loading skeleton and a reduced-motion fallback
    -   Container queries for at least one reusable component
    -   Verified at 320px, 768px, 1024px, and 1440px
    -   Keep this version. Session 7 rebuilds the same page in Tailwind, and
        comparing the two is the point.

------------------------------------------------------------------------

# Session 7 — Tailwind

**Duration**: 5 hours — **Goal**: rebuild the capstone with utility classes,
and be able to argue for either approach on a real project.

> Everything here was already taught in Sessions 1–6. This session only remaps
> those concepts onto class names. Nothing here is a new mental model.

## Topics

### Setup

-   What Tailwind is and the utility-first idea
-   The honest trade-off: design decisions move into the markup
-   Installing `tailwindcss` and `@tailwindcss/vite` in a Vite project
-   `@import "tailwindcss";` and what Preflight changes silently
-   Automatic content detection and what it ignores
-   Enabling class completions in your editor
-   Reading a generated rule in DevTools

### Reading It, Not Memorising It

-   Categories: layout, spacing, sizing, typography, colors, borders, effects,
    transitions
-   The standard scales — spacing `1` → `0.25rem`, the default breakpoints
-   Conflicts resolve by stylesheet order, not attribute order (`p-4 px-6`)
-   Reading the docs by pattern instead of guessing names
-   The two or three utilities you will actually use every day

### The Working Set

-   Spacing: `p-*`, `m-*`, `gap-*`, `space-*`, and negative values like `-mt-4`
-   Sizing: `w-*`, `h-*`, `size-*`, fractions `w-1/2`, `min-*`, `max-*`, `w-fit`
-   Layout: `flex`, `flex-col`, `grid`, `grid-cols-*`, `col-span-*`,
    `justify-*`, `items-*`
-   Position: `relative`, `absolute`, `fixed`, `sticky`, `inset-*`, `z-*`
-   Typography: `text-{size}`, `leading-*`, `tracking-*`, `font-*`, `truncate`,
    `line-clamp-*`
-   Colors: the `50`–`950` palette, `bg-*`, `text-*`, `border-*`, opacity
    modifiers like `bg-black/50`, gradients
-   Borders and effects: `border-*`, `rounded-*`, `shadow-*`, `ring-*`, `blur-*`
-   Motion: `transition-*`, `duration-*`, `scale-*`, `rotate-*`,
    `translate-*`, `motion-reduce:`

### Variants

-   `hover:`, `focus-visible:`, `active:`, `disabled:`, `checked:`
-   `valid:`, `invalid:`, `user-invalid:`
-   `first:`, `last:`, `odd:`, `even:`, `empty:`
-   `group-hover:*` and `peer-checked:*`, and a dropdown with no JavaScript
-   `data-[state=open]:*` and `aria-*` for driving UI from external state
-   `dark:` and the fact that it follows the OS by default

### Responsive

-   Mobile-first: the unprefixed class *is* the small screen
-   `sm: md: lg: xl: 2xl:`
-   Grouping variants and the override-order trap
-   `@container` and container query units (`w-cqw`, `text-cqi`)

### Configuration

-   `@theme` and the namespaces it exposes
-   What `--color-brand-500` unlocks: `bg-brand-500`, `text-brand-500`, and
    the rest
-   `@custom-variant`, `@utility`, `@plugin`
-   **The pitfall everyone hits**: `` `text-${color}-500` `` produces nothing at
    build time — and the fix, `@source inline(...)` for classes that only exist
    conditionally
-   The `cn()` helper — `clsx` + `tailwind-merge` — and why `tailwind-merge`
    exists
-   `@apply` works, and why the Tailwind team discourages it
-   `@theme inline` and when it is required instead of plain `@theme`
-   Arbitrary properties and child selectors: `[color:var(--x)]`, `[&>*]:mt-2`

### Choosing

-   CSS vs Tailwind: a decision rule
-   Cost of Tailwind: a build step, a dependency, a learning curve
-   When a plain stylesheet, a component, or a plugin is the better answer
-   Why `cn()` and a component API matter more than any individual class
-   What to learn next: CSS Modules, vanilla-extract, and the CSS-in-JS
    trade-off

### Optional Extensions

-   Custom plugins and the Tailwind plugin API
-   Container query syntax in detail, and named containers
-   The typography and forms plugins
-   Migrating a v3 project to v4
-   Debugging a build that silently drops classes

## Live Coding

-   Install Tailwind into the Session 6 project, rebuild the navbar, and
    inspect the generated rules
-   Break a component on purpose with a dynamic class name, then fix it with
    `cn()`

## Homework

-   Rebuild the Session 6 capstone in Tailwind

## Project Work

-   **GameZone Landing Page — version 2, Tailwind**
    -   The same four sections, the same behaviour
    -   Tokens in `@theme`; no raw hex value in any component
    -   `group`, `peer`, or `data-*` variants for every interactive state
    -   Container queries for at least two reusable components
    -   A persisted `dark:` toggle
    -   `motion-reduce:` on every animation
    -   A `cn()` helper and at least three shared components with a variant API
    -   No custom CSS file other than the `@theme` block and any `@keyframes`
    -   Verified at 320px, 768px, 1024px, and 1440px
-   **The comparison** — this is the actual deliverable
    -   Which version you shipped faster
    -   Which one you would rather maintain in six months
    -   One thing you would still write in plain CSS in the Tailwind version
    -   Where the Tailwind markup became harder to read
    -   Which one you would hand to a junior developer

------------------------------------------------------------------------

# Final Deliverables

-   Typography practice page (Session 1)
-   Profile Card (Session 2)
-   Favorite Movie Showcase (Sessions 3 & 4)
-   Dashboard Grid layout (Session 5)
-   Themed component kit with a dark mode toggle (Session 6)
-   **GameZone Landing Page — CSS version (Session 6)**
-   **GameZone Landing Page — Tailwind version (Session 7)**
-   **The written comparison of the two (Session 7)**

## Assessment

**Versions 1 and 2**

-   **Correctness**: no fixed pixel values where a fluid value works
-   **Responsiveness**: verified at 320px, 768px, 1024px, and 1440px
-   **Accessibility**: contrast passes AA in both themes, visible focus states,
    a `prefers-reduced-motion` / `motion-reduce` fallback, no animation as the
    only feedback
-   **RTL**: the layout survives `dir="rtl"` without editing one declaration,
    because the layout is built from logical properties
-   **Performance**: transforms and opacity for animation, `will-change` used
    sparingly, no layout shift from images
-   **Submission**: both versions pushed to a Git repository with a README

**Tailwind version only**

-   **Tokens**: colours, spacing, and type come from `@theme`; no raw values in
    components
-   **Correctness of composition**: `cn()` used wherever classes are
    conditional; no dynamically constructed class names
-   **Reuse**: shared components with a variant API; no duplicated class strings

**The comparison**

-   Specific, reasoned, and honest — not "Tailwind is better"
