# THEO DÕI VÀ QUẢN LÝ DỰ ÁN: HỆ THỐNG QUẢN LÝ GARA Ô TÔ (GaraMan)
> **Mã đề:** Đề bài 26 (Debai26.txt)  
> **Môn học:** Phân tích và Thiết kế Hệ thống / Thực tập tốt nghiệp 2 CNPM  
> **Tài liệu phương pháp chuẩn:** `BG HP TTTN 2 CNPM 2020 final.pdf`

---

## 1. TỔNG QUAN HỆ THỐNG (GaraMan)

Hệ thống quản lý gara ô tô (**GaraMan**) phục vụ 4 tác nhân chính sau khi đăng nhập:
1. **Nhân viên quản lý:**
   - Xem các loại thống kê: dịch vụ, phụ tùng, khách hàng và nhà cung cấp.
   - Quản lý thông tin dịch vụ, thông tin phụ tùng.
2. **Nhân viên kho:**
   - Nhập phụ tùng từ nhà cung cấp.
   - Quản lý thông tin nhà cung cấp.
3. **Nhân viên bán hàng:**
   - Nhận khách.
   - Nhận yêu cầu dịch vụ và phụ tùng từ khách.
   - Phân công nhân viên kỹ thuật theo dịch vụ khách yêu cầu.
   - Nhận thanh toán từ khách hàng.
4. **Khách hàng:**
   - Tìm kiếm thông tin dịch vụ/phụ tùng.
   - Đặt lịch hẹn trực tuyến.

---

## 2. HAI (02) MODULE TRỌNG TÂM CẦN LÀM CHI TIẾT

Trong toàn bộ quá trình Phân tích - Thiết kế - Lập trình, đề bài yêu cầu tập trung làm chi tiết cho **2 module** sau:

### Module 1: Khách hàng tìm kiếm thông tin dịch vụ (và phụ tùng)
- **Tác nhân:** Khách hàng
- **Quy trình nghiệp vụ:**
  1. Khách hàng chọn menu tìm thông tin dịch vụ / phụ tùng.
  2. Nhập tên (từ khóa) dịch vụ / phụ tùng để tìm kiếm.
  3. Hệ thống hiển thị danh sách các dịch vụ / phụ tùng có tên chứa từ khóa vừa nhập.
  4. Khách hàng click vào một dịch vụ / phụ tùng cụ thể để xem chi tiết.
  5. Hệ thống hiển thị thông tin chi tiết về dịch vụ / phụ tùng đó.

### Module 2: Nhân viên kho nhập phụ tùng từ nhà cung cấp
- **Tác nhân:** Nhân viên kho
- **Quy trình nghiệp vụ:**
  1. Nhân viên chọn menu "Nhập phụ tùng".
  2. Tìm và chọn nhà cung cấp theo tên (thêm mới nhà cung cấp nếu chưa có trong hệ thống).
  3. Lặp cho đến khi hết danh sách phụ tùng muốn nhập:
     - Tìm và chọn phụ tùng theo tên (nhập mới phụ tùng nếu chưa có).
     - Nhập số lượng và đơn giá nhập.
  4. Hết vòng lặp, xác nhận hóa đơn nhập.
  5. In hóa đơn nhập và thực hiện thanh toán cho nhà cung cấp.

---

## 3. CHECKLIST CÁC HẠNG MỤC CẦN NỘP VÀ TRẠNG THÁI TRIỂN KHAI

| Giai đoạn | Hạng mục công việc chi tiết | Yêu cầu chuẩn tài liệu tham khảo | Trạng thái | Ghi chú / Link form nộp |
| :--- | :--- | :--- | :---: | :--- |
| **I. ĐẶC TẢ** | **1. Bảng từ khóa (Glossary List)** | Bảng 4 cột: TT, Tiếng Việt, Tiếng Anh, Giải thích (chia 3 nhóm: Con người, Hoạt động, Đối tượng) | `DONE` | Đã xong tại PHAN1_DAC_TA_YEU_CAU.md |
| | **2. Mô tả HT bằng ngôn ngữ tự nhiên** | Đúng 5 bước chuẩn mục 3.1.2 trong sách | `DONE` | Đã xong tại PHAN1_DAC_TA_YEU_CAU.md |
| | **3. Biểu đồ Use Case tổng quan** | Các actor phân cấp kế thừa, use case mịn hóa | `DONE` | Đã xong tại PHAN1_DAC_TA_YEU_CAU.md |
| | **4. Bảng mô tả Use Case tổng quan** | Bảng mô tả vắn tắt từng use case | `DONE` | Đã xong tại PHAN1_DAC_TA_YEU_CAU.md |
| | **5. Biểu đồ Use Case chi tiết 2 module** | Use case phân rã (include, extend nếu có) | `DONE` | Đã xong tại PHAN1_DAC_TA_YEU_CAU.md |
| | **6. Bảng mô tả Use Case chi tiết 2 module** | Tên UC, Actor, Pre-condition, Post-condition, Luồng chính, Luồng ngoại lệ | `DONE` | Đã xong tại PHAN1_DAC_TA_YEU_CAU.md |
| | **7. Code PlantUML cho Đặc tả** | Lưu mã nguồn PlantUML các sơ đồ đặc tả | `DONE` | Form 1: https://forms.gle/WjBeCqMYZnMPHmcV7 |
| **II. PHÂN TÍCH** | **1. Kịch bản (Scenario v1.0) 2 module** | Định dạng bảng theo case study mục 3.2.1 (luồng chính, ngoại lệ chi tiết) | `DONE` | Đã xong tại PHAN2_PHAN_TICH_YEU_CAU.md |
| | **2. Dựng Sơ đồ lớp thực thể HỆ THỐNG** | Thực hiện đủ 5 bước trích danh từ mục 3.2.2 | `DONE` | Đã xong tại PHAN2_PHAN_TICH_YEU_CAU.md & PlantUML 2.1 |
| | **3. Trích & vẽ Biểu đồ lớp cho 2 module** | Lớp biên (GD..., tiền tố in, out, sub), Lớp thực thể, phân bổ method (mục 3.2.3) | `DONE` | Nộp PlantUML Form 2 (Mục 2.2 & 2.3) |
| | **4. Biểu đồ trạng thái (State Diagram) 2 module** | Trạng thái = giao diện chờ tương tác (mục 3.2.4) | `DONE` | Nộp PlantUML Form 2 (Mục 2.4 & 2.5) |
| | **5. Kịch bản chi tiết (Scenario ver 2.0)** | Từng bước là tương tác giữa Actor, Boundary và Entity (mục 3.2.4) | `DONE` | Đã xong tại PHAN2_PHAN_TICH_YEU_CAU.md |
| | **6. Biểu đồ giao tiếp (Communication Diagram)** | Đúng thứ tự thông điệp theo kịch bản v2.0 (mục 3.2.4) | `DONE` | Nộp PlantUML Form 2 (Mục 2.6 & 2.7) |
| | **7. Code PlantUML cho Phân tích** | Lưu mã nguồn PlantUML các sơ đồ phân tích | `DONE` | Form 2: https://forms.gle/ciKQDmZntpPKuH4H7 |
| **III. THIẾT KẾ** | **1. Sơ đồ lớp thực thể toàn hệ thống (Thiết kế)** | Thêm id, kiểu dữ liệu ngôn ngữ (Java), quan hệ aggregation/composition (mục 4.1) | `TODO` | Nộp PlantUML Form 3 |
| | **2. Sơ đồ CSDL hệ thống (Database Diagram)** | Bảng `tbl...`, khóa chính PK, khóa ngoại FK, kiểu dữ liệu SQL (mục 4.2) | `TODO` | Nộp PlantUML Form 3 |
| | **3. Thiết kế giao diện (UI Mockup) 2 module** | Wireframe/mockup các màn hình JSP cho từng bước nghiệp vụ (mục 4.3.1) | `TODO` | |
| | **4. Biểu đồ lớp thiết kế chi tiết 2 module** | 3 tầng: UI (JSP/Servlet), DAO (truy cập CSDL), Model (Thực thể) (mục 4.3.1) | `TODO` | Nộp PlantUML Form 3 |
| | **5. Biểu đồ hoạt động (Activity Diagram) 2 module** | Các action ứng với các method được gọi (mục 4.3.2) | `TODO` | Nộp PlantUML Form 3 |
| | **6. Kịch bản thiết kế (Scenario ver 3.0) 2 module** | Gọi hàm cụ thể trên DAO và Model (mục 4.3.2) | `TODO` | |
| | **7. Biểu đồ tuần tự (Sequence Diagram) 2 module** | Lifeline cho UI, DAO, Model; gọi đúng tên method, đúng thời gian sống (mục 4.3.2) | `TODO` | Nộp PlantUML Form 3 |
| | **8. Biểu đồ gói (Package Diagram)** | Kiến trúc package: `model`, `dao`, `view` (chia theo module/actor) (mục 4.3.3) | `TODO` | Nộp PlantUML Form 3 |
| | **9. Biểu đồ triển khai (Deployment Diagram)** | Kiến trúc phần cứng/phần mềm: Client (Browser) - Server (Tomcat) - DB (MySQL) (mục 4.3.3) | `TODO` | Nộp PlantUML Form 3 |
| | **10. Code PlantUML cho Thiết kế** | Lưu mã nguồn PlantUML các sơ đồ thiết kế | `TODO` | Form: https://forms.gle/rqmj7ZFnfQ5n7FzD7 |
| **IV. LẬP TRÌNH & ĐÓNG GÓI** | **1. Cài đặt CSDL MySQL** | File SQL tạo bảng, dữ liệu mẫu | `TODO` | |
| | **2. Cài đặt Java Web (Model - DAO - View)** | Cài đặt DAO, Model, UI JSP/Servlet theo kiến trúc Eclipse chuẩn (mục 5.1, 5.2) | `TODO` | |
| | **3. Ảnh chụp giao diện thực tế** | Chụp đầy đủ màn hình các bước chạy của 2 module | `TODO` | |
| | **4. Ảnh chụp cấu trúc file project** | Chụp cấu trúc thư mục trong IDE/editor (Eclipse / VS Code / IntelliJ) | `TODO` | |
| | **5. Mã nguồn & Link GitHub** | Đẩy toàn bộ source code lên GitHub repo | `TODO` | |
| **V. PHỤ LỤC & TỰ ĐÁNH GIÁ** | **1. Phụ lục các Prompt đã dùng** | Ghi chép prompt, mô tả cách dùng kết quả (dùng luôn, sửa, tham khảo, vẽ lại...) | `TODO` | |
| | **2. Form tự đánh giá** | Điền đánh giá bài làm | `TODO` | Form: https://forms.gle/yuLGeZZtWheGsnPu5 |

---

## 4. DANH SÁCH LINK GOOGLE FORMS NỘP BÀI
- **Form nộp code PlantUML Đặc tả:** [https://forms.gle/WjBeCqMYZnMPHmcV7](https://forms.gle/WjBeCqMYZnMPHmcV7)
- **Form nộp code PlantUML Phân tích:** [https://forms.gle/ciKQDmZntpPKuH4H7](https://forms.gle/ciKQDmZntpPKuH4H7)
- **Form nộp code PlantUML Thiết kế:** [https://forms.gle/rqmj7ZFnfQ5n7FzD7](https://forms.gle/rqmj7ZFnfQ5n7FzD7)
- **Form tự đánh giá bài làm:** [https://forms.gle/yuLGeZZtWheGsnPu5](https://forms.gle/yuLGeZZtWheGsnPu5)

---

## 5. HƯỚNG DẪN AI TRONG MỖI BƯỚC HỖ TRỢ
Khi người dùng yêu cầu làm bất kỳ phần nào (Đặc tả, Phân tích, Thiết kế, Code, Vẽ sơ đồ PlantUML):
1. **Tra cứu quy chuẩn:** Mở file `TAI_LIEU_THAM_KHAO_MAP.md` để lấy đúng template, đúng quy tắc 5 bước, đúng quy ước đặt tên (`in_`, `out_`, `sub_`, `tbl...`, `XDAO`, `model`, `dao`, `view`).
2. **Cập nhật tiến độ:** Đánh dấu lại trạng thái (`IN_PROGRESS`, `DONE`) trong bảng checklist ở file này.
3. **Sinh mã PlantUML:** Đảm bảo cú pháp chuẩn, render đẹp, sẵn sàng để nộp vào form.
4. **Lưu vết prompt:** Hỗ trợ chuẩn bị sẵn bảng ghi chép prompt phục vụ phần "Phụ lục prompt".
