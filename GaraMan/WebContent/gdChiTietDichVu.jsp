<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.text.*, java.util.*, model.*, dao.*"%>
<%
    int id = Integer.parseInt(request.getParameter("id"));
    String lastKeyword = request.getParameter("lastKeyword");
    DichVu dv = new DichVuDAO().getDichVuById(id);
    NumberFormat nf = NumberFormat.getCurrencyInstance(new Locale("vi", "VN"));
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Chi Tiết Dịch Vụ - GaraMan</title>
</head>
<body>
    <div class="container" style="max-width: 650px;">
        <%@ include file="header.jsp" %>
        <h3>Chi Tiết Dịch Vụ</h3>
        <table class="data-table">
            <tr>
                <th style="width: 160px;">Tên dịch vụ</th>
                <td><strong><%= dv.getTenDichVu() %></strong></td>
            </tr>
            <tr>
                <th>Phân loại</th>
                <td><%= dv.getLoaiDichVu() %></td>
            </tr>
            <tr>
                <th>Đơn giá</th>
                <td style="color: #2563eb; font-weight: bold; font-size: 16px;"><%= nf.format(dv.getDonGia()) %></td>
            </tr>
            <tr>
                <th>Bảo hành</th>
                <td><%= dv.getThoiGianBaoHanh() %></td>
            </tr>
        </table>
        <div style="margin-top: 20px;">
            <a href="gdTimKiemDVPT.jsp?tuKhoa=<%= lastKeyword != null ? lastKeyword : "" %>" class="btn btn-secondary">Quay lại</a>
        </div>
    </div>
</body>
</html>
