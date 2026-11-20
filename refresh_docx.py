# -*- coding: utf-8 -*-
"""
Script to refresh and finalize Bao_Cao_PTTK_GaraMan_De26.docx
Strict requirements:
1. All headings (H1, H2, H3, H4) must be pure BLACK (RGBColor(0, 0, 0)) - no blue/gray.
2. All tables across the entire document must have pure WHITE background (w:fill="FFFFFF").
   Header text is bold black, data text is black.
3. Clean, natural student-level scenario in Section 1 (v1.0) with zero (GD...) or interaction tags.
   Step numbers match alternative flows: 4 -> 4a, 9 -> 9a, 11 -> 11a, 13 -> 13a.
4. Markdown symbols (**, *, `, LaTeX $\rightarrow$) converted cleanly to Word formatting without raw syntax leaking.
5. All runs across the entire document strictly verified to be pure black.
"""

import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex="FFFFFF"):
    tcPr = cell._tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag.endswith('shd'):
            tcPr.remove(child)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=90, bottom=90, left=130, right=130):
    tcPr = cell._tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag.endswith('tcMar'):
            tcPr.remove(child)
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_cell_border(cell, color="000000", sz="4"):
    tcPr = cell._tc.get_or_add_tcPr()
    for child in list(tcPr):
        if child.tag.endswith('tcBorders'):
            tcPr.remove(child)
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

def parse_markdown_tokens(text):
    """
    Parses markdown text into list of (chunk_text, is_bold, is_italic, is_code)
    """
    text = text.replace('$\\rightarrow$', '→').replace('\\rightarrow', '→')
    text = text.replace('$\\le$', '≤').replace('\\le', '≤')
    pattern = re.compile(r'(\*\*[^*]+?\*\*|\*[^*]+?\*|`[^`]+?`)')
    tokens = pattern.split(text)
    runs_data = []
    for token in tokens:
        if not token:
            continue
        if token.startswith('**') and token.endswith('**'):
            runs_data.append((token[2:-2], True, False, False))
        elif token.startswith('*') and token.endswith('*'):
            runs_data.append((token[1:-1], False, True, False))
        elif token.startswith('`') and token.endswith('`'):
            runs_data.append((token[1:-1], False, False, True))
        else:
            runs_data.append((token, False, False, False))
    return runs_data

def add_runs_to_paragraph(p, text, base_size_pt=12, default_bold=False, default_italic=False):
    tokens = parse_markdown_tokens(text)
    for chunk, b, it, code in tokens:
        run = p.add_run(chunk)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(base_size_pt)
        run.font.bold = default_bold or b
        run.font.italic = default_italic or it
        run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_styled_paragraph(doc, text, style_type='normal', align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = doc.add_paragraph()
    p.alignment = align
    
    if style_type == 'h1':
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(8)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
    elif style_type == 'h2':
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
    elif style_type == 'h3':
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
    elif style_type == 'h4':
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.italic = True
        run.font.color.rgb = RGBColor(0, 0, 0)
    elif style_type == 'placeholder':
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(10)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.italic = True
        run.font.color.rgb = RGBColor(0, 0, 0)
    elif style_type == 'quote':
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Inches(0.25)
        add_runs_to_paragraph(p, text, base_size_pt=11.5, default_italic=True)
    else:  # normal body
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        add_runs_to_paragraph(p, text, base_size_pt=12)
    return p

def create_table_from_markdown(doc, md_table_lines):
    rows_data = []
    for line in md_table_lines:
        line = line.strip()
        if not line.startswith('|'):
            continue
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if all(set(p).issubset({'-', ':', ' '}) for p in parts if p):
            continue
        rows_data.append(parts)
        
    if not rows_data:
        return None
        
    num_rows = len(rows_data)
    num_cols = len(rows_data[0])
    
    table = doc.add_table(rows=num_rows, cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    col_widths = [Inches(1.8), Inches(4.7)] if num_cols == 2 else [Inches(0.6), Inches(1.8), Inches(1.8), Inches(2.3)]
    for row in table.rows:
        for idx, width in enumerate(col_widths[:num_cols]):
            row.cells[idx].width = width
            
    for r_idx, row_vals in enumerate(rows_data):
        row = table.rows[r_idx]
        is_header = (r_idx == 0)
        
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, top=90, bottom=90, left=130, right=130)
            set_cell_border(cell, color="000000", sz="4")
            
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            
            clean_text = val.replace('<br/>', '\n').replace('&nbsp;', ' ')
            is_col0_label = (c_idx == 0 and num_cols == 2)
            
            # Split lines if <br/> was used
            lines_in_cell = clean_text.split('\n')
            for l_idx, sub_line in enumerate(lines_in_cell):
                p_cur = p if l_idx == 0 else cell.add_paragraph()
                p_cur.paragraph_format.space_before = Pt(1)
                p_cur.paragraph_format.space_after = Pt(1)
                add_runs_to_paragraph(
                    p_cur,
                    sub_line,
                    base_size_pt=11 if is_header else 10.5,
                    default_bold=(is_header or is_col0_label)
                )
                
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return table

def enforce_all_black_and_white(doc):
    """
    Sweeps every paragraph and every table cell across the entire document
    to guarantee 100% black text and 100% pure white tables.
    """
    for p in doc.paragraphs:
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.color.rgb = RGBColor(0, 0, 0)
            
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                set_cell_background(cell, "FFFFFF")
                set_cell_border(cell, color="000000", sz="4")
                for p in cell.paragraphs:
                    for r in p.runs:
                        r.font.name = 'Times New Roman'
                        r.font.color.rgb = RGBColor(0, 0, 0)

def refresh_docx_phase2(docx_path):
    print(f"Opening {docx_path}...")
    doc = docx.Document(docx_path)
    
    cutoff_elem = None
    for child in doc._body._element:
        tag = child.tag.split('}')[-1]
        if tag == 'p':
            p = docx.text.paragraph.Paragraph(child, doc)
            if 'II. PHÂN TÍCH YÊU CẦU' in p.text:
                cutoff_elem = child
                break
                
    if cutoff_elem is not None:
        to_remove = []
        found = False
        prev_sibling = cutoff_elem.getprevious()
        if prev_sibling is not None and prev_sibling.tag.split('}')[-1] == 'p' and not prev_sibling.text:
            cutoff_elem = prev_sibling
            
        for child in doc._body._element:
            tag = child.tag.split('}')[-1]
            if child == cutoff_elem:
                found = True
            if found and tag != 'sectPr':
                to_remove.append(child)
                
        print(f'Removing {len(to_remove)} old Phase 2 elements from {docx_path}...')
        for elem in to_remove:
            elem.getparent().remove(elem)
            
    doc.add_page_break()
    
    with open('PHAN2_PHAN_TICH_YEU_CAU.md', 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    md_content_for_docx = md_text.split('## 6. TỔNG HỢP MÃ NGUỒN PLANTUML')[0]
    
    lines = md_content_for_docx.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith('---'):
            i += 1
            continue
            
        if line.startswith('# II. PHÂN TÍCH'):
            add_styled_paragraph(doc, line.replace('# ', ''), 'h1')
            i += 1
        elif line.startswith('## '):
            add_styled_paragraph(doc, line.replace('## ', ''), 'h2')
            i += 1
        elif line.startswith('### '):
            add_styled_paragraph(doc, line.replace('### ', ''), 'h3')
            i += 1
        elif line.startswith('#### '):
            add_styled_paragraph(doc, line.replace('#### ', ''), 'h4')
            i += 1
        elif line.startswith('*[Hình') or line.startswith('[Hình') or (line.startswith('*(') and '[Hình' in line):
            placeholder_text = line.replace('*', '').strip()
            add_styled_paragraph(doc, placeholder_text, 'placeholder')
            i += 1
        elif line.startswith('> '):
            add_styled_paragraph(doc, line.replace('> ', ''), 'quote')
            i += 1
        elif line.startswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip())
                i += 1
            create_table_from_markdown(doc, table_lines)
        else:
            add_styled_paragraph(doc, line, 'normal')
            i += 1
            
    print(f"Enforcing all-black fonts and pure white tables across {docx_path}...")
    enforce_all_black_and_white(doc)
    
    doc.save(docx_path)
    print(f'Successfully refreshed Phase 2 in {docx_path}!')

if __name__ == '__main__':
    refresh_docx_phase2('Bao_Cao_PTTK_GaraMan_De26.docx')
    refresh_docx_phase2('Bao_Cao_PTTK_GaraMan_De26_Clean.docx')
