<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.*, model.*, dao.*"%>
<%
    request.setCharacterEncoding("UTF-8");
    NVKho nvKho = (NVKho) session.getAttribute("nvKho");
    if (nvKho == null) {
        nvKho = new NVKho(1, "nvkho1", "123456", "Lê Hoàng Kho", null, "12 Giải Phóng, Hà Nội", "0901234567", "nvkho@garaman.vn", "Thủ kho trưởng", 2.8f);
        session.setAttribute("nvKho", nvKho);
    }

    NhaCungCapDAO nccDAO = new NhaCungCapDAO();
    if ("chon".equals(request.getParameter("action"))) {
        int idNCC = Integer.parseInt(request.getParameter("idNCC"));
        for (NhaCungCap n : nccDAO.getNhaCungCapTheoTen("")) {
            if (n.getId() == idNCC) {
                HoaDonNhap hdn = new HoaDonNhap();
                hdn.setNhaCungCap(n);
                hdn.setNvKho(nvKho);
                session.setAttribute("hoaDonNhap", hdn);
                response.sendRedirect("gdNhapPhuTung.jsp");
                return;
            }
        }
    }

    String tuKhoa = request.getParameter("txtTenNCC");
    boolean daTim = (tuKhoa != null && !tuKhoa.trim().isEmpty());
    ArrayList<NhaCungCap> dsNCC = daTim ? nccDAO.getNhaCungCapTheoTen(tuKhoa.trim()) : null;
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Tìm Nhà Cung Cấp - GaraMan</title>
</head>
<body>
    <div class="container">
        <%@ include file="header.jsp" %>
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-bottom: 16px;">
            <h3 style="margin: 0; border: none; padding: 0;">Tìm Nhà Cung Cấp</h3>
            <a href="gdThemNCC.jsp" class="btn btn-success">+ Thêm mới NCC</a>
        </div>

        <form action="gdTimNCC.jsp" method="GET" style="margin-bottom: 20px;">
            <div style="display: flex; gap: 10px;">
                <input type="text" name="txtTenNCC" class="form-control" style="width: 380px;" 
                       placeholder="Nhập tên nhà cung cấp cần tìm..." value="<%= tuKhoa != null ? tuKhoa : "" %>" required />
                <button type="submit" class="btn btn-primary">Tìm kiếm</button>
            </div>
        </form>

        <% if (daTim) { %>
            <% if (dsNCC != null && !dsNCC.isEmpty()) { %>
            <table class="data-table">
                <thead>
                    <tr>
                        <th style="width: 50px; text-align: center;">STT</th>
                        <th>Tên nhà cung cấp</th>
                        <th>Địa chỉ</th>
                        <th style="width: 140px;">Điện thoại</th>
                        <th style="width: 100px; text-align: center;">Thao tác</th>
                    </tr>
                </thead>
                <tbody>
                    <% int stt = 1; for (NhaCungCap ncc : dsNCC) { %>
                    <tr>
                        <td style="text-align: center;"><%= stt++ %></td>
                        <td><strong><%= ncc.getTenNCC() %></strong></td>
                        <td><%= ncc.getDiaChi() %></td>
                        <td><%= ncc.getSoDienThoai() %></td>
                        <td style="text-align: center;">
                            <a href="gdTimNCC.jsp?action=chon&idNCC=<%= ncc.getId() %>" class="btn btn-primary" style="padding: 4px 12px; font-size: 13px;">Chọn</a>
                        </td>
                    </tr>
                    <% } %>
                </tbody>
            </table>
            <% } else { %>
            <div style="text-align: center; color: #dc2626; padding: 25px; border: 1px dashed #fca5a5; border-radius: 6px; margin: 20px 0;">
                Không tìm thấy nhà cung cấp nào phù hợp với "<%= tuKhoa %>".<br/>
                <a href="gdThemNCC.jsp" class="btn btn-success" style="margin-top: 10px;">Thêm mới nhà cung cấp</a>
            </div>
            <% } %>
        <% } else { %>
            <div style="text-align: center; color: #64748b; padding: 35px; border: 1px dashed #cbd5e1; border-radius: 6px; margin-top: 20px;">
                Vui lòng nhập tên nhà cung cấp vào ô trên và nhấn <strong>Tìm kiếm</strong>.
            </div>
        <% } %>

        <div style="margin-top: 20px;">
            <a href="gdChinhKho.jsp" class="btn btn-secondary">Quay lại</a>
        </div>
    </div>
</body>
</html>
