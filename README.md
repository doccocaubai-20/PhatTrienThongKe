# Hệ Thống Quản Lý Gara Ô Tô (GaraMan) - Đề tài 26
> **Học viện Công nghệ Bưu chính Viễn thông (PTIT)**  
> **Môn học:** Phân tích và Thiết kế Hệ thống Thông tin

---

## 📌 Tổng quan dự án
Dự án thực hiện phân tích, thiết kế và lập trình demo hệ thống quản lý gara ô tô **GaraMan** (Đề bài 26) theo chuẩn bài giảng Thực tập tốt nghiệp CNPM (PTIT), tập trung chuyên sâu vào **02 module cốt lõi**:
1. **Module 1:** Khách hàng tra cứu thông tin Dịch vụ & Phụ tùng.
2. **Module 2:** Nhân viên kho lập phiếu nhập Phụ tùng từ Nhà cung cấp.

---

## 📁 Cấu trúc thư mục tài liệu & mã nguồn

```text
├── GaraMan/                     # Mã nguồn web demo Java (JSP, Servlet/DAO, MySQL, Maven)
│   ├── src/                     # Source code Java (DAO, Model) & 21 JUnit Tests
│   ├── WebContent/              # Giao diện web JSP (gdTimKiemDVPT, gdNhapPhuTung,...)
│   ├── garaman.sql              # Script tạo cơ sở dữ liệu MySQL
│   ├── pom.xml                  # Cấu hình dự án Maven & Tomcat Embedded
│   └── run.bat                  # File khởi động nhanh web server
├── PHAN1_DAC_TA_YEU_CAU.md       # Báo cáo Phần 1: Đặc tả yêu cầu & Biểu đồ Use Case
├── PHAN2_PHAN_TICH_YEU_CAU.md    # Báo cáo Phần 2: Phân tích yêu cầu & Biểu đồ lớp phân tích
├── PHAN3_THIET_KE_HE_THONG.md    # Báo cáo Phần 3: Thiết kế thực thể, CSDL & Sequence Diagram
├── PLANTUML_SUBMISSION.puml      # Tổng hợp toàn bộ mã PlantUML nộp qua Google Form
├── DEBAI_GARAMAN_TRACKING.md     # Bản đồ theo dõi yêu cầu Đề 26
├── TAI_LIEU_THAM_KHAO_MAP.md     # Bản đồ tham chiếu giáo trình PTIT
├── Debai26.txt                   # Nội dung đề bài gốc số 26
└── Bao_Cao_PTTK_GaraMan_De26.docx# Báo cáo tổng hợp hoàn chỉnh (Word)
```

---

## 🚀 Hướng dẫn chạy dự án Web demo (GaraMan)

### 1. Chuẩn bị môi trường:
- Java JDK 11 trở lên (khuyến nghị JDK 17 hoặc 21).
- MySQL Server (cổng 3306, tài khoản `root` / mật khẩu `123456`).
- Apache Maven.

### 2. Cài đặt CSDL:
```bash
mysql -u root -p123456 < GaraMan/garaman.sql
```

### 3. Chạy ứng dụng:
Vào thư mục `GaraMan` và chạy:
```bash
mvn exec:java
```
Hoặc nháy đúp vào file `run.bat`.

Truy cập hệ thống tại: **`http://localhost:8080/index.jsp`**
