import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

docx_path = r"C:\Users\admin\Documents\PTTK\Bao_Cao_Giai_Doan_3_Thiet_Ke.docx"
img_dir = r"C:\Users\admin\Documents\PTTK\anh_chuan_hoa"
base_img_dir = r"C:\Users\admin\Documents\PTTK"

doc = docx.Document()

# Page Margins 2cm
sections = doc.sections
for s in sections:
    s.top_margin = Inches(0.79)
    s.bottom_margin = Inches(0.79)
    s.left_margin = Inches(0.98)
    s.right_margin = Inches(0.79)

def style_run(run, font_name="Times New Roman", size_pt=13, bold=False, italic=False, color_rgb=(0,0,0)):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)
    rPr = run._r.get_or_add_rPr()
    rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{font_name}" w:hAnsi="{font_name}" w:cs="{font_name}"/>')
    rPr.append(rFonts)

def add_p(doc, text="", font_name="Times New Roman", size_pt=13, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=6, line_spacing=1.2):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if text:
        r = p.add_run(text)
        style_run(r, font_name, size_pt, bold, italic)
    return p

def add_heading1(doc, text):
    return add_p(doc, text, size_pt=15, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=14, space_after=6)

def add_heading2(doc, text):
    return add_p(doc, text, size_pt=13.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=10, space_after=4)

def add_heading3(doc, text):
    return add_p(doc, text, size_pt=13, bold=True, italic=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=8, space_after=3)

def add_img_with_caption(doc, path, caption, width_in=6.2):
    if os.path.exists(path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(4)
        p_img.add_run().add_picture(path, width=Inches(width_in))
        add_p(doc, caption, size_pt=11, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    else:
        add_p(doc, f"[{caption}]", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

def set_cell_border_and_shading(cell, fill_hex="FFFFFF"):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>
            <w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def create_table(doc, headers, data, col_widths=None):
    tbl = doc.add_table(rows=len(data) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ci, h in enumerate(headers):
        cell = tbl.cell(0, ci)
        set_cell_border_and_shading(cell, "F2F2F2")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(h)
        style_run(r, size_pt=11.5, bold=True)
    for ri, row in enumerate(data):
        for ci, val in enumerate(row):
            cell = tbl.cell(ri + 1, ci)
            set_cell_border_and_shading(cell, "FFFFFF")
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(str(val))
            style_run(r, size_pt=11)
    if col_widths:
        for r in tbl.rows:
            for ci, w in enumerate(col_widths):
                r.cells[ci].width = Inches(w)
    add_p(doc, "", space_after=6)
    return tbl

# --- COVER / TITLE ---
add_p(doc, "BÁO CÁO BÀI TẬP LỚN PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG", size_pt=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=4)
add_p(doc, "ĐỀ TÀI: HỆ THỐNG QUẢN LÝ GARA Ô TÔ (GARAMAN) - ĐỀ SỐ 26", size_pt=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=6)
add_p(doc, "PHẦN III: THIẾT KẾ HỆ THỐNG (BẢN CHUẨN HÓA VÀ KHẮC PHỤC SAI LỆCH)", size_pt=13, bold=True, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=18)

# --- 1. THIẾT KẾ LỚP THỰC THỂ TOÀN HỆ THỐNG ---
add_heading1(doc, "1. THIẾT KẾ LỚP THỰC THỂ TOÀN HỆ THỐNG")
add_p(doc, "Biểu đồ lớp thực thể pha thiết kế được xây dựng dựa trên biểu đồ pha phân tích (Hình 5.1), tuân thủ 4 bước chuẩn hóa trong Giáo trình PTIT (Mục 4.1.1):")
add_p(doc, "1. Bổ sung thuộc tính khóa chính id (kiểu int) cho các lớp thực thể không kế thừa.")
add_p(doc, "2. Gán kiểu dữ liệu cụ thể trong ngôn ngữ lập trình Java (int, double, float, String, Date, boolean).")
add_p(doc, "3. Chuyển đổi các liên kết ngữ nghĩa thành quan hệ kết tập (Aggregation) hoặc hợp thành (Composition), đồng bộ thuộc tính tham chiếu giữa các đối tượng.")
add_p(doc, "4. Bổ sung các phương thức getter/setter và phương thức xử lý nghiệp vụ nội tại của thực thể.")

add_heading2(doc, "1.1 Bảng rà soát chuẩn hóa các lớp thực thể")
headers_tt = ["Lớp thực thể", "Kế thừa / Quan hệ", "Thuộc tính thiết kế chuẩn", "Phương thức nghiệp vụ"]
data_tt = [
    ["ThanhVien", "Lớp cha", "id: int, tenDangNhap, matKhau, hoTen, ngaySinh: Date, diaChi, soDienThoai, email", "ThanhVien(), getter/setter"],
    ["KhachHang", "ThanhVien", "dsXe: List<Xe>", "KhachHang(), themXe(x: Xe)"],
    ["NhanVien", "ThanhVien", "viTri: String, heSoLuong: float", "NhanVien(), getter/setter"],
    ["NVKho", "NhanVien", "(Kế thừa viTri, heSoLuong từ NhanVien)", "NVKho(), getter/setter"],
    ["LichHen", "Độc lập", "id: int, thoiGianHen: Date, trangThai: String, khachHang: KhachHang, xe: Xe, dsDV: List<DichVu>", "LichHen(), getter/setter"],
    ["DichVu", "Độc lập", "id: int, tenDichVu: String, loaiDichVu: String, donGia: double, thoiGianBaoHanh: String", "DichVu(), getter/setter"],
    ["PhuTung", "Độc lập", "id: int, tenPhuTung: String, hangSanXuat: String, donViTinh: String, donGiaNiemYet: double, soLuongTon: int", "PhuTung(), capNhatTonKho(soLuongTang: int): boolean"],
    ["NhaCungCap", "Độc lập", "id: int, tenNCC: String, diaChi: String, soDienThoai: String", "NhaCungCap(), getter/setter"],
    ["HoaDonNhap", "Độc lập", "id: int, ngayGioNhap: Date, tongTien: double, trangThaiThanhToan: String, nhaCungCap: NhaCungCap, nvKho: NVKho, dsChiTietNhap: List<ChiTietNhap>", "HoaDonNhap(), themChiTiet(ct: ChiTietNhap), tinhTongTien(): double, luuHoaDonNhap(): boolean"],
    ["ChiTietNhap", "Hợp thành HDN", "id: int, soLuongNhap: int, donGiaNhap: double, thanhTien: double, phuTung: PhuTung, hoaDonNhap: HoaDonNhap", "ChiTietNhap(), tinhThanhTien(): double"],
    ["TKPhuTung", "PhuTung", "soLuongDaBan: int (chuẩn số nguyên)", "TKPhuTung(), getter/setter"]
]
create_table(doc, headers_tt, data_tt, [1.1, 1.1, 2.8, 1.8])

add_p(doc, "*[Hình 4.1: Biểu đồ lớp thực thể pha thiết kế toàn hệ thống GaraMan]*", bold=True, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)
img11_path = os.path.join(base_img_dir, "extracted_p315_media_image11.png")
if os.path.exists(img11_path):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture(img11_path, width=Inches(6.4))
    add_p(doc, "Hình 4.1: Biểu đồ lớp thực thể pha thiết kế toàn hệ thống GaraMan (đã chuẩn hóa)", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

# --- 2. THIẾT KẾ CƠ SỞ DỮ LIỆU TOÀN HỆ THỐNG ---
add_heading1(doc, "2. THIẾT KẾ CƠ SỞ DỮ LIỆU TOÀN HỆ THỐNG")
add_p(doc, "Mô hình Cơ sở dữ liệu quan hệ được chuyển đổi trực tiếp từ Biểu đồ lớp thực thể pha thiết kế theo các nguyên tắc chuẩn hóa:")
add_p(doc, "1. Mỗi lớp thực thể ánh xạ thành một bảng CSDL (tiền tố tbl).")
add_p(doc, "2. Kế thừa một - một (1-1): Bảng con kế thừa khóa chính từ bảng cha (tblThanhVienid vừa là PK vừa là FK).")
add_p(doc, "3. Khắc phục đứt gãy quan hệ nhiều - nhiều giữa LichHen và DichVu bằng bảng liên kết trung gian tblLichHen_DichVu.")
add_p(doc, "4. Đảm bảo toàn vẹn dữ liệu thời gian bằng kiểu datetime cho ngayGioNhap, thoiGianHen, ngayHoanThanh.")

add_heading2(doc, "2.1 Bảng đặc tả các bảng CSDL chính liên quan 2 module")
headers_db = ["Tên bảng", "Khóa chính (PK)", "Khóa ngoại (FK)", "Các cột dữ liệu và kiểu dữ liệu chuẩn", "Ghi chú"]
data_db = [
    ["tblThanhVien", "id (int, AI)", "Không", "tenDangNhap varchar(255) UNIQUE, matKhau varchar(255), hoTen varchar(255), ngaySinh date, diaChi varchar(255), soDienThoai varchar(255), email varchar(255)", "Bảng cha thông tin người dùng"],
    ["tblKhachHang", "tblThanhVienid (int)", "tblThanhVienid", "-", "Phân cấp khách hàng"],
    ["tblNVKho", "tblNhanVienid (int)", "tblNhanVienid", "-", "Phân cấp nhân viên kho"],
    ["tblLichHen", "id (int, AI)", "tblKhachHangid, tblXeid", "thoiGianHen datetime, trangThai varchar(255)", "Lịch hẹn tiếp nhận xe"],
    ["tblLichHen_DichVu", "id (int, AI)", "tblLichHenid, tblDichVuid", "ghiChu varchar(255)", "Bảng trung gian n-n nối LichHen và DichVu"],
    ["tblDichVu", "id (int, AI)", "Không", "tenDichVu varchar(255), loaiDichVu varchar(255), donGia double, thoiGianBaoHanh varchar(255)", "Danh mục gói dịch vụ"],
    ["tblPhuTung", "id (int, AI)", "Không", "tenPhuTung varchar(255), hangSanXuat varchar(255), donViTinh varchar(255), donGiaNiemYet double, soLuongTon int", "Danh mục phụ tùng kho"],
    ["tblNhaCungCap", "id (int, AI)", "Không", "tenNCC varchar(255), diaChi varchar(255), soDienThoai varchar(255)", "Đối tác cung ứng linh kiện"],
    ["tblHoaDonNhap", "id (int, AI)", "tblNhaCungCapid, tblNVKhoid", "ngayGioNhap datetime, tongTien double, trangThaiThanhToan varchar(255)", "Chứng từ nhập phụ tùng kho"],
    ["tblChiTietNhap", "id (int, AI)", "tblHoaDonNhapid, tblPhuTungid", "soLuongNhap int, donGiaNhap double, thanhTien double", "Dòng mặt hàng trong hóa đơn nhập"]
]
create_table(doc, headers_db, data_db, [1.1, 1.0, 1.3, 2.2, 1.2])

add_p(doc, "*[Hình 4.2: Sơ đồ thiết kế Cơ sở dữ liệu toàn hệ thống GaraMan]*", bold=True, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)
img12_path = os.path.join(base_img_dir, "extracted_p318_media_image12.png")
if os.path.exists(img12_path):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture(img12_path, width=Inches(6.4))
    add_p(doc, "Hình 4.2: Sơ đồ thiết kế Cơ sở dữ liệu quan hệ toàn hệ thống GaraMan (17 bảng)", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

# --- 3. THIẾT KẾ CHI TIẾT 2 MODULE ---
add_heading1(doc, "3. THIẾT KẾ CHI TIẾT CHO 2 MODULE")

# 3.1 MODULE 1
add_heading2(doc, "3.1 Module 1: Khách hàng tìm kiếm thông tin dịch vụ / phụ tùng")
add_heading3(doc, "a) Thiết kế Giao diện (Mockup UI)")
add_p(doc, "Giao diện module 1 gồm 3 màn hình: Trang chủ khách hàng (gdChinhKH.jsp), Tìm kiếm dịch vụ/phụ tùng (gdTimKiemDVPT.jsp), và 2 trang chi tiết (gdChiTietDichVu.jsp và gdChiTietPhuTung.jsp). Đã khắc phục triệt để lỗi lệch cột bảng phụ tùng và đồng bộ đầy đủ các trường thông tin theo lớp thực thể.")

img_ui1 = os.path.join(img_dir, "01_Giao_dien_Tim_thong_tin.png")
if os.path.exists(img_ui1):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture(img_ui1, width=Inches(6.4))
    add_p(doc, "Hình 4.3: Giao diện chi tiết module Tìm kiếm thông tin dịch vụ / phụ tùng", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_heading3(doc, "b) Thiết kế Lớp chi tiết 3 tầng")
add_p(doc, "Cấu trúc 3 tầng gồm:")
add_p(doc, "- Tầng Giao diện (JSP): gdChinhKH.jsp, gdTimKiemDVPT.jsp, gdChiTietDichVu.jsp (bổ sung thuộc tính datLichHen: link), gdChiTietPhuTung.jsp.")
add_p(doc, "- Tầng DAO: DAO kết nối CSDL, DichVuDAO (bổ sung getDichVuById), PhuTungDAO (bổ sung getPhuTungById).")
add_p(doc, "- Tầng Thực thể: ThanhVien (sửa thành soDienThoai), KhachHang, DichVu (bỏ thoiGianDuKien, có loaiDichVu), PhuTung.")

img_cls1 = os.path.join(img_dir, "03_Lop_chi_tiet_Tim_thong_tin.png")
if os.path.exists(img_cls1):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture(img_cls1, width=Inches(6.4))
    add_p(doc, "Hình 4.4: Sơ đồ lớp thiết kế chi tiết 3 tầng module Tìm kiếm dịch vụ / phụ tùng", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

# 3.2 MODULE 2
add_heading2(doc, "3.2 Module 2: Nhân viên kho nhập phụ tùng từ nhà cung cấp")
add_heading3(doc, "a) Thiết kế Giao diện (Mockup UI)")
add_p(doc, "Giao diện module 2 bám sát đúng kịch bản phân tích Giai đoạn 2. Đã loại bỏ các chức năng phát sinh thừa (sửa/xóa dòng đã nhập, popup xác nhận, nút thêm phụ tùng trên GD nhập, luồng thanh toán cho NCC). Mockup gdNhapSoLuongGia.jsp đã bỏ các nhãn bị in lặp.")

img_ui2 = os.path.join(img_dir, "02_Giao_dien_Nhap_phu_tung.png")
if os.path.exists(img_ui2):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture(img_ui2, width=Inches(6.4))
    add_p(doc, "Hình 4.5: Giao diện chi tiết module Nhập phụ tùng từ nhà cung cấp", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_heading3(doc, "b) Thiết kế Lớp chi tiết 3 tầng")
add_p(doc, "Sơ đồ lớp thiết kế chi tiết Module 2 đã khắc phục:")
add_p(doc, "- Bổ sung đường nối phiên làm việc giữa gdChinhKho.jsp và NVKho.")
add_p(doc, "- Sửa chính tả thuộc tính -tblChiTietNhap: Table trong gdNhapPhuTung.jsp.")
add_p(doc, "- Khôi phục các phương thức nghiệp vụ thực thể: HoaDonNhap.themChiTiet(), HoaDonNhap.tinhTongTien(), HoaDonNhap.luuHoaDonNhap(), ChiTietNhap.tinhThanhTien(), PhuTung.capNhatTonKho().")
add_p(doc, "- Đồng bộ kiểu trả về của DAO: NhaCungCapDAO.themNhaCungCap trả về NhaCungCap; PhuTungDAO.themPhuTung trả về PhuTung.")
add_p(doc, "- Loại bỏ hàm ghiNhanThanhToan khỏi HoaDonNhapDAO để đúng phạm vi phân hệ kho.")

img_cls2 = os.path.join(img_dir, "04_Lop_chi_tiet_Nhap_phu_tung.png")
if os.path.exists(img_cls2):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture(img_cls2, width=Inches(6.4))
    add_p(doc, "Hình 4.6: Sơ đồ lớp thiết kế chi tiết 3 tầng module Nhập phụ tùng từ nhà cung cấp", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

# --- 4. THIẾT KẾ ĐỘNG (HOẠT ĐỘNG VÀ TUẦN TỰ) ---
add_heading1(doc, "4. THIẾT KẾ HOẠT ĐỘNG VÀ TUẦN TỰ")

add_heading2(doc, "4.1 Module 1: Tìm kiếm thông tin dịch vụ / phụ tùng")
add_heading3(doc, "a) Biểu đồ hoạt động (Activity Diagram)")
add_p(doc, "Đã sửa lỗi logic: Mũi tên [click quay lại] từ trang chi tiết dịch vụ/phụ tùng trỏ ngược về màn hình gdTimKiemDVPT.jsp để giữ nguyên từ khóa tìm kiếm và bảng kết quả, không đi ra trạng thái Kết thúc.")

img_act1 = os.path.join(img_dir, "05_Activity_Tim_thong_tin.png")
if os.path.exists(img_act1):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture(img_act1, width=Inches(6.0))
    add_p(doc, "Hình 4.7: Biểu đồ hoạt động module Tìm kiếm thông tin dịch vụ / phụ tùng", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_heading3(doc, "b) Biểu đồ tuần tự (Sequence Diagram)")
img_seq1 = os.path.join(img_dir, "07_Sequence_Tim_thong_tin.png")
if os.path.exists(img_seq1):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.add_run().add_picture(img_seq1, width=Inches(6.2))
    add_p(doc, "Hình 4.8: Biểu đồ tuần tự module Tìm kiếm thông tin dịch vụ / phụ tùng", italic=True, align=WD_ALIGN_PARAGRAPH.CENTER)

add_heading3(doc, "c) Kịch bản thiết kế chi tiết v3.0 (Module 1)")
steps_v3_m1 = [
    "1. Tại trang gdChinhKH.jsp, sau khi đăng nhập, khách hàng click chọn chức năng Tìm kiếm thông tin dịch vụ / phụ tùng.",
    "2. Trang gdChinhKH.jsp gọi trang gdTimKiemDVPT.jsp.",
    "3. Trang gdTimKiemDVPT.jsp hiển thị ô nhập từ khóa tìm kiếm và nút Tìm kiếm cho khách hàng.",
    "4. Khách hàng nhập từ khóa tìm kiếm và click nút Tìm kiếm.",
    "5. Trang gdTimKiemDVPT.jsp gọi lớp DichVuDAO yêu cầu lấy danh sách dịch vụ khớp với từ khóa.",
    "6. Lớp DichVuDAO gọi hàm getDichVuTheoTen(tuKhoa).",
    "7. Hàm getDichVuTheoTen(tuKhoa) thực hiện truy vấn CSDL và gọi lớp DichVu đóng gói thông tin.",
    "8. Lớp DichVu đóng gói thông tin thực thể.",
    "9. Lớp DichVu trả kết quả về cho hàm getDichVuTheoTen(tuKhoa).",
    "10. Hàm getDichVuTheoTen(tuKhoa) trả kết quả về cho trang gdTimKiemDVPT.jsp.",
    "11. Trang gdTimKiemDVPT.jsp gọi lớp PhuTungDAO yêu cầu lấy danh sách phụ tùng khớp với từ khóa.",
    "12. Lớp PhuTungDAO gọi hàm getPhuTungTheoTen(tuKhoa).",
    "13. Hàm getPhuTungTheoTen(tuKhoa) thực hiện truy vấn CSDL và gọi lớp PhuTung đóng gói thông tin.",
    "14. Lớp PhuTung đóng gói thông tin thực thể.",
    "15. Lớp PhuTung trả kết quả về cho hàm getPhuTungTheoTen(tuKhoa).",
    "16. Hàm getPhuTungTheoTen(tuKhoa) trả kết quả về cho trang gdTimKiemDVPT.jsp.",
    "17. Trang gdTimKiemDVPT.jsp hiển thị hai bảng danh sách kết quả Dịch vụ và Phụ tùng cho khách hàng.",
    "18. Khách hàng click xem chi tiết một dịch vụ trên bảng kết quả.",
    "19. Trang gdTimKiemDVPT.jsp gọi trang gdChiTietDichVu.jsp kèm mã định danh dịch vụ (id).",
    "20. Trang gdChiTietDichVu.jsp gọi lớp DichVuDAO yêu cầu lấy thông tin chi tiết dịch vụ.",
    "21. Lớp DichVuDAO gọi hàm getDichVuById(id).",
    "22. Hàm getDichVuById(id) thực hiện truy vấn CSDL và gọi lớp DichVu đóng gói thông tin.",
    "23. Lớp DichVu đóng gói thông tin thực thể.",
    "24. Lớp DichVu trả kết quả về cho hàm getDichVuById(id).",
    "25. Hàm getDichVuById(id) trả kết quả về cho trang gdChiTietDichVu.jsp.",
    "26. Trang gdChiTietDichVu.jsp hiển thị thông tin chi tiết dịch vụ, nút Đặt lịch hẹn và nút Quay lại cho khách hàng.",
    "27. Khách hàng click nút Quay lại.",
    "28. Trang gdChiTietDichVu.jsp gọi quay lại trang gdTimKiemDVPT.jsp và giữ nguyên trạng thái kết quả tìm kiếm trước đó.",
    "29. Khách hàng click xem chi tiết một phụ tùng trên bảng kết quả.",
    "30. Trang gdTimKiemDVPT.jsp gọi trang gdChiTietPhuTung.jsp kèm mã định danh phụ tùng (id).",
    "31. Trang gdChiTietPhuTung.jsp gọi lớp PhuTungDAO yêu cầu lấy thông tin chi tiết phụ tùng.",
    "32. Lớp PhuTungDAO gọi hàm getPhuTungById(id).",
    "33. Hàm getPhuTungById(id) thực hiện truy vấn CSDL và gọi lớp PhuTung đóng gói thông tin.",
    "34. Lớp PhuTung đóng gói thông tin thực thể.",
    "35. Lớp PhuTung trả kết quả về cho hàm getPhuTungById(id).",
    "36. Hàm getPhuTungById(id) trả kết quả về cho trang gdChiTietPhuTung.jsp.",
    "37. Trang gdChiTietPhuTung.jsp hiển thị thông tin chi tiết phụ tùng, số lượng tồn kho và nút Quay lại cho khách hàng.",
    "38. Khách hàng click nút Quay lại.",
    "39. Trang gdChiTietPhuTung.jsp gọi quay lại trang gdTimKiemDVPT.jsp và giữ nguyên trạng thái kết quả tìm kiếm trước đó."
]

for s in steps_v3_m1:
    add_p(doc, s, size_pt=11, space_before=1, space_after=3)

add_heading2(doc, "4.2 Module 2: Nhân viên kho nhập phụ tùng từ nhà cung cấp")
add_heading3(doc, "a) Biểu đồ hoạt động (Activity Diagram)")
add_img_with_caption(doc, os.path.join(img_dir, "06_Activity_Nhap_phu_tung.png"), "Hình 4.6: Biểu đồ hoạt động module nhập phụ tùng từ nhà cung cấp")

add_heading3(doc, "b) Biểu đồ tuần tự (Sequence Diagram)")
add_img_with_caption(doc, os.path.join(img_dir, "08_Sequence_Nhap_phu_tung.png"), "Hình 4.8: Biểu đồ tuần tự module nhập phụ tùng từ nhà cung cấp")

add_heading3(doc, "c) Kịch bản thiết kế chi tiết v3.0 (Module 2)")
steps_v3_m2 = [
    "1. Tại trang gdChinhKho.jsp, sau khi đăng nhập, nhân viên kho click chọn menu Nhập phụ tùng.",
    "2. Trang gdChinhKho.jsp gọi mở giao diện tìm kiếm nhà cung cấp gdTimNCC.jsp (gdChonNCC.jsp).",
    "3. Trang gdTimNCC.jsp hiển thị ô nhập từ khóa tên NCC và nút Tìm kiếm cho nhân viên kho.",
    "4. Nhân viên kho nhập tên nhà cung cấp và click nút Tìm kiếm.",
    "5. Trang gdTimNCC.jsp gọi lớp NhaCungCapDAO yêu cầu tìm kiếm danh sách nhà cung cấp.",
    "6. Lớp NhaCungCapDAO gọi hàm getNhaCungCapTheoTen(ten).",
    "7. Hàm getNhaCungCapTheoTen(ten) thực hiện truy vấn CSDL và gọi lớp NhaCungCap đóng gói thông tin.",
    "8. Lớp NhaCungCap đóng gói thông tin thực thể.",
    "9. Lớp NhaCungCap trả kết quả về cho hàm getNhaCungCapTheoTen(ten).",
    "10. Hàm getNhaCungCapTheoTen(ten) trả kết quả về cho trang gdTimNCC.jsp.",
    "11. Trang gdTimNCC.jsp hiển thị danh sách nhà cung cấp lên bảng cho nhân viên kho.",
    "7a.1. Nhân viên kho bấm nút Thêm mới NCC trên trang gdTimNCC.jsp.",
    "7a.2. Trang gdTimNCC.jsp gọi mở giao diện thêm nhà cung cấp gdThemNCC.jsp.",
    "7a.3. Trang gdThemNCC.jsp hiển thị form điền thông tin Nhà cung cấp mới cho nhân viên kho.",
    "7a.4. Nhân viên kho nhập thông tin NCC mới và bấm nút Lưu NCC.",
    "7a.5. Trang gdThemNCC.jsp gọi lớp NhaCungCapDAO yêu cầu lưu NCC mới.",
    "7a.6. Lớp NhaCungCapDAO gọi hàm themNhaCungCap(ncc).",
    "7a.7. Hàm themNhaCungCap(ncc) thực hiện lưu vào CSDL, lấy id tự sinh và gọi lớp NhaCungCap đóng gói thông tin thực thể.",
    "7a.8. Lớp NhaCungCap đóng gói thông tin thực thể.",
    "7a.9. Lớp NhaCungCap trả kết quả về cho hàm themNhaCungCap(ncc).",
    "7a.10. Hàm themNhaCungCap(ncc) trả đối tượng NhaCungCap mới về cho trang gdThemNCC.jsp.",
    "7a.11. Trang gdThemNCC.jsp chuyển đối tượng NhaCungCap mới tạo sang trang gdNhapPhuTung.jsp để tiếp tục quy trình lập hóa đơn.",
    "12. Tại luồng chính: Nhân viên kho bấm nút Chọn một nhà cung cấp trên danh sách của trang gdTimNCC.jsp.",
    "13. Trang gdTimNCC.jsp chuyển thông tin NCC đã chọn sang giao diện lập hóa đơn nhập gdNhapPhuTung.jsp.",
    "14. Trang gdNhapPhuTung.jsp hiển thị thông tin NCC, bảng mặt hàng rỗng và tổng tiền = 0.",
    "15. Nhân viên kho bấm nút Tìm phụ tùng trên trang gdNhapPhuTung.jsp.",
    "16. Trang gdNhapPhuTung.jsp gọi mở giao diện tìm kiếm phụ tùng gdTimPhuTung.jsp.",
    "17. Trang gdTimPhuTung.jsp hiển thị ô từ khóa và nút Tìm kiếm cho nhân viên kho.",
    "18. Nhân viên kho nhập tên phụ tùng và bấm nút Tìm kiếm.",
    "19. Trang gdTimPhuTung.jsp gọi lớp PhuTungDAO yêu cầu tìm kiếm thông tin phụ tùng.",
    "20. Lớp PhuTungDAO gọi hàm getPhuTungTheoTen(tuKhoa).",
    "21. Hàm getPhuTungTheoTen(tuKhoa) thực hiện truy vấn CSDL và gọi lớp PhuTung đóng gói thông tin.",
    "22. Lớp PhuTung đóng gói thông tin thực thể.",
    "23. Lớp PhuTung trả kết quả về cho hàm getPhuTungTheoTen(tuKhoa).",
    "24. Hàm getPhuTungTheoTen(tuKhoa) trả kết quả về cho trang gdTimPhuTung.jsp.",
    "25. Trang gdTimPhuTung.jsp hiển thị danh sách phụ tùng lên bảng cho nhân viên kho.",
    "18a.1. Nhân viên kho bấm nút Thêm mới phụ tùng trên trang gdTimPhuTung.jsp.",
    "18a.2. Trang gdTimPhuTung.jsp gọi mở giao diện thêm phụ tùng gdThemPhuTung.jsp.",
    "18a.3. Trang gdThemPhuTung.jsp hiển thị form nhập phụ tùng mới và nút Lưu cho nhân viên kho.",
    "18a.4. Nhân viên kho nhập thông tin phụ tùng mới và bấm nút Lưu.",
    "18a.5. Trang gdThemPhuTung.jsp gọi lớp PhuTungDAO yêu cầu lưu phụ tùng mới.",
    "18a.6. Lớp PhuTungDAO gọi hàm themPhuTung(pt).",
    "18a.7. Hàm themPhuTung(pt) thực hiện lưu vào CSDL, lấy id tự sinh và gọi lớp PhuTung đóng gói thông tin thực thể.",
    "18a.8. Lớp PhuTung đóng gói thông tin thực thể.",
    "18a.9. Lớp PhuTung trả kết quả về cho hàm themPhuTung(pt).",
    "18a.10. Hàm themPhuTung(pt) trả đối tượng PhuTung mới về cho trang gdThemPhuTung.jsp.",
    "18a.11. Trang gdThemPhuTung.jsp chuyển đối tượng PhuTung mới tạo sang giao diện gdNhapSoLuongGia.jsp để nhân viên nhập số lượng và giá mua.",
    "26. Tại luồng chính: Nhân viên kho bấm nút Chọn một phụ tùng trên danh sách của trang gdTimPhuTung.jsp.",
    "27. Trang gdTimPhuTung.jsp chuyển đối tượng phụ tùng đã chọn sang giao diện nhập số lượng và giá gdNhapSoLuongGia.jsp.",
    "28. Trang gdNhapSoLuongGia.jsp hiển thị thông tin phụ tùng và ô nhập số lượng, đơn giá cho nhân viên kho.",
    "29. Nhân viên kho nhập Số lượng nhập, Đơn giá nhập và bấm nút Thêm vào hóa đơn.",
    "30. Trang gdNhapSoLuongGia.jsp gọi lớp ChiTietNhap yêu cầu tạo mới chi tiết nhập.",
    "31. Lớp ChiTietNhap gọi hàm tinhThanhTien().",
    "32. Hàm tinhThanhTien() thực hiện tính thành tiền (soLuongNhap * donGiaNhap) và gọi lớp ChiTietNhap đóng gói thông tin.",
    "33. Lớp ChiTietNhap đóng gói thông tin thực thể.",
    "34. Lớp ChiTietNhap trả kết quả về cho hàm tinhThanhTien().",
    "35. Hàm tinhThanhTien() trả đối tượng ChiTietNhap về cho trang gdNhapSoLuongGia.jsp.",
    "36. Trang gdNhapSoLuongGia.jsp chuyển đối tượng ChiTietNhap sang trang gdNhapPhuTung.jsp.",
    "37. Trang gdNhapPhuTung.jsp gọi lớp HoaDonNhap để thêm chi tiết nhập và cập nhật tổng tiền.",
    "38. Lớp HoaDonNhap gọi hàm themChiTiet(ctn) và gọi hàm tinhTongTien().",
    "39. Hàm tinhTongTien() thực hiện cộng dồn thành tiền các chi tiết nhập và gọi lớp HoaDonNhap đóng gói thông tin.",
    "40. Lớp HoaDonNhap đóng gói thông tin thực thể.",
    "41. Lớp HoaDonNhap trả kết quả dữ liệu HoaDonNhap đã cập nhật về cho trang gdNhapPhuTung.jsp.",
    "42. Trang gdNhapPhuTung.jsp đọc dữ liệu cập nhật từ HoaDonNhap và hiển thị lại bảng danh sách mặt hàng cùng tổng tiền mới.",
    "43. Lặp lại các bước 15 đến 42 cho đến khi nhập xong toàn bộ các mặt hàng trong chuyến hàng.",
    "44. Nhân viên kho kiểm tra danh sách mặt hàng, tổng tiền trên trang gdNhapPhuTung.jsp và bấm nút Lưu hóa đơn.",
    "45. Trang gdNhapPhuTung.jsp gọi lớp HoaDonNhapDAO yêu cầu lưu hóa đơn nhập kho.",
    "46. Lớp HoaDonNhapDAO gọi hàm luuHoaDonNhap(hdn).",
    "47. Hàm luuHoaDonNhap(hdn) thực hiện giao dịch (Transaction) CSDL: thêm mới vào tblHoaDonNhap, thêm mới các dòng vào tblChiTietNhap, cập nhật tăng số lượng tồn kho trong tblPhuTung và commit giao dịch.",
    "48. Lớp HoaDonNhapDAO trả kết quả lưu thành công về cho trang gdNhapPhuTung.jsp.",
    "49. Trang gdNhapPhuTung.jsp gọi trang gdHoaDonNhap.jsp.",
    "50. Trang gdHoaDonNhap.jsp hiển thị toàn bộ hóa đơn nhập hoàn tất kèm nút In hóa đơn cho nhân viên kho.",
    "51. Nhân viên kho bấm nút In hóa đơn để hoàn tất quy trình nhập kho."
]

for s in steps_v3_m2:
    add_p(doc, s, size_pt=11, space_before=1, space_after=3)

doc.save(docx_path)
print(f"Successfully generated standalone standardized report: {docx_path}")


