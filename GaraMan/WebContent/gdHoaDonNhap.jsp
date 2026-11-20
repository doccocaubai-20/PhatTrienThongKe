<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.text.*, java.util.*, model.*, dao.*"%>
<%
    int id = Integer.parseInt(request.getParameter("id"));
    HoaDonNhap hdn = new HoaDonNhapDAO().getHoaDonNhapById(id);
    NumberFormat nf = NumberFormat.getCurrencyInstance(new Locale("vi", "VN"));
    SimpleDateFormat df = new SimpleDateFormat("dd/MM/yyyy HH:mm");
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Hóa Đơn Nhập Kho #<%= hdn.getId() %> - GaraMan</title>
    <style>
        @media print {
            .no-print { display: none !important; }
            body { background: white !important; margin: 0; padding: 0; }
            .container { box-shadow: none !important; border: none !important; }
        }
    </style>
</head>
<body>
    <div class="container" style="max-width: 800px;">
        <div class="no-print">
            <%@ include file="header.jsp" %>
            <div style="display: flex; justify-content: flex-end; gap: 10px; margin-bottom: 20px;">
                <button onclick="window.print()" class="btn btn-primary">In Hóa Đơn</button>
                <a href="gdTimNCC.jsp" class="btn btn-success">+ Lập phiếu mới</a>
                <a href="gdChinhKho.jsp" class="btn btn-secondary">Về Trang Chủ Kho</a>
            </div>
        </div>

        <div style="text-align: center; margin-bottom: 24px;">
            <h2 style="margin: 0; color: #1e293b;">HÓA ĐƠN NHẬP KHO</h2>
            <div style="color: #64748b; font-size: 14px; margin-top: 4px;">Số phiếu: HDN-<%= String.format("%04d", hdn.getId()) %></div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px;">
            <div class="info-box" style="margin: 0;">
                <strong>Nhà cung cấp:</strong> <%= hdn.getNhaCungCap().getTenNCC() %><br/>
                <strong>Địa chỉ:</strong> <%= hdn.getNhaCungCap().getDiaChi() %><br/>
                <strong>Điện thoại:</strong> <%= hdn.getNhaCungCap().getSoDienThoai() %>
            </div>
            <div class="info-box" style="margin: 0;">
                <strong>Thời gian:</strong> <%= hdn.getNgayGioNhap() != null ? df.format(hdn.getNgayGioNhap()) : "" %><br/>
                <strong>Thủ kho:</strong> <%= hdn.getNvKho() != null ? hdn.getNvKho().getHoTen() : "" %><br/>
                <strong>Trạng thái:</strong> <%= hdn.getTrangThaiThanhToan() %>
            </div>
        </div>

        <table class="data-table">
            <thead>
                <tr>
                    <th style="width: 40px; text-align: center;">STT</th>
                    <th>Tên phụ tùng</th>
                    <th style="width: 80px; text-align: center;">ĐVT</th>
                    <th style="width: 90px; text-align: right;">Số lượng</th>
                    <th style="width: 130px; text-align: right;">Đơn giá</th>
                    <th style="width: 140px; text-align: right;">Thành tiền</th>
                </tr>
            </thead>
            <tbody>
                <% if (hdn.getDsChiTietNhap() != null) { int stt = 1; for (ChiTietNhap ct : hdn.getDsChiTietNhap()) { %>
                <tr>
                    <td style="text-align: center;"><%= stt++ %></td>
                    <td><strong><%= ct.getPhuTung().getTenPhuTung() %></strong></td>
                    <td style="text-align: center;"><%= ct.getPhuTung().getDonViTinh() %></td>
                    <td style="text-align: right; font-weight: bold;"><%= ct.getSoLuongNhap() %></td>
                    <td style="text-align: right;"><%= nf.format(ct.getDonGiaNhap()) %></td>
                    <td style="text-align: right; font-weight: bold;"><%= nf.format(ct.getThanhTien()) %></td>
                </tr>
                <% } } %>
            </tbody>
            <tfoot>
                <tr style="background: #f8fafc;">
                    <td colspan="5" style="text-align: right; font-weight: bold; padding: 12px;">TỔNG CỘNG:</td>
                    <td style="text-align: right; font-weight: bold; color: #dc2626; font-size: 16px; padding: 12px;"><%= nf.format(hdn.getTongTien()) %></td>
                </tr>
            </tfoot>
        </table>

        <div style="display: grid; grid-template-columns: 1fr 1fr; text-align: center; margin-top: 40px;">
            <div>
                <strong>ĐẠI DIỆN NHÀ CUNG CẤP</strong><br/>
                <span style="font-size: 12px; color: #64748b;">(Ký, ghi rõ họ tên)</span>
                <div style="height: 60px;"></div>
                <strong><%= hdn.getNhaCungCap().getTenNCC() %></strong>
            </div>
            <div>
                <strong>THỦ KHO TIẾP NHẬN</strong><br/>
                <span style="font-size: 12px; color: #64748b;">(Ký, ghi rõ họ tên)</span>
                <div style="height: 60px;"></div>
                <strong><%= hdn.getNvKho() != null ? hdn.getNvKho().getHoTen() : "" %></strong>
            </div>
        </div>
    </div>
</body>
</html>
