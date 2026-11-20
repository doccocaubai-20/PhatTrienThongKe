package model;

import java.io.Serializable;

public class NhaCungCap implements Serializable {
    private static final long serialVersionUID = 1L;

    private int id;
    private String tenNCC;
    private String diaChi;
    private String soDienThoai;

    public NhaCungCap() {
    }

    public NhaCungCap(int id, String tenNCC, String diaChi, String soDienThoai) {
        this.id = id;
        this.tenNCC = tenNCC;
        this.diaChi = diaChi;
        this.soDienThoai = soDienThoai;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTenNCC() {
        return tenNCC;
    }

    public void setTenNCC(String tenNCC) {
        this.tenNCC = tenNCC;
    }

    public String getDiaChi() {
        return diaChi;
    }

    public void setDiaChi(String diaChi) {
        this.diaChi = diaChi;
    }

    public String getSoDienThoai() {
        return soDienThoai;
    }

    public void setSoDienThoai(String soDienThoai) {
        this.soDienThoai = soDienThoai;
    }
}
