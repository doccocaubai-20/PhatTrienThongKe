package model;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class LichHen implements Serializable {
    private static final long serialVersionUID = 1L;

    private int id;
    private Date thoiGianHen;
    private String trangThai;
    private KhachHang khachHang;
    private Xe xe;
    private List<DichVu> dsDV;

    public LichHen() {
        this.dsDV = new ArrayList<>();
    }

    public LichHen(int id, Date thoiGianHen, String trangThai, KhachHang khachHang, Xe xe) {
        this.id = id;
        this.thoiGianHen = thoiGianHen;
        this.trangThai = trangThai;
        this.khachHang = khachHang;
        this.xe = xe;
        this.dsDV = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Date getThoiGianHen() {
        return thoiGianHen;
    }

    public void setThoiGianHen(Date thoiGianHen) {
        this.thoiGianHen = thoiGianHen;
    }

    public String getTrangThai() {
        return trangThai;
    }

    public void setTrangThai(String trangThai) {
        this.trangThai = trangThai;
    }

    public KhachHang getKhachHang() {
        return khachHang;
    }

    public void setKhachHang(KhachHang khachHang) {
        this.khachHang = khachHang;
    }

    public Xe getXe() {
        return xe;
    }

    public void setXe(Xe xe) {
        this.xe = xe;
    }

    public List<DichVu> getDsDV() {
        return dsDV;
    }

    public void setDsDV(List<DichVu> dsDV) {
        this.dsDV = dsDV;
    }
}
