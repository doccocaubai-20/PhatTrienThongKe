# PHẦN III: THIẾT KẾ HỆ THỐNG (SYSTEM DESIGN)
**Học phần:** Phân tích và Thiết kế Hệ thống  
**Hệ thống:** Quản lý Gara Ô tô – GaraMan (Đề tài 26)  
**Tiêu chuẩn tài liệu:** Bám sát giáo trình *Bài giảng Thực tập nghề nghiệp 2 - CNPM (PTIT 2020)*, Chương 4: Thiết kế.  
**Trạng thái:** Đã chuẩn hóa toàn diện 13 điểm sai lệch theo phản hồi của Giảng viên hướng dẫn.

---

## 1. THIẾT KẾ LỚP THỰC THỂ TOÀN HỆ THỐNG (DESIGN ENTITY CLASS DIAGRAM)

### 1.1 Quy trình thực hiện (Theo mục 4.1.1 Giáo trình PTIT)
Quá trình chuyển đổi từ biểu đồ lớp phân tích (Hình 5.1) sang biểu đồ lớp thực thể pha thiết kế tuân thủ nghiêm ngặt 4 bước:
1. **Bổ sung thuộc tính `id: int`**: Định danh khóa chính cho tất cả các lớp thực thể cơ sở không kế thừa (`ThanhVien`, `Xe`, `LichHen`, `NhaCungCap`, `DichVu`, `PhuTung`, `HoaDonNhap`, `ChiTietNhap`, `HoaDonThanhToan`, `ChiTietDichVuSuDung`, `ChiTietPhuTungSuDung`). Các lớp con kế thừa `id` từ lớp cha.
2. **Gán kiểu dữ liệu chuẩn Java**: Toàn bộ thuộc tính được gán kiểu dữ liệu cụ thể (`int`, `double`, `float`, `String`, `Date`, `boolean`). Đặc biệt:
   - `TKPhuTung.soLuongDaBan: int` (chuẩn hóa từ `double` để đúng với bản chất đếm số lượng phụ tùng bán ra).
   - `NhanVien.heSoLuong: float` (đồng bộ giữa lớp và CSDL).
3. **Chuyển đổi liên kết ngữ nghĩa thành kết tập / hợp thành**:
   - `HoaDonNhap` hợp thành (`*--`) với `ChiTietNhap` (1..*).
   - `HoaDonThanhToan` hợp thành (`*--`) với `ChiTietDichVuSuDung` (0..*) và `ChiTietPhuTungSuDung` (0..*).
   - `KhachHang` hợp thành (`*--`) với `Xe` (0..*).
   - `LichHen` liên kết với `KhachHang` (`cuaKH`), `Xe` (`theoXe`), và danh sách dịch vụ đăng ký `List<DichVu> dsDV` (`dangKyDV`).
   - **Lưu ý chuẩn hóa:** Loại bỏ liên kết trực tiếp giữa `LichHen` và `HoaDonThanhToan` trên thực thể `LichHen`. `LichHen` là thực thể lập trước phục vụ tiếp nhận dịch vụ trực tuyến; khi khách hàng thanh toán dịch vụ, `HoaDonThanhToan` mới tham chiếu tới `LichHen` (nếu có).
4. **Bổ sung đầy đủ phương thức nghiệp vụ và getter/setter**:
   - `HoaDonNhap`: `+ themChiTiet(ctn: ChiTietNhap)`, `+ tinhTongTien(): double`.
   - `ChiTietNhap`: `+ tinhThanhTien(): double`.
   - `PhuTung`: `+ capNhatTonKho(soLuongTang: int): boolean`.
   - `HoaDonThanhToan`: `+ tinhTongTien(): double`.

### 1.2 Bảng rà soát chuẩn hóa các lớp thực thể
| STT | Tên lớp | Lớp cha | Thuộc tính chính | Phương thức chính | Vai trò / Ghi chú chuẩn hóa |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | `ThanhVien` | *(Gốc)* | `id: int`, `tenDangNhap: String`, `matKhau: String`, `hoTen: String`, `ngaySinh: Date`, `diaChi: String`, `soDienThoai: String`, `email: String`, `vaiTro: String` | `ThanhVien()`, getter/setter | Lớp cha trừu tượng của toàn bộ người dùng. Chuẩn hóa dùng `-soDienThoai: String`. |
| 2 | `KhachHang` | `ThanhVien` | `dsXe: List<Xe>` | `KhachHang()`, getter/setter | Chủ phương tiện, có thể sở hữu nhiều xe (`List<Xe>`). |
| 3 | `NhanVien` | `ThanhVien` | `viTri: String`, `heSoLuong: float` | `NhanVien()`, getter/setter | Chuẩn hóa `heSoLuong: float` khớp tuyệt đối với CSDL. |
| 4 | `NVKho` | `NhanVien` | *(Kế thừa)* | `NVKho()`, getter/setter | Nhân viên thực hiện nhập hàng từ Nhà cung cấp. |
| 5 | `NVBanHang` | `NhanVien` | *(Kế thừa)* | `NVBanHang()`, getter/setter | Nhân viên lập hóa đơn thanh toán và tư vấn. |
| 6 | `NVQuanLy` | `NhanVien` | *(Kế thừa)* | `NVQuanLy()`, getter/setter | Quản lý gara, xem các báo cáo thống kê. |
| 7 | `NhanVienKyThuat` | `NhanVien` | `chuyenMon: String`, `trangThaiKT: String` | `NhanVienKyThuat()`, getter/setter | Kỹ thuật viên sửa chữa, bảo dưỡng ô tô. |
| 8 | `Xe` | *(Gốc)* | `id: int`, `bienSoXe: String`, `hangXe: String`, `dongXe: String`, `mauSon: String`, `khachHang: KhachHang` | `Xe()`, getter/setter | Phương tiện ô tô của khách hàng. |
| 9 | `LichHen` | *(Gốc)* | `id: int`, `thoiGianHen: Date`, `trangThai: String`, `xe: Xe`, `khachHang: KhachHang`, `dsDV: List<DichVu>` | `LichHen()`, getter/setter | Bổ sung `khachHang: KhachHang` và `dsDV: List<DichVu>`. Bỏ thuộc tính `hoaDonThanhToan`. |
| 10 | `NhaCungCap` | *(Gốc)* | `id: int`, `tenNCC: String`, `diaChi: String`, `soDienThoai: String` | `NhaCungCap()`, getter/setter | Đối tác cung cấp linh kiện, phụ tùng. |
| 11 | `PhuTung` | *(Gốc)* | `id: int`, `tenPhuTung: String`, `hangSanXuat: String`, `donViTinh: String`, `donGiaNiemYet: double`, `soLuongTon: int` | `PhuTung()`, `capNhatTonKho(sl: int): boolean`, getter/setter | Khôi phục phương thức `capNhatTonKho()`. |
| 12 | `DichVu` | *(Gốc)* | `id: int`, `tenDichVu: String`, `loaiDichVu: String`, `donGia: double`, `thoiGianBaoHanh: String` | `DichVu()`, getter/setter | Gói dịch vụ gara cung cấp. |
| 13 | `HoaDonNhap` | *(Gốc)* | `id: int`, `ngayGioNhap: Date`, `tongTien: double`, `trangThaiThanhToan: String`, `nhaCungCap: NhaCungCap`, `nvKho: NVKho`, `dsChiTietNhap: List<ChiTietNhap>` | `HoaDonNhap()`, `themChiTiet(ctn: ChiTietNhap)`, `tinhTongTien(): double`, getter/setter | Khôi phục phương thức nghiệp vụ `themChiTiet()`, `tinhTongTien()`. |
| 14 | `ChiTietNhap` | *(Gốc)* | `id: int`, `soLuongNhap: int`, `donGiaNhap: double`, `thanhTien: double`, `phuTung: PhuTung`, `hoaDonNhap: HoaDonNhap` | `ChiTietNhap()`, `tinhThanhTien(): double`, getter/setter | Khôi phục phương thức `tinhThanhTien()`. |
| 15 | `HoaDonThanhToan` | *(Gốc)* | `id: int`, `ngayLap: Date`, `ngayHoanThanh: Date`, `tongTien: double`, `trangThai: String`, `khachHang: KhachHang`, `nvBanHang: NVBanHang`, `lichHen: LichHen`, `dsDichVuSuDung: List<ChiTietDichVuSuDung>`, `dsPhuTungSuDung: List<ChiTietPhuTungSuDung>` | `HoaDonThanhToan()`, `tinhTongTien(): double`, getter/setter | Hóa đơn thanh toán xuất cho khách. |
| 16 | `ChiTietDichVuSuDung`| *(Gốc)* | `id: int`, `donGiaThucHien: double`, `thanhTien: double`, `ghiChu: String`, `dichVu: DichVu`, `hoaDonThanhToan: HoaDonThanhToan`, `ktvPhuTrach: NhanVienKyThuat` | `ChiTietDichVuSuDung()`, `tinhThanhTien(): double`, getter/setter | Dòng chi tiết gói dịch vụ thực hiện trên xe. |
| 17 | `ChiTietPhuTungSuDung`| *(Gốc)* | `id: int`, `soLuongXuat: int`, `donGiaXuat: double`, `thanhTien: double`, `phuTung: PhuTung`, `hoaDonThanhToan: HoaDonThanhToan` | `ChiTietPhuTungSuDung()`, `tinhThanhTien(): double`, getter/setter | Dòng chi tiết linh kiện phụ tùng thay thế. |
| 18 | `TKPhuTung` | `PhuTung` | `soLuongDaBan: int` | `TKPhuTung()`, getter/setter | Chuẩn hóa kiểu dữ liệu `soLuongDaBan: int`. |
| 19 | `TKDichVu` | `DichVu` | `soLuotSuDung: int`, `tongDoanhThu: double` | `TKDichVu()`, getter/setter | Lớp thống kê hiệu quả kinh doanh dịch vụ. |
| 20 | `TKNCC` | `NhaCungCap` | `tongGiaTriNhap: double` | `TKNCC()`, getter/setter | Lớp thống kê nhà cung cấp theo doanh số nhập. |
| 21 | `TKKhachHang` | `KhachHang` | `soLanSuDung: int`, `tongChiTieu: double` | `TKKhachHang()`, getter/setter | Lớp thống kê khách hàng tiềm năng. |

---

## 2. THIẾT KẾ CƠ SỞ DỮ LIỆU TOÀN HỆ THỐNG (DATABASE SCHEMA)

### 2.1 Quy trình thực hiện (Theo mục 4.2.1 Giáo trình PTIT)
1. **Ánh xạ Lớp thực thể thành Bảng CSDL**: Mỗi lớp thực thể ánh xạ thành một bảng tương ứng với tiền tố `tbl...`. Các lớp con kế thừa từ `ThanhVien` được tổ chức theo chiến lược Single Table Inheritance (`tblThanhVien` chứa cột phân loại `vaiTro: VARCHAR(30)`) để tối ưu hóa truy vấn và bảo đảm toàn vẹn khóa ngoại.
2. **Khắc phục đứt gãy quan hệ nhiều - nhiều giữa `LichHen` và `DichVu`**:
   - Biểu đồ lớp thiết kế thể hiện `LichHen` có `List<DichVu> dsDV`.
   - Trong CSDL, quan hệ nhiều - nhiều này bắt buộc phải được chuẩn hóa qua **bảng trung gian `tblLichHen_DichVu`** gồm 2 khóa ngoại `tblLichHen_id` và `tblDichVu_id`.
3. **Đồng bộ quan hệ `LichHen` – `KhachHang`**: Bảng `tblLichHen` lưu khóa ngoại `tblKhachHang_id` tham chiếu `tblThanhVien(id)` và `tblXe_id` tham chiếu `tblXe(id)`.
4. **Loại bỏ khóa ngoại đột ngột `tblHoaDonThanhToan_id` khỏi `tblLichHen`**: Lịch hẹn được tạo trước khi xe đến xưởng; hóa đơn thanh toán được lập sau khi công việc hoàn tất. Khóa ngoại tham chiếu được lưu tại `tblHoaDonThanhToan (tblLichHen_id)` chứ không lưu tại `tblLichHen`.
5. **Chuẩn hóa kiểu dữ liệu thời gian**:
   - Sử dụng kiểu dữ liệu `DATETIME` cho các trường lưu cả ngày và giờ: `ngayGioNhap` (bảng `tblHoaDonNhap`), `thoiGianHen` (bảng `tblLichHen`), `ngayHoanThanh` (bảng `tblHoaDonThanhToan`), tránh mất thông tin giờ phút khi dùng kiểu `DATE`.
   - Cột `heSoLuong` trong `tblThanhVien` chuẩn hóa dùng kiểu `FLOAT` (khớp với thực thể).

### 2.2 Bảng đặc tả các bảng CSDL chính liên quan 2 module trọng tâm

#### 1. Bảng `tblThanhVien` (Lưu người dùng hệ thống):
| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Mã định danh người dùng |
| `tenDangNhap` | `VARCHAR(50)` | `NOT NULL, UNIQUE` | Tên đăng nhập hệ thống |
| `matKhau` | `VARCHAR(255)` | `NOT NULL` | Mật khẩu mã hóa |
| `hoTen` | `VARCHAR(100)` | `NOT NULL` | Họ và tên |
| `ngaySinh` | `DATE` | `NULL` | Ngày tháng năm sinh |
| `diaChi` | `VARCHAR(255)` | `NULL` | Địa chỉ |
| `soDienThoai` | `VARCHAR(15)` | `NOT NULL` | Số điện thoại liên hệ (chuẩn hóa tên cột) |
| `email` | `VARCHAR(100)` | `NULL` | Thư điện tử |
| `vaiTro` | `VARCHAR(30)` | `NOT NULL` | KhachHang, NVBanHang, NVKho, NVQuanLy, NhanVienKyThuat |
| `viTri` | `VARCHAR(50)` | `NULL` | Chức vụ nhân viên |
| `heSoLuong` | `FLOAT` | `NULL` | Hệ số lương (chuẩn hóa kiểu FLOAT) |
| `chuyenMon` | `VARCHAR(100)` | `NULL` | Chuyên môn kỹ thuật (KTV) |
| `trangThaiKT` | `VARCHAR(30)` | `NULL` | Trạng thái công việc của KTV |

#### 2. Bảng `tblXe` (Phương tiện khách hàng):
| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Mã định danh xe |
| `bienSoXe` | `VARCHAR(20)` | `NOT NULL, UNIQUE` | Biển kiểm soát |
| `hangXe` | `VARCHAR(50)` | `NOT NULL` | Hãng sản xuất |
| `dongXe` | `VARCHAR(50)` | `NOT NULL` | Dòng xe |
| `mauSon` | `VARCHAR(30)` | `NULL` | Màu sơn |
| `tblKhachHang_id`| `INT` | `NOT NULL, FK -> tblThanhVien(id)`| Chủ sở hữu xe |

#### 3. Bảng `tblLichHen` (Lịch hẹn dịch vụ trực tuyến):
| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Mã định danh lịch hẹn |
| `thoiGianHen` | `DATETIME` | `NOT NULL` | Ngày giờ hẹn tiếp nhận (chuẩn hóa DATETIME) |
| `trangThai` | `VARCHAR(30)` | `NOT NULL` | ChoXacNhan, DaXacNhan, DaTiepNhan, DaHuy |
| `tblKhachHang_id`| `INT` | `NOT NULL, FK -> tblThanhVien(id)`| Khách hàng đặt hẹn (bổ sung chuẩn hóa) |
| `tblXe_id` | `INT` | `NOT NULL, FK -> tblXe(id)` | Xe ô tô đăng ký bảo dưỡng/sửa chữa |

#### 4. Bảng `tblLichHen_DichVu` (Bảng trung gian N-N Lịch hẹn - Dịch vụ):
| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Mã dòng đăng ký dịch vụ theo hẹn |
| `tblLichHen_id`| `INT` | `NOT NULL, FK -> tblLichHen(id)` | Khóa ngoại tham chiếu lịch hẹn |
| `tblDichVu_id` | `INT` | `NOT NULL, FK -> tblDichVu(id)` | Khóa ngoại tham chiếu dịch vụ chọn trước |
| `ghiChu` | `VARCHAR(255)` | `NULL` | Ghi chú yêu cầu riêng của khách |

#### 5. Bảng `tblNhaCungCap` (Nhà cung cấp phụ tùng):
| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Mã đối tác nhà cung cấp |
| `tenNCC` | `VARCHAR(150)` | `NOT NULL` | Tên đầy đủ nhà cung cấp |
| `diaChi` | `VARCHAR(255)` | `NULL` | Địa chỉ trụ sở/kho hàng |
| `soDienThoai` | `VARCHAR(15)` | `NOT NULL` | Điện thoại liên hệ |

#### 6. Bảng `tblPhuTung` (Danh mục phụ tùng linh kiện):
| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Mã phụ tùng |
| `tenPhuTung` | `VARCHAR(150)` | `NOT NULL` | Tên phụ tùng |
| `hangSanXuat` | `VARCHAR(100)` | `NULL` | Hãng sản xuất linh kiện |
| `donViTinh` | `VARCHAR(30)` | `NOT NULL` | Đơn vị tính (Cái, Bình, Bộ...) |
| `donGiaNiemYet`| `DECIMAL(12,2)` | `NOT NULL, DEFAULT 0` | Đơn giá bán lẻ niêm yết |
| `soLuongTon` | `INT` | `NOT NULL, DEFAULT 0` | Số lượng tồn kho hiện tại |

#### 7. Bảng `tblDichVu` (Danh mục gói dịch vụ gara):
| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Mã dịch vụ |
| `tenDichVu` | `VARCHAR(150)` | `NOT NULL` | Tên dịch vụ |
| `loaiDichVu` | `VARCHAR(50)` | `NOT NULL` | Phân loại (Bảo dưỡng, Sửa chữa, Đồng sơn...) |
| `donGia` | `DECIMAL(12,2)` | `NOT NULL, DEFAULT 0` | Đơn giá niêm yết |
| `thoiGianBaoHanh`| `VARCHAR(50)` | `NULL` | Thời hạn bảo hành dịch vụ |

#### 8. Bảng `tblHoaDonNhap` (Chứng từ nhập kho phụ tùng):
| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Số chứng từ hóa đơn nhập |
| `ngayGioNhap` | `DATETIME` | `NOT NULL` | Ngày giờ lập phiếu nhập (chuẩn hóa DATETIME) |
| `tongTien` | `DECIMAL(14,2)` | `NOT NULL, DEFAULT 0` | Tổng giá trị lô hàng nhập |
| `trangThaiThanhToan` | `VARCHAR(30)` | `NOT NULL` | Trạng thái (ChuaThanhToan / DaThanhToan) |
| `tblNhaCungCap_id` | `INT` | `NOT NULL, FK -> tblNhaCungCap(id)`| Nhà cung cấp hàng |
| `tblNVKho_id` | `INT` | `NOT NULL, FK -> tblThanhVien(id)` | Nhân viên kho thực hiện nhập |

#### 9. Bảng `tblChiTietNhap` (Dòng mặt hàng nhập kho):
| Tên cột | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PK, AUTO_INCREMENT` | Mã chi tiết dòng nhập |
| `tblHoaDonNhap_id` | `INT` | `NOT NULL, FK -> tblHoaDonNhap(id)` | Khóa ngoại hóa đơn nhập |
| `tblPhuTung_id` | `INT` | `NOT NULL, FK -> tblPhuTung(id)` | Phụ tùng được nhập về |
| `soLuongNhap` | `INT` | `NOT NULL` | Số lượng nhập kho |
| `donGiaNhap` | `DECIMAL(12,2)` | `NOT NULL` | Đơn giá mua thực tế từ NCC |
| `thanhTien` | `DECIMAL(14,2)` | `NOT NULL` | Thành tiền (SL * Đơn giá) |

---

## 3. THIẾT KẾ CHI TIẾT TĨNH CHO 2 MODULE TRỌNG TÂM (STATIC DESIGN)

### 3.1 Mô hình kiến trúc 3 tầng (3-Tier Architecture)
Hệ thống tuân thủ mô hình 3 tầng chuẩn theo giáo trình PTIT:
- **Tầng Giao diện (Presentation Layer - View)**: Xây dựng bằng công nghệ Java Web (JSP / Servlet). Nhận tương tác người dùng, gửi yêu cầu xuống tầng điều khiển/DAO và hiển thị dữ liệu trả về.
- **Tầng Xử lý Nghiệp vụ & Dữ liệu (Business & Data Access Layer - DAO)**: Chứa các lớp DAO (`NhaCungCapDAO`, `PhuTungDAO`, `HoaDonNhapDAO`, `DichVuDAO`) kế thừa lớp cơ sở `DAO` (chứa kết nối `Connection con`). Thực thi các câu lệnh SQL an toàn (`PreparedStatement`), đóng gói dữ liệu vào thực thể và trả về giao diện.
- **Tầng Thực thể (Entity Layer - Model)**: Chứa các Java Bean đại diện cho cấu trúc dữ liệu và xử lý nghiệp vụ nội tại (`tinhTongTien`, `capNhatTonKho`...).

---

### 3.2 Module 1: Khách hàng tìm kiếm thông tin dịch vụ / phụ tùng

#### 1. Thiết kế Giao diện (Mockup UI)
Màn hình Module 1 được chuẩn hóa các lỗi hiển thị:
- **`GDTimKiemDVPT` (Tra cứu tích hợp)**:
  - Form tìm kiếm: Ô nhập từ khóa `inTuKhoa`, nút `[Tìm kiếm]`.
  - **Bảng Dịch vụ**: STT, Tên dịch vụ, Loại dịch vụ, Đơn giá niêm yết, Thao tác (`[Xem chi tiết]`).
  - **Bảng Phụ tùng (Đã sửa lỗi lệch cột)**: Cột đúng thứ tự: STT, Tên phụ tùng, Đơn vị tính, Đơn giá niêm yết (Đơn vị tính: Bình, Bộ, Lít...; Đơn giá: 180.000 VNĐ, 250.000 VNĐ). Giá không bị đẩy sang cột Số lượng.
- **`gdChiTietDichVu.jsp` (Chi tiết gói dịch vụ)**:
  - Bỏ thuộc tính `thoiGianDuKien` (do lớp thực thể và CSDL không có thuộc tính này).
  - Bổ sung hiển thị `loaiDichVu`.
  - Bổ sung nút liên kết `[Đặt lịch hẹn]` (chuyển sang chức năng đặt lịch).
  - Nút `[Quay lại danh sách]`.
- **`gdChiTietPhuTung.jsp` (Chi tiết linh kiện phụ tùng)**:
  - Bổ sung đầy đủ mockup trang chi tiết phụ tùng: Mã phụ tùng, Tên phụ tùng, Hãng sản xuất, Đơn vị tính, Đơn giá niêm yết, Số lượng tồn kho, nút `[Quay lại danh sách]`.

![Giao diện Module 1](file:///C:/Users/admin/Documents/PTTK/anh_chuan_hoa/01_Giao_dien_Tim_thong_tin.png)

#### 2. Thiết kế Lớp chi tiết 3 tầng Module 1
- **Chuẩn hóa tên thuộc tính `ThanhVien`**: Sử dụng `-soDienThoai: String` (đồng bộ hoàn toàn với CSDL và Module 2, không dùng `-dienThoai`).
- **Bổ sung phương thức truy vấn chi tiết cho DAO**:
  - `DichVuDAO`: Bổ sung `+ getDichVuById(id: int): DichVu`.
  - `PhuTungDAO`: Bổ sung `+ getPhuTungById(id: int): PhuTung`.
- **Kết nối tầng giao diện chi tiết tới DAO**:
  - `gdChiTietDichVu.jsp` kết nối tới `DichVuDAO` và gọi `getDichVuById(id)`.
  - `gdChiTietPhuTung.jsp` kết nối tới `PhuTungDAO` và gọi `getPhuTungById(id)`.

![Lớp chi tiết Module 1](file:///C:/Users/admin/Documents/PTTK/anh_chuan_hoa/03_Lop_chi_tiet_Tim_thong_tin.png)

---

### 3.3 Module 2: Nhân viên kho nhập phụ tùng từ nhà cung cấp

#### 1. Thiết kế Giao diện (Mockup UI)
Loại bỏ triệt để các nghiệp vụ phát sinh ngoài phạm vi phân tích:
- **Loại bỏ**: Tính năng sửa/xóa dòng phụ tùng trên hóa đơn, popup xác nhận lưu, nút thêm phụ tùng mới trên giao diện lập hóa đơn nhập, và nghiệp vụ thanh toán cho NCC (`HoaDonNhapDAO.ghiNhanThanhToan`, `btnThanhToan`).
- **Sửa lỗi chính tả và trùng lặp**:
  - Giao diện `GDNhapSoLuongGia`: Sửa lỗi hiển thị lặp hai lần chữ "Số lượng" và hai lần chữ "Giá". Form chuẩn gồm: Tên phụ tùng, Hãng SX, ĐVT; ô nhập Số lượng; ô nhập Đơn giá; nút `[Thêm vào hóa đơn]`, nút `[Quay lại]`.
  - Bảng chi tiết trên `gdNhapPhuTung.jsp` sửa tên thuộc tính thành `-tblChiTietNhap: Table` (khắc phục lỗi viết nhầm `-blChiTietNhap`).
  - Nối `gdChinhKho.jsp` với thực thể `NVKho` qua liên kết điều hướng.

![Giao diện Module 2](file:///C:/Users/admin/Documents/PTTK/anh_chuan_hoa/02_Giao_dien_Nhap_phu_tung.png)

#### 2. Thiết kế Lớp chi tiết 3 tầng Module 2
- **Khôi phục phương thức nghiệp vụ thực thể**:
  - `HoaDonNhap`: `+ themChiTiet(ctn: ChiTietNhap)`, `+ tinhTongTien(): double`.
  - `ChiTietNhap`: `+ tinhThanhTien(): double`.
  - `PhuTung`: `+ capNhatTonKho(soLuongTang: int): boolean`.
- **Đồng bộ kiểu trả về DAO**:
  - Cùng là thao tác thêm mới đối tượng để chọn tiếp vào quy trình, phương thức thêm mới được chuẩn hóa trả về chính đối tượng vừa thêm (có `id` tự tăng sinh ra từ CSDL):
    * `NhaCungCapDAO.themNhaCungCap(ncc: NhaCungCap): NhaCungCap`
    * `PhuTungDAO.themPhuTung(pt: PhuTung): PhuTung` (sửa từ `boolean` thành `PhuTung` để `GDThemPhuTung` chuyển tiếp trực tiếp sang `GDNhapSoLuongGia`).

![Lớp chi tiết Module 2](file:///C:/Users/admin/Documents/PTTK/anh_chuan_hoa/04_Lop_chi_tiet_Nhap_phu_tung.png)

---

## 4. THIẾT KẾ HOẠT ĐỘNG VÀ ĐỘNG LỰC HỆ THỐNG (DYNAMIC DESIGN)

### 4.1 Module 1: Khách hàng tìm kiếm thông tin dịch vụ / phụ tùng

#### 1. Biểu đồ hoạt động (Activity Diagram)
- **Chuẩn hóa luồng nút Quay lại**: Trên sơ đồ hoạt động, khi người dùng bấm `[Quay lại danh sách]` từ `gdChiTietDichVu.jsp` hoặc `gdChiTietPhuTung.jsp`, luồng điều khiển **quay trở lại màn hình `gdTimKiemDVPT.jsp`** (giữ nguyên kết quả tìm kiếm trước đó), không đi thẳng ra trạng thái Kết thúc.
- **Sửa lỗi vẽ khối**: Khối `Nhận thông tin KH` được kết nối luồng vào thông suốt từ đăng nhập trang chủ. Bỏ viền kép thừa trên khối `gdChiTietPhuTung.jsp`.

![Activity Module 1](file:///C:/Users/admin/Documents/PTTK/anh_chuan_hoa/05_Activity_Tim_thong_tin.png)

#### 2. Biểu đồ tuần tự (Sequence Diagram)
Biểu đồ tuần tự Module 1 mô hình hóa chính xác tương tác 3 tầng:
1. `GDChinhKhachHang` gọi mở `gdTimKiemDVPT.jsp`.
2. Khách hàng nhập từ khóa và nhấn `[Tìm kiếm]`.
3. `gdTimKiemDVPT.jsp` gọi `DichVuDAO.getDichVuTheoTen(tuKhoa)` và `PhuTungDAO.getPhuTungTheoTen(tuKhoa)`.
4. Các DAO truy vấn CSDL, đóng gói vào `List<DichVu>` và `List<PhuTung>`, trả về JSP hiển thị.
5. Khi khách hàng bấm xem chi tiết:
   - Nếu chọn Dịch vụ: `gdTimKiemDVPT.jsp` chuyển tiếp tới `gdChiTietDichVu.jsp?id=...`. `gdChiTietDichVu.jsp` gọi `DichVuDAO.getDichVuById(id)` lấy đối tượng `DichVu` hiển thị.
   - Nếu chọn Phụ tùng: `gdTimKiemDVPT.jsp` chuyển tiếp tới `gdChiTietPhuTung.jsp?id=...`. `gdChiTietPhuTung.jsp` gọi `PhuTungDAO.getPhuTungById(id)` lấy đối tượng `PhuTung` hiển thị.

![Sequence Module 1](file:///C:/Users/admin/Documents/PTTK/anh_chuan_hoa/07_Sequence_Tim_thong_tin.png)

#### 3. Kịch bản thiết kế chi tiết (Scenario v3.0) - Module 1
*Định dạng chuẩn giáo trình PTIT (Giao diện -> DAO -> CSDL -> Entity -> Giao diện):*
1. Tại trang gdChinhKH.jsp, sau khi đăng nhập, khách hàng click chọn chức năng Tìm kiếm thông tin dịch vụ / phụ tùng.
2. Trang gdChinhKH.jsp gọi trang gdTimKiemDVPT.jsp.
3. Trang gdTimKiemDVPT.jsp hiển thị ô nhập từ khóa tìm kiếm và nút Tìm kiếm cho khách hàng.
4. Khách hàng nhập từ khóa tìm kiếm và click nút Tìm kiếm.
5. Trang gdTimKiemDVPT.jsp gọi lớp DichVuDAO yêu cầu lấy danh sách dịch vụ khớp với từ khóa.
6. Lớp DichVuDAO gọi hàm getDichVuTheoTen(tuKhoa).
7. Hàm getDichVuTheoTen(tuKhoa) thực hiện truy vấn CSDL và gọi lớp DichVu đóng gói thông tin.
8. Lớp DichVu đóng gói thông tin thực thể.
9. Lớp DichVu trả kết quả về cho hàm getDichVuTheoTen(tuKhoa).
10. Hàm getDichVuTheoTen(tuKhoa) trả kết quả về cho trang gdTimKiemDVPT.jsp.
11. Trang gdTimKiemDVPT.jsp gọi lớp PhuTungDAO yêu cầu lấy danh sách phụ tùng khớp với từ khóa.
12. Lớp PhuTungDAO gọi hàm getPhuTungTheoTen(tuKhoa).
13. Hàm getPhuTungTheoTen(tuKhoa) thực hiện truy vấn CSDL và gọi lớp PhuTung đóng gói thông tin.
14. Lớp PhuTung đóng gói thông tin thực thể.
15. Lớp PhuTung trả kết quả về cho hàm getPhuTungTheoTen(tuKhoa).
16. Hàm getPhuTungTheoTen(tuKhoa) trả kết quả về cho trang gdTimKiemDVPT.jsp.
17. Trang gdTimKiemDVPT.jsp hiển thị hai bảng danh sách kết quả Dịch vụ và Phụ tùng cho khách hàng.
18. Khách hàng click xem chi tiết một dịch vụ trên bảng kết quả.
19. Trang gdTimKiemDVPT.jsp gọi trang gdChiTietDichVu.jsp kèm mã định danh dịch vụ (id).
20. Trang gdChiTietDichVu.jsp gọi lớp DichVuDAO yêu cầu lấy thông tin chi tiết dịch vụ.
21. Lớp DichVuDAO gọi hàm getDichVuById(id).
22. Hàm getDichVuById(id) thực hiện truy vấn CSDL và gọi lớp DichVu đóng gói thông tin.
23. Lớp DichVu đóng gói thông tin thực thể.
24. Lớp DichVu trả kết quả về cho hàm getDichVuById(id).
25. Hàm getDichVuById(id) trả kết quả về cho trang gdChiTietDichVu.jsp.
26. Trang gdChiTietDichVu.jsp hiển thị thông tin chi tiết dịch vụ, nút Đặt lịch hẹn và nút Quay lại cho khách hàng.
27. Khách hàng click nút Quay lại.
28. Trang gdChiTietDichVu.jsp gọi quay lại trang gdTimKiemDVPT.jsp và giữ nguyên trạng thái kết quả tìm kiếm trước đó.
29. Khách hàng click xem chi tiết một phụ tùng trên bảng kết quả.
30. Trang gdTimKiemDVPT.jsp gọi trang gdChiTietPhuTung.jsp kèm mã định danh phụ tùng (id).
31. Trang gdChiTietPhuTung.jsp gọi lớp PhuTungDAO yêu cầu lấy thông tin chi tiết phụ tùng.
32. Lớp PhuTungDAO gọi hàm getPhuTungById(id).
33. Hàm getPhuTungById(id) thực hiện truy vấn CSDL và gọi lớp PhuTung đóng gói thông tin.
34. Lớp PhuTung đóng gói thông tin thực thể.
35. Lớp PhuTung trả kết quả về cho hàm getPhuTungById(id).
36. Hàm getPhuTungById(id) trả kết quả về cho trang gdChiTietPhuTung.jsp.
37. Trang gdChiTietPhuTung.jsp hiển thị thông tin chi tiết phụ tùng, số lượng tồn kho và nút Quay lại cho khách hàng.
38. Khách hàng click nút Quay lại.
39. Trang gdChiTietPhuTung.jsp gọi quay lại trang gdTimKiemDVPT.jsp và giữ nguyên trạng thái kết quả tìm kiếm trước đó.

---

### 4.2 Module 2: Nhân viên kho nhập phụ tùng từ nhà cung cấp

#### 1. Biểu đồ hoạt động (Activity Diagram)
Biểu đồ hoạt động thể hiện đầy đủ, rõ ràng:
- Luồng chính: Tìm NCC -> Chọn NCC -> Mở GD Lập hóa đơn -> Tìm Phụ tùng -> Chọn Phụ tùng -> Nhập SL & Giá -> Thêm vào bảng -> Lặp cho đến khi hết mặt hàng -> Lưu hóa đơn -> In phiếu hoàn tất.
- Rẽ nhánh 7a: Khi không tìm thấy NCC -> Bấm thêm NCC -> Lưu NCC -> Lấy NCC mới chuyển thẳng sang GD Lập hóa đơn.
- Rẽ nhánh 18a: Khi không tìm thấy Phụ tùng -> Bấm thêm Phụ tùng -> Lưu Phụ tùng -> Lấy Phụ tùng mới chuyển thẳng sang GD Nhập số lượng và giá.

![Activity Module 2](file:///C:/Users/admin/Documents/PTTK/anh_chuan_hoa/06_Activity_Nhap_phu_tung.png)

#### 2. Biểu đồ tuần tự (Sequence Diagram)
Biểu đồ tuần tự mô hình hóa các bước gọi hàm đồng bộ 100% giữa View, DAO, CSDL và Model Entity.

![Sequence Module 2](file:///C:/Users/admin/Documents/PTTK/anh_chuan_hoa/08_Sequence_Nhap_phu_tung.png)

#### 3. Kịch bản thiết kế chi tiết (Scenario v3.0) - Module 2
*Định dạng chuẩn giáo trình PTIT theo mẫu Giảng viên yêu cầu, khớp từng bước với kịch bản gốc và kịch bản v2.0:*
1. Tại trang gdChinhKho.jsp, sau khi đăng nhập, nhân viên kho click chọn menu Nhập phụ tùng.
2. Trang gdChinhKho.jsp gọi mở giao diện tìm kiếm nhà cung cấp gdTimNCC.jsp (gdChonNCC.jsp).
3. Trang gdTimNCC.jsp hiển thị ô nhập từ khóa tên NCC và nút Tìm kiếm cho nhân viên kho.
4. Nhân viên kho nhập tên nhà cung cấp và click nút Tìm kiếm.
5. Trang gdTimNCC.jsp gọi lớp NhaCungCapDAO yêu cầu tìm kiếm danh sách nhà cung cấp.
6. Lớp NhaCungCapDAO gọi hàm getNhaCungCapTheoTen(ten).
7. Hàm getNhaCungCapTheoTen(ten) thực hiện truy vấn CSDL và gọi lớp NhaCungCap đóng gói thông tin.
8. Lớp NhaCungCap đóng gói thông tin thực thể.
9. Lớp NhaCungCap trả kết quả về cho hàm getNhaCungCapTheoTen(ten).
10. Hàm getNhaCungCapTheoTen(ten) trả kết quả về cho trang gdTimNCC.jsp.
11. Trang gdTimNCC.jsp hiển thị danh sách nhà cung cấp lên bảng cho nhân viên kho.
7a.1. Nhân viên kho bấm nút Thêm mới NCC trên trang gdTimNCC.jsp.
7a.2. Trang gdTimNCC.jsp gọi mở giao diện thêm nhà cung cấp gdThemNCC.jsp.
7a.3. Trang gdThemNCC.jsp hiển thị form điền thông tin Nhà cung cấp mới cho nhân viên kho.
7a.4. Nhân viên kho nhập thông tin NCC mới và bấm nút Lưu NCC.
7a.5. Trang gdThemNCC.jsp gọi lớp NhaCungCapDAO yêu cầu lưu NCC mới.
7a.6. Lớp NhaCungCapDAO gọi hàm themNhaCungCap(ncc).
7a.7. Hàm themNhaCungCap(ncc) thực hiện lưu vào CSDL, lấy id tự sinh và gọi lớp NhaCungCap đóng gói thông tin thực thể.
7a.8. Lớp NhaCungCap đóng gói thông tin thực thể.
7a.9. Lớp NhaCungCap trả kết quả về cho hàm themNhaCungCap(ncc).
7a.10. Hàm themNhaCungCap(ncc) trả đối tượng NhaCungCap mới về cho trang gdThemNCC.jsp.
7a.11. Trang gdThemNCC.jsp chuyển đối tượng NhaCungCap mới tạo sang trang gdNhapPhuTung.jsp để tiếp tục quy trình lập hóa đơn.
12. Tại luồng chính: Nhân viên kho bấm nút Chọn một nhà cung cấp trên danh sách của trang gdTimNCC.jsp.
13. Trang gdTimNCC.jsp chuyển thông tin NCC đã chọn sang giao diện lập hóa đơn nhập gdNhapPhuTung.jsp.
14. Trang gdNhapPhuTung.jsp hiển thị thông tin NCC, bảng mặt hàng rỗng và tổng tiền = 0.
15. Nhân viên kho bấm nút Tìm phụ tùng trên trang gdNhapPhuTung.jsp.
16. Trang gdNhapPhuTung.jsp gọi mở giao diện tìm kiếm phụ tùng gdTimPhuTung.jsp.
17. Trang gdTimPhuTung.jsp hiển thị ô từ khóa và nút Tìm kiếm cho nhân viên kho.
18. Nhân viên kho nhập tên phụ tùng và bấm nút Tìm kiếm.
19. Trang gdTimPhuTung.jsp gọi lớp PhuTungDAO yêu cầu tìm kiếm thông tin phụ tùng.
20. Lớp PhuTungDAO gọi hàm getPhuTungTheoTen(tuKhoa).
21. Hàm getPhuTungTheoTen(tuKhoa) thực hiện truy vấn CSDL và gọi lớp PhuTung đóng gói thông tin.
22. Lớp PhuTung đóng gói thông tin thực thể.
23. Lớp PhuTung trả kết quả về cho hàm getPhuTungTheoTen(tuKhoa).
24. Hàm getPhuTungTheoTen(tuKhoa) trả kết quả về cho trang gdTimPhuTung.jsp.
25. Trang gdTimPhuTung.jsp hiển thị danh sách phụ tùng lên bảng cho nhân viên kho.
18a.1. Nhân viên kho bấm nút Thêm mới phụ tùng trên trang gdTimPhuTung.jsp.
18a.2. Trang gdTimPhuTung.jsp gọi mở giao diện thêm phụ tùng gdThemPhuTung.jsp.
18a.3. Trang gdThemPhuTung.jsp hiển thị form nhập phụ tùng mới và nút Lưu cho nhân viên kho.
18a.4. Nhân viên kho nhập thông tin phụ tùng mới và bấm nút Lưu.
18a.5. Trang gdThemPhuTung.jsp gọi lớp PhuTungDAO yêu cầu lưu phụ tùng mới.
18a.6. Lớp PhuTungDAO gọi hàm themPhuTung(pt).
18a.7. Hàm themPhuTung(pt) thực hiện lưu vào CSDL, lấy id tự sinh và gọi lớp PhuTung đóng gói thông tin thực thể.
18a.8. Lớp PhuTung đóng gói thông tin thực thể.
18a.9. Lớp PhuTung trả kết quả về cho hàm themPhuTung(pt).
18a.10. Hàm themPhuTung(pt) trả đối tượng PhuTung mới về cho trang gdThemPhuTung.jsp.
18a.11. Trang gdThemPhuTung.jsp chuyển đối tượng PhuTung mới tạo sang giao diện gdNhapSoLuongGia.jsp để nhân viên nhập số lượng và giá mua.
26. Tại luồng chính: Nhân viên kho bấm nút Chọn một phụ tùng trên danh sách của trang gdTimPhuTung.jsp.
27. Trang gdTimPhuTung.jsp chuyển đối tượng phụ tùng đã chọn sang giao diện nhập số lượng và giá gdNhapSoLuongGia.jsp.
28. Trang gdNhapSoLuongGia.jsp hiển thị thông tin phụ tùng và ô nhập số lượng, đơn giá cho nhân viên kho.
29. Nhân viên kho nhập Số lượng nhập, Đơn giá nhập và bấm nút Thêm vào hóa đơn.
30. Trang gdNhapSoLuongGia.jsp gọi lớp ChiTietNhap yêu cầu tạo mới chi tiết nhập.
31. Lớp ChiTietNhap gọi hàm tinhThanhTien().
32. Hàm tinhThanhTien() thực hiện tính thành tiền (soLuongNhap * donGiaNhap) và gọi lớp ChiTietNhap đóng gói thông tin.
33. Lớp ChiTietNhap đóng gói thông tin thực thể.
34. Lớp ChiTietNhap trả kết quả về cho hàm tinhThanhTien().
35. Hàm tinhThanhTien() trả đối tượng ChiTietNhap về cho trang gdNhapSoLuongGia.jsp.
36. Trang gdNhapSoLuongGia.jsp chuyển đối tượng ChiTietNhap sang trang gdNhapPhuTung.jsp.
37. Trang gdNhapPhuTung.jsp gọi lớp HoaDonNhap để thêm chi tiết nhập và cập nhật tổng tiền.
38. Lớp HoaDonNhap gọi hàm themChiTiet(ctn) và gọi hàm tinhTongTien().
39. Hàm tinhTongTien() thực hiện cộng dồn thành tiền các chi tiết nhập và gọi lớp HoaDonNhap đóng gói thông tin.
40. Lớp HoaDonNhap đóng gói thông tin thực thể.
41. Lớp HoaDonNhap trả kết quả dữ liệu HoaDonNhap đã cập nhật về cho trang gdNhapPhuTung.jsp.
42. Trang gdNhapPhuTung.jsp đọc dữ liệu cập nhật từ HoaDonNhap và hiển thị lại bảng danh sách mặt hàng cùng tổng tiền mới.
43. Lặp lại các bước 15 đến 42 cho đến khi nhập xong toàn bộ các mặt hàng trong chuyến hàng.
44. Nhân viên kho kiểm tra danh sách mặt hàng, tổng tiền trên trang gdNhapPhuTung.jsp và bấm nút Lưu hóa đơn.
45. Trang gdNhapPhuTung.jsp gọi lớp HoaDonNhapDAO yêu cầu lưu hóa đơn nhập kho.
46. Lớp HoaDonNhapDAO gọi hàm luuHoaDonNhap(hdn).
47. Hàm luuHoaDonNhap(hdn) thực hiện giao dịch (Transaction) CSDL: thêm mới vào tblHoaDonNhap, thêm mới các dòng vào tblChiTietNhap, cập nhật tăng số lượng tồn kho trong tblPhuTung và commit giao dịch.
48. Lớp HoaDonNhapDAO trả kết quả lưu thành công về cho trang gdNhapPhuTung.jsp.
49. Trang gdNhapPhuTung.jsp gọi trang gdHoaDonNhap.jsp.
50. Trang gdHoaDonNhap.jsp hiển thị toàn bộ hóa đơn nhập hoàn tất kèm nút In hóa đơn cho nhân viên kho.
51. Nhân viên kho bấm nút In hóa đơn để hoàn tất quy trình nhập kho.

---
## 5. TỔNG HỢP DANH MỤC CÁC TỆP ĐÃ ĐỒNG BỘ VÀ KIỂM ĐỊNH

Tất cả các bản vẽ, mã nguồn và tài liệu thiết kế đã được chuẩn hóa đồng bộ 100%:
1. **Dự án Visual Paradigm:**
   - Tệp chính: `C:\Users\admin\Documents\flashcard\GaraMan-De26\GaraMan-De26-Activity-Sequence.vpp`
   - Đã biên dịch tự động qua Visual Paradigm CLI (`ImportXML.bat`), chứa đầy đủ 18 sơ đồ thiết kế chi tiết.
2. **Bộ ảnh xuất khẩu chuẩn hóa (PNG độ phân giải cao):**
   - Thư mục: `C:\Users\admin\Documents\PTTK\anh_chuan_hoa\`
   - Gồm 8 hình ảnh chi tiết phục vụ báo cáo:
     * `01_Giao_dien_Tim_thong_tin.png`
     * `02_Giao_dien_Nhap_phu_tung.png`
     * `03_Lop_chi_tiet_Tim_thong_tin.png`
     * `04_Lop_chi_tiet_Nhap_phu_tung.png`
     * `05_Activity_Tim_thong_tin.png`
     * `06_Activity_Nhap_phu_tung.png`
     * `07_Sequence_Tim_thong_tin.png`
     * `08_Sequence_Nhap_phu_tung.png`
3. **Mã nguồn PlantUML toàn diện:**
   - Tệp: `C:\Users\admin\Documents\PTTK\PLANTUML_SUBMISSION.puml` (Blocks 11 đến 18 đã cập nhật chuẩn hóa toàn bộ 13 điểm).
4. **Báo cáo tài liệu Word độc lập:**
   - Tệp: `C:\Users\admin\Documents\PTTK\Bao_Cao_Giai_Doan_3_Thiet_Ke.docx`
   - Trình bày chuẩn học thuật: font chữ đen 100% (`#000000`), nền bảng trắng 100% (`#FFFFFF`), viền đen mảnh đơn, nhúng sẵn ảnh chất lượng cao và kịch bản chi tiết v3.0.
   - **Cam kết:** Tệp báo cáo chính của người dùng `Bao_Cao_PTTK_GaraMan_De26.docx` được giữ nguyên vẹn tuyệt đối, người dùng có thể tự sao chép phần mong muốn vào tệp chính khi cần thiết.
