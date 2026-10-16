# Session 2A — Fonts, Text, Opacity

**Duration:** 2.5 hours — **Goal:** Master typography and visual effects.

## 1. Fonts
### Slides
- font-family, system stack, fallbacks
- @font-face, font-display, web fonts, variable fonts
### Code
`css
body{font-family:system-ui,sans-serif}
` 
### Talk track
> Prefer system fonts for speed; use font-display: swap if loading web fonts.

## 2. Text
### Slides
- type scale, line-height (unitless), letter-spacing, text-align, white-space, overflow-wrap, word-break, text-wrap: balance/pretty, ::marker
### Code
`css
p{line-height:1.6; text-wrap:pretty}
` 
### Talk track
> Unitless line-height scales with font-size.

## 3. Opacity, Filters & Icons
### Slides
- opacity vs rgba, filter, backdrop-filter, SVG styling (fill/stroke)
### Code
`css.fade{opacity:.8}.blur{filter:blur(4px)} svg{fill:currentColor}
` 
### Talk track
> opacity affects children; use rgba for bg only.

## Recap
- Typography + opacity mastered.
