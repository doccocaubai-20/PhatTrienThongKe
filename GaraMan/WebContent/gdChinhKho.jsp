<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="model.*"%>
<%
    NVKho nvKho = (NVKho) session.getAttribute("nvKho");
    if (nvKho == null) {
        nvKho = new NVKho(1, "nvkho1", "123456", "Lê Hoàng Kho", null, "12 Giải Phóng, Hà Nội", "0901234567", "nvkho@garaman.vn", "Thủ kho trưởng", 2.8f);
        session.setAttribute("nvKho", nvKho);
    }
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Quản Lý Kho - GaraMan</title>
</head>
<body>
    <div class="container">
        <%@ include file="header.jsp" %>
        <div class="info-box">
            <strong>Nhân viên kho:</strong> <%= nvKho.getHoTen() %> | 
            <strong>Vị trí:</strong> <%= nvKho.getViTri() %> | 
            <strong>SĐT:</strong> <%= nvKho.getSoDienThoai() %>
        </div>
        <div style="margin: 24px 0;">
            <a href="gdTimNCC.jsp" class="btn" style="font-size: 15px; padding: 12px 24px;">
                Nhập phụ tùng từ Nhà cung cấp
            </a>
        </div>
    </div>
</body>
</html>
