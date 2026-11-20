package model;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class HoaDonNhap implements Serializable {
    private static final long serialVersionUID = 1L;

    private int id;
    private Date ngayGioNhap;
    private double tongTien;
    private String trangThaiThanhToan;
    private NhaCungCap nhaCungCap;
    private NVKho nvKho;
    private List<ChiTietNhap> dsChiTietNhap;

    public HoaDonNhap() {
        this.dsChiTietNhap = new ArrayList<>();
        this.ngayGioNhap = new Date();
        this.trangThaiThanhToan = "DaThanhToan";
        this.tongTien = 0;
    }

    public HoaDonNhap(int id, Date ngayGioNhap, NhaCungCap nhaCungCap, NVKho nvKho) {
        this.id = id;
        this.ngayGioNhap = ngayGioNhap != null ? ngayGioNhap : new Date();
        this.trangThaiThanhToan = "DaThanhToan";
        this.nhaCungCap = nhaCungCap;
        this.nvKho = nvKho;
        this.dsChiTietNhap = new ArrayList<>();
        this.tongTien = 0;
    }

    public void themChiTiet(ChiTietNhap ct) {
        if (this.dsChiTietNhap == null) {
            this.dsChiTietNhap = new ArrayList<>();
        }
        ct.setHoaDonNhap(this);
        this.dsChiTietNhap.add(ct);
        tinhTongTien();
    }

    public double tinhTongTien() {
        double tong = 0;
        if (this.dsChiTietNhap != null) {
            for (ChiTietNhap ct : this.dsChiTietNhap) {
                tong += ct.getThanhTien();
            }
        }
        this.tongTien = tong;
        return this.tongTien;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Date getNgayGioNhap() {
        return ngayGioNhap;
    }

    public void setNgayGioNhap(Date ngayGioNhap) {
        this.ngayGioNhap = ngayGioNhap;
    }

    public double getTongTien() {
        return tongTien;
    }

    public void setTongTien(double tongTien) {
        this.tongTien = tongTien;
    }

    public String getTrangThaiThanhToan() {
        return trangThaiThanhToan;
    }

    public void setTrangThaiThanhToan(String trangThaiThanhToan) {
        this.trangThaiThanhToan = trangThaiThanhToan;
    }

    public NhaCungCap getNhaCungCap() {
        return nhaCungCap;
    }

    public void setNhaCungCap(NhaCungCap nhaCungCap) {
        this.nhaCungCap = nhaCungCap;
    }

    public NVKho getNvKho() {
        return nvKho;
    }

    public void setNvKho(NVKho nvKho) {
        this.nvKho = nvKho;
    }

    public List<ChiTietNhap> getDsChiTietNhap() {
        return dsChiTietNhap;
    }

    public void setDsChiTietNhap(List<ChiTietNhap> dsChiTietNhap) {
        this.dsChiTietNhap = dsChiTietNhap;
        tinhTongTien();
    }
}
