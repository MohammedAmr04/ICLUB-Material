"""Layout audit: measures real rendered text height for every text frame
and reports shapes whose text does not fit, or that leave the slide bounds.

Usage:  python check_overflow.py [deck.pptx]
"""
import glob
import os
import sys

from PIL import ImageFont
from pptx import Presentation
from pptx.util import Emu

EMU_IN = 914400
SLIDE_W = 13.333
SLIDE_H = 7.5

FONT_FILES = {
    ("Segoe UI", False): "segoeui.ttf",
    ("Segoe UI", True): "segoeuib.ttf",
    ("Consolas", False): "consola.ttf",
    ("Consolas", True): "consolab.ttf",
}

_cache = {}


def font_for(name, bold, size_pt):
    key = (name, bool(bold), round(size_pt, 1))
    if key not in _cache:
        fname = FONT_FILES.get((name, bool(bold))) or FONT_FILES[("Segoe UI", bool(bold))]
        path = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", fname)
        if not os.path.exists(path):
            path = os.path.join(
                os.environ.get("WINDIR", r"C:\Windows"), "Fonts", "segoeui.ttf"
            )
        _cache[key] = ImageFont.truetype(path, max(1, int(round(size_pt * 4))))
    return _cache[key]


def text_width_pt(text, name, bold, size_pt):
    f = font_for(name, bold, size_pt)
    return f.getlength(text) / 4.0


def wrap_lines(words_runs, avail_pt):
    """Greedy word wrap across a list of (word, font_name, bold, size_pt) runs."""
    lines = 1
    cur = 0.0
    space = 0.0
    for word, fname, bold, size in words_runs:
        if word == "\n":
            lines += 1
            cur = 0.0
            space = 0.0
            continue
        w = text_width_pt(word, fname, bold, size)
        sw = text_width_pt(" ", fname, bold, size)
        if cur == 0.0:
            cur = w
        elif cur + space + w <= avail_pt:
            cur += space + w
        else:
            lines += 1
            cur = w
        space = sw
    return lines


def frame_required_height(shape):
    """Estimated required height in inches for a shape's text."""
    tf = shape.text_frame
    box_w_pt = (shape.width - tf.margin_left - tf.margin_right) / EMU_IN * 72.0
    box_h_pt = (shape.height - tf.margin_top - tf.margin_bottom) / EMU_IN * 72.0
    if box_w_pt <= 4:
        return 0.0, box_h_pt

    total = 0.0
    for para in tf.paragraphs:
        runs = [(r.text, r.font.name or "Segoe UI", bool(r.font.bold),
                 (r.font.size.pt if r.font.size else 18.0)) for r in para.runs if r.text]
        if not runs:
            total += 12.0
            continue
        max_size = max(r[3] for r in runs)
        runs = [(w, n, b, s) for (w, n, b, s) in runs]
        n_lines = wrap_lines(runs, box_w_pt)
        ls = para.line_spacing if isinstance(para.line_spacing, float) else 1.0
        line_h = max_size * 1.22 * ls
        total += n_lines * line_h
        if para.space_after is not None:
            total += para.space_after.pt
        elif para.space_before is not None:
            total += para.space_before.pt
    return total / 72.0, box_h_pt / 72.0


def audit(path):
    prs = Presentation(path)
    issues = []
    for idx, slide in enumerate(prs.slides, start=1):
        for shape in slide.shapes:
            if shape.left is None or shape.top is None:
                continue
            l = shape.left / EMU_IN
            t = shape.top / EMU_IN
            r = l + (shape.width or 0) / EMU_IN
            b = t + (shape.height or 0) / EMU_IN
            if l < -0.01 or t < -0.01 or r > SLIDE_W + 0.01 or b > SLIDE_H + 0.01:
                label = (shape.text_frame.text[:40] if shape.has_text_frame else shape.shape_type)
                issues.append((idx, "OUT-OF-BOUNDS", f"box {l:.2f},{t:.2f} -> {r:.2f},{b:.2f}", label))
            if not shape.has_text_frame or not shape.text_frame.text.strip():
                continue
            need, have = frame_required_height(shape)
            if need > have + 0.02:
                issues.append((idx, "OVERFLOW",
                               f"needs {need:.2f}in, has {have:.2f}in",
                               shape.text_frame.text[:55].replace("\n", " ")))
    return prs, issues


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "html-bootcamp.pptx"
    if not os.path.exists(target):
        cands = sorted(glob.glob("*.pptx"))
        if not cands:
            print("no .pptx found")
            return 1
        target = cands[0]

    prs, issues = audit(target)
    slides = len(prs.slides._sldIdLst)
    print(f"deck      : {target}")
    print(f"slides    : {slides}")
    print(f"size      : {prs.slide_width / EMU_IN:.3f} x {prs.slide_height / EMU_IN:.3f} in")
    notes = sum(1 for s in prs.slides if s.has_notes_slide and s.notes_slide.notes_text_frame.text.strip())
    print(f"with notes: {notes}/{slides}")
    print(f"issues    : {len(issues)}")
    for sl, kind, detail, label in issues:
        print(f"  [slide {sl:>2}] {kind:<14} {detail}  :: {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
