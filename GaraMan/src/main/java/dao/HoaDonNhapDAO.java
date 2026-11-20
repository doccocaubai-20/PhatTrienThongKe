package dao;

import java.sql.*;
import java.util.ArrayList;
import model.*;

public class HoaDonNhapDAO extends DAO {

    public HoaDonNhapDAO() {
        super();
    }

    public boolean luuHoaDonNhap(HoaDonNhap hdn) {
        if (hdn == null || hdn.getNhaCungCap() == null || hdn.getDsChiTietNhap() == null
                || hdn.getDsChiTietNhap().isEmpty()) {
            return false;
        }

        String sqlHD = "INSERT INTO tblHoaDonNhap (ngayGioNhap, tongTien, trangThaiThanhToan, tblNhaCungCapid, tblNVKhoid) VALUES (?, ?, ?, ?, ?)";
        String sqlCT = "INSERT INTO tblChiTietNhap (tblHoaDonNhapid, tblPhuTungid, soLuongNhap, donGiaNhap, thanhTien) VALUES (?, ?, ?, ?, ?)";
        String sqlKho = "UPDATE tblPhuTung SET soLuongTon = soLuongTon + ? WHERE id = ?";

        boolean autoCommitGoc = true;
        try {
            if (con == null || con.isClosed())
                con = getConnection();
            if (con == null)
                return false;

            autoCommitGoc = con.getAutoCommit();
            con.setAutoCommit(false);

            // 1. Lưu Hóa đơn
            PreparedStatement psHD = con.prepareStatement(sqlHD, Statement.RETURN_GENERATED_KEYS);
            Timestamp ts = hdn.getNgayGioNhap() != null ? new Timestamp(hdn.getNgayGioNhap().getTime())
                    : new Timestamp(System.currentTimeMillis());
            psHD.setTimestamp(1, ts);
            psHD.setDouble(2, hdn.getTongTien());
            psHD.setString(3, hdn.getTrangThaiThanhToan() != null ? hdn.getTrangThaiThanhToan() : "DaThanhToan");
            psHD.setInt(4, hdn.getNhaCungCap().getId());
            psHD.setInt(5, hdn.getNvKho() != null && hdn.getNvKho().getId() > 0 ? hdn.getNvKho().getId() : 1);
            psHD.executeUpdate();

            ResultSet rsHD = psHD.getGeneratedKeys();
            int hdnId = rsHD.next() ? rsHD.getInt(1) : 0;
            hdn.setId(hdnId);

            // 2. Lưu Chi tiết & Cập nhật tồn kho
            PreparedStatement psCT = con.prepareStatement(sqlCT, Statement.RETURN_GENERATED_KEYS);
            PreparedStatement psKho = con.prepareStatement(sqlKho);

            for (ChiTietNhap ct : hdn.getDsChiTietNhap()) {
                // Lưu dòng chi tiết
                psCT.setInt(1, hdnId);
                psCT.setInt(2, ct.getPhuTung().getId());
                psCT.setInt(3, ct.getSoLuongNhap());
                psCT.setDouble(4, ct.getDonGiaNhap());
                psCT.setDouble(5, ct.getThanhTien());
                psCT.executeUpdate();

                ResultSet rsCT = psCT.getGeneratedKeys();
                if (rsCT.next())
                    ct.setId(rsCT.getInt(1));

                // Tự động tăng số lượng tồn kho
                psKho.setInt(1, ct.getSoLuongNhap());
                psKho.setInt(2, ct.getPhuTung().getId());
                psKho.executeUpdate();
            }

            con.commit(); // THÀNH CÔNG -> COMMIT
            con.setAutoCommit(autoCommitGoc);
            return true;

        } catch (Exception e) {
            e.printStackTrace();
            try {
                if (con != null)
                    con.rollback();
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
            return false;
        }
    }

    public HoaDonNhap getHoaDonNhapById(int id) {
        String sqlHD = "SELECT hd.*, ncc.tenNCC, ncc.diaChi, ncc.soDienThoai, tv.hoTen as tenNV " +
                "FROM tblHoaDonNhap hd " +
                "JOIN tblNhaCungCap ncc ON hd.tblNhaCungCapid = ncc.id " +
                "JOIN tblThanhVien tv ON hd.tblNVKhoid = tv.id " +
                "WHERE hd.id = ?";
        String sqlCT = "SELECT ct.*, pt.tenPhuTung, pt.hangSanXuat, pt.donViTinh " +
                "FROM tblChiTietNhap ct " +
                "JOIN tblPhuTung pt ON ct.tblPhuTungid = pt.id " +
                "WHERE ct.tblHoaDonNhapid = ?";

        HoaDonNhap hdn = null;
        try {
            if (con == null || con.isClosed())
                con = getConnection();
            if (con != null) {
                PreparedStatement psHD = con.prepareStatement(sqlHD);
                psHD.setInt(1, id);
                ResultSet rsHD = psHD.executeQuery();

                if (rsHD.next()) {
                    hdn = new HoaDonNhap();
                    hdn.setId(rsHD.getInt("id"));
                    hdn.setNgayGioNhap(rsHD.getTimestamp("ngayGioNhap"));
                    hdn.setTongTien(rsHD.getDouble("tongTien"));
                    hdn.setTrangThaiThanhToan(rsHD.getString("trangThaiThanhToan"));

                    // Gán NCC
                    NhaCungCap ncc = new NhaCungCap(rsHD.getInt("tblNhaCungCapid"), rsHD.getString("tenNCC"),
                            rsHD.getString("diaChi"), rsHD.getString("soDienThoai"));
                    hdn.setNhaCungCap(ncc);

                    // Gán NV Kho
                    NVKho nv = new NVKho();
                    nv.setId(rsHD.getInt("tblNVKhoid"));
                    nv.setHoTen(rsHD.getString("tenNV"));
                    hdn.setNvKho(nv);

                    // Lấy danh sách chi tiết
                    PreparedStatement psCT = con.prepareStatement(sqlCT);
                    psCT.setInt(1, id);
                    ResultSet rsCT = psCT.executeQuery();
                    ArrayList<ChiTietNhap> dsCT = new ArrayList<>();

                    while (rsCT.next()) {
                        ChiTietNhap ct = new ChiTietNhap();
                        ct.setId(rsCT.getInt("id"));
                        ct.setSoLuongNhap(rsCT.getInt("soLuongNhap"));
                        ct.setDonGiaNhap(rsCT.getDouble("donGiaNhap"));
                        ct.setThanhTien(rsCT.getDouble("thanhTien"));

                        PhuTung pt = new PhuTung();
                        pt.setId(rsCT.getInt("tblPhuTungid"));
                        pt.setTenPhuTung(rsCT.getString("tenPhuTung"));
                        pt.setHangSanXuat(rsCT.getString("hangSanXuat"));
                        pt.setDonViTinh(rsCT.getString("donViTinh"));

                        ct.setPhuTung(pt);
                        ct.setHoaDonNhap(hdn);
                        dsCT.add(ct);
                    }
                    hdn.setDsChiTietNhap(dsCT);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return hdn;
    }
}
