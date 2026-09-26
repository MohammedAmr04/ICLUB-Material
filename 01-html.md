# HTML Bootcamp (2 Sessions)

- **Level**: Beginner
- **Sessions**: 2
- **Final Project**: Restaurant Menu & Order Page
- **Next Track**: [CSS Bootcamp](./02-css.md)

------------------------------------------------------------------------

## Prerequisites

-   Comfortable creating folders, files, and navigating your system
-   A code editor (VS Code recommended) with HTML support
-   No programming experience required

## Sessions

-   [Session 1 — Structure, Text, Links & Media](#session-1--structure-text-links--media)
-   [Session 2 — Forms, Semantics, Tables & Media](#session-2--forms-semantics-tables--media)
-   [Final Deliverables](#final-deliverables)
-   [Assessment](#assessment)

> **Core vs optional**: every topic under `## Topics` is required. Anything
> under `### Optional Extensions` is a bonus — it will not appear in the
> assessment unless stated otherwise.

> **Pacing note**: both sessions are dense. Session 1 is roughly
> 5 hours, Session 2 is roughly 6. If you need to split, the natural break is
> between "Forms" and "Semantics" inside Session 2.

------------------------------------------------------------------------

# Session 1 — Structure, Text, Links & Media

**Duration**: 5 hours — **Goal**: write a complete, valid, accessible page from
memory and navigate it correctly.

## Topics

### How HTML Works

-   What HTML is and the problem it solves
-   Parse, compile, render — how a file becomes a page
-   A local server (Live Server) and why you need one for modules later
-   Inspecting the DOM tree in DevTools

### Document Structure

-   `<!DOCTYPE html>` and why it must be the first line
-   The three required parts: `<html>`, `<head>`, `<body>`
-   Root attributes: `lang` and `dir`
-   `<meta charset="UTF-8">` and the viewport meta tag
-   Meta description, author, and Open Graph basics
-   `<link rel="preload">` and `<link rel="preconnect">` for critical resources
-   `<base>` and why it is almost never the answer
-   `<noscript>` and what graceful degradation looks like in practice
-   Parent / child relationships and how nested elements form a tree

### Tags, Elements & Attributes

-   Tag vs element vs content
-   Void elements: `img`, `br`, `hr`, `input`, `meta`, `link`
-   Attribute syntax, quoting, and boolean attributes
-   Case sensitivity and always writing lowercase

### Text Content

-   Comments `<!-- -->` and when not to use them
-   Headings `<h1>`–`<h6>` and the outline they create
-   Heading hierarchy rules and never skipping levels for styling
-   Paragraphs `<p>` and what may live inside one
-   `<br>` vs `&nbsp;` vs a new block element
-   Formatting: `<strong>`, `<em>`, `<small>`, `<mark>`, `<del>`
-   `<pre>` and `<code>`
-   `<abbr>`, `<cite>`, `<q>`, `<dfn>`

### Links

-   The `href` attribute
-   Absolute vs relative paths
-   Internal links and fragment links (`#id`)
-   `target="_blank"` and the security cost — always pair it with
    `rel="noopener noreferrer"`
-   Special schemes: `mailto:`, `tel:`, `sms:`
-   The `download` attribute
-   Clickable vs non-clickable links — the "fake link" anti-pattern

### Paths & File Structure

-   How the browser resolves `../` and `./`
-   Absolute paths from the project root and why they break
-   Recommended folder structure for a site
-   `index.html` and default documents

### Images

-   `img` and the required `alt`
-   Meaningful alt text vs decorative images (`alt=""`)
-   `width` and `height` and how they prevent layout shift
-   `loading="lazy"` and `decoding="async"`
-   `srcset` and `sizes` for responsive images
-   `<picture>` and when it beats `srcset` alone
-   Formats: JPEG, PNG, WebP, AVIF, SVG
-   When to use inline SVG vs a file

### Lists

-   `<ul>` and `<ol>`, plus `start`, `reversed`, `value`
-   Nested lists and why indentation comes for free
-   Description lists `<dl>`, `<dt>`, `<dd>`
-   When a list is the right element for navigation

### Entities

-   Named: `&nbsp;`, `&amp;`, `&lt;`, `&copy;`
-   Numeric: `&#169;` and `&#xA9;`
-   When escaping is mandatory
-   Non-breaking spaces and why they help with units
-   Bidi entities: `&lrm;`, `&rlm;`, `&ltr;`, `&rtl;` — and why mixed
    Arabic/Latin text needs them at the edges
-   `<bdo>` when a fragment genuinely needs a direction override

### Optional Extensions

-   Inline SVG: `viewBox`, scaling, and why inline beats an image file
-   `<canvas>` and the rare case that needs it
-   The `<template>` element
-   Web Components: custom elements and the Shadow DOM
-   The Microdata vocabulary (JSON-LD covers the same ground)

## Live Coding

-   Build the skeleton of a page from memory in ten minutes
-   Convert a plain text document into headings and paragraphs
-   Find and fix three intentionally broken documents

## Homework

-   **Personal Profile Page**: your name, a short bio, and your hobbies, with a
    nav bar of links and one image

## Project Work

-   Personal Profile Page as a valid HTML document, with correct heading
    hierarchy, a fragment-link table of contents, and a `<footer>`

------------------------------------------------------------------------

# Session 2 — Forms, Semantics, Tables & Media

**Duration**: 6 hours — **Goal**: build forms, meaningful page structure, and
data-rich content — then ship the capstone.

## Topics

### Forms & Inputs

-   The `form` element, `action`, `method` (`get` / `post`), and the query
    string
-   `name` and `value` — the only two things that actually get submitted
-   `autocomplete` and why you should not fight the browser
-   Text inputs: `text`, `email`, `password`, `search`, `tel`, `url`
-   `number` with `min`, `max`, `step`
-   `date`, `time`, `datetime-local`
-   `file` with `accept` and `multiple`
-   `checkbox` vs `radio` and how to group them
-   `range`, `color`, `hidden`
-   `readonly` vs `disabled`
-   `required`, `pattern`, `minlength`, `maxlength`
-   `placeholder` and why it is not a label

### Other Form Controls

-   `label` and `for` — the single accessibility rule that matters most
-   Wrapping a control in a label as an alternative
-   `select`, `option`, `optgroup`
-   `textarea` and its resizing behaviour
-   `datalist` for suggestions
-   `fieldset` and `legend` for related controls
-   `button` types: `submit`, `reset`, `button`

### Form Validation & UX

-   Native constraint validation
-   `:user-invalid` for styling invalid fields
-   Specific, readable error messages
-   `aria-describedby` to attach help text and errors
-   Grouping radios semantically, not by visual proximity

### Semantics & Structure

-   The three audiences: browsers, screen readers, search engines
-   The cost of a page built entirely from `div` and `span`
-   Landmarks: `<header>`, `<nav>`, `<main>`, `<footer>`
-   `<article>` vs `<section>`, and when each is correct
-   `<aside>`, `<address>`, `<time>`, `<figure>`, `<figcaption>`
-   `role` and `aria-*` as a last resort, never a shortcut
-   `div` vs `span` — when each one is right
-   `id` vs `class`, and when each is appropriate
-   The `hidden` attribute vs inline `display: none`
-   `data-*` for custom data
-   A skip link to the main content

### Tables

-   `table`, `caption`, `thead`, `tbody`, `tfoot`
-   `tr`, `th`, `td`
-   `scope` for screen readers
-   `colspan` and `rowspan`
-   Styling hooks without a class on every cell
-   Tables are for data, never for layout
-   Responsive tables in a scroll container

### Audio & Video

-   `audio` and `video` and their required attributes
-   `controls`, `autoplay` (and why it needs `muted`), `preload`
-   `<source>` with multiple formats
-   `<track>` for captions and subtitles
-   `poster` for thumbnails
-   `playsinline` on mobile

### Embedding

-   `iframe` for maps, video, and third-party widgets
-   `sandbox`, `allow`, `referrerpolicy`, `loading`
-   `title` on every iframe (accessibility)
-   `embed` and `object`, and why you should avoid them
-   The performance cost of third-party embeds

### ARIA: the Essentials

-   The first rule of ARIA: do not use it when a semantic element exists
-   `role`, and why `role="presentation"` strips semantics instead of adding
    them
-   Implicit landmark roles: `banner`, `navigation`, `main`, `contentinfo`,
    `search`
-   Live regions: `aria-live="polite"` for updates, `role="alert"` for
    something urgent
-   `aria-labelledby` and `aria-describedby` for names and descriptions
-   `aria-expanded` on a disclosure, and keeping it honest
-   `aria-current="page"` for the active nav link
-   `aria-hidden` and the accessibility tree
-   `aria-modal` and `role="dialog"` for modal dialogs
-   `aria-label` only when there is no visible text to point at
-   Reading the accessibility tree in DevTools, and what ARIA actually changes

### Optional Extensions

-   The native `<dialog>` element and `showModal()`
-   The `popover` attribute and `popovertarget`
-   Form-associated custom elements
-   Advanced SEO: `canonical`, `robots.txt`, sitemaps, `hreflang`
-   Advanced ARIA: live-region politeness debugging, and the ARIA Authoring
    Practices patterns

### Quality

-   Validating markup with the W3C validator
-   Reading HTML out loud as a debugging technique
-   SEO essentials: one `h1`, a meta description, meaningful link text
-   Structured data with `application/ld+json` and schema.org
-   Keyboard navigation and focus order in a static page

## Live Coding

-   Build a registration form with eight fields, fully labelled
-   Refactor a 200-line `div` soup page into semantic HTML
-   Build an accessible data table and compare the accessibility tree before
    and after

## Homework

-   **Registration Form**: name, email, password, confirm, date of birth,
    country select, terms checkbox — with native validation and no CSS

## Project Work

-   Restaurant Menu & Order Page — the track capstone
    -   Header with the restaurant name and a nav menu
    -   Menu as an accessible table: item, category, price, availability
    -   Order form with at least eight validated fields
    -   An embedded map or video with the correct `title` and `sandbox`
    -   Semantic landmarks, a skip link, and a meaningful `<footer>`
    -   Passes the W3C validator with zero errors

------------------------------------------------------------------------

# Final Deliverables

-   Personal Profile Page (Session 1)
-   Registration Form (Session 2)
-   **Restaurant Menu & Order Page — the capstone (Session 2)**

## Assessment

-   **Correctness**: valid markup, zero W3C validator errors
-   **Semantics**: meaningful elements, one `h1`, correct heading order, no
    `div` used where a landmark fits
-   **Accessibility**: every input has a label, every image has alt text,
    iframes have titles, the page is keyboard navigable
-   **ARIA**: used only where no semantic element fits, and correctly — an
    `aria-expanded` that matches reality, one live region, and no ARIA that
    duplicates a native element
-   **Structure**: relative paths, tidy folders, no inline styles or scripts
-   **Submission**: pushed to a Git repository with a README
