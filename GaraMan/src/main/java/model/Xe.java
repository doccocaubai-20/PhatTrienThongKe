package model;

import java.io.Serializable;

public class Xe implements Serializable {
    private static final long serialVersionUID = 1L;

    private int id;
    private String bienSoXe;
    private String hangXe;
    private String dongXe;
    private String mauSon;
    private KhachHang khachHang;

    public Xe() {
    }

    public Xe(int id, String bienSoXe, String hangXe, String dongXe, String mauSon, KhachHang khachHang) {
        this.id = id;
        this.bienSoXe = bienSoXe;
        this.hangXe = hangXe;
        this.dongXe = dongXe;
        this.mauSon = mauSon;
        this.khachHang = khachHang;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getBienSoXe() {
        return bienSoXe;
    }

    public void setBienSoXe(String bienSoXe) {
        this.bienSoXe = bienSoXe;
    }

    public String getHangXe() {
        return hangXe;
    }

    public void setHangXe(String hangXe) {
        this.hangXe = hangXe;
    }

    public String getDongXe() {
        return dongXe;
    }

    public void setDongXe(String dongXe) {
        this.dongXe = dongXe;
    }

    public String getMauSon() {
        return mauSon;
    }

    public void setMauSon(String mauSon) {
        this.mauSon = mauSon;
    }

    public KhachHang getKhachHang() {
        return khachHang;
    }

    public void setKhachHang(KhachHang khachHang) {
        this.khachHang = khachHang;
    }
}
