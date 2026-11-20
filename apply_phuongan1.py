# -*- coding: utf-8 -*-
import docx

def update_docx():
    doc = docx.Document('Bao_Cao_PTTK_GaraMan_De26.docx')
    
    # 1. Update Table 1 (Glossary List)
    t1 = doc.tables[1]
    # Delete row 37 (Xe ô tô)
    row_to_delete = t1.rows[37]
    tr = row_to_delete._tr
    tr.getparent().remove(tr)
    
    # Renumber rows from 37 onwards
    # After removing row 37, the old row 38 becomes row 37
    for idx in range(37, len(t1.rows)):
        cell0 = t1.rows[idx].cells[0]
        # Current number should be idx - 3 (since 3 rows are headers/non-data)
        # Let's check: row 34 is 31, row 35 is 32, row 36 is 33.
        # So row idx is (idx - 3)
        new_num = str(idx - 3)
        cell0.text = new_num
        cell0.paragraphs[0].runs[0].font.name = "Times New Roman"
        cell0.paragraphs[0].runs[0].font.size = docx.shared.Pt(10)
        cell0.paragraphs[0].alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER

    # 2. Update Paragraph 22 (Section 2.4)
    # Let's inspect P22 and replace text
    for p in doc.paragraphs:
        if "Loại khách hàng, Mã số thuế cá nhân" in p.text:
            p.text = p.text.replace("Loại khách hàng, Mã số thuế cá nhân.", "Biển số xe.")
        if "  - Xe ô tô: Mã xe, Biển số xe, Hãng xe, Dòng xe, Năm sản xuất, Màu sơn.\n" in p.text:
            p.text = p.text.replace("  - Xe ô tô: Mã xe, Biển số xe, Hãng xe, Dòng xe, Năm sản xuất, Màu sơn.\n", "")
        if "Khách hàng, Xe, Dịch vụ yêu cầu" in p.text:
            p.text = p.text.replace("Khách hàng, Xe, Dịch vụ yêu cầu", "Khách hàng, Biển số xe, Dịch vụ yêu cầu")
        if "Khách hàng, Xe, Nhân viên bán hàng" in p.text:
            p.text = p.text.replace("Khách hàng, Xe, Nhân viên bán hàng", "Khách hàng, Biển số xe, Nhân viên bán hàng")

    # 3. Update Paragraph 24 (Section 2.5)
    for p in doc.paragraphs:
        if "• Một khách hàng sở hữu một hoặc nhiều xe ô tô (1 - n).\n" in p.text:
            p.text = p.text.replace("• Một khách hàng sở hữu một hoặc nhiều xe ô tô (1 - n).\n", "")
        if "mỗi lịch hẹn gắn với một xe và dịch vụ đăng ký ban đầu" in p.text:
            p.text = p.text.replace("mỗi lịch hẹn gắn với một xe và dịch vụ đăng ký ban đầu", "mỗi lịch hẹn gắn với một dịch vụ đăng ký ban đầu và biển số xe của khách")
        if "lập cho một khách hàng và một xe cụ thể (n - 1)" in p.text:
            p.text = p.text.replace("lập cho một khách hàng và một xe cụ thể (n - 1)", "lập cho một khách hàng (n - 1) gắn với biển số xe sửa chữa")

    doc.save('Bao_Cao_PTTK_GaraMan_De26.docx')
    # also save a copy to clean
    doc.save('Bao_Cao_PTTK_GaraMan_De26_Clean.docx')
    print("Updated Bao_Cao_PTTK_GaraMan_De26.docx successfully with Phuong An 1!")

if __name__ == "__main__":
    update_docx()
