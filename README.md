## Cấu trúc thư mục tài liệu và mã nguồn

```text
├── GaraMan/                     # Mã nguồn web demo Java (JSP, DAO/Model, garaman.sql, 21 JUnit Tests)
│   ├── src/                     # Source code Java (DAO, Model) và JUnit Tests
│   ├── WebContent/              # Giao diện web JSP (gdTimKiemDVPT, gdNhapPhuTung,...)
│   ├── garaman.sql              # Script tạo cơ sở dữ liệu MySQL
│   ├── pom.xml                  # Cấu hình dự án Maven và Tomcat Embedded
│   └── run.bat                  # Khởi động nhanh web server
├── Bao_Cao_PTTK.md              # Báo cáo phân tích và thiết kế hệ thống hoàn chỉnh (kèm mã PlantUML và phụ lục prompt)
└── README.md                    # Hướng dẫn chạy dự án
```

## Hướng dẫn chạy dự án Web demo (GaraMan)

### 1. Chuẩn bị môi trường:
- Java JDK 11 trở lên (khuyến nghị JDK 17 hoặc 21).
- MySQL Server (cổng 3306, tài khoản root / mật khẩu 123456).
- Apache Maven.

### 2. Cài đặt CSDL:
```bash
mysql -u root -p123456 < GaraMan/garaman.sql
```

### 3. Chạy ứng dụng:
Vào thư mục GaraMan và chạy:
```bash
mvn exec:java
```
Hoặc nháy đúp vào file run.bat.

Truy cập hệ thống tại: **http://localhost:8080/index.jsp**
