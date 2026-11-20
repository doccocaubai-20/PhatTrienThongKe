import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_cell_border(cell, **kwargs):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
    for border_name in ['top', 'left', 'bottom', 'right']:
        edge_data = kwargs.get(border_name)
        if edge_data:
            val, sz, space, color = edge_data
            b_xml = parse_xml(f'<w:{border_name} {nsdecls("w")} w:val="{val}" w:sz="{sz}" w:space="{space}" w:color="{color}"/>')
            tcBorders.append(b_xml)
        else:
            b_xml = parse_xml(f'<w:{border_name} {nsdecls("w")} w:val="single" w:sz="4" w:space="0" w:color="D3D3D3"/>')
            tcBorders.append(b_xml)
    tcPr.append(tcBorders)

def add_styled_paragraph(doc, text, style_type='normal', align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = doc.add_paragraph()
    p.alignment = align
    run = p.add_run(text)
    
    if style_type == 'h1':
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(8)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(16)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    elif style_type == 'h2':
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x2C, 0x4D, 0x75)
    elif style_type == 'h3':
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    elif style_type == 'h4':
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.italic = True
        run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    elif style_type == 'placeholder':
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(10)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.italic = True
        run.font.color.rgb = RGBColor(0x33, 0x55, 0x88)
    elif style_type == 'quote':
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.left_indent = Inches(0.25)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(11.5)
        run.font.italic = True
        run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    else: # normal
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

def create_table_from_markdown(doc, md_table_lines):
    # Parse markdown table
    rows_data = []
    for line in md_table_lines:
        line = line.strip()
        if not line.startswith('|'):
            continue
        # Split by |
        parts = [p.strip() for p in line.split('|')[1:-1]]
        # Check if separator
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
    
    # Assign widths
    col_widths = [Inches(1.8), Inches(4.7)] if num_cols == 2 else [Inches(0.6), Inches(1.8), Inches(1.8), Inches(2.3)]
    for row in table.rows:
        for idx, width in enumerate(col_widths[:num_cols]):
            row.cells[idx].width = width
            
    for r_idx, row_vals in enumerate(rows_data):
        row = table.rows[r_idx]
        is_header = (r_idx == 0)
        bg_color = "1B365D" if is_header else ("F4F6F9" if r_idx % 2 == 1 else "FFFFFF")
        
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=90, bottom=90, left=130, right=130)
            set_cell_border(cell)
            
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            
            # Format text (handling <br/> and bold)
            clean_text = val.replace('<br/>', '\n').replace('&nbsp;', ' ')
            runs = clean_text.split('**')
            bold_flag = False
            for chunk in runs:
                if chunk:
                    r = p.add_run(chunk)
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(10.5) if not is_header else Pt(11)
                    if is_header:
                        r.font.bold = True
                        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                    else:
                        r.font.bold = bold_flag or (c_idx == 0 and num_cols == 2)
                        r.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
                bold_flag = not bold_flag
                
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return table

def append_phase2_to_doc(docx_path):
    doc = docx.Document(docx_path)
    
    # Check if Phase 2 already exists
    for p in doc.paragraphs:
        if 'II. PHÂN TÍCH YÊU CẦU' in p.text:
            print(f'{docx_path} already contains Phase 2!')
            return
            
    # Page break
    doc.add_page_break()
    
    with open('PHAN2_PHAN_TICH_YEU_CAU.md', 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    lines = md_text.split('\n')
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
        elif line.startswith('*[Hình'):
            placeholder_text = line.strip('*')
            add_styled_paragraph(doc, placeholder_text, 'placeholder')
            i += 1
        elif line.startswith('> '):
            add_styled_paragraph(doc, line.replace('> ', ''), 'quote')
            i += 1
        elif line.startswith('|'):
            # Collect full table
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i].strip())
                i += 1
            create_table_from_markdown(doc, table_lines)
        else:
            add_styled_paragraph(doc, line, 'normal')
            i += 1
            
    doc.save(docx_path)
    print(f'Successfully appended Phase 2 to {docx_path}!')

append_phase2_to_doc('Bao_Cao_PTTK_GaraMan_De26_Clean.docx')
append_phase2_to_doc('Bao_Cao_PTTK_GaraMan_De26.docx')
