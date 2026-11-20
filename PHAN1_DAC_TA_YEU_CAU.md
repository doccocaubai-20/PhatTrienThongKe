BỘ GIÁO DỤC VÀ ĐÀO TẠO
HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG
KHOA CÔNG NGHỆ THÔNG TIN

-----------------------***-----------------------

BÁO CÁO BÀI TẬP LỚN
PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG

HỆ THỐNG QUẢN LÝ GARA Ô TÔ (GaraMan)

| Học phần: | Phân tích và Thiết kế Hệ thống |
| :--- | --- |
| Giảng viên hướng dẫn: | [Họ và tên Giảng viên] |
| Sinh viên thực hiện: | [Họ và tên Sinh viên] |
| Mã sinh viên / Lớp: | [Mã SV] - [Lớp] |


# I. ĐẶC TẢ YÊU CẦU

## 1. Bảng từ khóa (Glossary List)

Tập hợp và phân loại các từ khóa chuyên môn trong phạm vi hoạt động của hệ thống quản lý gara ô tô:

| TT | Tên Tiếng Việt | Tên Tiếng Anh | Giải thích chi tiết |
| :--- | --- | --- | --- |
| **Nhóm các khái niệm liên quan đến con người** | | | |
| 1 | Thành viên | Member | Người có tài khoản và mật khẩu để đăng nhập vào hệ thống, là lớp cha trừu tượng của toàn bộ người dùng tương tác. |
| 2 | Nhân viên | Staff | Thành viên làm việc tại gara ô tô, được phân quyền các nghiệp vụ nội bộ theo chức vụ. |
| 3 | Nhân viên quản lý | Manager | Người điều hành gara, xem các báo cáo thống kê kinh doanh và quản lý danh mục dịch vụ, phụ tùng. |
| 4 | Nhân viên kho | Warehouse Staff | Người phụ trách việc nhập kho phụ tùng từ nhà cung cấp và quản lý hồ sơ đối tác cung ứng. |
| 5 | Nhân viên bán hàng | Sales Staff | Người tiếp nhận khách hàng và xe, lập phiếu sửa chữa, phân công thợ kỹ thuật và thu tiền thanh toán. |
| 6 | Khách hàng | Customer | Chủ sở hữu hoặc người điều khiển ô tô sử dụng dịch vụ tại gara hoặc đặt lịch hẹn trực tuyến qua hệ thống. |
| 7 | Nhân viên kỹ thuật | Technician | Thợ máy trực tiếp thực hiện sửa chữa tại xưởng; đóng vai trò là thực thể dữ liệu nhân sự để nhân viên bán hàng phân công phụ trách dịch vụ. |
| 8 | Nhà cung cấp | Supplier | Đối tác kinh doanh cung ứng phụ tùng cho gara; đóng vai trò là thực thể đối tác giao dịch lưu trữ trong CSDL. |
| **Nhóm các khái niệm liên quan đến hoạt động của con người** | | | |
| 9 | Đăng nhập | Login | Quá trình người dùng xác thực tài khoản và mật khẩu để truy cập vào hệ thống GaraMan. |
| 10 | Đăng xuất | Logout | Hoạt động kết thúc phiên làm việc an toàn của người dùng trên hệ thống. |
| 11 | Đổi mật khẩu | Change Password | Hoạt động người dùng chủ động cập nhật mật khẩu mới để bảo mật tài khoản cá nhân. |
| 12 | Tìm kiếm thông tin dịch vụ / phụ tùng | Search Service Info & Parts | Thao tác của khách hàng nhập từ khóa để tra cứu danh mục dịch vụ hoặc phụ tùng và xem thông tin chi tiết. |
| 13 | Xem chi tiết dịch vụ | View Service Detail | Mở trang hiển thị thông số chi tiết, giá cả niêm yết, quy trình, bảo hành của một dịch vụ cụ thể. |
| 14 | Xem chi tiết phụ tùng | View Spare Part Detail | Mở trang hiển thị thông số chi tiết, hãng sản xuất, giá bán niêm yết, tình trạng tồn kho của một phụ tùng. |
| 15 | Đặt lịch hẹn trực tuyến | Book Online Appointment | Hoạt động khách hàng chọn trước ngày giờ, loại xe và dịch vụ mong muốn để gara sắp xếp chỗ đón tiếp. |
| 16 | Nhập phụ tùng | Import Spare Parts | Quy trình nhân viên kho chọn nhà cung cấp, chọn danh mục phụ tùng, nhập số lượng, đơn giá và lưu hóa đơn nhập. |
| 17 | Quản lý nhà cung cấp | Manage Suppliers | Cập nhật, lưu trữ hồ sơ liên hệ, địa chỉ và lịch sử giao dịch với các đơn vị cung cấp phụ tùng. |
| 18 | Thêm mới nhà cung cấp | Add New Supplier | Hoạt động lưu thông tin một đối tác cung cấp mới khi chưa có trong danh bạ hệ thống trong quá trình nhập hàng. |
| 19 | Thêm mới phụ tùng | Add New Spare Part | Hoạt động khai báo loại phụ tùng mới vào danh mục khi tiến hành nhập hàng chưa từng có trước đó. |
| 20 | Quản lý dịch vụ | Manage Services | Hoạt động thêm mới, điều chỉnh tên gọi, mô tả chi tiết, giá niêm yết hoặc ngừng cung cấp các hạng mục dịch vụ. |
| 21 | Quản lý phụ tùng | Manage Spare Parts | Hoạt động thêm mới, cập nhật đơn giá bán lẻ, định mức tồn kho và quy cách của phụ tùng. |
| 22 | Nhận khách | Receive Customer | Nhân viên bán hàng đón tiếp khách, ghi nhận thông tin xe và tình trạng ban đầu khi đưa vào xưởng. |
| 23 | Nhận yêu cầu dịch vụ và phụ tùng | Receive Service Request | Ghi nhận chi tiết các gói bảo dưỡng, sửa chữa hoặc phụ tùng thay thế mà khách hàng đồng ý thực hiện. |
| 24 | Phân công kỹ thuật | Assign Technician | Nhân viên bán hàng lựa chọn kỹ thuật viên phù hợp để phụ trách từng hạng mục dịch vụ cụ thể trên xe khách. |
| 25 | Nhận thanh toán | Receive Payment | Nhân viên bán hàng chốt chi phí, thu tiền từ khách và xuất hóa đơn dịch vụ hoàn tất giao dịch. |
| 26 | Xem thống kê | View Statistics | Quản lý thực hiện tra cứu số liệu tổng hợp về doanh thu, lượt phục vụ theo dịch vụ, phụ tùng, đối tác và khách hàng. |
| 27 | Thống kê dịch vụ | Service Statistics | Báo cáo xếp hạng dịch vụ theo doanh thu và số lượt thực hiện trong một chu kỳ thời gian. |
| 28 | Thống kê phụ tùng | Part Statistics | Báo cáo số lượng phụ tùng tiêu thụ, doanh thu và tồn kho của các mặt hàng. |
| 29 | Thống kê khách hàng | Customer Statistics | Báo cáo tổng hợp số lần sử dụng dịch vụ và tổng tiền chi tiêu của từng khách hàng. |
| 30 | Thống kê nhà cung cấp | Supplier Statistics | Báo cáo tổng giá trị hàng nhập và số lần giao dịch theo từng đơn vị cung cấp. |
| **Nhóm các khái niệm liên quan đến vật, đối tượng xử lí** | | | |
| 31 | Mặt hàng | Item | Lớp cha trừu tượng của các hàng hóa/dịch vụ kinh doanh tại gara (mã, tên, đơn giá, mô tả). |
| 32 | Dịch vụ | Service | Công việc kỹ thuật gara cung cấp (kế thừa Mặt hàng, có thêm: thời gian dự kiến, bảo hành). |
| 33 | Phụ tùng | Spare Part | Linh kiện, vật tư thay thế cho xe (kế thừa Mặt hàng, có thêm: hãng sản xuất, xuất xứ, đơn vị tính, số lượng tồn kho). |
| 34 | Xe ô tô | Vehicle / Car | Đối tượng phương tiện của khách hàng tiếp nhận các dịch vụ sửa chữa, bảo dưỡng và thay thế phụ tùng tại gara. |
| 35 | Hóa đơn nhập | Import Invoice | Chứng từ lưu lại số lượng, giá mua, tổng tiền và ngày giao dịch khi nhập phụ tùng từ nhà cung cấp. |
| 36 | Chi tiết phụ tùng nhập | Imported Part Item | Dòng dữ liệu trong hóa đơn nhập, thể hiện một mặt hàng phụ tùng, số lượng và đơn giá nhập cụ thể. |
| 37 | Phiếu sửa chữa (Hóa đơn dịch vụ) | Repair Order / Job Sheet | Chứng từ xuyên suốt theo dõi tiến trình tiếp nhận xe, liên kết dịch vụ đã làm, phụ tùng đã thay, thợ phụ trách và thanh toán. |
| 38 | Chi tiết dịch vụ sử dụng | Service Usage Detail | Hạng mục dịch vụ được thực hiện trong phiếu sửa chữa và kỹ thuật viên đảm nhận. |
| 39 | Chi tiết phụ tùng thay thế | Part Replacement Detail | Phụ tùng được xuất kho lắp ráp cho xe và đơn giá bán tương ứng. |
| 40 | Lịch hẹn | Appointment | Bản ghi hẹn trước về ngày giờ, loại xe và dịch vụ mà khách hàng đăng ký trên hệ thống. |
| 41 | Báo cáo thống kê | Statistics Report | Dữ liệu tổng hợp theo tiêu chí thời gian phục vụ công tác quản trị của nhân viên quản lý. |


## 2. Mô tả hệ thống bằng ngôn ngữ tự nhiên

### 2.1 Giới thiệu mục đích hệ thống

Hệ thống quản lý gara ô tô (GaraMan) là một ứng dụng nền tảng web phục vụ công tác quản lý quy trình dịch vụ sửa chữa, bảo dưỡng ô tô; quản lý danh mục và hoạt động nhập phụ tùng từ nhà cung cấp; tiếp nhận yêu cầu, phân công kỹ thuật và thanh toán của khách hàng; hỗ trợ khách hàng tra cứu dịch vụ, phụ tùng, đặt lịch hẹn trực tuyến và cung cấp các báo cáo thống kê phục vụ công tác quản trị gara.

### 2.2 Phạm vi hệ thống

Hệ thống được thiết kế phục vụ 4 tác nhân chính trực tiếp đăng nhập và sử dụng các chức năng nghiệp vụ:

• Thành viên hệ thống: Đăng nhập, Đăng xuất, Đổi mật khẩu cá nhân.
• Khách hàng: Được thực hiện các chức năng của thành viên sau khi đăng nhập, Tìm kiếm thông tin dịch vụ / phụ tùng, Xem thông tin chi tiết dịch vụ/phụ tùng, Đặt lịch hẹn trực tuyến.
• Nhân viên bán hàng: Được thực hiện các chức năng của thành viên, Nhận khách và xe, Nhận yêu cầu dịch vụ và phụ tùng từ khách, Phân công nhân viên kỹ thuật theo dịch vụ yêu cầu, Nhận thanh toán và xuất hóa đơn cho khách hàng.
• Nhân viên kho: Được thực hiện các chức năng của thành viên, Nhập phụ tùng từ nhà cung cấp, Quản lý thông tin nhà cung cấp (tìm kiếm, thêm mới, cập nhật).
• Nhân viên quản lý: Được thực hiện các chức năng của thành viên, Quản lý thông tin dịch vụ (thêm, sửa, khóa), Quản lý thông tin phụ tùng (thêm, sửa đơn giá bán, định mức tồn), Xem các loại thống kê: thống kê dịch vụ, thống kê phụ tùng, thống kê khách hàng, thống kê nhà cung cấp.

### 2.3 Hoạt động nghiệp vụ của các chức năng

Mô tả chi tiết luồng tương tác và xử lý nghiệp vụ của các chức năng chính:

#### a. Chức năng Khách hàng tìm kiếm thông tin dịch vụ / phụ tùng:
Sau khi đăng nhập thành công, từ giao diện chính của khách hàng, khách hàng chọn menu "Tìm thông tin dịch vụ / phụ tùng". Hệ thống hiển thị giao diện tìm kiếm với ô nhập từ khóa tìm kiếm và nút "Tìm kiếm".
Khách hàng nhập từ khóa tên dịch vụ hoặc phụ tùng cần tìm (ví dụ: "thay dầu", "lọc gió") và click "Tìm kiếm". Hệ thống truy vấn CSDL và hiển thị danh sách các dịch vụ/phụ tùng có tên chứa từ khóa vừa nhập (gồm: Mã, Tên, Đơn giá niêm yết, và nút "Xem chi tiết").
Khách hàng click vào một mục dịch vụ hoặc phụ tùng trong danh sách: Nếu là dịch vụ, chuyển sang giao diện chi tiết dịch vụ hiển thị Mã dịch vụ, Tên dịch vụ, Đơn giá, Thời gian dự kiến thực hiện, Mô tả quy trình, Thời gian bảo hành; Nếu là phụ tùng, chuyển sang giao diện chi tiết phụ tùng hiển thị Mã phụ tùng, Tên phụ tùng, Hãng sản xuất, Xuất xứ, Đơn vị tính, Đơn giá bán niêm yết, Tình trạng còn hàng.
Khách hàng có thể nhấn "Quay lại" để tiếp tục tra cứu từ khóa khác. Trường hợp không tìm thấy kết quả phù hợp, hệ thống xuất thông báo cảnh báo và cho phép người dùng nhập lại từ khóa khác.

#### b. Chức năng Nhân viên kho nhập phụ tùng từ nhà cung cấp:
Sau khi đăng nhập thành công, từ giao diện chính của nhân viên kho, nhân viên chọn menu "Nhập phụ tùng". Giao diện tìm kiếm nhà cung cấp hiển thị ô tìm kiếm nhà cung cấp theo tên, nút "Tìm kiếm" và nút "Thêm mới NCC". Nhân viên nhập tên NCC và click "Tìm kiếm". Hệ thống hiển thị danh sách NCC phù hợp (Mã NCC, Tên, SĐT, Địa chỉ, Mã số thuế) kèm nút "Chọn". Trường hợp NCC chưa có trong hệ thống, nhân viên click "Thêm mới NCC", giao diện thêm NCC hiển thị form nhập thông tin đối tác -> bấm "Lưu NCC" -> Hệ thống lưu vào CSDL và tự động chọn NCC này.
Sau khi đã chọn xong 1 NCC, hệ thống chuyển sang giao diện lập hóa đơn nhập phụ tùng. Màn hình hiển thị: Thông tin NCC đã chọn; Bảng danh sách các mặt hàng phụ tùng đã chọn nhập trong phiên làm việc hiện tại, ban đầu rỗng; Nút "Tìm phụ tùng"; và nút "Lưu hóa đơn".
Vòng lặp nhập phụ tùng diễn ra như sau: Nhân viên click "Tìm phụ tùng", mở giao diện tìm phụ tùng -> Nhân viên nhập tên phụ tùng và bấm "Tìm kiếm" -> Hệ thống hiện danh sách phụ tùng kèm nút "Chọn" (nếu phụ tùng mới chưa có trong danh mục, nhân viên bấm "Thêm mới phụ tùng", mở giao diện thêm mới phụ tùng để nhập Tên, Hãng SX, Xuất xứ, Đơn vị tính, Đơn giá bán niêm yết dự kiến và bấm Lưu) -> Sau khi chọn phụ tùng, hệ thống chuyển sang giao diện nhập số lượng giá -> Nhân viên nhập Số lượng nhập và Đơn giá nhập, bấm "Thêm vào hóa đơn" -> Hệ thống cập nhật phụ tùng vào giỏ hàng, tính lại Tổng tiền và quay về giao diện nhập phụ tùng. Nhân viên lặp lại các bước trên cho đến khi nhập xong toàn bộ các mặt hàng.
Khi đã kiểm tra đầy đủ danh sách phụ tùng, nhân viên click nút "Lưu hóa đơn". Hệ thống thực hiện lưu hóa đơn nhập. Sau đó hệ thống chuyển sang giao diện xem hóa đơn để nhân viên in phiếu và thanh toán cho nhà cung cấp.

#### c. Chức năng Nhân viên quản lý xem thống kê dịch vụ:
Nhân viên quản lý đăng nhập vào hệ thống -> chọn chức năng "Xem thống kê" -> hệ thống hiện giao diện chọn loại thống kê -> chọn "Thống kê theo dịch vụ" -> Quản lý chọn khoảng thời gian cần thống kê (Từ ngày - Đến ngày) -> Kết quả thống kê hiện lên, mỗi dịch vụ trên một dòng, xếp theo thứ tự doanh thu từ cao nhất đến thấp nhất (STT, Mã dịch vụ, Tên dịch vụ, Số lượt thực hiện, Tổng doanh thu) -> Quản lý click vào một dịch vụ cụ thể -> Hệ thống hiển thị danh sách các lần thực hiện dịch vụ đó (Ngày thực hiện, Biển số xe, Tên khách hàng, Kỹ thuật viên phụ trách, Số tiền thanh toán).

### 2.4 Thông tin các đối tượng cần xử lý, quản lý

• Nhóm người dùng:
  - Thành viên: Tên đăng nhập, Mật khẩu, Họ và tên, Ngày sinh, Địa chỉ, Số điện thoại, Email.
  - Khách hàng: Kế thừa Thành viên, có thêm Biển số xe.
  - Nhân viên: Kế thừa Thành viên, có thêm Mã nhân viên, Vị trí công việc, Hệ số lương.
  - Nhân viên quản lý, Nhân viên kho, Nhân viên bán hàng: Kế thừa Nhân viên.
• Nhóm danh mục và đối tác:
  - Nhà cung cấp: Mã nhà cung cấp, Tên nhà cung cấp, Địa chỉ, Số điện thoại, Mã số thuế, Email, Ghi chú.
  - Dịch vụ: Mã dịch vụ, Tên dịch vụ, Đơn giá, Thời gian dự kiến thực hiện, Mô tả quy trình, Thời gian bảo hành.
  - Phụ tùng: Mã phụ tùng, Tên phụ tùng, Hãng sản xuất, Xuất xứ, Đơn vị tính, Số lượng tồn kho, Đơn giá bán, Mô tả.
• Nhóm vận hành và giao dịch:

- Lịch hẹn: Mã lịch hẹn, Thời gian hẹn, Khách hàng, Dịch vụ, Trạng thái.
  - Hóa đơn nhập: Mã hóa đơn nhập, Ngày giờ nhập, Nhân viên kho, Nhà cung cấp, Tổng tiền, Trạng thái thanh toán.
  - Chi tiết hóa đơn nhập: Mã chi tiết nhập, Hóa đơn nhập, Phụ tùng, Số lượng nhập, Đơn giá nhập, Thành tiền.
  - Hóa đơn thanh toán: Mã hóa đơn thanh toán, Ngày lập, Ngày giờ hoàn thành, Khách hàng, Nhân viên bán hàng, Tổng tiền thanh toán, Trạng thái.
  - Chi tiết dịch vụ sử dụng: Mã chi tiết dịch vụ, Mã hóa đơn thanh toán, Dịch vụ, Kỹ thuật viên phụ trách, Đơn giá thực hiện, Trạng thái hoàn thành.
  - Chi tiết phụ tùng sử dụng: Mã chi tiết phụ tùng, Mã hóa đơn thanh toán, Phụ tùng, Số lượng xuất, Đơn giá bán, Thành tiền.
• Nhóm báo cáo thống kê:
  - Thống kê dịch vụ: Theo số lượt sử dụng, theo tổng doanh thu.
  - Thống kê phụ tùng: Theo số lượng tiêu thụ, theo doanh thu bán lẻ.
  - Thống kê khách hàng: Theo tần suất sử dụng, theo tổng chi tiêu.
  - Thống kê nhà cung cấp: Theo tổng giá trị hàng nhập, theo số lần nhập hàng.

### 2.5 Quan hệ giữa các đối tượng, thông tin

• Một khách hàng có thể phát sinh nhiều hóa đơn thanh toán dịch vụ và sửa chữa tại gara theo thời gian.
• Một nhà cung cấp có thể liên kết với nhiều hóa đơn nhập phụ tùng của gara.
• Mỗi hóa đơn nhập phụ tùng ứng với một nhà cung cấp duy nhất và do một nhân viên kho trực tiếp lập.
• Mỗi hóa đơn nhập phụ tùng bao gồm nhiều chi tiết phụ tùng nhập; mỗi chi tiết xác định một phụ tùng, số lượng nhập và đơn giá nhập của đợt nhập đó.
• Mỗi hóa đơn thanh toán do một nhân viên bán hàng lập cho một khách hàng, có thể ghi nhận biển số xe tương ứng.
• Mỗi hóa đơn thanh toán bao gồm nhiều chi tiết dịch vụ sử dụng và nhiều chi tiết phụ tùng sử dụng.
• Mỗi dịch vụ trong hóa đơn thanh toán có thể được phân công cho một nhân viên kỹ thuật phụ trách thực hiện.
• Một nhân viên kỹ thuật có thể được phân công phụ trách nhiều dịch vụ khác nhau trên các hóa đơn thanh toán tại các thời điểm khác nhau.

## 3. Biểu đồ Use Case tổng quan và mô tả ca sử dụng

### 3.1 Biểu đồ Use Case tổng quan hệ thống

Dưới đây là biểu đồ ca sử dụng tổng quan của hệ thống GaraMan, thể hiện các tác nhân và các chức năng tương ứng trong hệ thống:

*[Hình 3.1: Biểu đồ Use Case tổng quan hệ thống GaraMan]*

### 3.2 Bảng mô tả tóm tắt Use Case tổng quan

| STT | Tên Use Case | Tác nhân chính | Mô tả chức năng |
| :--- | --- | --- | --- |
| 1 | Đăng nhập | Thành viên | Xác thực tài khoản và mật khẩu để truy cập vào đúng phân quyền chức năng trong hệ thống. |
| 2 | Đăng xuất | Thành viên | Thoát khỏi phiên làm việc hiện tại của tài khoản người dùng. |
| 3 | Đổi mật khẩu | Thành viên | Người dùng chủ động cập nhật mật khẩu mới để đảm bảo tính bảo mật cá nhân. |
| 4 | Tìm kiếm thông tin dịch vụ / phụ tùng | Khách hàng | Khách hàng nhập từ khóa để tra cứu danh mục bảng giá dịch vụ và linh kiện hiện có tại gara. |
| 5 | Đặt lịch hẹn trực tuyến | Khách hàng | Khách hàng chủ động chọn ngày, khung giờ hẹn, loại xe và dịch vụ mong muốn trước khi đưa xe đến xưởng. |
| 6 | Quản lý dịch vụ | NV Quản lý | Nhân viên quản lý thiết lập danh mục gói bảo dưỡng/sửa chữa mới, cập nhật giá cước hoặc tạm dừng cung cấp dịch vụ. |
| 7 | Quản lý phụ tùng | NV Quản lý | Nhân viên quản lý thêm danh mục linh kiện mới, điều chỉnh đơn giá niêm yết bán lẻ hoặc định mức phụ tùng. |
| 8 | Xem thống kê | NV Quản lý | Quản lý tra cứu và trích xuất các báo cáo doanh thu dịch vụ, phụ tùng, khách hàng và giá trị nhập hàng theo thời gian. |
| 9 | Nhập phụ tùng | NV Kho | Nhân viên kho tạo phiếu nhập, chọn nhà cung cấp, nhập số lượng, đơn giá và xác nhận tăng lượng tồn kho. |
| 10 | Quản lý nhà cung cấp | NV Kho | Nhân viên kho tra cứu, thêm mới đối tác hoặc sửa đổi thông tin liên hệ của các nhà cung cấp linh kiện. |
| 11 | Nhận khách và xe | NV Bán hàng | Nhân viên bán hàng tiếp nhận xe, ghi nhận thông tin khách hàng, tình trạng ban đầu của xe khi vào xưởng. |
| 12 | Nhận yêu cầu dịch vụ và phụ tùng | NV Bán hàng | Lập danh sách các gói dịch vụ sửa chữa/bảo dưỡng và linh kiện thay thế theo yêu cầu và thỏa thuận với khách. |
| 13 | Phân công kỹ thuật viên | NV Bán hàng | Chọn và chỉ định kỹ thuật viên phù hợp để phụ trách từng hạng mục dịch vụ đã tiếp nhận. |
| 14 | Nhận thanh toán | NV Bán hàng | Chốt danh sách dịch vụ - phụ tùng hoàn thành, tính tổng chi phí, nhận tiền từ khách và xuất hóa đơn thanh toán. |


## 4. Biểu đồ Use Case chi tiết và mô tả ca sử dụng

### 4.1 Chức năng Khách hàng tìm kiếm thông tin dịch vụ / phụ tùng

Biểu đồ ca sử dụng chi tiết cho chức năng tìm kiếm thông tin dịch vụ / phụ tùng:

*[Hình 4.1: Biểu đồ Use Case chi tiết - Module Tìm kiếm thông tin dịch vụ / phụ tùng]*

#### Bảng đặc tả Use Case chi tiết: Tìm kiếm thông tin dịch vụ / phụ tùng

| Tên Use Case | Tìm kiếm thông tin dịch vụ / phụ tùng |
| :--- | --- |
| Tác nhân chính | Khách hàng |
| Tiền điều kiện | Khách hàng đã đăng nhập thành công vào hệ thống. |
| Hậu điều kiện | Khách hàng xem được danh sách kết quả và thông tin chi tiết dịch vụ/phụ tùng theo nhu cầu. |
| Luồng sự kiện chính (Main Flow) | 1. Khách hàng bấm chọn menu "Tìm thông tin dịch vụ / phụ tùng".<br/>2. Hệ thống hiển thị giao diện tìm kiếm với ô nhập từ khóa và nút "Tìm kiếm".<br/>3. Khách hàng nhập tên từ khóa cần tìm (ví dụ: "thay dầu", "lọc gió") và click "Tìm kiếm".<br/>4. Hệ thống hiển thị danh sách các dịch vụ/phụ tùng có tên khớp với từ khóa vừa nhập.<br/>5. Khách hàng click vào một dịch vụ hoặc phụ tùng trong danh sách.<br/>6. Hệ thống hiển thị toàn bộ thông tin chi tiết của dịch vụ hoặc phụ tùng đã chọn.<br/>7. Khách hàng có thể nhấn "Quay lại" để tiếp tục tra cứu từ khóa khác. |
| Luồng ngoại lệ (Alternative Flow) | 3a. Từ khóa để trống:<br/>- Nếu khách hàng click "Tìm kiếm" mà chưa nhập từ khóa, hệ thống hiển thị thông báo yêu cầu nhập từ khóa tra cứu.<br/>4a. Không tìm thấy dữ liệu phù hợp:<br/>- Nếu không có dịch vụ hoặc phụ tùng nào chứa từ khóa, hệ thống thông báo: "Không tìm thấy kết quả phù hợp!" và cho phép người dùng nhập từ khóa khác. |


### 4.2 Chức năng Nhân viên kho nhập phụ tùng từ nhà cung cấp

Biểu đồ ca sử dụng chi tiết cho chức năng nhân viên kho nhập phụ tùng từ nhà cung cấp:

*[Hình 4.2: Biểu đồ Use Case chi tiết - Module Nhập phụ tùng từ nhà cung cấp]*

#### Bảng đặc tả Use Case chi tiết: Nhập phụ tùng từ nhà cung cấp

| Tên Use Case | Nhập phụ tùng từ nhà cung cấp |
| :--- | --- |
| Tác nhân chính | Nhân viên kho |
| Tiền điều kiện | Nhân viên kho đã đăng nhập thành công vào hệ thống. |
| Hậu điều kiện | Hóa đơn nhập được lưu vĩnh viễn vào CSDL, số lượng tồn kho phụ tùng tăng tương ứng, chứng từ nhập kho hiển thị hoàn tất để in và thanh toán. |
| Luồng sự kiện chính (Main Flow) | 1. Nhân viên kho chọn menu "Nhập phụ tùng".<br/>2. Hệ thống hiển thị giao diện tìm kiếm nhà cung cấp.<br/>3. Nhân viên nhập tên nhà cung cấp và click "Tìm kiếm".<br/>4. Hệ thống hiển thị danh sách các nhà cung cấp phù hợp, nhân viên click "Chọn" nhà cung cấp mong muốn.<br/>5. Hệ thống chuyển sang giao diện lập hóa đơn nhập phụ tùng với thông tin nhà cung cấp đã chọn và danh sách phụ tùng (ban đầu rỗng).<br/>6. Nhân viên click nút "Tìm phụ tùng", hệ thống hiển thị giao diện tìm kiếm phụ tùng.<br/>7. Nhân viên nhập tên phụ tùng cần tìm và click "Chọn" phụ tùng muốn nhập.<br/>8. Hệ thống chuyển sang giao diện nhập số lượng và đơn giá. Nhân viên điền số lượng nhập, đơn giá nhập và bấm "Thêm vào hóa đơn".<br/>9. Hệ thống lưu phụ tùng vào danh sách hóa đơn, tính lại tổng tiền và quay về giao diện lập hóa đơn.<br/>(Các bước 6-9 được lặp lại cho đến khi nhân viên nhập xong toàn bộ các mặt hàng cần nhập).<br/>10. Nhân viên kiểm tra danh sách và click nút "Lưu hóa đơn".<br/>11. Hệ thống lưu thông tin hóa đơn nhập, lưu các chi tiết phụ tùng và cập nhật số lượng tồn kho, sau đó chuyển sang giao diện hiển thị hóa đơn nhập hoàn chỉnh để in và thanh toán cho nhà cung cấp. |
| Luồng ngoại lệ (Alternative Flow) | 4a. Nhà cung cấp chưa tồn tại:<br/>- Nhân viên click "Thêm mới NCC", hệ thống hiển thị form nhập thông tin đối tác -> nhân viên nhập thông tin và bấm "Lưu NCC". Hệ thống lưu nhà cung cấp mới và tự động chọn để tiếp tục lập hóa đơn.<br/>7a. Phụ tùng mới chưa có trong danh mục:<br/>- Nhân viên click "Thêm mới phụ tùng", hệ thống hiển thị form nhập thông tin phụ tùng -> nhân viên nhập thông tin và bấm "Lưu". Hệ thống lưu phụ tùng mới và tự động chọn để chuyển sang bước nhập số lượng, đơn giá.<br/>8a. Nhập số liệu sai:<br/>- Nếu số lượng <= 0 hoặc đơn giá <= 0, hệ thống báo lỗi yêu cầu nhập số dương hợp lệ.<br/>10a. Hóa đơn chưa có phụ tùng:<br/>- Nếu bấm "Lưu hóa đơn" khi danh sách phụ tùng đang trống, hệ thống hiển thị cảnh báo: "Chưa có phụ tùng nào được chọn vào hóa đơn!". |

