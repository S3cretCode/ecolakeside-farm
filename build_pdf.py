#!/usr/bin/env python3
"""
EcoLakeside Farm - Complete Website Document PDF Generator
Generates an executive, publication-grade PDF from EcoLakeside_Farm_Complete_Website_Document.md
Zero external dependencies, pure Python vector PDF 1.4 output.
"""

import sys
import os
import re

# Standard Letter Page Dimensions (points)
PAGE_WIDTH = 612.0
PAGE_HEIGHT = 792.0
MARGIN_LEFT = 50.0
MARGIN_RIGHT = 50.0
MARGIN_TOP = 54.0
MARGIN_BOTTOM = 52.0
CONTENT_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT  # 512.0 pt
CONTENT_HEIGHT = PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM  # 686.0 pt

# AFM Character Widths for Helvetica (per 1000 units)
# Default average fallback width: 500
HELVETICA_WIDTHS = {
    ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667, "'": 191,
    '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333, '.': 278, '/': 278,
    '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556, '7': 556,
    '8': 556, '9': 556, ':': 278, ';': 278, '<': 584, '=': 584, '>': 584, '?': 556,
    '@': 1015, 'A': 667, 'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778,
    'H': 722, 'I': 278, 'J': 500, 'K': 667, 'L': 556, 'M': 833, 'N': 722, 'O': 778,
    'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 278, '\\': 278, ']': 278, '^': 469, '_': 556,
    '`': 333, 'a': 556, 'b': 556, 'c': 500, 'd': 556, 'e': 556, 'f': 278, 'g': 556,
    'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222, 'm': 833, 'n': 556, 'o': 556,
    'p': 556, 'q': 556, 'r': 333, 's': 500, 't': 278, 'u': 556, 'v': 500, 'w': 722,
    'x': 500, 'y': 500, 'z': 500, '{': 334, '|': 260, '}': 334, '~': 584
}

HELVETICA_BOLD_WIDTHS = {
    ' ': 278, '!': 333, '"': 474, '#': 556, '$': 556, '%': 889, '&': 722, "'": 238,
    '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333, '.': 278, '/': 278,
    '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556, '7': 556,
    '8': 556, '9': 556, ':': 333, ';': 333, '<': 584, '=': 584, '>': 584, '?': 611,
    '@': 975, 'A': 722, 'B': 722, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778,
    'H': 722, 'I': 278, 'J': 556, 'K': 722, 'L': 611, 'M': 833, 'N': 722, 'O': 778,
    'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 333, '\\': 278, ']': 333, '^': 584, '_': 556,
    '`': 333, 'a': 556, 'b': 611, 'c': 556, 'd': 611, 'e': 556, 'f': 333, 'g': 611,
    'h': 611, 'i': 278, 'j': 278, 'k': 556, 'l': 278, 'm': 889, 'n': 611, 'o': 611,
    'p': 611, 'q': 611, 'r': 389, 's': 556, 't': 333, 'u': 611, 'v': 556, 'w': 778,
    'x': 556, 'y': 556, 'z': 500, '{': 389, '|': 280, '}': 389, '~': 584
}

def string_width(text, font_name, font_size):
    widths_table = HELVETICA_BOLD_WIDTHS if 'Bold' in font_name else HELVETICA_WIDTHS
    total_w = 0
    for ch in text:
        w = widths_table.get(ch, 550)
        total_w += w
    return (total_w / 1000.0) * font_size

def escape_pdf_string(text):
    """Clean string for WinAnsi / PDF literal string."""
    replacements = {
        '—': '---',
        '–': '--',
        '•': '*',
        '’': "'",
        '‘': "'",
        '“': '"',
        '”': '"',
        '…': '...',
        '–': '-',
        '™': '(TM)',
        '©': '(C)',
        '®': '(R)',
        '±': '+/-',
        '°': ' deg',
        '³': '^3',
        '²': '^2',
        'é': 'e',
        'è': 'e',
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    
    # Escape backslash and parens
    res = []
    for char in text:
        if char == '\\':
            res.append('\\\\')
        elif char == '(':
            res.append('\\(')
        elif char == ')':
            res.append('\\)')
        elif ord(char) < 32 or ord(char) > 126:
            res.append(' ')
        else:
            res.append(char)
    return "".join(res)

class PDFDocument:
    def __init__(self):
        self.pages = []  # list of list of content stream strings
        self.current_page = []
        self.page_number = 0
        self.y = PAGE_HEIGHT - MARGIN_TOP

    def new_page(self):
        if self.current_page:
            self.pages.append(self.current_page)
        self.current_page = []
        self.page_number += 1
        self.y = PAGE_HEIGHT - MARGIN_TOP

    def finish_current_page(self):
        if self.current_page:
            self.pages.append(self.current_page)
            self.current_page = []

    def ensure_space(self, height_needed):
        if self.y - height_needed < MARGIN_BOTTOM + 25:
            self.new_page()

    def draw_rect(self, x, y, w, h, fill_rgb=None, stroke_rgb=None, line_width=1.0):
        cmd = ["q"]
        if fill_rgb:
            cmd.append(f"{fill_rgb[0]:.3f} {fill_rgb[1]:.3f} {fill_rgb[2]:.3f} rg")
        if stroke_rgb:
            cmd.append(f"{stroke_rgb[0]:.3f} {stroke_rgb[1]:.3f} {stroke_rgb[2]:.3f} RG")
        cmd.append(f"{line_width:.2f} w")
        cmd.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re")
        if fill_rgb and stroke_rgb:
            cmd.append("B")
        elif fill_rgb:
            cmd.append("f")
        elif stroke_rgb:
            cmd.append("S")
        cmd.append("Q")
        self.current_page.append(" ".join(cmd))

    def draw_line(self, x1, y1, x2, y2, stroke_rgb=(0.7, 0.7, 0.7), line_width=0.75):
        cmd = [
            "q",
            f"{stroke_rgb[0]:.3f} {stroke_rgb[1]:.3f} {stroke_rgb[2]:.3f} RG",
            f"{line_width:.2f} w",
            f"{x1:.2f} {y1:.2f} m",
            f"{x2:.2f} {y2:.2f} l",
            "S",
            "Q"
        ]
        self.current_page.append(" ".join(cmd))

    def draw_text(self, x, y, text, font="F1", size=10, rgb=(0.1, 0.1, 0.1)):
        clean = escape_pdf_string(text)
        cmd = [
            "BT",
            f"/{font} {size:.2f} Tf",
            f"{rgb[0]:.3f} {rgb[1]:.3f} {rgb[2]:.3f} rg",
            f"{x:.2f} {y:.2f} Td",
            f"({clean}) Tj",
            "ET"
        ]
        self.current_page.append(" ".join(cmd))

    def wrap_text(self, text, font_name, font_size, max_width):
        words = text.split()
        if not words:
            return [""]
        lines = []
        cur_line = []
        cur_w = 0.0
        space_w = string_width(" ", font_name, font_size)

        for w in words:
            w_len = string_width(w, font_name, font_size)
            if not cur_line:
                cur_line.append(w)
                cur_w = w_len
            else:
                if cur_w + space_w + w_len <= max_width:
                    cur_line.append(w)
                    cur_w += space_w + w_len
                else:
                    lines.append(" ".join(cur_line))
                    cur_line = [w]
                    cur_w = w_len
        if cur_line:
            lines.append(" ".join(cur_line))
        return lines

    def build_pdf_bytes(self):
        self.finish_current_page()
        total_pages = len(self.pages)
        if total_pages == 0:
            total_pages = 1
            self.pages = [[]]

        # First, add Running Header & Footer to every page content stream
        for idx, page_ops in enumerate(self.pages):
            pnum = idx + 1
            header_ops = []
            # Header on pages 2+
            if pnum > 1:
                header_ops.append(
                    f"q 0.500 0.550 0.520 rg /F2 8.5 Tf {MARGIN_LEFT:.2f} {PAGE_HEIGHT - 34:.2f} Td (ECOLAKESIDE FARM  |  ENVIRONMENTAL MASTER PLAN BRIEFING) Tj Q"
                )
                header_ops.append(
                    f"q 0.820 0.850 0.820 RG 0.5 w {MARGIN_LEFT:.2f} {PAGE_HEIGHT - 39:.2f} m {PAGE_WIDTH - MARGIN_RIGHT:.2f} {PAGE_HEIGHT - 39:.2f} l S Q"
                )
            # Footer on all pages
            footer_text_left = "EcoLakeside Farm - Complete Website Content & Presentation Briefing"
            footer_text_right = f"Page {pnum} of {total_pages}"
            right_w = string_width(footer_text_right, "Helvetica", 8.5)
            
            header_ops.append(
                f"q 0.820 0.850 0.820 RG 0.5 w {MARGIN_LEFT:.2f} {MARGIN_BOTTOM - 12:.2f} m {PAGE_WIDTH - MARGIN_RIGHT:.2f} {MARGIN_BOTTOM - 12:.2f} l S Q"
            )
            header_ops.append(
                f"q 0.500 0.550 0.520 rg /F1 8.5 Tf {MARGIN_LEFT:.2f} {MARGIN_BOTTOM - 24:.2f} Td ({escape_pdf_string(footer_text_left)}) Tj Q"
            )
            header_ops.append(
                f"q 0.400 0.450 0.420 rg /F2 8.5 Tf {PAGE_WIDTH - MARGIN_RIGHT - right_w:.2f} {MARGIN_BOTTOM - 24:.2f} Td ({escape_pdf_string(footer_text_right)}) Tj Q"
            )
            # Prepend or append to page_ops
            page_ops.extend(header_ops)

        # PDF Objects assembly
        # Obj 1: Catalog
        # Obj 2: Pages
        # Obj 3..N: Page objects, Font objects, Content streams
        objects = {}
        next_obj = 1

        catalog_id = next_obj
        next_obj += 1
        pages_id = next_obj
        next_obj += 1

        font1_id = next_obj
        next_obj += 1
        font2_id = next_obj
        next_obj += 1
        font3_id = next_obj
        next_obj += 1

        page_ids = []
        stream_ids = []

        for _ in range(total_pages):
            page_ids.append(next_obj)
            next_obj += 1
            stream_ids.append(next_obj)
            next_obj += 1

        # Catalog
        objects[catalog_id] = f"<< /Type /Catalog /Pages {pages_id} 0 R >>"

        # Pages collection
        kids_str = " ".join([f"{pid} 0 R" for pid in page_ids])
        objects[pages_id] = f"<< /Type /Pages /Kids [{kids_str}] /Count {total_pages} >>"

        # Fonts (Helvetica, Helvetica-Bold, Helvetica-Oblique)
        objects[font1_id] = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>"
        objects[font2_id] = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>"
        objects[font3_id] = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>"

        # Assemble Page and Stream objects
        for idx in range(total_pages):
            pid = page_ids[idx]
            sid = stream_ids[idx]
            content_str = "\n".join(self.pages[idx])
            content_bytes = content_str.encode('latin1', errors='replace')

            objects[pid] = (
                f"<< /Type /Page /Parent {pages_id} 0 R "
                f"/MediaBox [0 0 {PAGE_WIDTH:.2f} {PAGE_HEIGHT:.2f}] "
                f"/Contents {sid} 0 R "
                f"/Resources << /Font << /F1 {font1_id} 0 R /F2 {font2_id} 0 R /F3 {font3_id} 0 R >> >> >>"
            )

            objects[sid] = (
                f"<< /Length {len(content_bytes)} >>\nstream\n{content_str}\nendstream"
            )

        # Write output PDF
        out = bytearray()
        out.extend(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")

        offsets = {}
        for obj_idx in range(1, next_obj):
            offsets[obj_idx] = len(out)
            body = objects[obj_idx]
            if isinstance(body, str):
                body_bytes = body.encode('latin1', errors='replace')
            else:
                body_bytes = body
            out.extend(f"{obj_idx} 0 obj\n".encode('ascii'))
            out.extend(body_bytes)
            out.extend(b"\nendobj\n")

        xref_pos = len(out)
        out.extend(f"xref\n0 {next_obj}\n".encode('ascii'))
        out.extend(b"0000000000 65535 f \n")
        for obj_idx in range(1, next_obj):
            out.extend(f"{offsets[obj_idx]:010d} 00000 n \n".encode('ascii'))

        out.extend(
            f"trailer\n<< /Size {next_obj} /Root {catalog_id} 0 R >>\n"
            f"startxref\n{xref_pos}\n%%EOF\n".encode('ascii')
        )

        return bytes(out)


def render_document(markdown_path, output_pdf_path):
    with open(markdown_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    doc = PDFDocument()
    doc.new_page()

    # Brand Colors
    C_FOREST = (0.09, 0.22, 0.11)       # #17381C
    C_MID_GREEN = (0.17, 0.38, 0.20)    # #2C6133
    C_LIGHT_GREEN = (0.92, 0.96, 0.93)  # #EAF5ED
    C_BORDER_GREEN = (0.75, 0.85, 0.77) # #C0D9C4
    C_DARK_TEXT = (0.15, 0.17, 0.16)    # #262B28
    C_MUTED_TEXT = (0.42, 0.46, 0.43)   # #6B756E
    C_ACCENT_GOLD = (0.85, 0.62, 0.12)  # #D99E1F
    C_WHITE = (1.0, 1.0, 1.0)
    C_CARD_BG = (0.96, 0.98, 0.96)      # #F5FAF6

    # -------------------------------------------------------------
    # HERO BANNER ON PAGE 1
    # -------------------------------------------------------------
    hero_h = 145.0
    doc.y -= hero_h
    doc.draw_rect(MARGIN_LEFT, doc.y, CONTENT_WIDTH, hero_h, fill_rgb=C_FOREST, stroke_rgb=C_MID_GREEN, line_width=1.5)
    
    # Subtitle eyebrow inside banner
    doc.draw_text(MARGIN_LEFT + 20, doc.y + hero_h - 26, "SUSTAINABLE AGRICULTURE SUMMIT  *  CASE STUDY BRIEFING", font="F2", size=9, rgb=C_ACCENT_GOLD)
    
    # Main Banner Title
    doc.draw_text(MARGIN_LEFT + 20, doc.y + hero_h - 52, "ECOLAKESIDE FARM INITIATIVE", font="F2", size=22, rgb=C_WHITE)
    
    # Banner Tagline
    tagline = "Master Environmental Farm Plan: 240-Hectare Sustainable Companion Farming & Watershed Defense"
    doc.draw_text(MARGIN_LEFT + 20, doc.y + hero_h - 72, tagline, font="F3", size=10, rgb=(0.88, 0.94, 0.89))
    
    # Badges row inside banner
    doc.draw_line(MARGIN_LEFT + 20, doc.y + 44, MARGIN_LEFT + CONTENT_WIDTH - 20, doc.y + 44, stroke_rgb=(0.25, 0.45, 0.28), line_width=0.75)
    
    meta_pills = [
        "Potatoes & Garlic Companions",
        "4R Nutrient Stewardship",
        "Constructed Wetland Bio-Filter",
        "Nutrients For Life Partner"
    ]
    cur_x = MARGIN_LEFT + 20
    for p in meta_pills:
        pw = string_width(p, "Helvetica-Bold", 8) + 12
        doc.draw_rect(cur_x, doc.y + 18, pw, 18, fill_rgb=(0.14, 0.32, 0.17), stroke_rgb=(0.28, 0.52, 0.31), line_width=0.5)
        doc.draw_text(cur_x + 6, doc.y + 24, p, font="F2", size=8, rgb=C_WHITE)
        cur_x += pw + 8

    doc.y -= 18

    # -------------------------------------------------------------
    # 4 STAT METRICS CARDS (Hero stats)
    # -------------------------------------------------------------
    card_w = (CONTENT_WIDTH - 30) / 4.0
    card_h = 58.0
    doc.y -= card_h

    stats_data = [
        ("240 ha", "Total Landscape Area", "Whole Property"),
        ("210 ha", "Companion Cropland", "Potatoes & Garlic"),
        ("30 ha", "Water Buffer & Zones", "Wetlands & Forest"),
        ("0 Litres", "Lake Extraction", "100% Recycled Drip")
    ]

    for idx, (val, label, sub) in enumerate(stats_data):
        cx = MARGIN_LEFT + idx * (card_w + 10)
        doc.draw_rect(cx, doc.y, card_w, card_h, fill_rgb=C_CARD_BG, stroke_rgb=C_BORDER_GREEN, line_width=1.0)
        doc.draw_text(cx + 10, doc.y + card_h - 20, val, font="F2", size=14, rgb=C_MID_GREEN)
        doc.draw_text(cx + 10, doc.y + card_h - 35, label, font="F2", size=8.5, rgb=C_DARK_TEXT)
        doc.draw_text(cx + 10, doc.y + card_h - 48, sub, font="F1", size=7.5, rgb=C_MUTED_TEXT)

    doc.y -= 22

    # -------------------------------------------------------------
    # PARSING THE MARKDOWN CONTENT SECTION BY SECTION
    # -------------------------------------------------------------
    raw_lines = md_text.splitlines()

    # Skip the initial markdown header lines since we already created the rich Hero Banner
    # We will start parsing from "## 1. Header & Navigation Structure" or section 1
    start_index = 0
    for i, line in enumerate(raw_lines):
        if line.startswith("## 1. Header & Navigation Structure"):
            start_index = i
            break

    content_lines = raw_lines[start_index:]
    i = 0
    total_lines = len(content_lines)

    while i < total_lines:
        line = content_lines[i].strip()
        i += 1

        if not line:
            continue

        if line == "---":
            # Section separator
            doc.ensure_space(20)
            doc.draw_line(MARGIN_LEFT, doc.y, MARGIN_LEFT + CONTENT_WIDTH, doc.y, stroke_rgb=(0.82, 0.86, 0.83), line_width=0.75)
            doc.y -= 14
            continue

        # Major Section Header (## 1. / ## 2. / etc.)
        if line.startswith("## "):
            sec_title = line[3:].strip()
            # Clean up title
            doc.ensure_space(55)
            doc.y -= 10
            
            # Header container pill
            doc.draw_rect(MARGIN_LEFT, doc.y - 4, CONTENT_WIDTH, 26, fill_rgb=C_LIGHT_GREEN, stroke_rgb=C_BORDER_GREEN, line_width=0.75)
            doc.draw_rect(MARGIN_LEFT, doc.y - 4, 6, 26, fill_rgb=C_MID_GREEN)
            
            doc.draw_text(MARGIN_LEFT + 14, doc.y + 4, sec_title.upper(), font="F2", size=11, rgb=C_FOREST)
            doc.y -= 24
            continue

        # Subsection Header (### )
        if line.startswith("### "):
            sub_title = line[4:].strip()
            doc.ensure_space(34)
            doc.y -= 6
            doc.draw_text(MARGIN_LEFT, doc.y, sub_title, font="F2", size=10.5, rgb=C_MID_GREEN)
            doc.y -= 4
            doc.draw_line(MARGIN_LEFT, doc.y, MARGIN_LEFT + string_width(sub_title, "Helvetica-Bold", 10.5) + 20, doc.y, stroke_rgb=C_ACCENT_GOLD, line_width=1.0)
            doc.y -= 12
            continue

        # Sub-subsection Header (#### )
        if line.startswith("#### "):
            h4_title = line[5:].strip()
            doc.ensure_space(24)
            doc.draw_text(MARGIN_LEFT, doc.y, h4_title, font="F2", size=9.5, rgb=C_FOREST)
            doc.y -= 13
            continue

        # Blockquote (> )
        if line.startswith("> "):
            quote_text = line[2:].strip().replace("**", "")
            # Collect continuation lines if any
            while i < total_lines and content_lines[i].strip().startswith("> "):
                quote_text += " " + content_lines[i].strip()[2:].strip().replace("**", "")
                i += 1
            
            wrapped = doc.wrap_text(quote_text, "Helvetica-Oblique", 9.5, CONTENT_WIDTH - 36)
            q_box_h = len(wrapped) * 14.0 + 16.0
            doc.ensure_space(q_box_h + 10)
            
            doc.draw_rect(MARGIN_LEFT, doc.y - q_box_h + 12, CONTENT_WIDTH, q_box_h, fill_rgb=C_LIGHT_GREEN, stroke_rgb=C_BORDER_GREEN, line_width=0.75)
            doc.draw_rect(MARGIN_LEFT, doc.y - q_box_h + 12, 4, q_box_h, fill_rgb=C_ACCENT_GOLD)
            
            qy = doc.y - 2
            for ql in wrapped:
                doc.draw_text(MARGIN_LEFT + 16, qy, ql, font="F3", size=9.5, rgb=C_FOREST)
                qy -= 14.0
            doc.y -= (q_box_h + 6)
            continue

        # Bullet List Item (- or *)
        if line.startswith("- ") or line.startswith("* "):
            bullet_raw = line[2:].strip()
            # If the item spans multiple indented lines:
            while i < total_lines and (content_lines[i].startswith("    ") or content_lines[i].startswith("  -") or content_lines[i].startswith("  *")):
                sub_l = content_lines[i].strip()
                if sub_l.startswith("- ") or sub_l.startswith("* "):
                    bullet_raw += " " + sub_l[2:].strip()
                else:
                    bullet_raw += " " + sub_l
                i += 1

            # Check for bold title prefix like: **Title:** Body
            bold_match = re.match(r"^\*\*(.*?)\*\*(.*)", bullet_raw)
            if bold_match:
                prefix = bold_match.group(1).strip()
                rest = bold_match.group(2).strip()
                full_text = f"{prefix} {rest}" if rest else prefix
            else:
                full_text = bullet_raw.replace("**", "").replace("*", "")

            # Word wrap for indented bullet list
            bullet_indent = 16.0
            wrap_w = CONTENT_WIDTH - bullet_indent
            wrapped = doc.wrap_text(full_text, "Helvetica", 9.0, wrap_w)
            
            item_h = len(wrapped) * 13.0 + 3.0
            doc.ensure_space(item_h)
            
            # Draw green bullet dot
            doc.draw_rect(MARGIN_LEFT + 4, doc.y + 1, 3.5, 3.5, fill_rgb=C_MID_GREEN)
            
            # First line
            first_line = wrapped[0]
            # If we had a bold prefix, try to emphasize the first words
            if bold_match and prefix:
                doc.draw_text(MARGIN_LEFT + bullet_indent, doc.y, first_line, font="F2" if len(wrapped) == 1 and not rest else "F1", size=9.0, rgb=C_DARK_TEXT)
            else:
                doc.draw_text(MARGIN_LEFT + bullet_indent, doc.y, first_line, font="F1", size=9.0, rgb=C_DARK_TEXT)
            
            doc.y -= 13.0
            for subsequent in wrapped[1:]:
                doc.draw_text(MARGIN_LEFT + bullet_indent, doc.y, subsequent, font="F1", size=9.0, rgb=C_DARK_TEXT)
                doc.y -= 13.0
            doc.y -= 2.0
            continue

        # Numbered List Item (1. , 2. , etc.)
        num_match = re.match(r"^(\d+)\.\s+(.*)", line)
        if num_match:
            num_str = num_match.group(1) + "."
            num_content = num_match.group(2).strip()
            
            # Collect continuation lines
            while i < total_lines and (content_lines[i].startswith("   ") or content_lines[i].startswith("\t")):
                num_content += " " + content_lines[i].strip()
                i += 1
                
            clean_text = num_content.replace("**", "").replace("*", "")
            wrap_w = CONTENT_WIDTH - 22.0
            wrapped = doc.wrap_text(clean_text, "Helvetica", 9.0, wrap_w)
            
            item_h = len(wrapped) * 13.0 + 3.0
            doc.ensure_space(item_h)
            
            doc.draw_text(MARGIN_LEFT + 2, doc.y, num_str, font="F2", size=9.0, rgb=C_MID_GREEN)
            doc.draw_text(MARGIN_LEFT + 22, doc.y, wrapped[0], font="F1", size=9.0, rgb=C_DARK_TEXT)
            doc.y -= 13.0
            for subsequent in wrapped[1:]:
                doc.draw_text(MARGIN_LEFT + 22, doc.y, subsequent, font="F1", size=9.0, rgb=C_DARK_TEXT)
                doc.y -= 13.0
            doc.y -= 2.0
            continue

        # Standard Paragraph Text
        clean_para = line.replace("**", "").replace("*", "")
        # Collect additional non-empty, non-header lines
        while i < total_lines:
            next_l = content_lines[i].strip()
            if not next_l or next_l.startswith("#") or next_l.startswith("-") or next_l.startswith("*") or next_l.startswith(">") or re.match(r"^\d+\.", next_l) or next_l == "---":
                break
            clean_para += " " + next_l.replace("**", "").replace("*", "")
            i += 1

        wrapped = doc.wrap_text(clean_para, "Helvetica", 9.0, CONTENT_WIDTH)
        para_h = len(wrapped) * 13.0 + 5.0
        doc.ensure_space(para_h)

        for pl in wrapped:
            doc.draw_text(MARGIN_LEFT, doc.y, pl, font="F1", size=9.0, rgb=C_DARK_TEXT)
            doc.y -= 13.0
        doc.y -= 4.0

    # Build and write final PDF
    pdf_bytes = doc.build_pdf_bytes()
    with open(output_pdf_path, 'wb') as f:
        f.write(pdf_bytes)

    print(f"Successfully generated PDF: {output_pdf_path} ({len(pdf_bytes)} bytes, {len(doc.pages)} pages)")

if __name__ == '__main__':
    md_file = "/Users/aayansikri/Documents/Antigravity/Agriculture Summit/EcoLakeside_Farm_Complete_Website_Document.md"
    pdf_file = "/Users/aayansikri/Documents/Antigravity/Agriculture Summit/EcoLakeside_Farm_Complete_Website_Document.pdf"
    render_document(md_file, pdf_file)
