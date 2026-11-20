package model;

import java.io.Serializable;

public class PhuTung implements Serializable {
    private static final long serialVersionUID = 1L;

    private int id;
    private String tenPhuTung;
    private String hangSanXuat;
    private String donViTinh;
    private double donGiaNiemYet;
    private int soLuongTon;

    public PhuTung() {
    }

    public PhuTung(int id, String tenPhuTung, String hangSanXuat, String donViTinh, double donGiaNiemYet, int soLuongTon) {
        this.id = id;
        this.tenPhuTung = tenPhuTung;
        this.hangSanXuat = hangSanXuat;
        this.donViTinh = donViTinh;
        this.donGiaNiemYet = donGiaNiemYet;
        this.soLuongTon = soLuongTon;
    }

    public boolean capNhatTonKho(int soLuongTang) {
        this.soLuongTon += soLuongTang;
        return true;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTenPhuTung() {
        return tenPhuTung;
    }

    public void setTenPhuTung(String tenPhuTung) {
        this.tenPhuTung = tenPhuTung;
    }

    public String getHangSanXuat() {
        return hangSanXuat;
    }

    public void setHangSanXuat(String hangSanXuat) {
        this.hangSanXuat = hangSanXuat;
    }

    public String getDonViTinh() {
        return donViTinh;
    }

    public void setDonViTinh(String donViTinh) {
        this.donViTinh = donViTinh;
    }

    public double getDonGiaNiemYet() {
        return donGiaNiemYet;
    }

    public void setDonGiaNiemYet(double donGiaNiemYet) {
        this.donGiaNiemYet = donGiaNiemYet;
    }

    public int getSoLuongTon() {
        return soLuongTon;
    }

    public void setSoLuongTon(int soLuongTon) {
        this.soLuongTon = soLuongTon;
    }
}
