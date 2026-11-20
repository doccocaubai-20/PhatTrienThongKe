package model;

import java.util.Date;

public class NhanVien extends ThanhVien {
    private static final long serialVersionUID = 1L;

    private String viTri;
    private float heSoLuong;

    public NhanVien() {
        super();
    }

    public NhanVien(int id, String tenDangNhap, String matKhau, String hoTen, Date ngaySinh, String diaChi,
                    String soDienThoai, String email, String vaiTro, String viTri, float heSoLuong) {
        super(id, tenDangNhap, matKhau, hoTen, ngaySinh, diaChi, soDienThoai, email, vaiTro);
        this.viTri = viTri;
        this.heSoLuong = heSoLuong;
    }

    public String getViTri() {
        return viTri;
    }

    public void setViTri(String viTri) {
        this.viTri = viTri;
    }

    public float getHeSoLuong() {
        return heSoLuong;
    }

    public void setHeSoLuong(float heSoLuong) {
        this.heSoLuong = heSoLuong;
    }
}
