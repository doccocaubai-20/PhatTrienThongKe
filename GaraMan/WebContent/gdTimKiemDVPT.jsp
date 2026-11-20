<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.text.*, java.util.*, model.*, dao.*"%>
<%
    request.setCharacterEncoding("UTF-8");
    String tuKhoa = request.getParameter("tuKhoa");
    boolean daTimKiem = (tuKhoa != null && !tuKhoa.trim().isEmpty());

    ArrayList<DichVu> dsDV = daTimKiem ? new DichVuDAO().getDichVuTheoTen(tuKhoa.trim()) : null;
    ArrayList<PhuTung> dsPT = daTimKiem ? new PhuTungDAO().getPhuTungTheoTen(tuKhoa.trim()) : null;
    NumberFormat nf = NumberFormat.getCurrencyInstance(new Locale("vi", "VN"));
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Tra Cứu Dịch Vụ & Phụ Tùng - GaraMan</title>
</head>
<body>
    <div class="container">
        <%@ include file="header.jsp" %>
        <h3>Tra Cứu Dịch Vụ & Phụ Tùng</h3>

        <form action="gdTimKiemDVPT.jsp" method="GET" style="margin-bottom: 24px;">
            <div style="display: flex; gap: 10px;">
                <input type="text" name="tuKhoa" class="form-control" style="width: 380px;" 
                       placeholder="Nhập tên dịch vụ hoặc phụ tùng cần tìm..." value="<%= tuKhoa != null ? tuKhoa : "" %>" required />
                <button type="submit" class="btn btn-primary">Tìm kiếm</button>
            </div>
        </form>

        <% if (daTimKiem) { %>
            <h4 style="margin: 20px 0 10px 0;">1. Danh Mục Dịch Vụ</h4>
            <% if (dsDV != null && !dsDV.isEmpty()) { %>
            <table class="data-table">
                <thead>
                    <tr>
                        <th style="width: 50px; text-align: center;">STT</th>
                        <th>Tên dịch vụ</th>
                        <th>Loại dịch vụ</th>
                        <th style="width: 140px; text-align: right;">Đơn giá</th>
                        <th style="width: 110px; text-align: center;">Thao tác</th>
                    </tr>
                </thead>
                <tbody>
                    <% int stt = 1; for (DichVu dv : dsDV) { %>
                    <tr>
                        <td style="text-align: center;"><%= stt++ %></td>
                        <td><strong><%= dv.getTenDichVu() %></strong></td>
                        <td><%= dv.getLoaiDichVu() %></td>
                        <td style="text-align: right;"><%= nf.format(dv.getDonGia()) %></td>
                        <td style="text-align: center;">
                            <a href="gdChiTietDichVu.jsp?id=<%= dv.getId() %>&lastKeyword=<%= tuKhoa %>" class="btn btn-primary" style="padding: 4px 10px; font-size: 13px;">Chi tiết</a>
                        </td>
                    </tr>
                    <% } %>
                </tbody>
            </table>
            <% } else { %>
                <div style="color: #dc2626; padding: 12px;">Không tìm thấy dịch vụ nào phù hợp với "<%= tuKhoa %>".</div>
            <% } %>

            <h4 style="margin: 28px 0 10px 0;">2. Danh Mục Phụ Tùng</h4>
            <% if (dsPT != null && !dsPT.isEmpty()) { %>
            <table class="data-table">
                <thead>
                    <tr>
                        <th style="width: 50px; text-align: center;">STT</th>
                        <th>Tên phụ tùng</th>
                        <th>Hãng sản xuất</th>
                        <th style="width: 80px; text-align: center;">ĐVT</th>
                        <th style="width: 140px; text-align: right;">Giá niêm yết</th>
                        <th style="width: 90px; text-align: center;">Tồn kho</th>
                        <th style="width: 110px; text-align: center;">Thao tác</th>
                    </tr>
                </thead>
                <tbody>
                    <% int stt = 1; for (PhuTung pt : dsPT) { %>
                    <tr>
                        <td style="text-align: center;"><%= stt++ %></td>
                        <td><strong><%= pt.getTenPhuTung() %></strong></td>
                        <td><%= pt.getHangSanXuat() %></td>
                        <td style="text-align: center;"><%= pt.getDonViTinh() %></td>
                        <td style="text-align: right;"><%= nf.format(pt.getDonGiaNiemYet()) %></td>
                        <td style="text-align: center; font-weight: bold;"><%= pt.getSoLuongTon() %></td>
                        <td style="text-align: center;">
                            <a href="gdChiTietPhuTung.jsp?id=<%= pt.getId() %>&lastKeyword=<%= tuKhoa %>" class="btn btn-primary" style="padding: 4px 10px; font-size: 13px;">Chi tiết</a>
                        </td>
                    </tr>
                    <% } %>
                </tbody>
            </table>
            <% } else { %>
                <div style="color: #dc2626; padding: 12px;">Không tìm thấy phụ tùng nào phù hợp với "<%= tuKhoa %>".</div>
            <% } %>
        <% } else { %>
            <div style="text-align: center; color: #64748b; padding: 40px; border: 1px dashed #cbd5e1; border-radius: 6px; margin-top: 20px;">
                Vui lòng nhập từ khóa vào ô phía trên và nhấn <strong>Tìm kiếm</strong> để xem danh sách dịch vụ & phụ tùng.
            </div>
        <% } %>

        <div style="margin-top: 20px;">
            <a href="gdChinhKH.jsp" class="btn btn-secondary">Quay lại</a>
        </div>
    </div>
</body>
</html>
