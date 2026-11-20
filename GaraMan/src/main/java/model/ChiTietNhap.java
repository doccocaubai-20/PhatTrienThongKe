package model;

import java.io.Serializable;

public class ChiTietNhap implements Serializable {
    private static final long serialVersionUID = 1L;

    private int id;
    private int soLuongNhap;
    private double donGiaNhap;
    private double thanhTien;
    private PhuTung phuTung;
    private HoaDonNhap hoaDonNhap;

    public ChiTietNhap() {
    }

    public ChiTietNhap(int id, int soLuongNhap, double donGiaNhap, PhuTung phuTung, HoaDonNhap hoaDonNhap) {
        this.id = id;
        this.soLuongNhap = soLuongNhap;
        this.donGiaNhap = donGiaNhap;
        this.phuTung = phuTung;
        this.hoaDonNhap = hoaDonNhap;
        this.thanhTien = tinhThanhTien();
    }

    public double tinhThanhTien() {
        this.thanhTien = this.soLuongNhap * this.donGiaNhap;
        return this.thanhTien;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getSoLuongNhap() {
        return soLuongNhap;
    }

    public void setSoLuongNhap(int soLuongNhap) {
        this.soLuongNhap = soLuongNhap;
        tinhThanhTien();
    }

    public double getDonGiaNhap() {
        return donGiaNhap;
    }

    public void setDonGiaNhap(double donGiaNhap) {
        this.donGiaNhap = donGiaNhap;
        tinhThanhTien();
    }

    public double getThanhTien() {
        return thanhTien;
    }

    public void setThanhTien(double thanhTien) {
        this.thanhTien = thanhTien;
    }

    public PhuTung getPhuTung() {
        return phuTung;
    }

    public void setPhuTung(PhuTung phuTung) {
        this.phuTung = phuTung;
    }

    public HoaDonNhap getHoaDonNhap() {
        return hoaDonNhap;
    }

    public void setHoaDonNhap(HoaDonNhap hoaDonNhap) {
        this.hoaDonNhap = hoaDonNhap;
    }
}
