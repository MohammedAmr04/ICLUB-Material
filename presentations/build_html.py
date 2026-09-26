"""Builds the HTML Bootcamp deck (2 sessions) from 01-html.md.

Run:  python build_html.py
Out:  html-bootcamp.pptx
"""

import os

from deck import (
    ACCENT, add_footer, new_deck, save, slide_cards, slide_code, slide_compare,
    slide_content, slide_divider, slide_exercise, slide_recap, slide_table,
    slide_title, slide_two_col,
)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html-bootcamp.pptx")

S1 = "HTML Bootcamp / Session 1"
S2 = "HTML Bootcamp / Session 2"

prs = new_deck()

# ==========================================================================
# Front matter
# ==========================================================================

slide_title(
    prs,
    "ICLUB / BOOTCAMP MATERIAL",
    "HTML Bootcamp",
    "2 sessions  \u00b7  ~11 hours  \u00b7  beginner  \u00b7  no experience required",
    notes=(
        "Welcome. Two sessions, and by the end of the second one everyone has "
        "shipped a real page.\n\n"
        "Set the expectation early: this is not a survey of every HTML element "
        "that exists. It is the subset that 95% of real pages use, taught properly. "
        "Anything we skip here you can look up in two minutes once you know the shape "
        "of the language.\n\n"
        "Ask who has written HTML before. If hands go up, tell them this session will "
        "still change how they write it, because almost everyone self-taught HTML "
        "learned it the div-soup way."
    ),
)

slide_cards(
    prs,
    "What you will be able to do",
    [
        ("Write valid HTML", "A document that passes the W3C validator with zero errors."),
        ("Structure pages", "Landmarks, headings, and sections a screen reader can navigate."),
        ("Build real forms", "Labelled, validated inputs that actually submit usable data."),
        ("Handle data + media", "Accessible tables, video, and iframes."),
        ("Think semantically", "Choosing the element that describes meaning, not looks."),
    ],
    kicker="OUTCOME",
    notes=(
        "Read the capstone out loud, because it is the thing they are working toward: "
        "a restaurant menu and order page. Nobody finds that exciting when they hear "
        "the words, so make the bet explicit — by session 2 they will have built it."
    ),
)

slide_table(
    prs,
    "The two sessions",
    ["Session", "Focus", "Duration", "Deliverable"],
    [
        ["1", "Structure, text, links, media, lists, entities", "5 h", "Personal Profile Page"],
        ["2", "Forms, semantics, tables, media, ARIA", "6 h", "Restaurant Menu + Order Form"],
    ],
    kicker="AGENDA",
    widths=[1.3, 5.3, 1.3, 3.9],
    notes=(
        "Both sessions are long. Session 2 especially — if the room is going slow, the "
        "correct cut is to drop Tables, not to drop Forms. Forms are the part they will "
        "use every single day.\n\n"
        "Natural break if you need to split into two evenings: after 'Forms and Inputs' "
        "inside session 2, before 'Semantics'."
    ),
)

# ==========================================================================
# Session 1
# ==========================================================================

slide_divider(
    prs, 1, "Structure, Text, Links & Media", "~5 hours",
    "Write a complete, valid, accessible page from memory and navigate it correctly.",
    "How HTML works  \u00b7  document structure  \u00b7  tags & attributes  \u00b7  text content  \u00b7  "
    "links  \u00b7  paths & folders  \u00b7  images  \u00b7  lists  \u00b7  entities",
    notes=(
        "Timing plan for this session:\n"
        "- 25 min: how HTML works + document structure\n"
        "- 45 min: tags, attributes, text content\n"
        "- 35 min: links + paths (do these together, they are one idea)\n"
        "- 60 min: images\n"
        "- 30 min: lists + entities\n"
        "- 40 min: live coding\n"
        "- 20 min: homework brief\n\n"
        "If you fall behind, cut srcset/sizes and the optional extensions. Do not cut "
        "alt text \u2014 it is the single most important thing on the slide."
    ),
)

slide_content(
    prs,
    "What HTML actually is",
    [
        ("A vocabulary for describing what a thing is, not what it looks like", 0, "strong"),
        ("The browser reads it, builds a tree of objects, and paints that tree", 0, "plain"),
        ("<h1> says \u201cthis is the main heading\u201d \u2014 not \u201cthis is 32px bold\u201d", 0, "note"),
        ("CSS answers \u201chow does it look\u201d. HTML answers \u201cwhat is it\u201d", 0, "plain"),
        ("Get this backwards and you end up styling paragraphs because you could not "
         "find a heading element", 0, "plain"),
    ],
    kicker="WHY IT MATTERS",
    notes=(
        "The most common beginner bug in web development: reaching for a <div> because "
        "'I need it big and bold' instead of an <h1>. Frame the whole course around "
        "meaning-first, and styling-second.\n\n"
        "Analogy that works: HTML is the label on a shipping box, not the paint colour. "
        "Nobody at the warehouse cares what colour your box is; they care that it says "
        "FRAGILE in the right place."
    ),
)

slide_code(
    prs,
    "From file to pixels",
    """
  .html  \u2192  parse  \u2192  DOM tree  \u2192  render  \u2192  layout  \u2192  paint
  bytes      tokens       objects      box        positions  pixels
""",
    caption="Parse errors are recoverable. Wrong elements are not \u2014 the browser fixes "
            "your markup and then quietly gives you a page you did not design.",
    kicker="HOW IT WORKS",
    notes=(
        "Only explain this far. Students do not need to know about script blocking or "
        "critical rendering paths yet.\n\n"
        "The takeaway is the last line. HTML is fault-tolerant, which is a blessing when "
        "you are learning and a curse when you are shipping: a typo does not error, it "
        "just gives you something else. This is exactly why the W3C validator is part of "
        "the assessment."
    ),
)

slide_code(
    prs,
    "The minimum valid document",
    """
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
  &lt;meta charset="UTF-8"&gt;
  &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
  &lt;title&gt;My page&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Hello&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;""",
    kicker="DOCUMENT STRUCTURE",
    size=13,
    height=4.0,
    notes=(
        "Type this live, character by character, and let them predict each line before "
        "you write it. By the end of session 1 this should be muscle memory.\n\n"
        "Two lines to dwell on:\n"
        "- charset must be in the first 1024 bytes, so it goes first. Without it, Arabic "
        "text can render as mojibake.\n"
        "- viewport is what makes a page not zoom out weirdly on a phone. Missing it is "
        "the number-one reason a first website looks broken on mobile."
    ),
)

slide_cards(
    prs,
    "The three parts, and nothing else",
    [
        ("<head>", "Metadata. Not visible. Title, charset, viewport, links, scripts."),
        ("<body>", "Everything visible. This is the page."),
        ("The <html> element", "The root. Carries lang and dir. Not a container you style."),
    ],
    kicker="DOCUMENT STRUCTURE",
    cols=3,
    notes=(
        "Common misconception: that <head> can hold anything. It cannot hold visible "
        "content. If you want it on the page, it goes in <body>.\n\n"
        "Also: people try to put a <style> or <script> inside <body>. The browser will "
        "recover, but it is invalid \u2014 and it matters for performance, because the "
        "parser stops and executes."
    ),
)

slide_compare(
    prs,
    "lang and dir are not decoration",
    "What they buy you",
    [
        "Screen readers switch voice and pronunciation per language",
        "Browsers use it to pick the right font and hyphenation",
        "Search engines use it to target the right locale",
        "dir=\"rtl\" flips the whole document correctly",
        "Arabic, Hebrew, Persian and Urdu all need it",
        "It is one attribute and it is unfixable later",
    ],
    "What you lose without them",
    [
        "An Arabic page read by an English screen reader is unusable",
        "The browser picks a Latin font for Arabic text",
        "Your page shows up for the wrong language searches",
        "You rebuild the entire layout to flip it",
        "Mirrored padding needs per-direction overrides",
        "One attribute, retrofitted across the whole codebase",
    ],
    kicker="DOCUMENT STRUCTURE",
    notes=(
        "This is the slide that matters most for this particular audience. If your "
        "students are building Arabic sites, lang and dir are the first thing to get "
        "right and the last thing anyone remembers.\n\n"
        "Demo it: take an English page, set lang=\"ar\" without changing the text, and "
        "let them hear what a screen reader does. Better than explaining.\n\n"
        "Mention the bidi entities now and come back to them in the entities section "
        "\u2014 do not front-load them."
    ),
)

slide_content(
    prs,
    "Meta tags that actually matter",
    [
        ("<meta charset=\"UTF-8\">", 0, "strong"),
        ("First thing in <head>. Without it, non-Latin text can break.", 1, "plain"),
        ("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">", 0, "strong"),
        ("Mandatory. Without it mobile browsers guess a 980px-wide screen.", 1, "plain"),
        ("<meta name=\"description\" content=\"...\">", 0, "strong"),
        ("The snippet under your title in search results.", 1, "plain"),
        ("<title> is not a meta tag, but forget it and the tab says the URL", 0, "warn"),
        ("Open Graph tags control how the link looks when shared on social media", 0, "note"),
    ],
    kicker="DOCUMENT STRUCTURE",
    notes=(
        "Do not turn this into a list. Teach the two required ones (charset, viewport), "
        "mention description, and move on.\n\n"
        "The viewport one deserves a demo: remove it, open DevTools device mode, set "
        "the viewport meta back, watch the page zoom. Ten seconds, and it never leaves."
    ),
)

slide_table(
    prs,
    "Tag vs element vs attribute",
    ["Code", "Term", "Meaning"],
    [
        ["<p>", "a tag", "Written with angle brackets"],
        ["<p>Hello</p>", "an element", "Tag + content + closing tag"],
        ["<p class=\"lead\">", "an attribute", "Extra information on the tag"],
    ],
    kicker="VOCABULARY",
    widths=[2.6, 2.4, 6.8],
    notes=(
        "Worth three minutes because it is the vocabulary they need for documentation "
        "and for every tutorial on the internet.\n\n"
        "The related point: an element is a live object in the DOM, not text. That is why "
        "the DevTools Elements panel can let you edit it live and the page changes."
    ),
)

slide_cards(
    prs,
    "Void elements take no closing tag",
    [
        ("<img>", "Image. All of them: the <img> you are reading is void."),
        ("<br>", "Line break. Use sparingly \u2014 see the text section."),
        ("<input>", "Form field. One tag, no children, no closing."),
        ("<hr>", "Thematic break. Rarely the right answer."),
        ("<meta>, <link>", "Head elements. Both void, both easy to forget and malform."),
    ],
    kicker="VOCABULARY",
    notes=(
        "The tell: if an element cannot have children, it is void. Nothing goes inside it, "
        "so there is nothing to close.\n\n"
        "Where beginners go wrong: writing <img ...></img>. The parser treats the second "
        "tag as a stray element. The validator flags it. It is not an error the browser "
        "will save you from."
    ),
)

slide_content(
    prs,
    "Headings build an outline, and the outline is a feature",
    [
        ("<h1> to <h6>. One question: what is this, in the hierarchy?", 0, "strong"),
        ("One <h1> per page, and it is the page title", 0, "strong"),
        ("Levels describe nesting, not font size", 0, "note"),
        ("Never skip a level to get a different size \u2014 that is CSS's job", 0, "warn"),
        ("Screen reader users navigate by jumping between headings", 0, "plain"),
        ("Search engines use the same outline", 0, "plain"),
        ("Choosing a heading by how big it looks is the most common structural mistake", 0, "bad"),
    ],
    kicker="TEXT CONTENT",
    notes=(
        "Demo the outline: open DevTools, and use the accessibility tree or the document "
        "outline panel. The headings become a nested table of contents. That is what a "
        "screen reader user experiences as \u2018jump to heading\u2019.\n\n"
        "The bad example that lands: a page using <h1> for the logo, <h2> for the nav, "
        "and then <h4> for section titles, because someone skipped a level trying to "
        "control size. Show it broken, then show the CSS-only fix."
    ),
)

slide_compare(
    prs,
    "Line breaks are not layout",
    "The right tool",
    [
        "Use a block element: <p>, <div>, <section>",
        "New block element = new line, and it is semantic",
        "<br> for a line break inside a sentence \u2014 an address, a poem",
        "Full control over spacing with CSS",
        "The DOM stays clean and shallow",
        "Copy-paste from your page looks correct",
    ],
    "The div-and-<br> reflex",
    [
        "A stack of <br> tags to force line breaks",
        "Or empty <div> elements as spacers",
        "Works, and breaks the moment the text reflows",
        "Responsive layout becomes impossible",
        "The DOM is a mess and screen readers announce it",
        "Looks wrong at every width except the one you built",
    ],
    kicker="TEXT CONTENT",
    notes=(
        "This is a habits problem, not a knowledge problem. Everybody learns HTML by "
        "copying, and every old tutorial teaches div-and-br.\n\n"
        "Make the rule explicit: a line break in the markup is a decision about content. "
        "A line break on screen is a decision about layout, and layout is CSS."
    ),
)

slide_two_col(
    prs,
    "Formatting: semantics or just looks?",
    "Means something",
    [
        "<strong> importance, not just weight",
        "<em> stress or emphasis",
        "<mark> highlighted as relevant right now",
        "<del> deleted, and visible as deleted",
        "<small> fine print, legal, side content",
    ],
    "Only means bold or italic",
    [
        "<b> \u2014 bold, nothing more",
        "<i> \u2014 italic, nothing more",
        "Both still valid, both legitimate uses",
        "No screen reader announces either one",
        "Choosing these loses the meaning for free",
    ],
    kicker="TEXT CONTENT",
    notes=(
        "Short slide. The rule of thumb: if you could remove the emphasis and the "
        "meaning would not change, it is <b>/<i>. If removing it changes what the text "
        "means, it is <strong>/<em>.\n\n"
        "Example that works: a warning label \u2018<strong>Warning:</strong> this will "
        "delete everything\u2019 vs \u2018<b>Warning:</b> this will delete everything\u2019."
    ),
)

slide_code(
    prs,
    "Links: the whole API in one attribute",
    """
&lt;a href="/about"&gt;About us&lt;/a&gt;
&lt;a href="#contact"&gt;Jump to contact&lt;/a&gt;
&lt;a href="../index.html"&gt;Up one level&lt;/a&gt;
&lt;a href="mailto:hello@example.com"&gt;Email us&lt;/a&gt;
&lt;a href="tel:+201234567890"&gt;Call us&lt;/a&gt;
&lt;a href="report.pdf" download&gt;Download the report&lt;/a&gt;""",
    kicker="LINKS",
    notes=(
        "Six forms, one element. If a link goes somewhere, it is an <a> with href.\n\n"
        "The download attribute only works for same-origin resources \u2014 the browser "
        "ignores it cross-origin. Mention it, move on."
    ),
)

slide_compare(
    prs,
    "target=\"_blank\" costs something",
    "The safe version",
    [
        "rel=\"noopener noreferrer\" always",
        "noopener severs window.opener \u2014 the old tab cannot reach the new one",
        "noreferrer withholds the Referer header",
        "Links to other sites: safer and more private",
        "Links inside your own app: usually avoid _blank entirely",
        "It is two words and it closes a real vulnerability",
    ],
    "target=\"_blank\" alone",
    [
        "The new page can read window.opener.location",
        "Reverse tabnabbing: the other site redirects you",
        "Referer leaks the URL you came from",
        "Nothing about it is a syntax error",
        "The validator will never warn you",
        "It still works, which is why nobody notices",
    ],
    kicker="LINKS",
    notes=(
        "The security point is real and it is not theoretical. But do not turn this into "
        "a security lecture \u2014 the actionable rule is one sentence: new tab, new origin, "
        "add noopener.\n\n"
        "The second half of the slide is the practical advice: inside a single-page app, "
        "opening a new tab for an internal route is almost always wrong."
    ),
)

slide_content(
    prs,
    "Paths: the thing that breaks when you move the file",
    [
        ("Absolute: /images/logo.png \u2014 from the site root", 0, "strong"),
        ("Breaks the moment you move the project to a subfolder", 0, "bad"),
        ("Relative: images/logo.png \u2014 from the current file's folder", 0, "strong"),
        ("Moves with the project. This is what you want.", 0, "good"),
        ("../ goes up one level, ./ is the current folder", 0, "plain"),
        ("A good test: the project still works when opened from a different path", 0, "note"),
    ],
    kicker="PATHS & FOLDER STRUCTURE",
    notes=(
        "This is the most common reason \u2018it works on my machine\u2019. A root-absolute "
        "path works perfectly on localhost and breaks the second you deploy to a "
        "subfolder, or open the HTML file directly from disk.\n\n"
        "The drill: after any project they finish, have them rename the top folder and "
        "reopen. If it still works, their paths are honest."
    ),
)

slide_cards(
    prs,
    "A folder structure that survives",
    [
        ("index.html", "The entry point. One per folder means the folder alone is a valid site."),
        ("assets/", "Everything non-content. img/, icons/, fonts/ inside it."),
        ("css/", "One stylesheet per concern, not per page."),
        ("js/", "Same rule, once you get there."),
    ],
    kicker="PATHS & FOLDER STRUCTURE",
    notes=(
        "Keep it this small. Beginners add nesting for its own sake and then cannot find "
        "anything.\n\n"
        "index.html is worth explaining: a URL ending in a slash means \u2018serve the "
        "index.html in this folder\u2019. It is why /about works without listing the file."
    ),
)

slide_code(
    prs,
    "Images: the four required things",
    """
&lt;img
  src="assets/img/cafe.jpg"
  alt="A small cafe with three tables and large windows"
  width="1200"
  height="800"
  loading="lazy"
  decoding="async"
/&gt;""",
    caption="src \u00b7 alt \u00b7 width + height \u00b7 loading. Four attributes, and the page "
            "does not jump around while it loads.",
    kicker="IMAGES",
    size=13,
    height=3.2,
    notes=(
        "Walk the four attributes in order and say what each one prevents.\n\n"
        "width/height preventing layout shift (CLS) is worth a demo: comment them out, "
        "reload, and watch the page jump. This directly connects to the Core Web Vitals "
        "they will meet in the React track \u2014 mention that in one sentence and move on."
    ),
)

slide_compare(
    prs,
    "Writing alt text",
    "What good looks like",
    [
        "Describe what the image conveys in context",
        "Skip \u2018image of\u2019 and \u2018picture of\u2019 \u2014 a screen reader says that already",
        "Keep it under about 125 characters",
        "Keyword context: \u2018oat flat white\u2019 beats \u2018coffee\u2019 on a cafe page",
        "Purely decorative? alt=\"\" and nothing else",
        "alt=\"\" tells the reader to skip it \u2014 that is the point",
    ],
    "What gets written instead",
    [
        "alt=\"\" on a photo that carries meaning",
        "alt=\"image1.jpg\" \u2014 a filename, not a description",
        "alt=\"spacer\" on a decorative gif",
        "Keyword stuffing a list of unrelated words",
        "Capturing text that is already on the page",
        "Silently deleting information the sighted user relies on",
    ],
    kicker="IMAGES",
    notes=(
        "The empty alt case is the one that confuses people. alt=\"\" is not forgetting "
        "\u2014 it is a deliberate instruction to the screen reader to skip the image, and "
        "it is correct for dividers, spacer gifs, and background texture.\n\n"
        "Test: turn on a screen reader for thirty seconds, or use DevTools \u2192 "
        "Accessibility tree to see what gets announced for each image on the page they "
        "built. That inspection is the whole lesson."
    ),
)

slide_table(
    prs,
    "Formats, and when each one wins",
    ["Format", "Use it for", "Watch out for"],
    [
        ["JPEG", "Photos, gradients", "No transparency. Artifacts on flat colour."],
        ["PNG", "Screenshots, logos, flat art", "Lossless, huge. Avoid on photos."],
        ["WebP", "Everything, by default now", "Smaller than both. Broad support."],
        ["AVIF", "Everything, budget permitting", "Smallest. Slower to encode."],
        ["SVG", "Icons, illustrations, charts", "Infinite, themable, DOM-addressable."],
    ],
    kicker="IMAGES",
    widths=[1.6, 3.9, 6.3],
    notes=(
        "Keep this to thirty seconds. The actionable takeaway: default to WebP, use SVG "
        "for icons, and stop shipping PNG screenshots of photos.\n\n"
        "The one interesting bit: an inline SVG is a real DOM subtree, so you can target "
        "its paths with CSS and change its fill from a currentColor parent. That is why "
        "icons in the CSS and React tracks can switch colour with the theme."
    ),
)

slide_content(
    prs,
    "Responsive images in four lines",
    [
        ("srcset offers the browser several files at different widths", 0, "strong"),
        ("sizes tells it how wide the image will actually render", 0, "strong"),
        ("The browser then downloads the smallest file that is still sharp", 0, "good"),
        ("<picture> goes further: art direction, not just resolution", 0, "note"),
        ("<picture><source media=\"...\"> then a final <img> fallback", 0, "plain"),
        ("sizes is where people go wrong \u2014 a wrong sizes means the wrong file", 0, "warn"),
    ],
    kicker="IMAGES",
    notes=(
        "Concept over syntax. The insight they need: you do not resize images in CSS, you "
        "let the browser pick the right file before it downloads.\n\n"
        "sizes is genuinely hard and they will get it wrong. The most common wrong answer "
        "is omitting it entirely, which makes the browser assume the image is as wide as "
        "the viewport \u2014 so it always downloads the largest file."
    ),
)

slide_two_col(
    prs,
    "Lists: structure, not bullets",
    "Use a list",
    [
        "Navigation menus",
        "A set of steps",
        "Ingredients, features, tags",
        "A glossary \u2014 <dl> with <dt> and <dd>",
        "Nested categories use nested <ul>",
        "Free indentation, and a screen reader announces \u2018list of 5\u2019",
    ],
    "Do not use a list",
    [
        "A row of links styled as a flex row",
        "That is a nav, not a list",
        "Five <div>s with bullets from background images",
        "Or paragraphs that happen to end in a period",
        "Or a table, which is never for layout",
        "Semantics first; the visual is your call",
    ],
    kicker="LISTS",
    notes=(
        "The takeaway: a list is a claim about meaning. If the items are a set of things "
        "of the same kind, it is a list \u2014 even if you style the markers away entirely.\n\n"
        "The description list is the one beginners never meet and immediately find useful. "
        "A glossary, a spec sheet, a FAQ pair \u2014 all of them are term/definition."
    ),
)

slide_content(
    prs,
    "Entities: reserved characters and beyond",
    [
        ("&amp; &lt; &gt; &quot; \u2014 must be escaped in content", 0, "strong"),
        ("&nbsp; \u00a0 \u2014 a non-breaking space, for units like 10\u00a0km", 0, "strong"),
        ("&copy; &reg; &deg; &mdash; &hellip; \u2014 typography", 0, "plain"),
        ("&#169; or &#xA9; \u2014 the numeric form of anything", 0, "plain"),
        ("Escaping is mandatory wherever user input is rendered", 0, "warn"),
        ("This is the exact mechanism an XSS payload uses \u2014 you will meet it in "
         "the JavaScript track", 0, "note"),
    ],
    kicker="ENTITIES",
    notes=(
        "Do not let them memorise the list. Teach the principle: an entity is a character "
        "the parser would otherwise interpret as syntax, or a character that is awkward "
        "to type.\n\n"
        "The last bullet is a deliberate seed. In the JavaScript track they will look at "
        "innerHTML and XSS. If they already know &lt; and &gt; are just escapes, that "
        "lesson lands much harder."
    ),
)

slide_content(
    prs,
    "Bidi entities \u2014 the Arabic edge cases",
    [
        ("Text direction is inferred, and inference fails at the edges", 0, "strong"),
        ("A phone number inside Arabic text renders in the wrong order", 0, "plain"),
        ("A URL at the end of a line moves the punctuation to the wrong side", 0, "plain"),
        ("&lrm; &ltr; \u2014 force a left-to-right run", 0, "strong"),
        ("&rlm; &rtl; \u2014 force a right-to-left run", 0, "strong"),
        ("<bdo dir=\"ltr\"> \u2014 override direction for a whole fragment", 0, "note"),
    ],
    kicker="ENTITIES",
    notes=(
        "Type the failing example live in Arabic, let them see the dot land on the wrong "
        "side, then wrap it in &lrm; and let them see it fix. Ten seconds, and every "
        "student who has ever shipped an Arabic page recognises the bug instantly.\n\n"
        "This is the slide that makes the course feel like it was written for them."
    ),
)

slide_exercise(
    prs,
    "LIVE CODING",
    "Write a page from memory",
    [
        "Build the skeleton of a valid HTML document with no reference",
        "Convert a plain text document into headings and paragraphs",
        "Find and fix three intentionally broken documents",
    ],
    hint="Broken #1 is a missing viewport meta. Broken #2 is <h3> used with no <h2> above "
         "it. Broken #3 is a root-absolute src that breaks when the folder moves.",
    minutes="40 min",
    notes=(
        "Do not let them copy from the slide \u2014 the point is recall. Stand at the back.\n\n"
        "Seed the three broken documents before the session. Make them realistic: not "
        "<h7>, but a page that is 90% right with one subtle mistake in it.\n\n"
        "The fix for #3 is the one that teaches the most: ask them to rename the project "
        "folder and reload, so they see it break for themselves."
    ),
)

slide_content(
    prs,
    "Homework & project",
    [
        ("Homework \u2014 Personal Profile Page", 0, "strong"),
        ("Your name, a short bio, and your hobbies as text", 1, "plain"),
        ("Use a heading hierarchy that would survive review", 1, "plain"),
        ("", 0, "plain"),
        ("Project Work \u2014 Personal Profile Page, properly", 0, "strong"),
        ("A valid document with correct heading hierarchy", 1, "plain"),
        ("A nav of links, and a fragment-link table of contents", 1, "plain"),
        ("A meaningful footer", 1, "plain"),
        ("No CSS yet. Structure only \u2014 that is the point of the session", 0, "warn"),
    ],
    kicker="SESSION 1 DELIVERABLES",
    notes=(
        "Insist on no CSS for this project. The instinct will be to make it pretty, and "
        "that instinct will let them skip validation. Structure first, always \u2014 it is "
        "the habit that separates people who can debug from people who cannot.\n\n"
        "Review method: open every submission in the W3C validator. A number will have "
        "errors, and reading the validator output is a skill worth teaching directly."
    ),
)

slide_recap(
    prs,
    "Session 1 \u2014 what you now know",
    [
        "HTML describes meaning; CSS describes appearance",
        "DOCTYPE, lang, charset, viewport \u2014 every document, no exceptions",
        "One h1, a real hierarchy, never skip a level",
        "Relative paths so the project survives being moved",
        "alt is a description, alt=\"\" is a decision",
        "width and height stop the page jumping",
        "Entities exist for a reason, and so do bidi ones",
        "Validate before you call it done",
    ],
    notes=(
        "Ask the room to give you one thing from the list that surprised them. Usually the "
        "bidi entities or the CLS thing \u2014 both worth five extra minutes if they land.\n\n"
        "Set the session 2 hook: next session everything they wrote gets forms and real "
        "semantics, and it becomes a real product."
    ),
)

# ==========================================================================
# Session 2
# ==========================================================================

slide_divider(
    prs, 2, "Forms, Semantics, Tables & Media", "~6 hours",
    "Build forms, meaningful page structure, and data-rich content \u2014 then ship the capstone.",
    "forms & inputs  \u00b7  validation UX  \u00b7  semantics & landmarks  \u00b7  div vs span  \u00b7  "
    "tables  \u00b7  audio & video  \u00b7  iframes  \u00b7  ARIA essentials  \u00b7  quality",
    notes=(
        "Longest session. Structure:\n"
        "- 90 min: forms and inputs\n"
        "- 30 min: validation UX\n"
        "- 60 min: semantics and landmarks\n"
        "- 30 min: tables\n"
        "- 25 min: media and iframes\n"
        "- 25 min: ARIA essentials\n"
        "- 45 min: live coding\n"
        "- 20 min: capstone brief\n\n"
        "If you are behind at the two-hour mark, cut Tables and media. Keep ARIA \u2014 it "
        "is the part they will not learn anywhere else."
    ),
)

slide_code(
    prs,
    "A form is three attributes and a promise",
    """
&lt;form action="/order" method="post"&gt;
  &lt;label for="email"&gt;Email&lt;/label&gt;
  &lt;input id="email" name="email" type="email" required&gt;
&lt;/form&gt;""",
    caption="action: where it goes \u00b7 method: how \u00b7 name: the key it arrives under. "
            "Without name, the field is not submitted \u2014 at all.",
    kicker="FORMS",
    height=2.4,
    notes=(
        "The name attribute is the single most important thing on this slide and the one "
        "they will forget. A field without a name is invisible to the server.\n\n"
        "Demo: submit the form to a page that dumps the query string, with one field "
        "missing name. It does not appear. That is a lesson they remember.\n\n"
        "method=\"get\" puts everything in the URL \u2014 good for search, bad for anything "
        "private. method=\"post\" is the default choice for forms with real data."
    ),
)

slide_cards(
    prs,
    "Input types are a contract with the browser",
    [
        ("type=\"email\"", "Mobile keyboard, plus built-in format validation."),
        ("type=\"number\"", "Numeric keyboard, plus min / max / step."),
        ("type=\"date\"", "A real date picker. Never build one yourself."),
        ("type=\"file\"", "accept filters the picker, multiple allows more than one."),
        ("checkbox vs radio", "Many vs one. Group radios by a shared name attribute."),
        ("type=\"search\"", "A search field: clear button and the right keyboard."),
    ],
    kicker="FORMS & INPUTS",
    notes=(
        "The point is not the list, it is the idea: the input type is how you tell the "
        "browser what the data is, and the browser then gives you keyboard, picker, "
        "validation and accessibility almost for free.\n\n"
        "Common mistake: type=\"text\" everywhere, then hand-rolling validation in "
        "JavaScript. type=\"email\" would have done it. Ask, for every text field, what "
        "the type should be."
    ),
)

slide_content(
    prs,
    "Constraints the browser checks for you",
    [
        ("required \u2014 cannot be empty", 0, "strong"),
        ("pattern=\"...\" \u2014 a regex the browser applies", 0, "strong"),
        ("minlength / maxlength", 0, "strong"),
        ("min / max / step on number and range", 0, "strong"),
        ("readonly is visible but not editable", 0, "plain"),
        ("disabled is not submitted and cannot be focused", 0, "warn"),
        ("These are constraints, not validation messages \u2014 the two are different", 0, "note"),
    ],
    kicker="FORMS & INPUTS",
    notes=(
        "Constraints stop the form submitting. They do not explain anything to the user. "
        "Both matter, and they are different jobs \u2014 that distinction is worth stating "
        "out loud because beginners conflate them.\n\n"
        "The readonly vs disabled distinction is a favourite interview question. The "
        "practical version: disabled data is not sent to the server, so a disabled field "
        "is a field the backend never hears about."
    ),
)

slide_content(
    prs,
    "Every input needs a label. This is the rule.",
    [
        ("<label for=\"email\"> \u2194 <input id=\"email\">", 0, "strong"),
        ("Clicking the label focuses the field. That is a usability feature.", 0, "good"),
        ("The screen reader announces the label instead of \u2018edit text, blank\u2019", 0, "strong"),
        ("Wrapping the input inside the label works too", 0, "plain"),
        ("id must be unique, and must match the label's for", 0, "note"),
        ("placeholder is a hint, not a label \u2014 it disappears and it fails contrast", 0, "bad"),
        ("aria-label is the fallback when there is no visible text at all", 0, "note"),
    ],
    kicker="FORMS & INPUTS",
    notes=(
        "Slow down here. This is the highest-value slide in the entire HTML track and "
        "the one most likely to be skipped in a self-taught course.\n\n"
        "Demo: tab through a form with labels and then one without. Unlabelled inputs "
        "announce as \u2018edit text\u2019 with no clue what goes there.\n\n"
        "The placeholder point deserves a full minute. Placeholders disappearing on focus "
        "means the user loses the prompt exactly when they need it, and the default grey "
        "fails contrast. It is a hint, not a replacement."
    ),
)

slide_content(
    prs,
    "Fieldsets group; they are not decoration",
    [
        ("<fieldset> \u2014 a related group of controls", 0, "strong"),
        ("<legend> \u2014 the group\u2019s caption", 0, "strong"),
        ("Radios belong in one fieldset \u2014 grouping by name alone is not enough", 0, "note"),
        ("A screen reader announces the legend as you enter the group", 0, "plain"),
        ("The default border and indentation are ugly \u2014 that is a CSS problem", 0, "warn"),
        ("Reset the border, keep the semantics", 0, "good"),
    ],
    kicker="FORMS & INPUTS",
    notes=(
        "The classic trap: four radio buttons that are visually stacked but semantically "
        "four unrelated things, because nobody wrapped them in a fieldset. A screen reader "
        "user has no idea they are one question.\n\n"
        "And the CSS advice matters, because beginners see the ugly default border and "
        "delete the fieldset. Teach them: border: 0; margin: 0; padding: 0; and you keep "
        "the semantics for free."
    ),
)

slide_content(
    prs,
    "Native validation, done properly",
    [
        ("The browser blocks submission and shows its own message", 0, "strong"),
        (":user-invalid styles a field only after interaction, not on page load", 0, "strong"),
        (":invalid would paint every empty required field red on arrival \u2014 avoid it", 0, "warn"),
        ("Custom messages: aria-describedby pointing at your own error text", 0, "note"),
        ("Client-side validation is a convenience, never a guarantee", 0, "warn"),
        ("The server validates everything again. Always. Twice.", 0, "bad"),
    ],
    kicker="VALIDATION & UX",
    notes=(
        ":user-invalid is newer and much better behaved than :invalid for this job. Worth "
        "showing both so they understand why.\n\n"
        "The last bullet is a real warning with real consequences. Client validation is "
        "UX. Security is the server. They will see the echo of this in the JavaScript "
        "track's security section."
    ),
)

slide_compare(
    prs,
    "Div and span",
    "<div> \u2014 block",
    [
        "Starts a new line by default",
        "For grouping content where no semantic element fits",
        "A generic container, and that is all",
        "No meaning to a screen reader",
        "The right answer when nothing else fits",
        "Common for layout before Flexbox and Grid",
    ],
    "<span> \u2014 inline",
    [
        "Stays inside the current line",
        "For a fragment of text inside a paragraph",
        "Used to attach a class to part of a sentence",
        "Cannot contain block-level content",
        "Also no meaning of its own",
        "Wrong tool for \u2018I need a box\u2019",
    ],
    kicker="SEMANTICS",
    notes=(
        "The rule of thumb: if you are reaching for a div because you do not know which "
        "element fits, you have not found the element yet. Search for the semantic one "
        "first, and fall back to div deliberately.\n\n"
        "div soup \u2014 a page made entirely of divs \u2014 is what a screen reader sees as "
        "one undifferentiated wall of text with no headings, no navigation, and no "
        "structure. Show the accessibility tree comparison if time allows."
    ),
)

slide_content(
    prs,
    "Landmarks: five elements that give the page a skeleton",
    [
        ("<header> \u2014 site or section header", 0, "strong"),
        ("<nav> \u2014 major navigation", 0, "strong"),
        ("<main> \u2014 the primary content, once per page", 0, "strong"),
        ("<footer> \u2014 site or section footer", 0, "strong"),
        ("<aside> \u2014 tangential content: a sidebar, a related links block", 0, "plain"),
        ("<article> \u2014 a self-contained piece: a post, a comment", 0, "plain"),
        ("<section> \u2014 a thematic grouping that has no better element", 0, "plain"),
    ],
    kicker="SEMANTICS",
    notes=(
        "Landmarks are what let a screen reader user jump straight to the navigation, or "
        "skip to the main content. That is not a nicety \u2014 on a long page it is the "
        "difference between usable and unusable.\n\n"
        "article vs section is the one that trips everyone. article = independently "
        "distributable (a blog post you could syndicate on its own). section = just a "
        "grouping. If you cannot answer \u2018could this stand alone as content?\u2019, it "
        "is a section."
    ),
)

slide_content(
    prs,
    "Why semantics pay off three times",
    [
        ("Screen readers \u2014 structure becomes navigable, not a wall of text", 0, "strong"),
        ("Search engines \u2014 headings and landmarks are a page outline", 0, "strong"),
        ("You \u2014 the code reads like what it does, six months later", 0, "strong"),
        ("Free side effect: correct default styling you did not have to write", 0, "good"),
        ("<time datetime=\"2026-01-15\"> renders localised, machine-readable", 0, "note"),
        ("<figure> + <figcaption> for images that need a caption", 0, "note"),
    ],
    kicker="SEMANTICS",
    notes=(
        "The third one is what convinces developers who are not yet convinced about the "
        "first two. Refactor a page from divs to landmarks and watch the CSS get shorter "
        "as well, because the elements have sensible defaults.\n\n"
        "<time datetime> is a small gem: the attribute is machine-readable ISO format, the "
        "text is whatever the reader sees, and the browser can localise it."
    ),
)

slide_table(
    prs,
    "Tables are for data. Never for layout.",
    ["Element", "What it is for"],
    [
        ["<table>", "The data table itself"],
        ["<caption>", "A title, announced before the data"],
        ["<thead> / <tbody> / <tfoot>", "Header, body, and summary rows"],
        ["<th> / <td>", "A header cell / a data cell"],
        ["scope=\"col\" / scope=\"row\"", "Tells a screen reader which axis it is on"],
        ["colspan / rowspan", "Spanning cells \u2014 use sparingly"],
    ],
    kicker="TABLES",
    widths=[4.1, 7.7],
    notes=(
        "Scope is the one that matters. Without it, a screen reader announcing a data "
        "cell has no idea whether it is the price or the category, because the visual grid "
        "is not in the accessibility tree.\n\n"
        "The layout-table argument: it was valid in 1998 and it is a disaster now. Layout "
        "tables nest, and every level of nesting is a more complicated mess for assistive "
        "technology. Use Grid."
    ),
)

slide_two_col(
    prs,
    "Media, done accessibly",
    "Video and audio",
    [
        "<video controls poster=\"...\"> with a width/height",
        "autoplay requires muted, or it is blocked",
        "<source> lets you offer WebM and MP4",
        "<track kind=\"captions\"> is not optional for a public site",
        "preload=\"none\" if the video is below the fold",
        "Always give it a poster frame",
    ],
    "Iframes",
    [
        "title is required \u2014 it is the accessible name",
        "sandbox locks down what the frame may do",
        "loading=\"lazy\" for anything not above the fold",
        "referrerpolicy to avoid leaking your URL",
        "Embeds are heavy and slow down the page",
        "Use the native element when one exists",
    ],
    kicker="MEDIA & EMBEDDING",
    notes=(
        "Captions are worth a moment. If your students are building for a public or "
        "institutional audience, uncaptained video is a compliance issue, not just an "
        "accessibility one.\n\n"
        "The iframe title point is the same as the image alt point: a frame with no title "
        "announces as \u2018frame\u2019, full stop. And embed a map from a third party? Say "
        "loudly that it costs a megabyte and several hundred milliseconds."
    ),
)

slide_content(
    prs,
    "ARIA: what it is and when to reach for it",
    [
        ("First rule: do not use ARIA if a semantic element exists", 0, "strong"),
        ("A native button is focusable, keyboard-operable, and announced correctly", 0, "good"),
        ("<div role=\"button\"> is none of those, and you now own the keyboard", 0, "bad"),
        ("aria-expanded on a disclosure \u2014 and keep it honest", 0, "strong"),
        ("aria-current=\"page\" on the active nav link", 0, "strong"),
        ("aria-live=\"polite\" for a status; role=\"alert\" for an error", 0, "strong"),
        ("aria-label only when there is no visible text to reference", 0, "note"),
        ("More ARIA is not better ARIA", 0, "warn"),
    ],
    kicker="ARIA ESSENTIALS",
    notes=(
        "Two hours in, the room will want to sprinkle ARIA everywhere. The most important "
        "sentence on this slide is the first one, and the most important warning is the "
        "last.\n\n"
        "The div-role-button example is worth building live: add role=\"button\", then try "
        "to make it respond to Enter and Space. Now they understand that ARIA is a "
        "description, not a behaviour. It tells assistive technology what something is; it "
        "does not make it work.\n\n"
        "Show the accessibility tree in DevTools and toggle one ARIA attribute, so they see "
        "the tree change."
    ),
)

slide_content(
    prs,
    "Ship it: what \u2018done\u2019 means for a page",
    [
        ("Passes the W3C validator with zero errors", 0, "strong"),
        ("One h1, real heading order, real landmarks", 0, "strong"),
        ("Every image has alt text, every iframe has a title", 0, "strong"),
        ("Every input has a label", 0, "strong"),
        ("You can tab through the whole page and reach everything", 0, "strong"),
        ("No inline styles and no inline scripts \u2014 keep it in files", 0, "note"),
        ("One brief structured-data block with application/ld+json", 0, "note"),
    ],
    kicker="QUALITY",
    notes=(
        "The W3C validator is at validator.w3.org/nu. Bookmark it in front of them.\n\n"
        "The tab-through test is the most practical thing on this slide. It takes two "
        "minutes, needs no tools, and finds a surprising number of problems: unreachable "
        "elements, focus you cannot see, skip links that do nothing.\n\n"
        "Reading HTML out loud is also a genuinely good debugging technique \u2014 it finds "
        "missing alt text and broken nesting surprisingly often."
    ),
)

slide_exercise(
    prs,
    "LIVE CODING",
    "Refactor and rebuild",
    [
        "Build an eight-field registration form, fully labelled, no CSS",
        "Refactor a 200-line div soup page into semantic HTML",
        "Build an accessible data table, and compare the accessibility tree before and after",
    ],
    hint="Start with the validator open in one tab. Run it before you think you are done, "
         "not after. The errors it reports are the exact errors you have been making.",
    minutes="45 min",
    notes=(
        "Exercise two is the one that changes how they write. Do not let them rush it \u2014 "
        "the refactor is tedious on purpose, because tedium is what makes the payoff obvious.\n\n"
        "Have them diff the accessibility tree before and after. Seeing \u2018formerly one "
        "anonymous blob, now six named landmarks\u2019 is the argument for semantics better "
        "than any lecture."
    ),
)

slide_content(
    prs,
    "The capstone \u2014 Restaurant Menu & Order Page",
    [
        ("Header with the restaurant name, and a nav menu", 0, "strong"),
        ("The menu as an accessible table: item, category, price, availability", 0, "strong"),
        ("An order form with at least eight validated fields", 0, "strong"),
        ("An embedded map or video, with title and sandbox", 0, "strong"),
        ("Semantic landmarks, a skip link, and a meaningful footer", 0, "strong"),
        ("Zero errors in the W3C validator", 0, "strong"),
        ("This is the deliverable. Everything above session 2 feeds it.", 0, "note"),
    ],
    kicker="CAPSTONE",
    notes=(
        "Set a hard deadline for this \u2014 the point is to ship, not to perfect. Everyone "
        "finishes with something that validates and works, which is a real skill, and "
        "everyone leaves with a known list of what to improve.\n\n"
        "Review rubric, in this order of weight: validity, then semantics, then "
        "accessibility, then structure. Tell them that order explicitly so nobody spends "
        "hours on a nav that is not the thing being marked."
    ),
)

slide_table(
    prs,
    "How the capstone is marked",
    ["Criterion", "Weight", "What earns the marks"],
    [
        ["Correctness", "30", "Zero validator errors. Nothing broken."],
        ["Semantics", "25", "Landmarks, one h1, real heading order, no layout tables."],
        ["Accessibility", "25", "Labels, alt text, iframe titles, keyboard navigable."],
        ["Structure", "20", "Relative paths, tidy folders, no inline styles or scripts."],
    ],
    kicker="ASSESSMENT",
    widths=[2.6, 1.2, 8.0],
    notes=(
        "Give them the rubric with the brief, not after. Self-assessment against a known "
        "rubric is worth more than a surprise grade.\n\n"
        "The weights are a message in themselves: semantics and accessibility together are "
        "half the mark. That is a deliberate signal about what the industry actually "
        "rewards."
    ),
)

slide_content(
    prs,
    "Where this track goes",
    [
        ("Next: the CSS + Tailwind bootcamp \u2014 7 sessions", 0, "strong"),
        ("You will style the exact pages you built here", 0, "note"),
        ("The box model explains why your layout fights you", 0, "note"),
        ("You will keep writing semantic HTML and add a layer on top", 0, "good"),
        ("", 0, "plain"),
        ("Before then \u2014 read the HTML you wrote and find every div that should not "
         "be a div", 0, "warn"),
        ("And check your capstone in the validator one more time", 0, "note"),
    ],
    kicker="WHAT NEXT",
    notes=(
        "Close by reading out the assessment criteria one more time and repeating the "
        "single hardest habit: no div where an element exists.\n\n"
        "If there is time, open their capstone live and run the validator in front of the "
        "room. Public failure of a tool is a better teacher than a slide about it."
    ),
)

# ==========================================================================

add_footer(prs, "ICLUB / HTML Bootcamp")
path = save(prs, OUT)
print(f"OK  {path}")
print(f"    {len(prs.slides._sldIdLst)} slides")
