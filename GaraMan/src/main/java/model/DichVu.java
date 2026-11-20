package model;

import java.io.Serializable;

public class DichVu implements Serializable {
    private static final long serialVersionUID = 1L;

    private int id;
    private String tenDichVu;
    private String loaiDichVu;
    private double donGia;
    private String thoiGianBaoHanh;

    public DichVu() {
    }

    public DichVu(int id, String tenDichVu, String loaiDichVu, double donGia, String thoiGianBaoHanh) {
        this.id = id;
        this.tenDichVu = tenDichVu;
        this.loaiDichVu = loaiDichVu;
        this.donGia = donGia;
        this.thoiGianBaoHanh = thoiGianBaoHanh;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTenDichVu() {
        return tenDichVu;
    }

    public void setTenDichVu(String tenDichVu) {
        this.tenDichVu = tenDichVu;
    }

    public String getLoaiDichVu() {
        return loaiDichVu;
    }

    public void setLoaiDichVu(String loaiDichVu) {
        this.loaiDichVu = loaiDichVu;
    }

    public double getDonGia() {
        return donGia;
    }

    public void setDonGia(double donGia) {
        this.donGia = donGia;
    }

    public String getThoiGianBaoHanh() {
        return thoiGianBaoHanh;
    }

    public void setThoiGianBaoHanh(String thoiGianBaoHanh) {
        this.thoiGianBaoHanh = thoiGianBaoHanh;
    }
}
