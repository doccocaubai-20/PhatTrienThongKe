<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.text.*, java.util.*, model.*, dao.*"%>
<%
    request.setCharacterEncoding("UTF-8");
    HoaDonNhap hdn = (HoaDonNhap) session.getAttribute("hoaDonNhap");
    int idPhuTung = Integer.parseInt(request.getParameter("idPhuTung"));
    PhuTung pt = new PhuTungDAO().getPhuTungById(idPhuTung);

    String errorMsg = null;
    if ("POST".equalsIgnoreCase(request.getMethod())) {
        try {
            int sl = Integer.parseInt(request.getParameter("soLuongNhap"));
            double gia = Double.parseDouble(request.getParameter("donGiaNhap"));
            ChiTietNhap ctn = new ChiTietNhap(0, sl, gia, pt, hdn);
            ctn.tinhThanhTien();
            hdn.themChiTiet(ctn);
            response.sendRedirect("gdNhapPhuTung.jsp");
            return;
        } catch (Exception e) {
            errorMsg = "Số lượng và giá phải là số hợp lệ!";
        }
    }
    NumberFormat nf = NumberFormat.getCurrencyInstance(new Locale("vi", "VN"));
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Nhập Số Lượng & Giá - GaraMan</title>
    <script>
        function tinhThanhTien() {
            var sl = parseFloat(document.getElementById("soLuongNhap").value) || 0;
            var gia = parseFloat(document.getElementById("donGiaNhap").value) || 0;
            document.getElementById("thanhTienText").innerText = new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(sl * gia);
        }
    </script>
</head>
<body>
    <div class="container" style="max-width: 550px;">
        <%@ include file="header.jsp" %>
        <h3>Nhập Số Lượng & Giá Nhập</h3>

        <% if (errorMsg != null) { %>
            <div style="background: #fee2e2; color: #991b1b; padding: 10px 14px; border-radius: 6px; margin-bottom: 16px;">
                <%= errorMsg %>
            </div>
        <% } %>

        <div class="info-box">
            <strong>Phụ tùng:</strong> <%= pt.getTenPhuTung() %> (<%= pt.getHangSanXuat() %>)<br/>
            <strong>Đơn vị tính:</strong> <%= pt.getDonViTinh() %> | <strong>Tồn kho:</strong> <%= pt.getSoLuongTon() %>
        </div>

        <form action="gdNhapSoLuongGia.jsp?idPhuTung=<%= pt.getId() %>" method="POST">
            <div style="margin-bottom: 14px;">
                <label style="display: block; font-weight: 500; margin-bottom: 6px;">Số lượng nhập (*):</label>
                <input type="number" id="soLuongNhap" name="soLuongNhap" class="form-control" style="width: 100%;" min="1" oninput="tinhThanhTien()" required autofocus />
            </div>

            <div style="margin-bottom: 14px;">
                <label style="display: block; font-weight: 500; margin-bottom: 6px;">Đơn giá nhập từ NCC (*):</label>
                <input type="number" id="donGiaNhap" step="1000" name="donGiaNhap" class="form-control" style="width: 100%;" min="1000" oninput="tinhThanhTien()" required />
            </div>

            <div style="margin-bottom: 20px; padding: 10px; background: #f0fdf4; border-radius: 6px;">
                <strong>Thành tiền dự tính: </strong>
                <span id="thanhTienText" style="font-size: 16px; font-weight: bold; color: #16a34a;">0 ₫</span>
            </div>

            <div style="display: flex; gap: 10px;">
                <button type="submit" class="btn btn-primary">Thêm vào phiếu</button>
                <a href="gdTimPhuTung.jsp" class="btn btn-secondary">Hủy</a>
            </div>
        </form>
    </div>
</body>
</html>
