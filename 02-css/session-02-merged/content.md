# Session 2 — Fonts, Text, Opacity, Sizing, Display, Box Model, Position, Borders, Shadows, Overflow

**Duration:** 5 hours — **Goal:** Control typography, visual effects, sizing, placement, and visual chrome.

## 1. Fonts
### Slides
- font-family, system font stack, fallbacks
- @font-face, font-display, web fonts, variable fonts
### Code
`css
body{font-family:system-ui,sans-serif}
` 
### Talk track
> Prefer system fonts for performance; use font-display:swap when loading web fonts.

## 2. Text
### Slides
- type scale, line-height (unitless), letter-spacing, text-align, text-transform, white-space, overflow-wrap, word-break, text-wrap: balance/pretty, ::marker
### Code
`css
p{line-height:1.6; text-wrap:pretty}
` 
### Talk track
> Unitless line-height scales proportionally with font size.

## 3. Opacity, Filters & Icons
### Slides
- opacity vs rgba/tokens, filter (blur/grayscale/brightness/contrast), backdrop-filter, SVG fill/stroke
### Code
`css.fade{opacity:.8}.blur{filter:blur(4px)} svg{fill:currentColor}
` 
### Talk track
> opacity affects children; use rgba for background only.

## 4. Sizing
### Slides
- width/height, min/max, fit-content/min-content/max-content, aspect-ratio
### Code
`css.box{width:10rem; aspect-ratio:16/9}
` 
### Talk track
> Avoid fixed heights unless necessary.

## 5. Display
### Slides
- block/inline/inline-block/inline-flex/inline-grid, display:none vs visibility:hidden vs opacity:0
### Code
`css.flex{display:flex}
` 
### Talk track
> display:none removes from layout flow.

## 6. The Box Model
### Slides
- content/padding/border/margin, box-sizing:border-box, margin collapsing
### Code
`css*{box-sizing:border-box}
` 
### Talk track
> Use border-box globally to make sizing predictable.

## 7. Position
### Slides
- static/relative/absolute/fixed/sticky, containing block, stacking context, z-index pitfalls
### Code
`css.abs{position:absolute;top:0;left:0}
` 
### Talk track
> Absolute positions relative to the nearest positioned ancestor.

## 8. Border, Shadows & Overflow
### Slides
- border-radius, outline vs border, box-shadow, drop-shadow, overflow, clip-path
### Code
`css.card{border-radius:.75rem;box-shadow:0 8px 24px rgba(0,0,0,.08);overflow:hidden}
` 
### Talk track
> Elevation via shadows, focus via outline (not removed).

## Recap / Checkpoints
- Typography and effects ready
- Layout, box model, positioning, and visual chrome controlled
