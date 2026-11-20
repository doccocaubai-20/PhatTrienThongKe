package model;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class KhachHang extends ThanhVien {
    private static final long serialVersionUID = 1L;

    private List<Xe> dsXe;

    public KhachHang() {
        super();
        this.dsXe = new ArrayList<>();
    }

    public KhachHang(int id, String tenDangNhap, String matKhau, String hoTen, Date ngaySinh, String diaChi,
                     String soDienThoai, String email) {
        super(id, tenDangNhap, matKhau, hoTen, ngaySinh, diaChi, soDienThoai, email, "KhachHang");
        this.dsXe = new ArrayList<>();
    }

    public List<Xe> getDsXe() {
        return dsXe;
    }

    public void setDsXe(List<Xe> dsXe) {
        this.dsXe = dsXe;
    }
}
