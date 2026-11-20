CREATE DATABASE IF NOT EXISTS garaman CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE garaman;

DROP TABLE IF EXISTS tblChiTietPhuTungSuDung;
DROP TABLE IF EXISTS tblChiTietDichVuSuDung;
DROP TABLE IF EXISTS tblHoaDonThanhToan;
DROP TABLE IF EXISTS tblChiTietNhap;
DROP TABLE IF EXISTS tblHoaDonNhap;
DROP TABLE IF EXISTS tblLichHen;
DROP TABLE IF EXISTS tblXe;
DROP TABLE IF EXISTS tblPhuTung;
DROP TABLE IF EXISTS tblDichVu;
DROP TABLE IF EXISTS tblNhaCungCap;
DROP TABLE IF EXISTS tblNVKyThuat;
DROP TABLE IF EXISTS tblNVBanHang;
DROP TABLE IF EXISTS tblNVKho;
DROP TABLE IF EXISTS tblNVQuanLy;
DROP TABLE IF EXISTS tblNhanVien;
DROP TABLE IF EXISTS tblKhachHang;
DROP TABLE IF EXISTS tblThanhVien;



CREATE TABLE tblThanhVien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tenDangNhap VARCHAR(255) NOT NULL UNIQUE,
    matKhau VARCHAR(255) NOT NULL,
    hoTen VARCHAR(255) NOT NULL,
    ngaySinh DATE NULL,
    diaChi VARCHAR(255) NULL,
    soDienThoai VARCHAR(255) NOT NULL,
    email VARCHAR(255) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblKhachHang (
    tblThanhVienid INT PRIMARY KEY,
    FOREIGN KEY (tblThanhVienid) REFERENCES tblThanhVien(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblNhanVien (
    tblThanhVienid INT PRIMARY KEY,
    viTri VARCHAR(255) NULL,
    heSoLuong DOUBLE NULL,
    FOREIGN KEY (tblThanhVienid) REFERENCES tblThanhVien(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblNVQuanLy (
    tblNhanVienid INT PRIMARY KEY,
    FOREIGN KEY (tblNhanVienid) REFERENCES tblNhanVien(tblThanhVienid) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblNVKho (
    tblNhanVienid INT PRIMARY KEY,
    FOREIGN KEY (tblNhanVienid) REFERENCES tblNhanVien(tblThanhVienid) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblNVBanHang (
    tblNhanVienid INT PRIMARY KEY,
    FOREIGN KEY (tblNhanVienid) REFERENCES tblNhanVien(tblThanhVienid) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblNVKyThuat (
    tblNhanVienid INT PRIMARY KEY,
    chuyenMon VARCHAR(255) NULL,
    trangThai VARCHAR(255) NULL,
    FOREIGN KEY (tblNhanVienid) REFERENCES tblNhanVien(tblThanhVienid) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



CREATE TABLE tblXe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bienSoXe VARCHAR(255) NOT NULL UNIQUE,
    hangXe VARCHAR(255) NULL,
    dongXe VARCHAR(255) NULL,
    mauSon VARCHAR(255) NULL,
    tblKhachHangid INT NOT NULL,
    FOREIGN KEY (tblKhachHangid) REFERENCES tblKhachHang(tblThanhVienid) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblDichVu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tenDichVu VARCHAR(255) NOT NULL,
    loaiDichVu VARCHAR(255) NOT NULL,
    donGia DOUBLE NOT NULL DEFAULT 0,
    thoiGianBaoHanh VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblPhuTung (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tenPhuTung VARCHAR(255) NOT NULL,
    hangSanXuat VARCHAR(255) NOT NULL,
    donViTinh VARCHAR(255) NOT NULL,
    donGiaNiemYet DOUBLE NOT NULL DEFAULT 0,
    soLuongTon INT NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblNhaCungCap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tenNCC VARCHAR(255) NOT NULL,
    diaChi VARCHAR(255) NOT NULL,
    soDienThoai VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE tblLichHen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    thoiGianHen DATETIME NULL,
    trangThai VARCHAR(255) NULL,
    tblXeid INT NOT NULL,
    tblKhachHangid INT NOT NULL,
    FOREIGN KEY (tblXeid) REFERENCES tblXe(id),
    FOREIGN KEY (tblKhachHangid) REFERENCES tblKhachHang(tblThanhVienid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblHoaDonNhap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngayGioNhap DATETIME NOT NULL,
    tongTien DOUBLE NOT NULL DEFAULT 0,
    trangThaiThanhToan VARCHAR(255) NOT NULL DEFAULT 'DaThanhToan',
    tblNhaCungCapid INT NOT NULL,
    tblNVKhoid INT NOT NULL,
    FOREIGN KEY (tblNhaCungCapid) REFERENCES tblNhaCungCap(id),
    FOREIGN KEY (tblNVKhoid) REFERENCES tblNVKho(tblNhanVienid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblChiTietNhap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    soLuongNhap INT NOT NULL,
    donGiaNhap DOUBLE NOT NULL,
    thanhTien DOUBLE NOT NULL,
    tblHoaDonNhapid INT NOT NULL,
    tblPhuTungid INT NOT NULL,
    FOREIGN KEY (tblHoaDonNhapid) REFERENCES tblHoaDonNhap(id) ON DELETE CASCADE,
    FOREIGN KEY (tblPhuTungid) REFERENCES tblPhuTung(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblHoaDonThanhToan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngayLap DATE NOT NULL,
    ngayHoanThanh DATETIME NULL,
    tongTien DOUBLE NOT NULL DEFAULT 0,
    trangThai VARCHAR(255) NULL,
    tblLichHenid INT NULL,
    tblKhachHangid INT NOT NULL,
    tblNVBanHangid INT NOT NULL,
    FOREIGN KEY (tblLichHenid) REFERENCES tblLichHen(id),
    FOREIGN KEY (tblKhachHangid) REFERENCES tblKhachHang(tblThanhVienid),
    FOREIGN KEY (tblNVBanHangid) REFERENCES tblNVBanHang(tblNhanVienid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblChiTietDichVuSuDung (
    id INT AUTO_INCREMENT PRIMARY KEY,
    donGiaThucHien DOUBLE NOT NULL,
    trangThaiHoanThanh VARCHAR(255) NULL,
    tblHoaDonThanhToanid INT NOT NULL,
    tblDichVuid INT NOT NULL,
    tblNVKyThuatid INT NOT NULL,
    FOREIGN KEY (tblHoaDonThanhToanid) REFERENCES tblHoaDonThanhToan(id) ON DELETE CASCADE,
    FOREIGN KEY (tblDichVuid) REFERENCES tblDichVu(id),
    FOREIGN KEY (tblNVKyThuatid) REFERENCES tblNVKyThuat(tblNhanVienid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE tblChiTietPhuTungSuDung (
    id INT AUTO_INCREMENT PRIMARY KEY,
    soLuongXuat INT NOT NULL,
    donGiaBan DOUBLE NOT NULL,
    thanhTien DOUBLE NOT NULL,
    tblHoaDonThanhToanid INT NOT NULL,
    tblPhuTungid INT NOT NULL,
    FOREIGN KEY (tblHoaDonThanhToanid) REFERENCES tblHoaDonThanhToan(id) ON DELETE CASCADE,
    FOREIGN KEY (tblPhuTungid) REFERENCES tblPhuTung(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- Thành viên
INSERT INTO tblThanhVien (id, tenDangNhap, matKhau, hoTen, ngaySinh, diaChi, soDienThoai, email) VALUES
(1, 'nvkho1', '123456', 'Lê Hoàng Kho', '1992-05-15', '12 Giải Phóng, Hà Nội', '0901234567', 'nvkho@garaman.vn'),
(2, 'khach1', '123456', 'Nguyễn Văn An', '1988-10-20', '88 Cầu Giấy, Hà Nội', '0912345678', 'an.nguyen@gmail.com'),
(3, 'khach2', '123456', 'Trần Thị Bình', '1995-03-12', '45 Lê Duẩn, Hà Nội', '0987654321', 'binh.tran@gmail.com'),
(4, 'nvbh1', '123456', 'Phạm Thu Ngân', '1996-08-08', '20 Phố Huế, Hà Nội', '0933221144', 'ngan.pham@garaman.vn'),
(5, 'quanly', '123456', 'Trần Văn Quản', '1980-01-01', '1 Hoàng Đạo Thúy, Hà Nội', '0999888777', 'quanly@garaman.vn'),
(6, 'ktv1', '123456', 'Ngô Minh Thợ', '1990-07-22', '50 Minh Khai, Hà Nội', '0944556677', 'ktv1@garaman.vn');

-- Phân bảng Khách hàng và Nhân viên
INSERT INTO tblKhachHang (tblThanhVienid) VALUES (2), (3);

INSERT INTO tblNhanVien (tblThanhVienid, viTri, heSoLuong) VALUES
(1, 'Thủ kho trưởng', 2.8),
(4, 'Tư vấn bán hàng', 2.5),
(5, 'Quản lý Gara', 4.5),
(6, 'Kỹ thuật viên máy gầm', 2.6);

INSERT INTO tblNVKho (tblNhanVienid) VALUES (1);
INSERT INTO tblNVBanHang (tblNhanVienid) VALUES (4);
INSERT INTO tblNVQuanLy (tblNhanVienid) VALUES (5);
INSERT INTO tblNVKyThuat (tblNhanVienid, chuyenMon, trangThai) VALUES (6, 'Động cơ & Phanh', 'SanSang');

-- Xe ô tô
INSERT INTO tblXe (id, bienSoXe, hangXe, dongXe, mauSon, tblKhachHangid) VALUES
(1, '30A-123.45', 'Toyota', 'Camry 2.5Q', 'Đen', 2),
(2, '30E-678.90', 'Hyundai', 'Accent 1.4AT', 'Trắng', 3);

-- Danh mục Dịch vụ
INSERT INTO tblDichVu (id, tenDichVu, loaiDichVu, donGia, thoiGianBaoHanh) VALUES
(1, 'Thay dầu động cơ Castrol Magnetic', 'Bảo dưỡng định kỳ', 180000, '3 tháng hoặc 5.000 km'),
(2, 'Bảo dưỡng hệ thống phanh 4 bánh', 'Bảo dưỡng gầm phanh', 250000, '6 tháng hoặc 10.000 km'),
(3, 'Cân chỉnh thước lái góc đặt bánh xe 3D', 'Kiểm định gầm', 300000, '3 tháng'),
(4, 'Vệ sinh kim phun buồng đốt bằng sóng siêu âm', 'Chăm sóc động cơ', 350000, '6 tháng'),
(5, 'Kiểm tra nạp gas điều hòa R134a', 'Hệ thống điện lạnh', 200000, '12 tháng'),
(6, 'Sơn dặm vá cản trước xe ô tô', 'Đồng sơn', 500000, '12 tháng');

-- Danh mục Phụ tùng
INSERT INTO tblPhuTung (id, tenPhuTung, hangSanXuat, donViTinh, donGiaNiemYet, soLuongTon) VALUES
(1, 'Dầu động cơ Castrol Magnatec 5W-30', 'Castrol', 'Can 4L', 450000, 25),
(2, 'Lọc dầu nhớt động cơ Toyota Camry', 'Toyota Denso', 'Cái', 120000, 40),
(3, 'Lọc gió điều hòa than hoạt tính Honda CRV', 'Honda OEM', 'Cái', 180000, 30),
(4, 'Má phanh trước xe Hyundai Accent', 'Hyundai Mobis', 'Bộ', 480000, 15),
(5, 'Bugi bạch kim Iridium NGK Laser', 'NGK Japan', 'Cái', 150000, 80),
(6, 'Nước làm mát động cơ cao cấp đỏ Prestone', 'Prestone USA', 'Bình 4L', 220000, 35),
(7, 'Bình ắc quy ô tô GS 12V-45Ah', 'GS Battery', 'Bình', 1250000, 12),
(8, 'Cần gạt mưa thân mềm Bosch Aerotwin', 'Bosch Germany', 'Cặp', 280000, 50);

-- Danh mục Nhà cung cấp
INSERT INTO tblNhaCungCap (id, tenNCC, diaChi, soDienThoai) VALUES
(1, 'Công ty Cổ phần Phụ tùng Ô tô Hòa Bình', '120 Trần Khát Chân, Hai Bà Trưng, Hà Nội', '02439761234'),
(2, 'Tổng kho Phụ tùng Denso Việt Nam', '45 Lê Văn Lương, Cầu Giấy, Hà Nội', '02438562345'),
(3, 'Công ty TNHH Linh kiện Ô tô Trường Long', '88 Tam Trinh, Hoàng Mai, Hà Nội', '02436453456'),
(4, 'Nhà phân phối Ắc quy & Dầu nhờn Petrolimex', '15 Giải Phóng, Đống Đa, Hà Nội', '02438644567');

-- Mẫu hóa đơn nhập cũ để test
INSERT INTO tblHoaDonNhap (id, ngayGioNhap, tongTien, trangThaiThanhToan, tblNhaCungCapid, tblNVKhoid) VALUES
(1, '2026-11-10 09:30:00', 8500000, 'DaThanhToan', 1, 1);

INSERT INTO tblChiTietNhap (id, soLuongNhap, donGiaNhap, thanhTien, tblHoaDonNhapid, tblPhuTungid) VALUES
(1, 10, 380000, 3800000, 1, 1),
(2, 20, 95000, 1900000, 1, 2),
(3, 6, 400000, 2400000, 1, 4),
(4, 2, 200000, 400000, 1, 6);