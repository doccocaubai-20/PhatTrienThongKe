package model;

import java.util.Date;

public class NVKho extends NhanVien {
    private static final long serialVersionUID = 1L;

    public NVKho() {
        super();
        setVaiTro("NVKho");
    }

    public NVKho(int id, String tenDangNhap, String matKhau, String hoTen, Date ngaySinh, String diaChi,
                 String soDienThoai, String email, String viTri, float heSoLuong) {
        super(id, tenDangNhap, matKhau, hoTen, ngaySinh, diaChi, soDienThoai, email, "NVKho", viTri, heSoLuong);
    }
}
