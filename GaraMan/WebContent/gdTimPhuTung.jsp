<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.text.*, java.util.*, model.*, dao.*"%>
<%
    request.setCharacterEncoding("UTF-8");
    HoaDonNhap hdn = (HoaDonNhap) session.getAttribute("hoaDonNhap");
    if (hdn == null) { response.sendRedirect("gdTimNCC.jsp"); return; }

    String tuKhoa = request.getParameter("txtTenPT");
    boolean daTim = (tuKhoa != null && !tuKhoa.trim().isEmpty());
    ArrayList<PhuTung> dsPhuTung = daTim ? new PhuTungDAO().getPhuTungTheoTen(tuKhoa.trim()) : null;
    NumberFormat nf = NumberFormat.getCurrencyInstance(new Locale("vi", "VN"));
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Tìm Phụ Tùng Nhập Kho - GaraMan</title>
</head>
<body>
    <div class="container">
        <%@ include file="header.jsp" %>
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-bottom: 16px;">
            <h3 style="margin: 0; border: none; padding: 0;">Tìm Phụ Tùng Nhập Kho</h3>
            <a href="gdThemPhuTung.jsp" class="btn btn-success">+ Thêm phụ tùng mới</a>
        </div>

        <form action="gdTimPhuTung.jsp" method="GET" style="margin-bottom: 20px;">
            <div style="display: flex; gap: 10px;">
                <input type="text" name="txtTenPT" class="form-control" style="width: 380px;" 
                       placeholder="Nhập tên phụ tùng cần tìm..." value="<%= tuKhoa != null ? tuKhoa : "" %>" required />
                <button type="submit" class="btn btn-primary">Tìm kiếm</button>
            </div>
        </form>

        <% if (daTim) { %>
            <% if (dsPhuTung != null && !dsPhuTung.isEmpty()) { %>
            <table class="data-table">
                <thead>
                    <tr>
                        <th style="width: 50px; text-align: center;">STT</th>
                        <th>Tên phụ tùng</th>
                        <th>Hãng sản xuất</th>
                        <th style="width: 80px; text-align: center;">ĐVT</th>
                        <th style="width: 140px; text-align: right;">Giá niêm yết</th>
                        <th style="width: 90px; text-align: center;">Tồn kho</th>
                        <th style="width: 100px; text-align: center;">Thao tác</th>
                    </tr>
                </thead>
                <tbody>
                    <% int stt = 1; for (PhuTung pt : dsPhuTung) { %>
                    <tr>
                        <td style="text-align: center;"><%= stt++ %></td>
                        <td><strong><%= pt.getTenPhuTung() %></strong></td>
                        <td><%= pt.getHangSanXuat() %></td>
                        <td style="text-align: center;"><%= pt.getDonViTinh() %></td>
                        <td style="text-align: right;"><%= nf.format(pt.getDonGiaNiemYet()) %></td>
                        <td style="text-align: center; font-weight: bold;"><%= pt.getSoLuongTon() %></td>
                        <td style="text-align: center;">
                            <a href="gdNhapSoLuongGia.jsp?idPhuTung=<%= pt.getId() %>" class="btn btn-primary" style="padding: 4px 12px; font-size: 13px;">Chọn</a>
                        </td>
                    </tr>
                    <% } %>
                </tbody>
            </table>
            <% } else { %>
            <div style="text-align: center; color: #dc2626; padding: 25px; border: 1px dashed #fca5a5; border-radius: 6px; margin: 20px 0;">
                Không tìm thấy phụ tùng nào phù hợp với "<%= tuKhoa %>".<br/>
                <a href="gdThemPhuTung.jsp" class="btn btn-success" style="margin-top: 10px;">Thêm mới phụ tùng này</a>
            </div>
            <% } %>
        <% } %>

        <div style="margin-top: 20px;">
            <a href="gdNhapPhuTung.jsp" class="btn btn-secondary">Quay lại phiếu nhập</a>
        </div>
    </div>
</body>
</html>
