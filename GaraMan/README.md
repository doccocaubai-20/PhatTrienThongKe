# HỆ THỐNG QUẢN LÝ GARA Ô TÔ – GARAMAN (ĐỀ TÀI SỐ 26)
**Học phần:** Phân tích và Thiết kế Hệ thống Thông tin (PTIT)  
**Kiến trúc:** 3-Tier MVC Java Web (JSP + DAO + Model/Entity) theo chuẩn học viện PTIT.

---

## 1. Tổng quan Kiến trúc & Phạm vi Đề tài

Hệ thống được xây dựng đồng bộ 100% với **Kịch bản Ca sử dụng v3.0** và **Hồ sơ Thiết kế hệ thống Giai đoạn 3**:

### Module 1: Khách hàng tìm kiếm dịch vụ & phụ tùng
- **Mục tiêu:** Khách hàng tra cứu nhanh danh mục gói dịch vụ sửa chữa và phụ tùng thay thế của gara, xem chi tiết và đặt lịch hẹn.
- **Các màn hình JSP:**
  1. `gdChinhKH.jsp`: Trang chủ khách hàng, thông tin cá nhân và xe.
  2. `gdTimKiemDVPT.jsp`: Giao diện tích hợp tìm kiếm Dịch vụ & Phụ tùng (Hiển thị đầy đủ thông tin: STT, Mã, Tên, Hãng sản xuất, ĐVT, Giá niêm yết, Số lượng tồn kho).
  3. `gdChiTietDichVu.jsp`: Xem thông tin chi tiết dịch vụ (Tên, Loại dịch vụ, Đơn giá, Thời gian bảo hành, Nút Đặt lịch hẹn, Nút Quay lại giữ nguyên từ khóa tìm kiếm).
  4. `gdChiTietPhuTung.jsp`: Xem thông tin chi tiết phụ tùng (Tên, Hãng, ĐVT, Đơn giá bán lẻ, Tồn kho, Nút Quay lại).

### Module 2: Nhân viên kho nhập phụ tùng từ Nhà cung cấp
- **Mục tiêu:** Quản lý quy trình nhập hàng, thêm mới nhà cung cấp / phụ tùng, kiểm soát giá nhập và tự động cập nhật tồn kho qua Transaction an toàn.
- **Các màn hình JSP:**
  1. `gdChinhKho.jsp`: Trang chủ nhân viên kho.
  2. `gdTimNCC.jsp`: Tìm kiếm và chọn nhà cung cấp giao hàng.
  3. `gdThemNCC.jsp`: Thêm mới thông tin nhà cung cấp đối tác.
  4. `gdNhapPhuTung.jsp`: Lập phiếu nhập kho, theo dõi danh sách phụ tùng đã chọn và tổng tiền hóa đơn.
  5. `gdTimPhuTung.jsp`: Tìm kiếm phụ tùng cần nhập thêm.
  6. `gdThemPhuTung.jsp`: Thêm mới phụ tùng vào danh mục khi nhà cung cấp giao mặt hàng mới.
  7. `gdNhapSoLuongGia.jsp`: Nhập số lượng và đơn giá nhập thực tế từ NCC, tự động tính thành tiền.
  8. `gdHoaDonNhap.jsp`: Hiển thị hóa đơn nhập kho chính thức, hỗ trợ in phiếu nhập (`window.print()`).

---

## 2. Cấu trúc Thư mục Dự án

```text
C:\Users\admin\Documents\GaraMan\
├── WebContent/                     # Tầng Giao diện JSP
│   ├── header.jsp                  # Thanh điều hướng và phong cách giao diện chung
│   ├── index.jsp                   # Trang chủ điều hướng chọn vai trò
│   ├── gdChinhKH.jsp               # Giao diện chính khách hàng
│   ├── gdTimKiemDVPT.jsp           # Giao diện tìm kiếm DV & PT tích hợp
│   ├── gdChiTietDichVu.jsp         # Chi tiết Dịch vụ
│   ├── gdChiTietPhuTung.jsp        # Chi tiết Phụ tùng
│   ├── gdChinhKho.jsp              # Giao diện chính Nhân viên kho
│   ├── gdTimNCC.jsp                # Tìm kiếm Nhà cung cấp
│   ├── gdThemNCC.jsp               # Thêm mới Nhà cung cấp
│   ├── gdNhapPhuTung.jsp           # Lập hóa đơn nhập phụ tùng
│   ├── gdTimPhuTung.jsp            # Tìm kiếm phụ tùng nhập kho
│   ├── gdThemPhuTung.jsp           # Thêm mới phụ tùng
│   ├── gdNhapSoLuongGia.jsp        # Nhập số lượng và đơn giá nhập
│   └── gdHoaDonNhap.jsp            # Xem và in hóa đơn nhập
├── src/
│   ├── main/java/
│   │   ├── model/                  # Tầng Thực thể (Entity / JavaBean)
│   │   │   ├── ThanhVien.java      (Lớp cha)
│   │   │   ├── KhachHang.java      (Kế thừa ThanhVien)
│   │   │   ├── NhanVien.java       (Kế thừa ThanhVien)
│   │   │   ├── NVKho.java          (Kế thừa NhanVien)
│   │   │   ├── Xe.java             (Thuộc KhachHang)
│   │   │   ├── DichVu.java         (Dịch vụ bảo dưỡng/sửa chữa)
│   │   │   ├── PhuTung.java        (Phụ tùng, capNhatTonKho())
│   │   │   ├── NhaCungCap.java     (Đối tác cung cấp phụ tùng)
│   │   │   ├── ChiTietNhap.java    (tinhThanhTien())
│   │   │   ├── HoaDonNhap.java     (themChiTiet(), tinhTongTien())
│   │   │   └── LichHen.java        (Lịch hẹn dịch vụ)
│   │   ├── dao/                    # Tầng Truy cập Dữ liệu (DAO)
│   │   │   ├── DAO.java            (Kết nối CSDL, đa cấu hình localhost)
│   │   │   ├── DichVuDAO.java      (getDichVuTheoTen, getDichVuById)
│   │   │   ├── PhuTungDAO.java     (getPhuTungTheoTen, getPhuTungById, themPhuTung, capNhatTonKho)
│   │   │   ├── NhaCungCapDAO.java  (getNhaCungCapTheoTen, themNhaCungCap)
│   │   │   └── HoaDonNhapDAO.java  (luuHoaDonNhap [Transaction], getHoaDonNhapById)
│   │   └── com/garaman/
│   │       └── Main.java           (Khởi chạy Embedded Tomcat 9 trên cổng 8080)
│   └── test/java/dao/              # Tầng Kiểm thử Đơn vị (Unit Test - JUnit 4)
│       ├── DichVuDAOTest.java
│       ├── PhuTungDAOTest.java
│       ├── NhaCungCapDAOTest.java
│       └── HoaDonNhapDAOTest.java
├── garaman.sql                     # Kịch bản khởi tạo CSDL & dữ liệu mẫu
├── pom.xml                         # Cấu hình Maven
└── run.bat                         # Kịch bản khởi chạy ứng dụng 1-click
```

---

## 3. Hướng dẫn Khởi chạy Ứng dụng

### Bước 1: Khởi động MySQL & Nạp CSDL
1. Đảm bảo dịch vụ MySQL đang chạy (qua XAMPP hoặc Windows Services `net start MySQL80`).
2. Mở MySQL Client / Navicat / DBeaver / Workbench và chạy toàn bộ nội dung file:
   ```text
   C:\Users\admin\Documents\GaraMan\garaman.sql
   ```
   *File script đã chuẩn bị sẵn cơ sở dữ liệu `garaman` cùng dữ liệu mẫu chuẩn cho cả Khách hàng, Xe, Dịch vụ, Phụ tùng, Nhà cung cấp và Nhân viên kho.*

### Bước 2: Chạy ứng dụng qua run.bat
- Nhấp đúp vào file `run.bat` tại thư mục `C:\Users\admin\Documents\GaraMan\run.bat`.
- Hệ thống sẽ tự động biên dịch và khởi chạy máy chủ nhúng Tomcat 9.
- Mở trình duyệt web và truy cập địa chỉ:
  - **Trang điều hướng tổng:** [http://localhost:8080/index.jsp](http://localhost:8080/index.jsp)
  - **Module 1 (Khách hàng):** [http://localhost:8080/gdChinhKH.jsp](http://localhost:8080/gdChinhKH.jsp)
  - **Module 2 (Thủ kho):** [http://localhost:8080/gdChinhKho.jsp](http://localhost:8080/gdChinhKho.jsp)

### Bước 3: Chạy Unit Tests
Trong thư mục dự án, chạy lệnh Maven:
```bash
mvn test
```
Tất cả các ca kiểm thử trong `DichVuDAOTest`, `PhuTungDAOTest`, `NhaCungCapDAOTest`, `HoaDonNhapDAOTest` sẽ được thực thi để kiểm định toàn bộ chức năng DAO và tính toàn vẹn nghiệp vụ.
