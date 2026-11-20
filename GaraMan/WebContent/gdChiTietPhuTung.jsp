<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.text.*, java.util.*, model.*, dao.*"%>
<%
    int id = Integer.parseInt(request.getParameter("id"));
    String lastKeyword = request.getParameter("lastKeyword");
    PhuTung pt = new PhuTungDAO().getPhuTungById(id);
    NumberFormat nf = NumberFormat.getCurrencyInstance(new Locale("vi", "VN"));
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Chi Tiết Phụ Tùng - GaraMan</title>
</head>
<body>
    <div class="container" style="max-width: 650px;">
        <%@ include file="header.jsp" %>
        <h3>Chi Tiết Phụ Tùng</h3>
        <table class="data-table">
            <tr>
                <th style="width: 160px;">Tên phụ tùng</th>
                <td><strong><%= pt.getTenPhuTung() %></strong></td>
            </tr>
            <tr>
                <th>Hãng sản xuất</th>
                <td><%= pt.getHangSanXuat() %></td>
            </tr>
            <tr>
                <th>Đơn vị tính</th>
                <td><%= pt.getDonViTinh() %></td>
            </tr>
            <tr>
                <th>Giá bán niêm yết</th>
                <td style="color: #2563eb; font-weight: bold; font-size: 16px;"><%= nf.format(pt.getDonGiaNiemYet()) %></td>
            </tr>
            <tr>
                <th>Số lượng tồn kho</th>
                <td style="font-weight: bold;"><%= pt.getSoLuongTon() %></td>
            </tr>
        </table>
        <div style="margin-top: 20px;">
            <a href="gdTimKiemDVPT.jsp?tuKhoa=<%= lastKeyword != null ? lastKeyword : "" %>" class="btn btn-secondary">Quay lại</a>
        </div>
    </div>
</body>
</html>
