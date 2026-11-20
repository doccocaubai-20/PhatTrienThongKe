# -*- coding: utf-8 -*-
import docx

def humanize_docx():
    doc = docx.Document('Bao_Cao_PTTK_GaraMan_De26.docx')

    # 1. Humanize Paragraph 22 (Section 2.4)
    p22_text = """• Nhóm người dùng:
  - Thành viên: Tên đăng nhập, Mật khẩu, Họ và tên, Ngày sinh, Địa chỉ, Số điện thoại, Email.
  - Khách hàng: Kế thừa Thành viên, có thêm Biển số xe.
  - Nhân viên: Kế thừa Thành viên, có thêm Mã nhân viên, Vị trí công việc, Hệ số lương.
  - Nhân viên quản lý, Nhân viên kho, Nhân viên bán hàng: Kế thừa Nhân viên.
  - Nhân viên kỹ thuật: Mã kỹ thuật viên, Họ và tên, Số điện thoại, Chuyên môn kỹ thuật, Trạng thái làm việc.
• Nhóm danh mục và đối tác:
  - Nhà cung cấp: Mã nhà cung cấp, Tên nhà cung cấp, Địa chỉ, Số điện thoại, Mã số thuế, Email, Ghi chú.
  - Dịch vụ: Mã dịch vụ, Tên dịch vụ, Đơn giá, Thời gian dự kiến thực hiện, Mô tả quy trình, Thời gian bảo hành.
  - Phụ tùng: Mã phụ tùng, Tên phụ tùng, Hãng sản xuất, Xuất xứ, Đơn vị tính, Số lượng tồn kho, Đơn giá bán, Mô tả.
• Nhóm vận hành và giao dịch:
  - Lịch hẹn: Mã lịch hẹn, Ngày giờ hẹn, Khách hàng, Biển số xe, Dịch vụ yêu cầu, Trạng thái.
  - Hóa đơn nhập: Mã hóa đơn nhập, Ngày giờ nhập, Nhân viên kho, Nhà cung cấp, Tổng tiền, Trạng thái thanh toán.
  - Chi tiết hóa đơn nhập: Mã chi tiết nhập, Hóa đơn nhập, Phụ tùng, Số lượng nhập, Đơn giá nhập, Thành tiền.
  - Phiếu sửa chữa: Mã phiếu sửa chữa, Ngày giờ tiếp nhận, Ngày giờ hoàn thành, Hiện trạng xe, Khách hàng, Biển số xe, Nhân viên bán hàng, Tổng tiền thanh toán, Thuế VAT, Phương thức thanh toán, Trạng thái.
  - Chi tiết dịch vụ sử dụng: Mã chi tiết dịch vụ, Phiếu sửa chữa, Dịch vụ, Kỹ thuật viên phụ trách, Đơn giá thực hiện, Trạng thái hoàn thành.
  - Chi tiết phụ tùng thay thế: Mã chi tiết phụ tùng, Phiếu sửa chữa, Phụ tùng, Số lượng xuất, Đơn giá bán, Thành tiền.
• Nhóm báo cáo thống kê:
  - Thống kê dịch vụ: Theo số lượt sử dụng, theo tổng doanh thu.
  - Thống kê phụ tùng: Theo số lượng tiêu thụ, theo doanh thu bán lẻ.
  - Thống kê khách hàng: Theo tần suất sử dụng, theo tổng chi tiêu.
  - Thống kê nhà cung cấp: Theo tổng giá trị hàng nhập, theo số lần nhập hàng."""

    for p in doc.paragraphs:
        if "Nhóm người dùng:" in p.text and "Mã nhân viên" in p.text:
            p.text = p22_text
            break

    # 2. Humanize Paragraph 24 (Section 2.5)
    p24_text = """• Một khách hàng có thể đặt nhiều lịch hẹn trực tuyến qua các mốc thời gian khác nhau.
• Một khách hàng có thể phát sinh nhiều lần sửa chữa, bảo dưỡng tại gara.
• Một nhà cung cấp có thể cung cấp nhiều loại phụ tùng khác nhau.
• Một nhà cung cấp có thể liên kết với nhiều hóa đơn nhập phụ tùng.
• Một hóa đơn nhập phụ tùng ứng với một nhà cung cấp duy nhất và do một nhân viên kho lập.
• Một hóa đơn nhập phụ tùng có thể chứa nhiều mặt hàng phụ tùng; mỗi phụ tùng có số lượng và đơn giá nhập riêng.
• Một phiếu sửa chữa do một nhân viên bán hàng lập cho một khách hàng cụ thể gắn với biển số xe.
• Một phiếu sửa chữa có thể bao gồm nhiều dịch vụ sửa chữa và nhiều phụ tùng thay thế.
• Mỗi dịch vụ trong phiếu sửa chữa có thể phân công cho một nhân viên kỹ thuật thực hiện.
• Một nhân viên kỹ thuật có thể được phân công phụ trách nhiều dịch vụ khác nhau trong các thời điểm khác nhau.
• Mỗi phiếu sửa chữa sau khi hoàn thành sẽ tiến hành thanh toán và xuất hóa đơn cho khách hàng."""

    for p in doc.paragraphs:
        if "Một nhà cung cấp có thể xuất nhiều hóa đơn nhập phụ tùng" in p.text or "Một khách hàng có thể đặt nhiều lịch hẹn trực tuyến" in p.text:
            p.text = p24_text
            break

    # 3. Humanize Section 3 intro
    for p in doc.paragraphs:
        if "Biểu đồ Use Case tổng quan thể hiện cấu trúc phân cấp kế thừa" in p.text:
            p.text = "Dưới đây là biểu đồ ca sử dụng (Use Case) tổng quan của hệ thống GaraMan, thể hiện các tác nhân và các chức năng tương ứng trong hệ thống:"

    # 4. Humanize Section 4 headings & intros
    for p in doc.paragraphs:
        if "4. Biểu đồ Use Case chi tiết và mô tả ca sử dụng (2 module trọng tâm)" in p.text:
            p.text = "4. Biểu đồ Use Case chi tiết và mô tả ca sử dụng"
        if "Biểu đồ phân rã Use Case thể hiện ca sử dụng gốc cùng các ca sử dụng chi tiết mở rộng" in p.text:
            p.text = "Biểu đồ ca sử dụng chi tiết cho chức năng tìm kiếm thông tin dịch vụ / phụ tùng:"
        if "Biểu đồ phân rã Use Case thể hiện các mục tiêu nghiệp vụ bắt buộc" in p.text:
            p.text = "Biểu đồ ca sử dụng chi tiết cho chức năng nhân viên kho nhập phụ tùng từ nhà cung cấp:"

    # 5. Humanize Table 5 (Module 1 Spec Table)
    t5 = doc.tables[5]
    # Row 2: Tiền điều kiện
    t5.rows[2].cells[1].text = "Khách hàng đã đăng nhập thành công vào hệ thống."
    # Row 4: Main Flow
    t5.rows[4].cells[1].text = ("1. Khách hàng bấm chọn menu \"Tìm thông tin dịch vụ / phụ tùng\".\n"
                                "2. Hệ thống hiển thị giao diện tìm kiếm với ô nhập từ khóa và nút \"Tìm kiếm\".\n"
                                "3. Khách hàng nhập tên từ khóa cần tìm (ví dụ: \"thay dầu\", \"lọc gió\") và click \"Tìm kiếm\".\n"
                                "4. Hệ thống hiển thị danh sách các dịch vụ/phụ tùng có tên khớp với từ khóa vừa nhập.\n"
                                "5. Khách hàng click vào một dịch vụ hoặc phụ tùng trong danh sách.\n"
                                "6. Hệ thống hiển thị toàn bộ thông tin chi tiết của dịch vụ hoặc phụ tùng đã chọn.\n"
                                "7. Khách hàng có thể nhấn \"Quay lại\" để tiếp tục tra cứu từ khóa khác.")
    # Row 5: Alt Flow
    t5.rows[5].cells[1].text = ("3a. Từ khóa để trống:\n"
                                "- Nếu khách hàng click \"Tìm kiếm\" mà chưa nhập từ khóa, hệ thống hiển thị thông báo yêu cầu nhập từ khóa tra cứu.\n"
                                "4a. Không tìm thấy dữ liệu phù hợp:\n"
                                "- Nếu không có dịch vụ hoặc phụ tùng nào chứa từ khóa, hệ thống thông báo: \"Không tìm thấy kết quả phù hợp!\" và cho phép người dùng nhập từ khóa khác.")

    # 6. Humanize Table 7 (Module 2 Spec Table)
    t7 = doc.tables[7]
    # Row 2: Tiền điều kiện
    t7.rows[2].cells[1].text = "Nhân viên kho đã đăng nhập thành công vào hệ thống."
    # Row 4: Main Flow
    t7.rows[4].cells[1].text = ("1. Nhân viên kho chọn menu \"Nhập phụ tùng\".\n"
                                "2. Hệ thống hiển thị giao diện tìm kiếm nhà cung cấp.\n"
                                "3. Nhân viên nhập tên nhà cung cấp và click \"Tìm kiếm\".\n"
                                "4. Hệ thống hiển thị danh sách các nhà cung cấp phù hợp, nhân viên click \"Chọn\" nhà cung cấp mong muốn.\n"
                                "5. Hệ thống chuyển sang giao diện lập hóa đơn nhập phụ tùng với thông tin nhà cung cấp đã chọn và danh sách phụ tùng (ban đầu rỗng).\n"
                                "6. Nhân viên click nút \"Tìm phụ tùng\", hệ thống hiển thị giao diện tìm kiếm phụ tùng.\n"
                                "7. Nhân viên nhập tên phụ tùng cần tìm và click \"Chọn\" phụ tùng muốn nhập.\n"
                                "8. Hệ thống chuyển sang giao diện nhập số lượng và đơn giá. Nhân viên điền số lượng nhập, đơn giá nhập và bấm \"Thêm vào hóa đơn\".\n"
                                "9. Hệ thống lưu phụ tùng vào danh sách hóa đơn, tính lại tổng tiền và quay về giao diện lập hóa đơn.\n"
                                "(Các bước 6-9 được lặp lại cho đến khi nhân viên nhập xong toàn bộ các mặt hàng cần nhập).\n"
                                "10. Nhân viên kiểm tra danh sách và click nút \"Lưu hóa đơn\".\n"
                                "11. Hệ thống lưu thông tin hóa đơn nhập, lưu các chi tiết phụ tùng và cập nhật số lượng tồn kho, sau đó chuyển sang giao diện hiển thị hóa đơn nhập hoàn chỉnh để in và thanh toán cho nhà cung cấp.")
    # Row 5: Alt Flow
    t7.rows[5].cells[1].text = ("4a. Nhà cung cấp chưa tồn tại:\n"
                                "- Nhân viên click \"Thêm mới NCC\", hệ thống hiển thị form nhập thông tin đối tác -> nhân viên nhập thông tin và bấm \"Lưu NCC\". Hệ thống lưu nhà cung cấp mới và tự động chọn để tiếp tục lập hóa đơn.\n"
                                "7a. Phụ tùng mới chưa có trong danh mục:\n"
                                "- Nhân viên click \"Thêm mới phụ tùng\", hệ thống hiển thị form nhập thông tin phụ tùng -> nhân viên nhập thông tin và bấm \"Lưu\". Hệ thống lưu phụ tùng mới và tự động chọn để chuyển sang bước nhập số lượng, đơn giá.\n"
                                "8a. Nhập số liệu sai:\n"
                                "- Nếu số lượng <= 0 hoặc đơn giá <= 0, hệ thống báo lỗi yêu cầu nhập số dương hợp lệ.\n"
                                "10a. Hóa đơn chưa có phụ tùng:\n"
                                "- Nếu bấm \"Lưu hóa đơn\" khi danh sách phụ tùng đang trống, hệ thống hiển thị cảnh báo: \"Chưa có phụ tùng nào được chọn vào hóa đơn!\".")

    # Re-apply standard font for updated table cells
    for t in [t5, t7]:
        for r in t.rows:
            for cell in r.cells:
                for p in cell.paragraphs:
                    for run in p.runs:
                        run.font.name = "Times New Roman"
                        run.font.size = docx.shared.Pt(10)

    doc.save('Bao_Cao_PTTK_GaraMan_De26.docx')
    doc.save('Bao_Cao_PTTK_GaraMan_De26_Clean.docx')
    print("Humanized Bao_Cao_PTTK_GaraMan_De26.docx successfully!")

if __name__ == "__main__":
    humanize_docx()
