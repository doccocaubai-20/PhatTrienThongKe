# -*- coding: utf-8 -*-
"""
Script to update Bao_Cao_PTTK_GaraMan_De26.docx from Step 5 onwards (Mục 3, 4, 5)
Preserves all user edits before Step 5 (Cover, Phase 1, Phase 2 Mục 1, Bước 1, 2, 3, 4, 5).
Ensures 100% black headings, white tables, zero leaked markdown syntax.
"""

import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def parse_markdown_tokens(text):
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

def enforce_all_black(doc):
    for p in doc.paragraphs:
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.color.rgb = RGBColor(0, 0, 0)

def update_docx_from_step5(docx_path):
    print(f"Opening {docx_path}...")
    doc = docx.Document(docx_path)
    
    cutoff_elem = None
    for child in doc._body._element:
        tag = child.tag.split('}')[-1]
        if tag == 'p':
            p = docx.text.paragraph.Paragraph(child, doc)
            if '3. BIỂU ĐỒ LỚP PHÂN TÍCH CHO 2 MODULE TRỌNG TÂM' in p.text:
                cutoff_elem = child
                break
                
    if cutoff_elem is None:
        print("Error: Could not find '3. BIỂU ĐỒ LỚP PHÂN TÍCH CHO 2 MODULE TRỌNG TÂM' paragraph!")
        return
        
    to_remove = []
    found = False
    for child in doc._body._element:
        tag = child.tag.split('}')[-1]
        if child == cutoff_elem:
            found = True
        if found and tag != 'sectPr':
            to_remove.append(child)
            
    print(f"Removing {len(to_remove)} old elements from Mục 3 onwards in {docx_path}...")
    for elem in to_remove:
        elem.getparent().remove(elem)
        
    with open('PHAN2_PHAN_TICH_YEU_CAU.md', 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    start_pos = md_text.find('## 3. BIỂU ĐỒ LỚP PHÂN TÍCH')
    end_pos = md_text.find('## 6. TỔNG HỢP MÃ NGUỒN PLANTUML')
    content_to_add = md_text[start_pos:end_pos].strip()
    
    lines = content_to_add.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith('---'):
            i += 1
            continue
            
        if line.startswith('## '):
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
        else:
            add_styled_paragraph(doc, line, 'normal')
            i += 1
            
    print(f"Enforcing all black text across {docx_path}...")
    enforce_all_black(doc)
    
    doc.save(docx_path)
    print(f"Successfully updated {docx_path} from Step 5 onwards!")

if __name__ == '__main__':
    update_docx_from_step5('Bao_Cao_PTTK_GaraMan_De26.docx')
