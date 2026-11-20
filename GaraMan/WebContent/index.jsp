<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <title>GaraMan - Trang chủ</title>
    </head>

    <body>
        <div class="container">
            <%@ include file="header.jsp" %>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 24px;">
                    <div
                        style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 24px; text-align: center; background: #ffffff;">
                        <h3 style="border: none; margin-bottom: 12px">Khách Hàng</h3>
                        <a href="gdChinhKH.jsp" class="btn btn-primary" style="padding: 10px 24px;">Vào Trang Khách
                            Hàng</a>
                    </div>

                    <div
                        style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 24px; text-align: center; background: #ffffff;">
                        <h3 style="border: none; margin-bottom: 12px">Nhân viên Kho</h3>
                        <a href="gdChinhKho.jsp" class="btn btn-success" style="padding: 10px 24px;">Vào Quản Lý Kho</a>
                    </div>
                </div>
        </div>
    </body>

    </html>