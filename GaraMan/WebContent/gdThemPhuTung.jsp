<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="model.*, dao.*"%>
<%
    request.setCharacterEncoding("UTF-8");
    String errorMsg = null;
    if ("POST".equalsIgnoreCase(request.getMethod())) {
        try {
            PhuTung pt = new PhuTung(0, request.getParameter("tenPhuTung"), request.getParameter("hangSanXuat"),
                request.getParameter("donViTinh"), Double.parseDouble(request.getParameter("donGiaNiemYet")), 0);
            pt = new PhuTungDAO().themPhuTung(pt);
            if (pt != null && pt.getId() > 0) {
                response.sendRedirect("gdNhapSoLuongGia.jsp?idPhuTung=" + pt.getId());
                return;
            }
            errorMsg = "Lưu phụ tùng thất bại!";
        } catch (Exception e) {
            errorMsg = "Dữ liệu không hợp lệ!";
        }
    }
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Thêm Phụ Tùng Mới - GaraMan</title>
</head>
<body>
    <div class="container" style="max-width: 550px;">
        <%@ include file="header.jsp" %>
        <h3>Thêm Phụ Tùng Mới</h3>

        <% if (errorMsg != null) { %>
            <div style="background: #fee2e2; color: #991b1b; padding: 10px 14px; border-radius: 6px; margin-bottom: 16px;">
                <%= errorMsg %>
            </div>
        <% } %>

        <form action="gdThemPhuTung.jsp" method="POST">
            <div style="margin-bottom: 14px;">
                <label style="display: block; font-weight: 500; margin-bottom: 6px;">Tên phụ tùng (*):</label>
                <input type="text" name="tenPhuTung" class="form-control" style="width: 100%;" required />
            </div>

            <div style="margin-bottom: 14px;">
                <label style="display: block; font-weight: 500; margin-bottom: 6px;">Hãng sản xuất (*):</label>
                <input type="text" name="hangSanXuat" class="form-control" style="width: 100%;" required />
            </div>

            <div style="margin-bottom: 14px;">
                <label style="display: block; font-weight: 500; margin-bottom: 6px;">Đơn vị tính (*):</label>
                <input type="text" name="donViTinh" class="form-control" style="width: 100%;" placeholder="Cái, Bộ, Can, Lít..." required />
            </div>

            <div style="margin-bottom: 20px;">
                <label style="display: block; font-weight: 500; margin-bottom: 6px;">Đơn giá niêm yết (*):</label>
                <input type="number" step="1000" name="donGiaNiemYet" class="form-control" style="width: 100%;" required />
            </div>

            <div style="display: flex; gap: 10px;">
                <button type="submit" class="btn btn-success">Lưu và Nhập Giá</button>
                <a href="gdTimPhuTung.jsp" class="btn btn-secondary">Hủy</a>
            </div>
        </form>
    </div>
</body>
</html>
