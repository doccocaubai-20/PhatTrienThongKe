<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
    <%@ page import="java.text.*, java.util.*, model.*, dao.*" %>
        <% request.setCharacterEncoding("UTF-8"); HoaDonNhap hdn=(HoaDonNhap) session.getAttribute("hoaDonNhap"); if
            (hdn==null || hdn.getNhaCungCap()==null) { response.sendRedirect("gdTimNCC.jsp"); return; } String
            errorMsg=null; if ("luuHoaDon".equals(request.getParameter("action"))) { if (hdn.getDsChiTietNhap()==null ||
            hdn.getDsChiTietNhap().isEmpty()) { errorMsg="Vui lòng chọn ít nhất một phụ tùng trước khi lưu!" ; } else {
            hdn.tinhTongTien(); if (new HoaDonNhapDAO().luuHoaDonNhap(hdn)) { int idMoi=hdn.getId();
            session.removeAttribute("hoaDonNhap"); response.sendRedirect("gdHoaDonNhap.jsp?id=" + idMoi);
                return;
            }
            errorMsg = " Lưu hóa đơn thất bại! Vui lòng thử lại."; } } NumberFormat
            nf=NumberFormat.getCurrencyInstance(new Locale("vi", "VN" )); %>
            <!DOCTYPE html>
            <html>

            <head>
                <meta charset="UTF-8">
                <title>Lập Phiếu Nhập Kho - GaraMan</title>
            </head>

            <body>
                <div class="container">
                    <%@ include file="header.jsp" %>
                        <h3>Lập Phiếu Nhập Kho</h3>

                        <% if (errorMsg !=null) { %>
                            <div
                                style="background: #fee2e2; color: #991b1b; padding: 10px 14px; border-radius: 6px; margin-bottom: 16px;">
                                <%= errorMsg %>
                            </div>
                            <% } %>

                                <div class="info-box">
                                    <strong>Nhà cung cấp:</strong>
                                    <%= hdn.getNhaCungCap().getTenNCC() %> |
                                        <strong>SĐT:</strong>
                                        <%= hdn.getNhaCungCap().getSoDienThoai() %> |
                                            <strong>Địa chỉ:</strong>
                                            <%= hdn.getNhaCungCap().getDiaChi() %>
                                </div>

                                <div
                                    style="display: flex; justify-content: space-between; align-items: center; margin: 18px 0 10px 0;">
                                    <h4 style="margin: 0;">Danh Sách Phụ Tùng Nhập</h4>
                                    <div style="display: flex; gap: 10px;">
                                        <a href="gdTimPhuTung.jsp" class="btn btn-primary">Tìm phụ tùng</a>
                                        <a href="gdThemPhuTung.jsp" class="btn btn-success">+ Thêm phụ tùng mới</a>
                                    </div>
                                </div>

                                <% if (hdn.getDsChiTietNhap() !=null && !hdn.getDsChiTietNhap().isEmpty()) { %>
                                    <table class="data-table">
                                        <thead>
                                            <tr>
                                                <th style="width: 50px; text-align: center;">STT</th>
                                                <th>Tên phụ tùng</th>
                                                <th style="width: 80px; text-align: center;">ĐVT</th>
                                                <th style="width: 100px; text-align: right;">Số lượng</th>
                                                <th style="width: 140px; text-align: right;">Đơn giá nhập</th>
                                                <th style="width: 160px; text-align: right;">Thành tiền</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <% int stt=1; for (ChiTietNhap ct : hdn.getDsChiTietNhap()) { %>
                                                <tr>
                                                    <td style="text-align: center;">
                                                        <%= stt++ %>
                                                    </td>
                                                    <td><strong>
                                                            <%= ct.getPhuTung().getTenPhuTung() %>
                                                        </strong> (<%= ct.getPhuTung().getHangSanXuat() %>)</td>
                                                    <td style="text-align: center;">
                                                        <%= ct.getPhuTung().getDonViTinh() %>
                                                    </td>
                                                    <td style="text-align: right; font-weight: bold;">
                                                        <%= ct.getSoLuongNhap() %>
                                                    </td>
                                                    <td style="text-align: right;">
                                                        <%= nf.format(ct.getDonGiaNhap()) %>
                                                    </td>
                                                    <td style="text-align: right; font-weight: bold; color: #2563eb;">
                                                        <%= nf.format(ct.getThanhTien()) %>
                                                    </td>
                                                </tr>
                                                <% } %>
                                        </tbody>
                                        <tfoot>
                                            <tr style="background: #f8fafc;">
                                                <td colspan="5"
                                                    style="text-align: right; font-weight: bold; padding: 12px;">TỔNG
                                                    TIỀN:</td>
                                                <td
                                                    style="text-align: right; font-weight: bold; color: #dc2626; font-size: 16px; padding: 12px;">
                                                    <%= nf.format(hdn.tinhTongTien()) %>
                                                </td>
                                            </tr>
                                        </tfoot>
                                    </table>
                                    <% } else { %>
                                        <div
                                            style="text-align: center; color: #64748b; padding: 30px; border: 1px dashed #cbd5e1; border-radius: 6px; margin: 16px 0;">
                                            Chưa có phụ tùng nào. Nhấn <strong>"Tìm phụ tùng"</strong> hoặc
                                            <strong>"Thêm phụ tùng mới"</strong> để chọn hàng.
                                        </div>
                                        <% } %>

                                            <div
                                                style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px;">
                                                <div style="display: flex; gap: 10px;">
                                                    <a href="gdChinhKho.jsp" class="btn btn-secondary"
                                                        onclick="return confirm('Hủy phiếu nhập này?');">Hủy</a>
                                                    <form action="gdNhapPhuTung.jsp" method="POST" style="margin: 0;">
                                                        <input type="hidden" name="action" value="luuHoaDon" />
                                                        <button type="submit" class="btn btn-success"
                                                            <%=(hdn.getDsChiTietNhap()==null ||
                                                            hdn.getDsChiTietNhap().isEmpty()) ? "disabled" : "" %>>
                                                            Lưu Hóa Đơn
                                                        </button>
                                                    </form>
                                                </div>
                                            </div>
                </div>
            </body>

            </html>