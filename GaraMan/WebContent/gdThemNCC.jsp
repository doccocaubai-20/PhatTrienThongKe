<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="model.*, dao.*"%>
<%
    request.setCharacterEncoding("UTF-8");
    NVKho nvKho = (NVKho) session.getAttribute("nvKho");
    String errorMsg = null;

    if ("POST".equalsIgnoreCase(request.getMethod())) {
        NhaCungCap ncc = new NhaCungCap(0, request.getParameter("tenNCC"), request.getParameter("diaChi"), request.getParameter("soDienThoai"));
        ncc = new NhaCungCapDAO().themNhaCungCap(ncc);
        if (ncc != null && ncc.getId() > 0) {
            HoaDonNhap hdn = new HoaDonNhap();
            hdn.setNhaCungCap(ncc);
            hdn.setNvKho(nvKho);
            session.setAttribute("hoaDonNhap", hdn);
            response.sendRedirect("gdNhapPhuTung.jsp");
            return;
        }
        errorMsg = "Lưu nhà cung cấp thất bại!";
    }
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Thêm Nhà Cung Cấp - GaraMan</title>
</head>
<body>
    <div class="container" style="max-width: 550px;">
        <%@ include file="header.jsp" %>
        <h3>Thêm Mới Nhà Cung Cấp</h3>

        <% if (errorMsg != null) { %>
            <div style="background: #fee2e2; color: #991b1b; padding: 10px 14px; border-radius: 6px; margin-bottom: 16px;">
                <%= errorMsg %>
            </div>
        <% } %>

        <form action="gdThemNCC.jsp" method="POST">
            <div style="margin-bottom: 14px;">
                <label style="display: block; font-weight: 500; margin-bottom: 6px;">Tên nhà cung cấp (*):</label>
                <input type="text" name="tenNCC" class="form-control" style="width: 100%;" required />
            </div>

            <div style="margin-bottom: 14px;">
                <label style="display: block; font-weight: 500; margin-bottom: 6px;">Địa chỉ:</label>
                <input type="text" name="diaChi" class="form-control" style="width: 100%;" />
            </div>

            <div style="margin-bottom: 20px;">
                <label style="display: block; font-weight: 500; margin-bottom: 6px;">Số điện thoại (*):</label>
                <input type="text" name="soDienThoai" class="form-control" style="width: 100%;" required />
            </div>

            <div style="display: flex; gap: 10px;">
                <button type="submit" class="btn">Lưu và Tiếp tục</button>
                <a href="gdTimNCC.jsp" class="btn btn-secondary">Hủy</a>
            </div>
        </form>
    </div>
</body>
</html>
