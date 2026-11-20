import os

puml_path = r"C:\Users\admin\Documents\PTTK\PLANTUML_SUBMISSION.puml"

with open(puml_path, "r", encoding="utf-8") as f:
    text = f.read()

# Find where Phase 3 starts
marker = "' PHẦN 3: CÁC BIỂU ĐỒ NỘP FORM 3"
idx = text.find(marker)
if idx == -1:
    marker = "@startuml Design_Entity_Class_Diagram_GaraMan"
    idx = text.find(marker)
    # go back to start of comment
    idx = text.rfind("' ---", 0, idx)

phase1_2 = text[:idx]

phase3 = """' ==============================================================================
' PHẦN 3: CÁC BIỂU ĐỒ NỘP FORM 3 - THIẾT KẾ HỆ THỐNG (ĐÃ CHUẨN HÓA 100%)
' ==============================================================================

' ------------------------------------------------------------------------------
' 3.1 BIỂU ĐỒ LỚP THỰC THỂ PHA THIẾT KẾ TOÀN HỆ THỐNG
' (Khắc phục: Thêm khachHang vào LichHen, gỡ LichHen-HoaDonThanhToan, sửa soLuongDaBan: int, heSoLuong: float)
' ------------------------------------------------------------------------------
@startuml Design_Entity_Class_Diagram_GaraMan
skinparam classAttributeIconSize 0
skinparam shadowing false

abstract class ThanhVien {
    - id : int
    - tenDangNhap : String
    - matKhau : String
    - hoTen : String
    - ngaySinh : Date
    - diaChi : String
    - soDienThoai : String
    - email : String
    + ThanhVien()
}

class KhachHang {
    - dsXe : List<Xe>
    + KhachHang()
    + themXe(x : Xe) : void
}

class NhanVien {
    - viTri : String
    - heSoLuong : float
    + NhanVien()
}

class NVQuanLy {
    + NVQuanLy()
}

class NVBanHang {
    + NVBanHang()
}

class NVKho {
    + NVKho()
}

class NhanVienKyThuat {
    - chuyenMon : String
    - trangThai : String
    + NhanVienKyThuat()
}

class Xe {
    - id : int
    - bienSoXe : String
    - hangXe : String
    - dongXe : String
    - mauSon : String
    - khachHang : KhachHang
    + Xe()
}

class LichHen {
    - id : int
    - thoiGianHen : Date
    - trangThai : String
    - khachHang : KhachHang
    - xe : Xe
    - dsDV : List<DichVu>
    + LichHen()
}

class NhaCungCap {
    - id : int
    - tenNCC : String
    - diaChi : String
    - soDienThoai : String
    + NhaCungCap()
}

class DichVu {
    - id : int
    - tenDichVu : String
    - loaiDichVu : String
    - donGia : double
    - thoiGianBaoHanh : String
    + DichVu()
}

class PhuTung {
    - id : int
    - tenPhuTung : String
    - hangSanXuat : String
    - donViTinh : String
    - donGiaNiemYet : double
    - soLuongTon : int
    + PhuTung()
    + capNhatTonKho(soLuongTang : int) : boolean
}

class HoaDonNhap {
    - id : int
    - ngayGioNhap : Date
    - tongTien : double
    - trangThaiThanhToan : String
    - nhaCungCap : NhaCungCap
    - nvKho : NVKho
    - dsChiTietNhap : List<ChiTietNhap>
    + HoaDonNhap()
    + themChiTiet(ct : ChiTietNhap) : void
    + tinhTongTien() : double
    + luuHoaDonNhap() : boolean
}

class ChiTietNhap {
    - id : int
    - soLuongNhap : int
    - donGiaNhap : double
    - thanhTien : double
    - phuTung : PhuTung
    - hoaDonNhap : HoaDonNhap
    + ChiTietNhap()
    + tinhThanhTien() : double
}

class HoaDonThanhToan {
    - id : int
    - ngayLap : Date
    - ngayHoanThanh : Date
    - tongTien : double
    - trangThai : String
    - khachHang : KhachHang
    - nvBanHang : NVBanHang
    - dsDichVuSuDung : List<ChiTietDichVuSuDung>
    - dsPhuTungSuDung : List<ChiTietPhuTungSuDung>
    + HoaDonThanhToan()
    + tinhTongTien() : double
}

class ChiTietDichVuSuDung {
    - id : int
    - donGiaThucHien : double
    - trangThaiHoanThanh : String
    - dichVu : DichVu
    - nvKyThuat : NhanVienKyThuat
    + ChiTietDichVuSuDung()
}

class ChiTietPhuTungSuDung {
    - id : int
    - soLuongXuat : int
    - donGiaBan : double
    - thanhTien : double
    - phuTung : PhuTung
    + ChiTietPhuTungSuDung()
    + tinhThanhTien() : double
}

class TKKhachHang {
    - soLanSuDung : int
    + TKKhachHang()
}

class TKNCC {
    - tongTienNhap : double
    + TKNCC()
}

class TKDichVu {
    - tongDoanhThu : double
    + TKDichVu()
}

class TKPhuTung {
    - soLuongDaBan : int
    + TKPhuTung()
}

' Kế thừa
ThanhVien <|-- KhachHang
ThanhVien <|-- NhanVien
NhanVien <|-- NVQuanLy
NhanVien <|-- NVBanHang
NhanVien <|-- NVKho
NhanVien <|-- NhanVienKyThuat

KhachHang <|-- TKKhachHang
NhaCungCap <|-- TKNCC
DichVu <|-- TKDichVu
PhuTung <|-- TKPhuTung

' Quan hệ kết tập / hợp thành
KhachHang "1" *-- "0..*" Xe : soHuu
LichHen "0..*" o-- "1" Xe : theoXe
LichHen "0..*" o-- "1" KhachHang : cuaKH
LichHen "0..*" o-- "1..*" DichVu : dangKyDV

HoaDonNhap "0..*" o-- "1" NhaCungCap : tuNCC
HoaDonNhap "0..*" o-- "1" NVKho : lapBoi
HoaDonNhap "1" *-- "1..*" ChiTietNhap : gomChiTiet
ChiTietNhap "0..*" o-- "1" PhuTung : nhapPT

HoaDonThanhToan "0..*" o-- "1" KhachHang : thanhToanBoi
HoaDonThanhToan "0..*" o-- "1" NVBanHang : lapBoi
HoaDonThanhToan "1" *-- "0..*" ChiTietDichVuSuDung : gomDichVu
HoaDonThanhToan "1" *-- "0..*" ChiTietPhuTungSuDung : gomPhuTung

ChiTietDichVuSuDung "0..*" o-- "1" DichVu : dungDV
ChiTietDichVuSuDung "0..*" o-- "1" NhanVienKyThuat : thiCongBoi
ChiTietPhuTungSuDung "0..*" o-- "1" PhuTung : dungPT
@enduml

' ------------------------------------------------------------------------------
' 3.2 SƠ ĐỒ THIẾT KẾ CƠ SỞ DỮ LIỆU (CSDL) TOÀN HỆ THỐNG
' (Khắc phục: Thêm tblLichHen_DichVu, bỏ tblLichHenid khỏi tblHoaDonThanhToan, kiểu datetime, heSoLuong float)
' ------------------------------------------------------------------------------
@startuml Database_Schema_GaraMan
skinparam linetype ortho
skinparam shadowing false

entity "tblThanhVien" as tblThanhVien {
    *id : int <<PK, AI>>
    --
    *tenDangNhap : varchar(255) <<UNIQUE>>
    *matKhau : varchar(255)
    *hoTen : varchar(255)
    ngaySinh : date
    diaChi : varchar(255)
    *soDienThoai : varchar(255)
    email : varchar(255)
}

entity "tblNhanVien" as tblNhanVien {
    *tblThanhVienid : int <<PK, FK>>
    --
    viTri : varchar(255)
    heSoLuong : float
}

entity "tblKhachHang" as tblKhachHang {
    *tblThanhVienid : int <<PK, FK>>
}

entity "tblNVQuanLy" as tblNVQuanLy {
    *tblNhanVienid : int <<PK, FK>>
}

entity "tblNVBanHang" as tblNVBanHang {
    *tblNhanVienid : int <<PK, FK>>
}

entity "tblNVKho" as tblNVKho {
    *tblNhanVienid : int <<PK, FK>>
}

entity "tblNVKyThuat" as tblNVKyThuat {
    *tblNhanVienid : int <<PK, FK>>
    --
    chuyenMon : varchar(255)
    trangThai : varchar(255)
}

entity "tblXe" as tblXe {
    *id : int <<PK, AI>>
    --
    *bienSoXe : varchar(255) <<UNIQUE>>
    hangXe : varchar(255)
    dongXe : varchar(255)
    mauSon : varchar(255)
    *tblKhachHangid : int <<FK>>
}

entity "tblLichHen" as tblLichHen {
    *id : int <<PK, AI>>
    --
    *thoiGianHen : datetime
    trangThai : varchar(255)
    *tblKhachHangid : int <<FK>>
    *tblXeid : int <<FK>>
}

entity "tblLichHen_DichVu" as tblLichHen_DichVu {
    *id : int <<PK, AI>>
    --
    *tblLichHenid : int <<FK>>
    *tblDichVuid : int <<FK>>
    ghiChu : varchar(255)
}

entity "tblNhaCungCap" as tblNhaCungCap {
    *id : int <<PK, AI>>
    --
    *tenNCC : varchar(255)
    diaChi : varchar(255)
    soDienThoai : varchar(255)
}

entity "tblDichVu" as tblDichVu {
    *id : int <<PK, AI>>
    --
    *tenDichVu : varchar(255)
    loaiDichVu : varchar(255)
    *donGia : double
    thoiGianBaoHanh : varchar(255)
}

entity "tblPhuTung" as tblPhuTung {
    *id : int <<PK, AI>>
    --
    *tenPhuTung : varchar(255)
    hangSanXuat : varchar(255)
    donViTinh : varchar(255)
    *donGiaNiemYet : double
    *soLuongTon : int
}

entity "tblHoaDonNhap" as tblHoaDonNhap {
    *id : int <<PK, AI>>
    --
    *ngayGioNhap : datetime
    *tongTien : double
    trangThaiThanhToan : varchar(255)
    *tblNhaCungCapid : int <<FK>>
    *tblNVKhoid : int <<FK>>
}

entity "tblChiTietNhap" as tblChiTietNhap {
    *id : int <<PK, AI>>
    --
    *soLuongNhap : int
    *donGiaNhap : double
    *thanhTien : double
    *tblHoaDonNhapid : int <<FK>>
    *tblPhuTungid : int <<FK>>
}

entity "tblHoaDonThanhToan" as tblHoaDonThanhToan {
    *id : int <<PK, AI>>
    --
    *ngayLap : datetime
    ngayHoanThanh : datetime
    *tongTien : double
    trangThai : varchar(255)
    *tblKhachHangid : int <<FK>>
    *tblNVBanHangid : int <<FK>>
}

entity "tblChiTietDichVuSuDung" as tblChiTietDichVuSuDung {
    *id : int <<PK, AI>>
    --
    *donGiaThucHien : double
    trangThaiHoanThanh : varchar(255)
    *tblHoaDonThanhToanid : int <<FK>>
    *tblDichVuid : int <<FK>>
    *tblNVKyThuatid : int <<FK>>
}

entity "tblChiTietPhuTungSuDung" as tblChiTietPhuTungSuDung {
    *id : int <<PK, AI>>
    --
    *soLuongXuat : int
    *donGiaBan : double
    *thanhTien : double
    *tblHoaDonThanhToanid : int <<FK>>
    *tblPhuTungid : int <<FK>>
}

' Quan hệ kế thừa 1-1 bảng cha - bảng con
tblThanhVien ||--o| tblNhanVien
tblThanhVien ||--o| tblKhachHang
tblNhanVien ||--o| tblNVQuanLy
tblNhanVien ||--o| tblNVBanHang
tblNhanVien ||--o| tblNVKho
tblNhanVien ||--o| tblNVKyThuat

' Khách hàng - Xe - Lịch hẹn
tblKhachHang ||--o{ tblXe
tblKhachHang ||--o{ tblLichHen
tblXe ||--o{ tblLichHen
tblLichHen ||--o{ tblLichHen_DichVu
tblDichVu ||--o{ tblLichHen_DichVu

' Nhập phụ tùng
tblNhaCungCap ||--o{ tblHoaDonNhap
tblNVKho ||--o{ tblHoaDonNhap
tblHoaDonNhap ||--|{ tblChiTietNhap
tblPhuTung ||--o{ tblChiTietNhap

' Thanh toán & Chi tiết sử dụng
tblKhachHang ||--o{ tblHoaDonThanhToan
tblNVBanHang ||--o{ tblHoaDonThanhToan
tblHoaDonThanhToan ||--o{ tblChiTietDichVuSuDung
tblDichVu ||--o{ tblChiTietDichVuSuDung
tblNVKyThuat ||--o{ tblChiTietDichVuSuDung

tblHoaDonThanhToan ||--o{ tblChiTietPhuTungSuDung
tblPhuTung ||--o{ tblChiTietPhuTungSuDung
@enduml

' ------------------------------------------------------------------------------
' 3.3 BIỂU ĐỒ LỚP THIẾT KẾ (3 TẦNG) - MODULE 1: TÌM KIẾM DỊCH VỤ / PHỤ TÙNG
' (Khắc phục: soDienThoai, thêm getDichVuById & getPhuTungById, nối chi tiết vào DAO)
' ------------------------------------------------------------------------------
@startuml Design_Class_Module1_Search
skinparam classAttributeIconSize 0
skinparam shadowing false

package "Giao diện (Presentation Layer - JSP)" {
    class "gdChinhKH.jsp" as GDChinh {
        - timThongTin : link
        - khachHang : KhachHang
    }
    class "gdTimKiemDVPT.jsp" as GDSearch {
        - txtTuKhoa : TextField
        - btnTim : submit
        - tblDichVu : Table
        - tblPhuTung : Table
        - xemDichVu : link
        - xemPhuTung : link
        - tuKhoa : String
        - dsDichVu : List<DichVu>
        - dsPhuTung : List<PhuTung>
    }
    class "gdChiTietDichVu.jsp" as GDDVDetail {
        - dichVu : DichVu
        - tuKhoa : String
        - quayLai : link
        - datLichHen : link
    }
    class "gdChiTietPhuTung.jsp" as GDPTDetail {
        - phuTung : PhuTung
        - tuKhoa : String
        - quayLai : link
    }
}

package "Điều khiển & Dữ liệu (Business & Data Layer - DAO)" {
    abstract class DAO {
        # con : Connection
        + DAO()
        + getConnection() : Connection
    }
    class DichVuDAO {
        + getDichVuTheoTen(tuKhoa : String) : List<DichVu>
        + getDichVuById(id : int) : DichVu
    }
    class PhuTungDAO {
        + getPhuTungTheoTen(tuKhoa : String) : List<PhuTung>
        + getPhuTungById(id : int) : PhuTung
    }
}

package "Thực thể (Model Layer - Entity)" {
    class ThanhVien {
        - id : int
        - tenDangNhap : String
        - matKhau : String
        - hoTen : String
        - ngaySinh : Date
        - diaChi : String
        - soDienThoai : String
        - email : String
    }
    class KhachHang {
        - dsXe : List<Xe>
    }
    class DichVu {
        - id : int
        - tenDichVu : String
        - loaiDichVu : String
        - donGia : double
        - thoiGianBaoHanh : String
    }
    class PhuTung {
        - id : int
        - tenPhuTung : String
        - hangSanXuat : String
        - donViTinh : String
        - donGiaNiemYet : double
        - soLuongTon : int
        + capNhatTonKho(soLuongTang : int) : boolean
    }
}

GDChinh --> GDSearch : <<chuyển hướng>>
GDSearch --> GDDVDetail : <<chuyển hướng>>
GDSearch --> GDPTDetail : <<chuyển hướng>>

GDSearch --> DichVuDAO : gọi timTheoTen()
GDSearch --> PhuTungDAO : gọi timTheoTen()
GDDVDetail --> DichVuDAO : gọi getDichVuById()
GDPTDetail --> PhuTungDAO : gọi getPhuTungById()

DichVuDAO --|> DAO : kế thừa
PhuTungDAO --|> DAO : kế thừa

DichVuDAO ..> DichVu : đóng gói
PhuTungDAO ..> PhuTung : đóng gói
KhachHang --|> ThanhVien : kế thừa
@enduml

' ------------------------------------------------------------------------------
' 3.4 BIỂU ĐỒ LỚP THIẾT KẾ (3 TẦNG) - MODULE 2: NHẬP PHỤ TÙNG TỪ NCC
' (Khắc phục: nối gdChinhKho với NVKho, chính tả -tblChiTietNhap, bỏ sửa/xóa/thanh toán, khôi phục phương thức thực thể, đồng bộ DAO)
' ------------------------------------------------------------------------------
@startuml Design_Class_Module2_Import
skinparam classAttributeIconSize 0
skinparam shadowing false

package "Giao diện (Presentation Layer - JSP)" {
    class "gdChinhKho.jsp" as GDChinhKho {
        - nhapPhuTung : link
        - nvKho : NVKho
    }
    class "gdTimNCC.jsp" as GDTimNCC {
        - txtTenNCC : TextField
        - btnTimNCC : submit
        - tblDsNCC : Table
        - chonNCC : link
        - themNCC : link
        - troVe : link
    }
    class "gdThemNCC.jsp" as GDThemNCC {
        - txtTenNCC : TextField
        - txtDiaChi : TextField
        - txtSoDienThoai : TextField
        - btnLuuNCC : submit
        - troVe : link
    }
    class "gdNhapPhuTung.jsp" as GDNhapPT {
        - outThongTinNCC : Label
        - btnTimPhuTung : submit
        - tblChiTietNhap : Table
        - outTongTien : Label
        - btnLuuHoaDon : submit
        - troVe : link
    }
    class "gdTimPhuTung.jsp" as GDTimPT {
        - txtTenPT : TextField
        - btnTimPT : submit
        - tblDsPT : Table
        - chonPT : link
        - themPT : link
        - troVe : link
    }
    class "gdThemPhuTung.jsp" as GDThemPT {
        - txtTenPT : TextField
        - txtHangSX : TextField
        - txtDonViTinh : TextField
        - txtDonGia : TextField
        - btnLuuPT : submit
        - troVe : link
    }
    class "gdNhapSoLuongGia.jsp" as GDNhapSLGia {
        - outThongTinPTChon : Label
        - txtSoLuongNhap : TextField
        - txtDonGiaNhap : TextField
        - btnThem : submit
        - troVe : link
    }
    class "gdHoaDonNhap.jsp" as GDHDNhap {
        - outHoaDonHoanTat : Panel
        - btnInHoaDon : submit
        - troVe : link
    }
}

package "Điều khiển & Dữ liệu (Business & Data Layer - DAO)" {
    abstract class DAO {
        # con : Connection
        + DAO()
        + getConnection() : Connection
    }
    class NhaCungCapDAO {
        + getNhaCungCapTheoTen(ten : String) : List<NhaCungCap>
        + themNhaCungCap(ncc : NhaCungCap) : NhaCungCap
    }
    class PhuTungDAO {
        + getPhuTungTheoTen(ten : String) : List<PhuTung>
        + themPhuTung(pt : PhuTung) : PhuTung
        + capNhatTonKho(idPhuTung : int, soLuongTang : int) : boolean
    }
    class HoaDonNhapDAO {
        + luuHoaDonNhap(hd : HoaDonNhap) : boolean
        + layTheoId(id : int) : HoaDonNhap
    }
}

package "Thực thể (Model Layer - Entity)" {
    class ThanhVien {
        - id : int
        - tenDangNhap : String
        - matKhau : String
        - hoTen : String
        - soDienThoai : String
    }
    class NhanVien {
        - viTri : String
        - heSoLuong : float
    }
    class NVKho {
    }
    class NhaCungCap {
        - id : int
        - tenNCC : String
        - diaChi : String
        - soDienThoai : String
    }
    class PhuTung {
        - id : int
        - tenPhuTung : String
        - hangSanXuat : String
        - donViTinh : String
        - donGiaNiemYet : double
        - soLuongTon : int
        + capNhatTonKho(soLuongTang : int) : boolean
    }
    class HoaDonNhap {
        - id : int
        - ngayGioNhap : Date
        - tongTien : double
        - trangThaiThanhToan : String
        - nhaCungCap : NhaCungCap
        - nvKho : NVKho
        - dsChiTietNhap : List<ChiTietNhap>
        + themChiTiet(ct : ChiTietNhap) : void
        + tinhTongTien() : double
        + luuHoaDonNhap() : boolean
    }
    class ChiTietNhap {
        - id : int
        - soLuongNhap : int
        - donGiaNhap : double
        - thanhTien : double
        - phuTung : PhuTung
        - hoaDonNhap : HoaDonNhap
        + tinhThanhTien() : double
    }
}

' Nối giao diện với NVKho
GDChinhKho --> NVKho : <<sở hữu phiên>>

' Chuyển hướng giao diện
GDChinhKho --> GDTimNCC : <<chuyển hướng>>
GDTimNCC --> GDThemNCC : <<chuyển hướng>>
GDTimNCC --> GDNhapPT : <<chuyển hướng>>
GDNhapPT --> GDTimPT : <<chuyển hướng>>
GDTimPT --> GDThemPT : <<chuyển hướng>>
GDTimPT --> GDNhapSLGia : <<chuyển hướng>>
GDNhapSLGia --> GDNhapPT : <<chuyển hướng>>
GDNhapPT --> GDHDNhap : <<chuyển hướng>>

' JSP gọi DAO
GDTimNCC --> NhaCungCapDAO : tìm kiếm
GDThemNCC --> NhaCungCapDAO : thêm mới
GDTimPT --> PhuTungDAO : tìm kiếm
GDThemPT --> PhuTungDAO : thêm mới
GDNhapPT --> HoaDonNhapDAO : lưu hóa đơn
GDHDNhap --> HoaDonNhapDAO : đọc hóa đơn đã lưu

' Kế thừa DAO
NhaCungCapDAO --|> DAO
PhuTungDAO --|> DAO
HoaDonNhapDAO --|> DAO

' DAO gọi Entity
NhaCungCapDAO ..> NhaCungCap
PhuTungDAO ..> PhuTung
HoaDonNhapDAO ..> HoaDonNhap

' Kế thừa & Quan hệ thực thể
ThanhVien <|-- NhanVien
NhanVien <|-- NVKho
HoaDonNhap "0..*" o-- "1" NhaCungCap
HoaDonNhap "0..*" o-- "1" NVKho
HoaDonNhap "1" *-- "1..*" ChiTietNhap
ChiTietNhap "0..*" o-- "1" PhuTung
@enduml

' ------------------------------------------------------------------------------
' 3.5 BIỂU ĐỒ HOẠT ĐỘNG (ACTIVITY DIAGRAM) - MODULE 1: TÌM KIẾM DỊCH VỤ / PHỤ TÙNG
' (Khắc phục: Mũi tên [Quay lại] quay về gdTimKiemDVPT.jsp, không đi ra Kết thúc)
' ------------------------------------------------------------------------------
@startuml Activity_Diagram_Module1_Search
skinparam shadowing false

start
:Khách hàng đăng nhập thành công;
:Click menu "Tìm kiếm thông tin DV/PT" trên gdChinhKH.jsp;
:Hệ thống mở gdTimKiemDVPT.jsp (Nhận thông tin KH);

repeat
    :Khách hàng nhập từ khóa tìm kiếm;
    :Click nút "Tìm kiếm";
    :gdTimKiemDVPT.jsp gọi DichVuDAO.getDichVuTheoTen();
    :gdTimKiemDVPT.jsp gọi PhuTungDAO.getPhuTungTheoTen();
    if (Tìm thấy kết quả?) then (Có)
        :Đổ dữ liệu lên 2 bảng: Danh sách Dịch vụ và Danh sách Phụ tùng;
    else (Không)
        :Hiển thị thông báo "Không tìm thấy kết quả phù hợp";
    endif

    repeat
        :Khách hàng click "Xem chi tiết" 1 Dịch vụ (hoặc 1 Phụ tùng);
        if (Chọn xem Dịch vụ?) then (Dịch vụ)
            :Mở gdChiTietDichVu.jsp;
            :Gọi DichVuDAO.getDichVuById();
            :Hiển thị tên DV, loại DV, đơn giá, bảo hành, nút "Đặt lịch hẹn";
        else (Phụ tùng)
            :Mở gdChiTietPhuTung.jsp;
            :Gọi PhuTungDAO.getPhuTungById();
            :Hiển thị tên PT, hãng SX, ĐVT, đơn giá, số lượng tồn kho;
        endif
        :Khách hàng bấm nút "Quay lại kết quả";
    repeat while (Khách hàng tiếp tục xem mục khác trong danh sách?) is (Có)

repeat while (Khách hàng nhập từ khóa mới để tìm tiếp?) is (Có)

:Khách hàng click "Về trang chủ" / Thoát;
stop
@enduml

' ------------------------------------------------------------------------------
' 3.6 BIỂU ĐỒ HOẠT ĐỘNG (ACTIVITY DIAGRAM) - MODULE 2: NHẬP PHỤ TÙNG TỪ NCC
' (Khắc phục: Bỏ sửa/xóa dòng, bỏ xác nhận phụ, bỏ thanh toán cho NCC)
' ------------------------------------------------------------------------------
@startuml Activity_Diagram_Module2_Import
skinparam shadowing false

start
:Nhân viên kho đăng nhập thành công;
:Click menu "Nhập phụ tùng" trên GDChinhNVKho;
:Hệ thống mở giao diện tìm NCC GDTimNCC;

repeat
    :Nhập tên NCC và click "Tìm kiếm";
    :Gọi NhaCungCapDAO.getNhaCungCapTheoTen();
    if (NCC đã tồn tại trong CSDL?) then (Có)
        :Hiển thị danh sách NCC lên bảng;
        :Nhân viên click "Chọn" NCC;
    else (Chưa có)
        :Click nút "Thêm mới NCC";
        :Mở form GDThemNCC;
        :Nhập tên, địa chỉ, SĐT và click "Lưu NCC";
        :NhaCungCapDAO lưu NCC mới và trả về đối tượng;
    endif
    break
repeat while (Tìm lại NCC khác?) is (Có)

:Chuyển sang giao diện lập hóa đơn GDNhapPhuTung;
:Hiển thị thông tin NCC đang làm việc;

repeat
    :Click nút "Tìm phụ tùng";
    :Mở giao diện GDTimPhuTung;
    :Nhập tên phụ tùng và click "Tìm kiếm";
    :Gọi PhuTungDAO.getPhuTungTheoTen();
    if (Phụ tùng đã có trong danh mục?) then (Có)
        :Hiển thị danh sách phụ tùng;
        :Nhân viên click "Chọn" phụ tùng;
    else (Chưa có)
        :Click nút "Thêm mới phụ tùng";
        :Mở GDThemPhuTung, nhập tên, hãng, ĐVT, đơn giá;
        :PhuTungDAO lưu phụ tùng mới và trả về đối tượng;
    endif
    :Mở GDNhapSoLuongGia;
    :Nhân viên nhập Số lượng nhập (>0) và Đơn giá nhập (>0);
    :Click nút "Thêm vào hóa đơn";
    :Hệ thống tạo ChiTietNhap, thêm vào HoaDonNhap;
    :Tự động cộng dồn thành tiền và cập nhật tổng tiền hóa đơn;
    :Hiển thị lại bảng danh sách mặt hàng tại GDNhapPhuTung;
repeat while (Tiếp tục nhập thêm mặt hàng phụ tùng khác?) is (Có)

:Nhân viên kho kiểm tra danh sách và bấm nút "Lưu hóa đơn";
:Hệ thống thực hiện giao dịch CSDL (Transaction):
- INSERT thông tin hóa đơn vào tblHoaDonNhap
- INSERT từng dòng chi tiết vào tblChiTietNhap
- UPDATE tăng tồn kho tương ứng trong tblPhuTung;
:Chuyển sang màn hình chứng từ hoàn tất GDHoaDonNhap;
:Nhân viên kho bấm nút "In hóa đơn nhập kho";
stop
@enduml

' ------------------------------------------------------------------------------
' 3.7 BIỂU ĐỒ TUẦN TỰ (SEQUENCE DIAGRAM) - MODULE 1: TÌM KIẾM DỊCH VỤ / PHỤ TÙNG
' (Khắc phục: Thêm getDichVuById, getPhuTungById, nút Quay lại giữ từ khóa)
' ------------------------------------------------------------------------------
@startuml Sequence_Diagram_Module1_Search
skinparam shadowing false
autonumber

actor "Khách hàng" as User
boundary "gdTimKiemDVPT.jsp" as GDSearch
boundary "gdChiTietDichVu.jsp" as GDDV
boundary "gdChiTietPhuTung.jsp" as GDPT
control "DichVuDAO" as DVDao
control "PhuTungDAO" as PTDao
database "CSDL (MySQL)" as DB

User -> GDSearch : Nhập từ khóa tên và bấm nút "Tìm kiếm"
activate GDSearch
GDSearch -> DVDao : getDichVuTheoTen(tuKhoa)
activate DVDao
DVDao -> DB : SELECT * FROM tblDichVu WHERE tenDichVu LIKE ?
activate DB
DB --> DVDao : ResultSet danh sách dịch vụ
deactivate DB
DVDao --> GDSearch : List<DichVu>
deactivate DVDao

GDSearch -> PTDao : getPhuTungTheoTen(tuKhoa)
activate PTDao
PTDao -> DB : SELECT * FROM tblPhuTung WHERE tenPhuTung LIKE ?
activate DB
DB --> PTDao : ResultSet danh sách phụ tùng
deactivate DB
PTDao --> GDSearch : List<PhuTung>
deactivate PTDao

GDSearch --> User : Hiển thị đồng thời 2 bảng kết quả Dịch vụ và Phụ tùng
deactivate GDSearch

alt Khách hàng chọn xem chi tiết 1 Dịch vụ
    User -> GDSearch : Click "Xem chi tiết" 1 dịch vụ (truyền id)
    activate GDSearch
    GDSearch -> GDDV : forward(id, tuKhoa)
    deactivate GDSearch
    activate GDDV
    GDDV -> DVDao : getDichVuById(id)
    activate DVDao
    DVDao -> DB : SELECT * FROM tblDichVu WHERE id = ?
    activate DB
    DB --> DVDao : ResultSet chi tiết dịch vụ
    deactivate DB
    DVDao --> GDDV : Đối tượng DichVu chi tiết
    deactivate DVDao
    GDDV --> User : Hiển thị tên DV, loại DV, đơn giá, bảo hành, nút Đặt lịch hẹn, Quay lại
    User -> GDDV : Click nút "Quay lại kết quả"
    GDDV -> GDSearch : Quay lại gdTimKiemDVPT.jsp (giữ nguyên từ khóa & kết quả)
    deactivate GDDV
    activate GDSearch
    GDSearch --> User : Hiển thị lại màn hình danh sách kết quả tra cứu
    deactivate GDSearch
else Khách hàng chọn xem chi tiết 1 Phụ tùng
    User -> GDSearch : Click "Xem chi tiết" 1 phụ tùng (truyền id)
    activate GDSearch
    GDSearch -> GDPT : forward(id, tuKhoa)
    deactivate GDSearch
    activate GDPT
    GDPT -> PTDao : getPhuTungById(id)
    activate PTDao
    PTDao -> DB : SELECT * FROM tblPhuTung WHERE id = ?
    activate DB
    DB --> PTDao : ResultSet chi tiết phụ tùng
    deactivate DB
    PTDao --> GDPT : Đối tượng PhuTung chi tiết
    deactivate PTDao
    GDPT --> User : Hiển thị tên PT, hãng SX, ĐVT, đơn giá, số lượng tồn kho, nút Quay lại
    User -> GDPT : Click nút "Quay lại kết quả"
    GDPT -> GDSearch : Quay lại gdTimKiemDVPT.jsp (giữ nguyên từ khóa & kết quả)
    deactivate GDPT
end
@enduml

' ------------------------------------------------------------------------------
' 3.8 BIỂU ĐỒ TUẦN TỰ (SEQUENCE DIAGRAM) - MODULE 2: NHẬP PHỤ TÙNG TỪ NCC
' (Khắc phục: Đồng bộ phương thức DAO, bỏ thanh toán NCC, chuẩn hóa lưu và in hóa đơn)
' ------------------------------------------------------------------------------
@startuml Sequence_Diagram_Module2_Import
skinparam shadowing false
autonumber

actor "Nhân viên kho" as NVKho
boundary "Giao diện Kho (JSP)" as UI
control "NhaCungCapDAO" as NCCDao
control "PhuTungDAO" as PTDao
control "HoaDonNhapDAO" as HDNDao
entity "HoaDonNhap" as HDN
database "CSDL (MySQL)" as DB

NVKho -> UI : Click menu "Nhập phụ tùng" (mở gdTimNCC.jsp)
activate UI
NVKho -> UI : Nhập tên NCC và click "Tìm kiếm"
UI -> NCCDao : getNhaCungCapTheoTen(ten)
activate NCCDao
NCCDao -> DB : SELECT * FROM tblNhaCungCap WHERE tenNCC LIKE ?
activate DB
DB --> NCCDao : ResultSet danh sách NCC
deactivate DB
NCCDao --> UI : List<NhaCungCap>
deactivate NCCDao
UI --> NVKho : Hiển thị bảng danh sách nhà cung cấp

opt Luồng 7a: Nhà cung cấp chưa tồn tại
    NVKho -> UI : Click "Thêm mới NCC" (mở gdThemNCC.jsp)
    NVKho -> UI : Nhập tên, địa chỉ, SĐT và click "Lưu NCC"
    UI -> NCCDao : themNhaCungCap(nccMoi)
    activate NCCDao
    NCCDao -> DB : INSERT INTO tblNhaCungCap (...) VALUES (...)
    activate DB
    DB --> NCCDao : Generated Keys (id mới)
    deactivate DB
    NCCDao --> UI : Đối tượng NhaCungCap vừa tạo
    deactivate NCCDao
end

NVKho -> UI : Click "Chọn" NCC (chuyển sang gdNhapPhuTung.jsp)
UI --> NVKho : Hiển thị thông tin NCC, bảng rỗng, tổng tiền = 0

loop Lặp cho từng mặt hàng phụ tùng cần nhập
    NVKho -> UI : Click "Tìm phụ tùng" (mở gdTimPhuTung.jsp)
    NVKho -> UI : Nhập tên phụ tùng và click "Tìm kiếm"
    UI -> PTDao : getPhuTungTheoTen(ten)
    activate PTDao
    PTDao -> DB : SELECT * FROM tblPhuTung WHERE tenPhuTung LIKE ?
    activate DB
    DB --> PTDao : ResultSet danh sách phụ tùng
    deactivate DB
    PTDao --> UI : List<PhuTung>
    deactivate PTDao
    UI --> NVKho : Hiển thị bảng phụ tùng

    opt Luồng 18a: Phụ tùng chưa có trong danh mục
        NVKho -> UI : Click "Thêm mới phụ tùng" (mở gdThemPhuTung.jsp)
        NVKho -> UI : Nhập tên PT, hãng SX, ĐVT, giá niêm yết và click "Lưu PT"
        UI -> PTDao : themPhuTung(ptMoi)
        activate PTDao
        PTDao -> DB : INSERT INTO tblPhuTung (...) VALUES (...)
        activate DB
        DB --> PTDao : Generated Keys (id mới)
        deactivate DB
        PTDao --> UI : Đối tượng PhuTung vừa tạo
        deactivate PTDao
    end

    NVKho -> UI : Click "Chọn" phụ tùng (mở gdNhapSoLuongGia.jsp)
    UI --> NVKho : Hiển thị form nhập: Số lượng nhập, Đơn giá nhập
    NVKho -> UI : Nhập Số lượng nhập, Đơn giá nhập và click "Thêm vào hóa đơn"
    UI -> HDN : themChiTiet(chiTietMoi)
    activate HDN
    HDN -> HDN : tinhTongTien()
    HDN --> UI : Cập nhật danh sách chi tiết và tổng tiền mới
    deactivate HDN
    UI --> NVKho : Hiển thị lại bảng phụ tùng đã nhập và tổng tiền cập nhật
end

NVKho -> UI : Kiểm tra danh sách mặt hàng và click "Lưu hóa đơn"
UI -> HDNDao : luuHoaDonNhap(hoaDonNhap)
activate HDNDao
HDNDao -> DB : BEGIN TRANSACTION
activate DB
HDNDao -> DB : INSERT INTO tblHoaDonNhap (...) VALUES (...)
HDNDao -> DB : INSERT INTO tblChiTietNhap (...) VALUES (...) (từng dòng)
HDNDao -> DB : UPDATE tblPhuTung SET soLuongTon = soLuongTon + ? WHERE id = ?
HDNDao -> DB : COMMIT TRANSACTION
DB --> HDNDao : Transaction thành công
deactivate DB
HDNDao --> UI : Lưu hóa đơn nhập thành công
deactivate HDNDao

UI -> UI : Chuyển sang gdHoaDonNhap.jsp
UI --> NVKho : Hiển thị chứng từ hóa đơn nhập hoàn tất
NVKho -> UI : Click nút "In hóa đơn nhập kho"
UI --> NVKho : Xuất phiếu in hóa đơn cho nhân viên kho
deactivate UI
@enduml

' ------------------------------------------------------------------------------
' 3.9 BIỂU ĐỒ GÓI (PACKAGE DIAGRAM)
' ------------------------------------------------------------------------------
@startuml Package_Diagram_GaraMan
skinparam packageStyle rectangle
skinparam shadowing false

package "com.garaman.presentation (Presentation Layer)" {
    [gdChinhKH.jsp]
    [gdTimKiemDVPT.jsp]
    [gdChiTietDichVu.jsp]
    [gdChiTietPhuTung.jsp]
    [gdChinhKho.jsp]
    [gdTimNCC.jsp]
    [gdThemNCC.jsp]
    [gdNhapPhuTung.jsp]
    [gdTimPhuTung.jsp]
    [gdThemPhuTung.jsp]
    [gdNhapSoLuongGia.jsp]
    [gdHoaDonNhap.jsp]
}

package "com.garaman.dao (Data Access Layer)" {
    [DAO]
    [DichVuDAO]
    [PhuTungDAO]
    [NhaCungCapDAO]
    [HoaDonNhapDAO]
}

package "com.garaman.model (Model Layer - Entities)" {
    [ThanhVien]
    [KhachHang]
    [NVKho]
    [DichVu]
    [PhuTung]
    [NhaCungCap]
    [HoaDonNhap]
    [ChiTietNhap]
    [Xe]
    [LichHen]
    [HoaDonThanhToan]
}

[com.garaman.presentation] ..> [com.garaman.dao] : <<use>>
[com.garaman.presentation] ..> [com.garaman.model] : <<use>>
[com.garaman.dao] ..> [com.garaman.model] : <<create/read>>
@enduml

' ------------------------------------------------------------------------------
' 3.10 BIỂU ĐỒ TRIỂN KHAI (DEPLOYMENT DIAGRAM)
' ------------------------------------------------------------------------------
@startuml Deployment_Diagram_GaraMan
skinparam shadowing false

node "Client Workstation / Web Browser" as Client {
    artifact "Web Browser (Chrome/Firefox/Edge)" as Browser
}

node "Application Server (Web / Servlet Container)" as AppServer {
    node "Apache Tomcat 9.0 / 10.0" as Tomcat {
        artifact "GaraMan.war (JSP, Servlets, DAO, JDBC Driver)" as WebApp
    }
}

node "Database Server" as DBServer {
    database "MySQL Database 8.0" as MySQL {
        frame "GaraMan_DB" {
            [tblThanhVien]
            [tblDichVu]
            [tblPhuTung]
            [tblNhaCungCap]
            [tblHoaDonNhap]
            [tblChiTietNhap]
            [tblLichHen]
            [tblLichHen_DichVu]
            [tblHoaDonThanhToan]
        }
    }
}

Browser -- Tomcat : HTTP / HTTPS (Port 8080 / 443)
Tomcat -- MySQL : JDBC / TCP-IP (Port 3306)
@enduml
"""

full_content = phase1_2.rstrip() + "\n\n" + phase3

with open(puml_path, "w", encoding="utf-8") as f:
    f.write(full_content)

print(f"Successfully updated {puml_path} with all standardized Phase 3 blocks!")
