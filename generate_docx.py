# -*- coding: utf-8 -*-
"""
Script to generate standard, clean academic submission DOCX for GaraMan
Updated with all critique feedback: 4 actors, clean Use Case decomposition,
no flowchart antipatterns, unified session/transaction screen flow.
"""

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_code_box(doc, code_text, caption="Mã nguồn PlantUML"):
    p_cap = doc.add_paragraph()
    p_cap.paragraph_format.space_before = Pt(8)
    p_cap.paragraph_format.space_after = Pt(3)
    p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_cap = p_cap.add_run(f"• {caption}:")
    r_cap.bold = True
    r_cap.font.name = "Times New Roman"
    r_cap.font.size = Pt(10.5)
    r_cap.font.color.rgb = RGBColor(0x1B, 0x4F, 0x72)

    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, "F8F9F9")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="BDC3C7"/><w:left w:val="single" w:sz="14" w:space="0" w:color="2874A6"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="BDC3C7"/><w:right w:val="single" w:sz="4" w:space="0" w:color="BDC3C7"/></w:tcBorders>')
    tcPr.append(borders)
    
    lines = code_text.strip().split('\n')
    for idx, line in enumerate(lines):
        p_line = cell.paragraphs[0] if idx == 0 else cell.add_paragraph()
        p_line.paragraph_format.space_before = Pt(0)
        p_line.paragraph_format.space_after = Pt(0)
        p_line.paragraph_format.line_spacing = 1.05
        run = p_line.add_run(line)
        run.font.name = "Consolas"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)

def create_report():
    doc = Document()
    
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0x20, 0x20, 0x20)
    normal_style.paragraph_format.line_spacing = 1.2
    normal_style.paragraph_format.space_after = Pt(4)

    # ==================== COVER PAGE ====================
    p_header = doc.add_paragraph()
    p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_header.paragraph_format.space_after = Pt(2)
    r1 = p_header.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\nHỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG\n")
    r1.bold = True
    r1.font.size = Pt(12)
    r2 = p_header.add_run("KHOA CÔNG NGHỆ THÔNG TIN\n")
    r2.bold = True
    r2.font.size = Pt(11)
    r2.font.color.rgb = RGBColor(0x50, 0x50, 0x50)
    
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_after = Pt(24)
    r_line = p_line.add_run("-----------------------***-----------------------")
    r_line.font.color.rgb = RGBColor(0x7F, 0x8C, 0x8D)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(8)
    r_t1 = p_title.add_run("BÁO CÁO BÀI TẬP LỚN\nPHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG")
    r_t1.bold = True
    r_t1.font.size = Pt(18)
    r_t1.font.color.rgb = RGBColor(0x1B, 0x4F, 0x72)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(28)
    r_t2 = p_sub.add_run("HỆ THỐNG QUẢN LÝ GARA Ô TÔ (GaraMan)")
    r_t2.bold = True
    r_t2.font.size = Pt(14)
    r_t2.font.color.rgb = RGBColor(0x28, 0x74, 0xA6)

    info_table = doc.add_table(rows=4, cols=2)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Học phần:", "Phân tích và Thiết kế Hệ thống"),
        ("Giảng viên hướng dẫn:", "[Họ và tên Giảng viên]"),
        ("Sinh viên thực hiện:", "[Họ và tên Sinh viên]"),
        ("Mã sinh viên / Lớp:", "[Mã SV] - [Lớp]")
    ]
    for i, (k, v) in enumerate(meta_data):
        row = info_table.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        set_cell_background(c0, "F8F9F9")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=60, bottom=60, left=100, right=100)
        set_cell_margins(c1, top=60, bottom=60, left=100, right=100)
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.size = Pt(11)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.size = Pt(11)

    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(24)

    # ==================== PHẦN I: ĐẶC TẢ YÊU CẦU ====================
    h1 = doc.add_heading("I. ĐẶC TẢ YÊU CẦU", level=1)
    h1.paragraph_format.space_before = Pt(18)
    h1.paragraph_format.space_after = Pt(8)
    for r in h1.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(16)
        r.font.color.rgb = RGBColor(0x1B, 0x4F, 0x72)
        r.bold = True

    # 1. Bảng từ khóa
    h2_1 = doc.add_heading("1. Bảng từ khóa (Glossary List)", level=2)
    h2_1.paragraph_format.space_before = Pt(12)
    h2_1.paragraph_format.space_after = Pt(6)
    for r in h2_1.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(13.5)
        r.font.color.rgb = RGBColor(0x28, 0x74, 0xA6)
        r.bold = True

    p_intro = doc.add_paragraph("Tập hợp và phân loại các từ khóa chuyên môn trong phạm vi hoạt động của hệ thống quản lý gara ô tô:")
    p_intro.paragraph_format.space_after = Pt(8)

    glossary_items = [
        ("HEADER", "Nhóm các khái niệm liên quan đến con người", "", ""),
        (1, "Thành viên", "Member", "Người có tài khoản và mật khẩu để đăng nhập vào hệ thống, là lớp cha trừu tượng của toàn bộ người dùng tương tác."),
        (2, "Nhân viên", "Staff / Employee", "Thành viên làm việc tại gara ô tô, được phân quyền các nghiệp vụ nội bộ theo chức vụ."),
        (3, "Nhân viên quản lý", "Manager", "Người điều hành gara, xem các báo cáo thống kê kinh doanh và quản lý danh mục dịch vụ, phụ tùng."),
        (4, "Nhân viên kho", "Warehouse Staff", "Người phụ trách việc nhập kho phụ tùng từ nhà cung cấp và quản lý hồ sơ đối tác cung ứng."),
        (5, "Nhân viên bán hàng", "Sales Staff", "Người tiếp nhận khách hàng và xe, lập phiếu sửa chữa, phân công thợ kỹ thuật và thu tiền thanh toán."),
        (6, "Khách hàng", "Customer", "Chủ sở hữu hoặc người điều khiển ô tô sử dụng dịch vụ tại gara hoặc đặt lịch hẹn trực tuyến qua hệ thống."),
        (7, "Nhân viên kỹ thuật", "Technician", "Thợ máy trực tiếp thực hiện sửa chữa tại xưởng; đóng vai trò là thực thể dữ liệu nhân sự để nhân viên bán hàng phân công phụ trách dịch vụ."),
        (8, "Nhà cung cấp", "Supplier", "Đối tác kinh doanh cung ứng phụ tùng cho gara; đóng vai trò là thực thể đối tác giao dịch lưu trữ trong CSDL."),
        ("HEADER", "Nhóm các khái niệm liên quan đến hoạt động của con người", "", ""),
        (9, "Đăng nhập", "Login", "Quá trình người dùng xác thực tài khoản và mật khẩu để truy cập vào hệ thống GaraMan."),
        (10, "Đăng xuất", "Logout", "Hoạt động kết thúc phiên làm việc an toàn của người dùng trên hệ thống."),
        (11, "Đổi mật khẩu", "Change Password", "Hoạt động người dùng chủ động cập nhật mật khẩu mới để bảo mật tài khoản cá nhân."),
        (12, "Tìm kiếm thông tin dịch vụ / phụ tùng", "Search Service Info & Parts", "Thao tác của khách hàng nhập từ khóa để tra cứu danh mục dịch vụ hoặc phụ tùng và xem thông tin chi tiết."),
        (13, "Xem chi tiết dịch vụ", "View Service Detail", "Mở trang hiển thị thông số chi tiết, giá cả niêm yết, quy trình, bảo hành của một dịch vụ cụ thể."),
        (14, "Xem chi tiết phụ tùng", "View Spare Part Detail", "Mở trang hiển thị thông số chi tiết, hãng sản xuất, giá bán niêm yết, tình trạng tồn kho của một phụ tùng."),
        (15, "Đặt lịch hẹn trực tuyến", "Book Online Appointment", "Hoạt động khách hàng chọn trước ngày giờ, loại xe và dịch vụ mong muốn để gara sắp xếp chỗ đón tiếp."),
        (16, "Nhập phụ tùng", "Import Spare Parts", "Quy trình nhân viên kho chọn nhà cung cấp, chọn danh mục phụ tùng, nhập số lượng, đơn giá và lưu hóa đơn nhập."),
        (17, "Quản lý nhà cung cấp", "Manage Suppliers", "Cập nhật, lưu trữ hồ sơ liên hệ, địa chỉ và lịch sử giao dịch với các đơn vị cung cấp phụ tùng."),
        (18, "Thêm mới nhà cung cấp", "Add New Supplier", "Hoạt động lưu thông tin một đối tác cung cấp mới khi chưa có trong danh bạ hệ thống trong quá trình nhập hàng."),
        (19, "Thêm mới phụ tùng", "Add New Spare Part", "Hoạt động khai báo loại phụ tùng mới vào danh mục khi tiến hành nhập hàng chưa từng có trước đó."),
        (20, "Quản lý dịch vụ", "Manage Services", "Hoạt động thêm mới, điều chỉnh tên gọi, mô tả chi tiết, giá niêm yết hoặc ngừng cung cấp các hạng mục dịch vụ."),
        (21, "Quản lý phụ tùng", "Manage Spare Parts", "Hoạt động thêm mới, cập nhật đơn giá bán lẻ, định mức tồn kho và quy cách của phụ tùng."),
        (22, "Nhận khách", "Receive Customer", "Nhân viên bán hàng đón tiếp khách, ghi nhận thông tin xe và tình trạng ban đầu khi đưa vào xưởng."),
        (23, "Nhận yêu cầu dịch vụ và phụ tùng", "Receive Service Request", "Ghi nhận chi tiết các gói bảo dưỡng, sửa chữa hoặc phụ tùng thay thế mà khách hàng đồng ý thực hiện."),
        (24, "Phân công kỹ thuật", "Assign Technician", "Nhân viên bán hàng lựa chọn kỹ thuật viên phù hợp để phụ trách từng hạng mục dịch vụ cụ thể trên xe khách."),
        (25, "Nhận thanh toán", "Receive Payment", "Nhân viên bán hàng chốt chi phí, thu tiền từ khách và xuất hóa đơn dịch vụ hoàn tất giao dịch."),
        (26, "Xem thống kê", "View Statistics", "Quản lý thực hiện tra cứu số liệu tổng hợp về doanh thu, lượt phục vụ theo dịch vụ, phụ tùng, đối tác và khách hàng."),
        (27, "Thống kê dịch vụ", "Service Statistics", "Báo cáo xếp hạng dịch vụ theo doanh thu và số lượt thực hiện trong một chu kỳ thời gian."),
        (28, "Thống kê phụ tùng", "Part Statistics", "Báo cáo số lượng phụ tùng tiêu thụ, doanh thu và tồn kho của các mặt hàng."),
        (29, "Thống kê khách hàng", "Customer Statistics", "Báo cáo tổng hợp số lần sử dụng dịch vụ và tổng tiền chi tiêu của từng khách hàng."),
        (30, "Thống kê nhà cung cấp", "Supplier Statistics", "Báo cáo tổng giá trị hàng nhập và số lần giao dịch theo từng đơn vị cung cấp."),
        ("HEADER", "Nhóm các khái niệm liên quan đến vật, đối tượng xử lí", "", ""),
        (31, "Mặt hàng", "Item", "Lớp cha trừu tượng của các hàng hóa/dịch vụ kinh doanh tại gara (mã, tên, đơn giá, mô tả)."),
        (32, "Dịch vụ", "Service", "Công việc kỹ thuật gara cung cấp (kế thừa Mặt hàng, có thêm: thời gian dự kiến, bảo hành)."),
        (33, "Phụ tùng", "Spare Part", "Linh kiện, vật tư thay thế cho xe (kế thừa Mặt hàng, có thêm: hãng sản xuất, xuất xứ, đơn vị tính, số lượng tồn kho)."),
        (34, "Xe ô tô", "Vehicle / Car", "Đối tượng phương tiện của khách hàng tiếp nhận các dịch vụ sửa chữa, bảo dưỡng và thay thế phụ tùng tại gara."),
        (35, "Hóa đơn nhập", "Import Invoice", "Chứng từ lưu lại số lượng, giá mua, tổng tiền và ngày giao dịch khi nhập phụ tùng từ nhà cung cấp."),
        (36, "Chi tiết phụ tùng nhập", "Imported Part Item", "Dòng dữ liệu trong hóa đơn nhập, thể hiện một mặt hàng phụ tùng, số lượng và đơn giá nhập cụ thể."),
        (37, "Phiếu sửa chữa (Hóa đơn dịch vụ)", "Repair Order / Job Sheet", "Chứng từ xuyên suốt theo dõi tiến trình tiếp nhận xe, liên kết dịch vụ đã làm, phụ tùng đã thay, thợ phụ trách và thanh toán."),
        (38, "Chi tiết dịch vụ sử dụng", "Service Usage Detail", "Hạng mục dịch vụ được thực hiện trong phiếu sửa chữa và kỹ thuật viên đảm nhận."),
        (39, "Chi tiết phụ tùng thay thế", "Part Replacement Detail", "Phụ tùng được xuất kho lắp ráp cho xe và đơn giá bán tương ứng."),
        (40, "Lịch hẹn", "Appointment", "Bản ghi hẹn trước về ngày giờ, loại xe và dịch vụ mà khách hàng đăng ký trên hệ thống."),
        (41, "Báo cáo thống kê", "Statistics Report", "Dữ liệu tổng hợp theo tiêu chí thời gian phục vụ công tác quản trị của nhân viên quản lý.")
    ]

    t_glossary = doc.add_table(rows=1, cols=4)
    t_glossary.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = t_glossary.rows[0].cells
    hdr_cells[0].width, hdr_cells[1].width, hdr_cells[2].width, hdr_cells[3].width = Inches(0.5), Inches(2.0), Inches(1.8), Inches(2.4)
    for idx, name in enumerate(["TT", "Tên Tiếng Việt", "Tên Tiếng Anh", "Giải thích chi tiết"]):
        set_cell_background(hdr_cells[idx], "2874A6")
        set_cell_margins(hdr_cells[idx], 80, 80, 100, 100)
        p = hdr_cells[idx].paragraphs[0]
        if idx == 0:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(name)
        r.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(10)

    for item in glossary_items:
        row = t_glossary.add_row()
        c = row.cells
        c[0].width, c[1].width, c[2].width, c[3].width = Inches(0.5), Inches(2.0), Inches(1.8), Inches(2.4)
        if item[0] == "HEADER":
            c[0].merge(c[3])
            set_cell_background(c[0], "EAECEE")
            set_cell_margins(c[0], 60, 60, 100, 100)
            p = c[0].paragraphs[0]
            r = p.add_run(item[1])
            r.bold = True
            r.font.size = Pt(10.5)
            r.font.color.rgb = RGBColor(0x1B, 0x4F, 0x72)
        else:
            set_cell_margins(c[0], 50, 50, 80, 80)
            set_cell_margins(c[1], 50, 50, 80, 80)
            set_cell_margins(c[2], 50, 50, 80, 80)
            set_cell_margins(c[3], 50, 50, 80, 80)
            
            p0 = c[0].paragraphs[0]
            p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p0.add_run(str(item[0])).font.size = Pt(10)
            
            p1 = c[1].paragraphs[0]
            r1 = p1.add_run(item[1])
            r1.bold = True
            r1.font.size = Pt(10)
            
            p2 = c[2].paragraphs[0]
            r2 = p2.add_run(item[2])
            r2.italic = True
            r2.font.size = Pt(10)
            
            p3 = c[3].paragraphs[0]
            p3.add_run(item[3]).font.size = Pt(10)

    # 2. Mô tả tự nhiên
    h2_2 = doc.add_heading("2. Mô tả hệ thống bằng ngôn ngữ tự nhiên", level=2)
    h2_2.paragraph_format.space_before = Pt(16)
    h2_2.paragraph_format.space_after = Pt(6)
    for r in h2_2.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(13.5)
        r.font.color.rgb = RGBColor(0x28, 0x74, 0xA6)
        r.bold = True

    # 2.1
    doc.add_heading("2.1 Giới thiệu mục đích hệ thống", level=3)
    doc.add_paragraph("Hệ thống quản lý gara ô tô (GaraMan) là một ứng dụng nền tảng web phục vụ công tác quản lý quy trình dịch vụ sửa chữa, bảo dưỡng ô tô; quản lý danh mục và hoạt động nhập phụ tùng từ nhà cung cấp; tiếp nhận yêu cầu, phân công kỹ thuật và thanh toán của khách hàng; hỗ trợ khách hàng tra cứu dịch vụ, phụ tùng, đặt lịch hẹn trực tuyến và cung cấp các báo cáo thống kê phục vụ công tác quản trị gara.")

    # 2.2
    doc.add_heading("2.2 Phạm vi hệ thống", level=3)
    doc.add_paragraph("Hệ thống được thiết kế phục vụ 4 tác nhân chính trực tiếp đăng nhập và sử dụng các chức năng nghiệp vụ:")
    p_b2 = doc.add_paragraph()
    p_b2.paragraph_format.left_indent = Inches(0.25)
    p_b2.add_run("• Thành viên hệ thống: ").bold = True
    p_b2.add_run("Đăng nhập, Đăng xuất, Đổi mật khẩu cá nhân.\n")
    p_b2.add_run("• Khách hàng: ").bold = True
    p_b2.add_run("Được thực hiện các chức năng của thành viên sau khi đăng nhập, Tìm kiếm thông tin dịch vụ / phụ tùng, Xem thông tin chi tiết dịch vụ/phụ tùng, Đặt lịch hẹn trực tuyến.\n")
    p_b2.add_run("• Nhân viên bán hàng: ").bold = True
    p_b2.add_run("Được thực hiện các chức năng của thành viên, Nhận khách và xe, Nhận yêu cầu dịch vụ và phụ tùng từ khách, Phân công nhân viên kỹ thuật theo dịch vụ yêu cầu, Nhận thanh toán và xuất hóa đơn cho khách hàng.\n")
    p_b2.add_run("• Nhân viên kho: ").bold = True
    p_b2.add_run("Được thực hiện các chức năng của thành viên, Nhập phụ tùng từ nhà cung cấp, Quản lý thông tin nhà cung cấp (tìm kiếm, thêm mới, cập nhật).\n")
    p_b2.add_run("• Nhân viên quản lý: ").bold = True
    p_b2.add_run("Được thực hiện các chức năng của thành viên, Quản lý thông tin dịch vụ (thêm, sửa, khóa), Quản lý thông tin phụ tùng (thêm, sửa đơn giá bán, định mức tồn), Xem các loại thống kê: thống kê dịch vụ, thống kê phụ tùng, thống kê khách hàng, thống kê nhà cung cấp.\n")
    p_b2.add_run("(Ghi chú: Nhân viên kỹ thuật và Nhà cung cấp đóng vai trò là các thực thể dữ liệu được quản lý trong cơ sở dữ liệu, không có tài khoản trực tiếp đăng nhập vào phần mềm).")

    # 2.3
    doc.add_heading("2.3 Hoạt động nghiệp vụ của các chức năng", level=3)
    doc.add_paragraph("Mô tả chi tiết luồng tương tác và xử lý nghiệp vụ của các chức năng chính:")
    
    p_b3_1 = doc.add_paragraph()
    r = p_b3_1.add_run("a. Chức năng Khách hàng tìm kiếm thông tin dịch vụ / phụ tùng:\n")
    r.bold = True
    p_b3_1.add_run("Sau khi đăng nhập thành công, từ giao diện chính của khách hàng (GDChinhKhachHang), khách hàng chọn menu \"Tìm thông tin dịch vụ / phụ tùng\". Hệ thống hiển thị giao diện tìm kiếm (GDTimKiemDVPT) với ô nhập từ khóa tìm kiếm và nút \"Tìm kiếm\".\n"
                   "Khách hàng nhập từ khóa tên dịch vụ hoặc phụ tùng cần tìm (ví dụ: \"thay dầu\", \"lọc gió\") và click \"Tìm kiếm\". Hệ thống truy vấn CSDL và hiển thị danh sách các dịch vụ/phụ tùng có tên chứa từ khóa vừa nhập (gồm: Mã, Tên, Đơn giá niêm yết, và nút \"Xem chi tiết\").\n"
                   "Khách hàng click vào một mục dịch vụ hoặc phụ tùng trong danh sách: Nếu là dịch vụ, chuyển sang giao diện chi tiết dịch vụ (GDChiTietDV) hiển thị Mã dịch vụ, Tên dịch vụ, Đơn giá, Thời gian dự kiến thực hiện, Mô tả quy trình, Thời gian bảo hành; Nếu là phụ tùng, chuyển sang giao diện chi tiết phụ tùng (GDChiTietPT) hiển thị Mã phụ tùng, Tên phụ tùng, Hãng sản xuất, Xuất xứ, Đơn vị tính, Đơn giá bán niêm yết, Tình trạng còn hàng.\n"
                   "Khách hàng có thể nhấn \"Quay lại\" để tiếp tục tra cứu từ khóa khác. Trường hợp không tìm thấy kết quả phù hợp, hệ thống xuất thông báo cảnh báo và cho phép người dùng nhập lại từ khóa khác.")

    p_b3_2 = doc.add_paragraph()
    r = p_b3_2.add_run("b. Chức năng Nhân viên kho nhập phụ tùng từ nhà cung cấp:\n")
    r.bold = True
    p_b3_2.add_run("Sau khi đăng nhập thành công, từ giao diện chính của nhân viên kho (GDChinhNVKho), nhân viên chọn menu \"Nhập phụ tùng\". Giao diện tìm kiếm nhà cung cấp (GDTimNCC) hiển thị ô tìm kiếm nhà cung cấp theo tên, nút \"Tìm kiếm\" và nút \"Thêm mới NCC\". Nhân viên nhập tên NCC và click \"Tìm kiếm\". Hệ thống hiển thị danh sách NCC phù hợp (Mã NCC, Tên, SĐT, Địa chỉ, Mã số thuế) kèm nút \"Chọn\". Trường hợp NCC chưa có trong hệ thống, nhân viên click \"Thêm mới NCC\", giao diện GDThemNCC hiển thị form nhập thông tin đối tác -> bấm \"Lưu NCC\" -> Hệ thống lưu vào CSDL và tự động chọn NCC này.\n"
                   "Sau khi đã chọn xong 1 NCC, hệ thống chuyển sang giao diện lập hóa đơn nhập phụ tùng (GDNhapPhuTung). Màn hình hiển thị: Thông tin NCC đã chọn; Bảng danh sách các mặt hàng phụ tùng đã chọn nhập trong phiên làm việc hiện tại (được lưu tạm thời trong Session, ban đầu rỗng); Nút \"Tìm phụ tùng\"; và nút \"Lưu hóa đơn\".\n"
                   "Vòng lặp nhập phụ tùng diễn ra như sau: Nhân viên click \"Tìm phụ tùng\", mở giao diện GDTimPhuTung -> Nhân viên nhập tên phụ tùng và bấm \"Tìm kiếm\" -> Hệ thống hiện danh sách phụ tùng kèm nút \"Chọn\" (nếu phụ tùng mới chưa có trong danh mục, nhân viên bấm \"Thêm mới phụ tùng\", mở GDThemPhuTung để nhập Tên, Hãng SX, Xuất xứ, Đơn vị tính, Đơn giá bán niêm yết dự kiến và bấm Lưu) -> Sau khi chọn phụ tùng, hệ thống chuyển sang giao diện GDNhapSoLuongGia -> Nhân viên nhập Số lượng nhập và Đơn giá nhập, bấm \"Thêm vào hóa đơn\" -> Hệ thống cập nhật phụ tùng vào giỏ Session, tính lại Tổng tiền và quay về GDNhapPhuTung. Nhân viên lặp lại các bước trên cho đến khi nhập xong toàn bộ các mặt hàng.\n"
                   "Khi đã kiểm tra đầy đủ danh sách phụ tùng, nhân viên click nút \"Lưu hóa đơn\". Hệ thống thực thi một Transaction cơ sở dữ liệu: Thêm bản ghi mới vào bảng tblHoaDonNhap (lấy ID tự sinh), thêm các bản ghi vào bảng tblChiTietNhap, cập nhật tăng số lượng tồn kho trong bảng tblPhuTung, kết thúc Transaction và giải phóng Session. Sau đó hệ thống chuyển sang giao diện xem chứng từ (GDHoaDonNhap) để nhân viên in phiếu và thanh toán cho nhà cung cấp.")

    p_b3_3 = doc.add_paragraph()
    r = p_b3_3.add_run("c. Chức năng Nhân viên quản lý xem thống kê dịch vụ:\n")
    r.bold = True
    p_b3_3.add_run("Nhân viên quản lý đăng nhập vào hệ thống -> chọn chức năng \"Xem thống kê\" -> hệ thống hiện giao diện chọn loại thống kê -> chọn \"Thống kê theo dịch vụ\" -> Quản lý chọn khoảng thời gian cần thống kê (Từ ngày - Đến ngày) -> Kết quả thống kê hiện lên, mỗi dịch vụ trên một dòng, xếp theo thứ tự doanh thu từ cao nhất đến thấp nhất (STT, Mã dịch vụ, Tên dịch vụ, Số lượt thực hiện, Tổng doanh thu) -> Quản lý click vào một dịch vụ cụ thể -> Hệ thống hiển thị danh sách các lần thực hiện dịch vụ đó (Ngày thực hiện, Biển số xe, Tên khách hàng, Kỹ thuật viên phụ trách, Số tiền thanh toán).")

    # 2.4
    doc.add_heading("2.4 Thông tin các đối tượng cần xử lý, quản lý", level=3)
    p_b4 = doc.add_paragraph()
    p_b4.paragraph_format.left_indent = Inches(0.2)
    p_b4.add_run("• Nhóm người dùng:\n").bold = True
    p_b4.add_run("  - Thành viên: Tên đăng nhập, Mật khẩu, Họ và tên, Ngày sinh, Địa chỉ, Số điện thoại, Email.\n"
                 "  - Khách hàng: Kế thừa Thành viên, có thêm Biển số xe.\n"
                 "  - Nhân viên: Kế thừa Thành viên, có thêm Mã nhân viên, Vị trí công việc, Hệ số lương.\n"
                 "  - Nhân viên quản lý, Nhân viên kho, Nhân viên bán hàng: Kế thừa Nhân viên.\n"
                 "  - Nhân viên kỹ thuật: Lưu trữ như một thực thể nhân sự trực thuộc gara (Mã thợ, Họ tên, SĐT, Chuyên môn tay nghề, Trạng thái làm việc).\n")
    p_b4.add_run("• Nhóm danh mục và đối tác:\n").bold = True
    p_b4.add_run("  - Nhà cung cấp: Mã NCC, Tên NCC, Địa chỉ, Số điện thoại, Mã số thuế, Email, Ghi chú.\n"
                 "  - Mặt hàng (lớp cha trừu tượng): Mã mặt hàng, Tên mặt hàng, Đơn giá niêm yết, Mô tả.\n"
                 "  - Dịch vụ: Kế thừa Mặt hàng, có thêm: Thời gian dự kiến thực hiện (phút), Thời gian bảo hành.\n"
                 "  - Phụ tùng: Kế thừa Mặt hàng, có thêm: Hãng sản xuất, Xuất xứ, Đơn vị tính, Số lượng tồn kho.\n")
    p_b4.add_run("• Nhóm vận hành và giao dịch:\n").bold = True
    p_b4.add_run("  - Lịch hẹn: Mã lịch hẹn, Ngày giờ hẹn, Khách hàng, Biển số xe, Dịch vụ yêu cầu, Trạng thái.\n"
                 "  - Hóa đơn nhập: Mã hóa đơn nhập, Ngày giờ nhập, Nhân viên kho, Nhà cung cấp, Tổng tiền, Trạng thái thanh toán.\n"
                 "  - Chi tiết phụ tùng nhập: Mã chi tiết, Hóa đơn nhập, Phụ tùng, Số lượng nhập, Đơn giá nhập.\n"
                 "  - Phiếu sửa chữa (Hóa đơn dịch vụ): Mã phiếu, Ngày giờ tiếp nhận, Ngày giờ hoàn thành, Hiện trạng xe, Khách hàng, Biển số xe, Nhân viên bán hàng, Tổng tiền thanh toán, Thuế VAT, Phương thức thanh toán, Trạng thái.\n"
                 "  - Chi tiết dịch vụ sử dụng: Mã chi tiết DV, Phiếu sửa chữa, Dịch vụ, Kỹ thuật viên phụ trách, Đơn giá thực hiện, Trạng thái hoàn thành.\n"
                 "  - Chi tiết phụ tùng thay thế: Mã chi tiết PT, Phiếu sửa chữa, Phụ tùng, Số lượng xuất, Đơn giá bán.\n")
    p_b4.add_run("• Nhóm báo cáo thống kê:\n").bold = True
    p_b4.add_run("  - Thống kê dịch vụ: Theo số lượt sử dụng, theo tổng doanh thu.\n"
                 "  - Thống kê phụ tùng: Theo số lượng tiêu thụ, theo doanh thu bán lẻ.\n"
                 "  - Thống kê khách hàng: Theo tần suất sử dụng, theo tổng chi tiêu.\n"
                 "  - Thống kê nhà cung cấp: Theo tổng giá trị hàng nhập, theo số lần nhập hàng.")

    # 2.5
    doc.add_heading("2.5 Quan hệ giữa các đối tượng, thông tin", level=3)
    p_b5 = doc.add_paragraph()
    p_b5.paragraph_format.left_indent = Inches(0.2)
    p_b5.add_run("• Một khách hàng có thể đặt nhiều lịch hẹn trực tuyến (1 - n), mỗi lịch hẹn gắn với một dịch vụ đăng ký ban đầu và biển số xe của khách.\n"
                 "• Một nhà cung cấp có thể xuất nhiều hóa đơn nhập phụ tùng cho gara (1 - n).\n"
                 "• Một hóa đơn nhập phụ tùng ứng với một nhà cung cấp duy nhất và do một nhân viên kho lập (n - 1).\n"
                 "• Hóa đơn nhập và Phụ tùng có quan hệ nhiều - nhiều (n - n), được tách thành hai quan hệ 1 - n thông qua thực thể trung gian Chi tiết phụ tùng nhập.\n"
                 "• Một phiếu sửa chữa do một nhân viên bán hàng tiếp nhận lập cho một khách hàng (n - 1) gắn với biển số xe sửa chữa.\n"
                 "• Phiếu sửa chữa và Dịch vụ có quan hệ nhiều - nhiều (n - n), được liên kết qua thực thể trung gian Chi tiết dịch vụ sử dụng. Mỗi chi tiết dịch vụ được phân công cho một nhân viên kỹ thuật thực hiện.\n"
                 "• Phiếu sửa chữa và Phụ tùng có quan hệ nhiều - nhiều (n - n), được liên kết qua thực thể trung gian Chi tiết phụ tùng thay thế.\n"
                 "• Một phiếu sửa chữa hoàn thành theo dõi toàn bộ chi phí và đóng vai trò là chứng từ thanh toán duy nhất cho một lần sửa chữa.")

    # 3. Biểu đồ Use Case tổng quan
    h2_3 = doc.add_heading("3. Biểu đồ Use Case tổng quan và mô tả ca sử dụng", level=2)
    h2_3.paragraph_format.space_before = Pt(16)
    h2_3.paragraph_format.space_after = Pt(6)
    for r in h2_3.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(13.5)
        r.font.color.rgb = RGBColor(0x28, 0x74, 0xA6)
        r.bold = True

    doc.add_heading("3.1 Biểu đồ Use Case tổng quan hệ thống", level=3)
    doc.add_paragraph("Biểu đồ Use Case tổng quan thể hiện cấu trúc phân cấp kế thừa của 4 tác nhân chính (Thành viên -> Khách hàng; Thành viên -> Nhân viên -> Nhân viên quản lý, Nhân viên kho, Nhân viên bán hàng) cùng toàn bộ các chức năng nghiệp vụ của hệ thống:")

    uml_overview = """@startuml
skinparam packageStyle rectangle
skinparam shadowing false
left to right direction

actor "Thành viên" as TV
actor "Khách hàng" as KH
actor "Nhân viên" as NV
actor "Nhân viên quản lý" as QL
actor "Nhân viên kho" as Kho
actor "Nhân viên bán hàng" as BH

TV <|-- KH
TV <|-- NV
NV <|-- QL
NV <|-- Kho
NV <|-- BH

rectangle "Hệ thống Quản lý Gara Ô tô (GaraMan)" {
    usecase "Đăng nhập" as UC_Login
    usecase "Đăng xuất" as UC_Logout
    usecase "Đổi mật khẩu" as UC_ChangePass

    usecase "Tìm kiếm thông tin\\ndịch vụ / phụ tùng" as UC_Search
    usecase "Đặt lịch hẹn trực tuyến" as UC_Book

    usecase "Quản lý dịch vụ" as UC_ManageService
    usecase "Quản lý phụ tùng" as UC_ManagePart
    usecase "Xem thống kê" as UC_Stat
    usecase "Thống kê dịch vụ" as UC_StatService
    usecase "Thống kê phụ tùng" as UC_StatPart
    usecase "Thống kê khách hàng" as UC_StatCustomer
    usecase "Thống kê nhà cung cấp" as UC_StatSupplier

    usecase "Nhập phụ tùng" as UC_ImportPart
    usecase "Quản lý nhà cung cấp" as UC_ManageSupplier

    usecase "Nhận khách và xe" as UC_ReceiveCar
    usecase "Nhận yêu cầu dịch vụ\\nvà phụ tùng" as UC_ReceiveRequest
    usecase "Phân công kỹ thuật viên" as UC_AssignTech
    usecase "Nhận thanh toán" as UC_Payment
}

TV --> UC_Login
TV --> UC_Logout
TV --> UC_ChangePass

KH --> UC_Search
KH --> UC_Book

QL --> UC_ManageService
QL --> UC_ManagePart
QL --> UC_Stat
UC_Stat <|-- UC_StatService
UC_Stat <|-- UC_StatPart
UC_Stat <|-- UC_StatCustomer
UC_Stat <|-- UC_StatSupplier

Kho --> UC_ImportPart
Kho --> UC_ManageSupplier

BH --> UC_ReceiveCar
BH --> UC_ReceiveRequest
BH --> UC_AssignTech
BH --> UC_Payment

@enduml"""
    add_code_box(doc, uml_overview, "Mã PlantUML: Biểu đồ Use Case tổng quan")

    doc.add_heading("3.2 Bảng mô tả tóm tắt Use Case tổng quan", level=3)
    uc_summary_data = [
        (1, "Đăng nhập", "Thành viên", "Xác thực tài khoản và mật khẩu để truy cập vào đúng phân quyền chức năng trong hệ thống."),
        (2, "Đăng xuất", "Thành viên", "Thoát khỏi phiên làm việc hiện tại của tài khoản người dùng."),
        (3, "Đổi mật khẩu", "Thành viên", "Người dùng chủ động cập nhật mật khẩu mới để đảm bảo tính bảo mật cá nhân."),
        (4, "Tìm kiếm thông tin dịch vụ / phụ tùng", "Khách hàng", "Khách hàng nhập từ khóa để tra cứu danh mục bảng giá dịch vụ và linh kiện hiện có tại gara."),
        (5, "Đặt lịch hẹn trực tuyến", "Khách hàng", "Khách hàng chủ động chọn ngày, khung giờ hẹn, loại xe và dịch vụ mong muốn trước khi đưa xe đến xưởng."),
        (6, "Quản lý dịch vụ", "NV Quản lý", "Nhân viên quản lý thiết lập danh mục gói bảo dưỡng/sửa chữa mới, cập nhật giá cước hoặc tạm dừng cung cấp dịch vụ."),
        (7, "Quản lý phụ tùng", "NV Quản lý", "Nhân viên quản lý thêm danh mục linh kiện mới, điều chỉnh đơn giá niêm yết bán lẻ hoặc định mức phụ tùng."),
        (8, "Xem thống kê", "NV Quản lý", "Quản lý tra cứu và trích xuất các báo cáo doanh thu dịch vụ, phụ tùng, khách hàng và giá trị nhập hàng theo thời gian."),
        (9, "Nhập phụ tùng", "NV Kho", "Nhân viên kho tạo phiếu nhập, chọn nhà cung cấp, nhập số lượng, đơn giá và xác nhận tăng lượng tồn kho."),
        (10, "Quản lý nhà cung cấp", "NV Kho", "Nhân viên kho tra cứu, thêm mới đối tác hoặc sửa đổi thông tin liên hệ của các nhà cung cấp linh kiện."),
        (11, "Nhận khách và xe", "NV Bán hàng", "Nhân viên bán hàng tiếp nhận xe, ghi nhận thông tin khách hàng, tình trạng ban đầu của xe khi vào xưởng."),
        (12, "Nhận yêu cầu dịch vụ và phụ tùng", "NV Bán hàng", "Lập danh sách các gói dịch vụ sửa chữa/bảo dưỡng và linh kiện thay thế theo yêu cầu và thỏa thuận với khách."),
        (13, "Phân công kỹ thuật viên", "NV Bán hàng", "Chọn và chỉ định kỹ thuật viên phù hợp để phụ trách từng hạng mục dịch vụ đã tiếp nhận."),
        (14, "Nhận thanh toán", "NV Bán hàng", "Chốt danh sách dịch vụ - phụ tùng hoàn thành, tính tổng chi phí, nhận tiền từ khách và xuất hóa đơn thanh toán.")
    ]
    t_uc = doc.add_table(rows=1, cols=4)
    t_uc.alignment = WD_TABLE_ALIGNMENT.CENTER
    h_uc = t_uc.rows[0].cells
    h_uc[0].width, h_uc[1].width, h_uc[2].width, h_uc[3].width = Inches(0.5), Inches(2.2), Inches(1.5), Inches(2.5)
    for idx, title in enumerate(["STT", "Tên Use Case", "Tác nhân chính", "Mô tả chức năng"]):
        set_cell_background(h_uc[idx], "2874A6")
        set_cell_margins(h_uc[idx], 80, 80, 100, 100)
        p = h_uc[idx].paragraphs[0]
        if idx == 0:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        r.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(10)

    for item in uc_summary_data:
        row = t_uc.add_row()
        c = row.cells
        c[0].width, c[1].width, c[2].width, c[3].width = Inches(0.5), Inches(2.2), Inches(1.5), Inches(2.5)
        for i in range(4):
            set_cell_margins(c[i], 50, 50, 80, 80)
        
        p0 = c[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.add_run(str(item[0])).font.size = Pt(10)
        
        p1 = c[1].paragraphs[0]
        r1 = p1.add_run(item[1])
        r1.bold = True
        r1.font.size = Pt(10)
        
        p2 = c[2].paragraphs[0]
        p2.add_run(item[2]).font.size = Pt(10)
        
        p3 = c[3].paragraphs[0]
        p3.add_run(item[3]).font.size = Pt(10)

    # 4. Use Case Chi tiết
    h2_4 = doc.add_heading("4. Biểu đồ Use Case chi tiết và mô tả ca sử dụng (2 module trọng tâm)", level=2)
    h2_4.paragraph_format.space_before = Pt(16)
    h2_4.paragraph_format.space_after = Pt(6)
    for r in h2_4.runs:
        r.font.name = "Times New Roman"
        r.font.size = Pt(13.5)
        r.font.color.rgb = RGBColor(0x28, 0x74, 0xA6)
        r.bold = True

    # 4.1
    doc.add_heading("4.1 Chức năng Khách hàng tìm kiếm thông tin dịch vụ / phụ tùng", level=3)
    doc.add_paragraph("Biểu đồ phân rã Use Case thể hiện ca sử dụng gốc cùng các ca sử dụng chi tiết mở rộng (<<extend>> Xem chi tiết dịch vụ, Xem chi tiết phụ tùng):")

    uml_m1 = """@startuml
skinparam packageStyle rectangle
skinparam shadowing false
left to right direction

actor "Khách hàng" as KH

rectangle "Phân rã Use Case: Tìm kiếm thông tin dịch vụ / phụ tùng" {
    usecase "Tìm kiếm thông tin\\ndịch vụ / phụ tùng" as UC_SearchRoot
    usecase "Xem chi tiết dịch vụ" as UC_ViewServiceDetail
    usecase "Xem chi tiết phụ tùng" as UC_ViewPartDetail
}

KH --> UC_SearchRoot

UC_ViewServiceDetail ..> UC_SearchRoot : <<extend>>
UC_ViewPartDetail ..> UC_SearchRoot : <<extend>>

@enduml"""
    add_code_box(doc, uml_m1, "Mã PlantUML: Phân rã Use Case Tìm kiếm thông tin dịch vụ / phụ tùng")

    p_spec1_title = doc.add_paragraph()
    p_spec1_title.paragraph_format.space_before = Pt(10)
    p_spec1_title.paragraph_format.space_after = Pt(4)
    r = p_spec1_title.add_run("Bảng đặc tả Use Case chi tiết: Tìm kiếm thông tin dịch vụ / phụ tùng")
    r.bold = True
    r.font.size = Pt(11)

    t_m1 = doc.add_table(rows=6, cols=2)
    t_m1.alignment = WD_TABLE_ALIGNMENT.CENTER
    m1_spec_data = [
        ("Tên Use Case", "Tìm kiếm thông tin dịch vụ / phụ tùng"),
        ("Tác nhân chính", "Khách hàng"),
        ("Tiền điều kiện", "Khách hàng đã đăng nhập thành công vào hệ thống và đang ở giao diện chính của khách hàng (GDChinhKhachHang)."),
        ("Hậu điều kiện", "Khách hàng xem được danh sách kết quả và thông tin chi tiết dịch vụ/phụ tùng theo nhu cầu."),
        ("Luồng sự kiện chính (Main Flow)", "1. Khách hàng bấm chọn menu \"Tìm thông tin dịch vụ / phụ tùng\".\n2. Hệ thống hiển thị giao diện tìm kiếm (GDTimKiemDVPT) với ô nhập từ khóa và nút \"Tìm kiếm\".\n3. Khách hàng nhập tên từ khóa cần tìm (ví dụ: \"thay dầu\") và click \"Tìm kiếm\".\n4. Hệ thống tìm kiếm trong CSDL và hiển thị danh sách các dịch vụ/phụ tùng có tên khớp với từ khóa.\n5. Khách hàng click vào một mục dịch vụ hoặc phụ tùng trong danh sách.\n6. Hệ thống hiển thị toàn bộ thông tin chi tiết của mục đã chọn (chuyển sang GDChiTietDV nếu là dịch vụ, hoặc GDChiTietPT nếu là phụ tùng).\n7. Khách hàng nhấn \"Quay lại\" để tiếp tục tra cứu từ khóa khác."),
        ("Luồng ngoại lệ (Alternative Flow)", "3a. Từ khóa để trống:\n- Nếu khách hàng click \"Tìm kiếm\" mà chưa nhập từ khóa, hệ thống hiển thị thông báo yêu cầu nhập từ khóa tra cứu.\n4a. Không tìm thấy dữ liệu phù hợp:\n- Nếu không có dịch vụ hoặc phụ tùng nào chứa từ khóa, hệ thống thông báo: \"Không tìm thấy kết quả phù hợp!\" và cho phép người dùng nhập từ khóa khác.")
    ]
    for idx, (k, v) in enumerate(m1_spec_data):
        row = t_m1.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.5)
        set_cell_background(c0, "F2F4F4")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 60, 60, 80, 80)
        set_cell_margins(c1, 60, 60, 80, 80)
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.size = Pt(10)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.size = Pt(10)

    # 4.2
    doc.add_heading("4.2 Chức năng Nhân viên kho nhập phụ tùng từ nhà cung cấp", level=3)
    doc.add_paragraph("Biểu đồ phân rã Use Case thể hiện các mục tiêu nghiệp vụ bắt buộc (<<include>> Tìm và chọn nhà cung cấp, Tìm và chọn phụ tùng) cùng các ca sử dụng mở rộng (<<extend>> Thêm mới nhà cung cấp, Thêm mới phụ tùng):")

    uml_m2 = """@startuml
skinparam packageStyle rectangle
skinparam shadowing false
left to right direction

actor "Nhân viên kho" as Kho

rectangle "Phân rã Use Case: Nhập phụ tùng từ nhà cung cấp" {
    usecase "Nhập phụ tùng" as UC_ImportRoot
    usecase "Tìm và chọn\\nnhà cung cấp" as UC_SelectNCC
    usecase "Thêm mới\\nnhà cung cấp" as UC_AddNCC
    usecase "Tìm và chọn phụ tùng" as UC_SelectPart
    usecase "Thêm mới phụ tùng" as UC_AddPart
}

Kho --> UC_ImportRoot

UC_ImportRoot ..> UC_SelectNCC : <<include>>
UC_ImportRoot ..> UC_SelectPart : <<include>>

UC_AddNCC ..> UC_SelectNCC : <<extend>>
UC_AddPart ..> UC_SelectPart : <<extend>>

@enduml"""
    add_code_box(doc, uml_m2, "Mã PlantUML: Phân rã Use Case Nhập phụ tùng từ nhà cung cấp")

    p_spec2_title = doc.add_paragraph()
    p_spec2_title.paragraph_format.space_before = Pt(10)
    p_spec2_title.paragraph_format.space_after = Pt(4)
    r = p_spec2_title.add_run("Bảng đặc tả Use Case chi tiết: Nhập phụ tùng từ nhà cung cấp")
    r.bold = True
    r.font.size = Pt(11)

    t_m2 = doc.add_table(rows=6, cols=2)
    t_m2.alignment = WD_TABLE_ALIGNMENT.CENTER
    m2_spec_data = [
        ("Tên Use Case", "Nhập phụ tùng từ nhà cung cấp"),
        ("Tác nhân chính", "Nhân viên kho"),
        ("Tiền điều kiện", "Nhân viên kho đã đăng nhập thành công vào hệ thống và đang ở giao diện chính của nhân viên kho (GDChinhNVKho)."),
        ("Hậu điều kiện", "Hóa đơn nhập được lưu vĩnh viễn vào CSDL, số lượng tồn kho phụ tùng tăng tương ứng, chứng từ nhập kho hiển thị hoàn tất để in và thanh toán."),
        ("Luồng sự kiện chính (Main Flow)", "1. Nhân viên kho chọn menu \"Nhập phụ tùng\".\n2. Hệ thống chuyển sang giao diện tìm kiếm nhà cung cấp (GDTimNCC).\n3. Nhân viên nhập tên NCC và click \"Tìm kiếm\".\n4. Hệ thống hiển thị danh sách NCC phù hợp, nhân viên click \"Chọn\" NCC mong muốn.\n5. Hệ thống chuyển sang giao diện lập hóa đơn nhập phụ tùng (GDNhapPhuTung) với thông tin NCC đã chọn và giỏ phụ tùng lưu trong Session (ban đầu rỗng).\n6. Nhân viên click nút \"Tìm phụ tùng\", hệ thống mở giao diện tìm phụ tùng (GDTimPhuTung).\n7. Nhân viên tìm kiếm và click \"Chọn\" phụ tùng muốn nhập.\n8. Hệ thống chuyển sang giao diện nhập số lượng và đơn giá (GDNhapSoLuongGia). Nhân viên nhập số lượng nhập và đơn giá nhập, sau đó bấm \"Thêm vào hóa đơn\".\n9. Hệ thống lưu phụ tùng vào giỏ Session, tính lại Tổng tiền và quay về GDNhapPhuTung.\n(Các bước 6-9 được lặp lại nhiều lần cho đến khi nhân viên nhập xong toàn bộ mặt hàng).\n10. Nhân viên click nút \"Lưu hóa đơn\" trên giao diện GDNhapPhuTung.\n11. Hệ thống thực thi Transaction lưu hóa đơn, lưu các chi tiết nhập, cập nhật tăng tồn kho phụ tùng trong CSDL, giải phóng Session và chuyển sang giao diện xem chứng từ (GDHoaDonNhap) để in và thanh toán."),
        ("Luồng ngoại lệ (Alternative Flow)", "4a. Nhà cung cấp chưa tồn tại:\n- Nhân viên click nút \"Thêm mới NCC\", hệ thống mở giao diện GDThemNCC -> nhân viên nhập thông tin đối tác và bấm \"Lưu NCC\". Hệ thống lưu NCC mới vào CSDL và tự động chọn NCC này để tiếp tục bước 5.\n7a. Phụ tùng mới chưa có trong danh mục:\n- Nhân viên click \"Thêm mới phụ tùng\", mở giao diện GDThemPhuTung -> nhập thông tin phụ tùng (kèm đơn giá bán niêm yết dự kiến) và bấm \"Lưu\". Hệ thống lưu phụ tùng mới với tồn kho = 0 và tự động chọn phụ tùng này để chuyển sang bước 8.\n8a. Nhập số liệu sai:\n- Nếu số lượng <= 0 hoặc đơn giá <= 0, hệ thống báo lỗi yêu cầu nhập số dương hợp lệ.\n10a. Hóa đơn chưa có phụ tùng:\n- Nếu bấm \"Lưu hóa đơn\" khi giỏ hàng trong Session đang trống, hệ thống cảnh báo: \"Chưa có phụ tùng nào được chọn vào hóa đơn!\".")
    ]
    for idx, (k, v) in enumerate(m2_spec_data):
        row = t_m2.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.5)
        set_cell_background(c0, "F2F4F4")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 60, 60, 80, 80)
        set_cell_margins(c1, 60, 60, 80, 80)
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.size = Pt(10)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.size = Pt(10)

    # Save
    out_path = r"c:\Users\admin\Documents\PTTK\Bao_Cao_PTTK_GaraMan_De26.docx"
    alt_path = r"c:\Users\admin\Documents\PTTK\Bao_Cao_PTTK_GaraMan_De26_Clean.docx"
    try:
        doc.save(out_path)
        print("Report regenerated successfully at:", out_path)
    except PermissionError:
        doc.save(alt_path)
        print(f"Main file locked. Saved to clean version at: {alt_path}")

if __name__ == "__main__":
    create_report()
