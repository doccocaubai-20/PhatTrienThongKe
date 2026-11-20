package dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import model.PhuTung;

public class PhuTungDAO extends DAO {

    public PhuTungDAO() {
        super();
    }

    public ArrayList<PhuTung> getPhuTungTheoTen(String tuKhoa) {
        ArrayList<PhuTung> list = new ArrayList<>();
        String sql = "SELECT * FROM tblPhuTung WHERE tenPhuTung LIKE ?";

        try {
            if (con == null || con.isClosed()) {
                con = getConnection();
            }
            if (con != null) {
                PreparedStatement ps = con.prepareStatement(sql);
                String pattern = "%" + (tuKhoa != null ? tuKhoa.trim() : "") + "%";
                ps.setString(1, pattern);
                ResultSet rs = ps.executeQuery();

                while (rs.next()) {
                    PhuTung pt = new PhuTung();
                    pt.setId(rs.getInt("id"));
                    pt.setTenPhuTung(rs.getString("tenPhuTung"));
                    pt.setHangSanXuat(rs.getString("hangSanXuat"));
                    pt.setDonViTinh(rs.getString("donViTinh"));
                    pt.setDonGiaNiemYet(rs.getDouble("donGiaNiemYet"));
                    pt.setSoLuongTon(rs.getInt("soLuongTon"));
                    list.add(pt);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return list;
    }

    public PhuTung getPhuTungById(int id) {
        PhuTung pt = null;
        String sql = "SELECT * FROM tblPhuTung WHERE id = ?";

        try {
            if (con == null || con.isClosed()) {
                con = getConnection();
            }
            if (con != null) {
                PreparedStatement ps = con.prepareStatement(sql);
                ps.setInt(1, id);
                ResultSet rs = ps.executeQuery();

                if (rs.next()) {
                    pt = new PhuTung();
                    pt.setId(rs.getInt("id"));
                    pt.setTenPhuTung(rs.getString("tenPhuTung"));
                    pt.setHangSanXuat(rs.getString("hangSanXuat"));
                    pt.setDonViTinh(rs.getString("donViTinh"));
                    pt.setDonGiaNiemYet(rs.getDouble("donGiaNiemYet"));
                    pt.setSoLuongTon(rs.getInt("soLuongTon"));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return pt;
    }

    public PhuTung themPhuTung(PhuTung pt) {
        String sql = "INSERT INTO tblPhuTung (tenPhuTung, hangSanXuat, donViTinh, donGiaNiemYet, soLuongTon) VALUES (?, ?, ?, ?, ?)";

        try {
            if (con == null || con.isClosed()) {
                con = getConnection();
            }
            if (con != null) {
                PreparedStatement ps = con.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
                ps.setString(1, pt.getTenPhuTung());
                ps.setString(2, pt.getHangSanXuat());
                ps.setString(3, pt.getDonViTinh());
                ps.setDouble(4, pt.getDonGiaNiemYet());
                ps.setInt(5, pt.getSoLuongTon());

                int affected = ps.executeUpdate();
                if (affected > 0) {
                    ResultSet rs = ps.getGeneratedKeys();
                    if (rs.next()) {
                        pt.setId(rs.getInt(1));
                    }
                    return pt;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean capNhatTonKho(int idPhuTung, int soLuongTang) {
        String sql = "UPDATE tblPhuTung SET soLuongTon = soLuongTon + ? WHERE id = ?";

        try {
            if (con == null || con.isClosed()) {
                con = getConnection();
            }
            if (con != null) {
                PreparedStatement ps = con.prepareStatement(sql);
                ps.setInt(1, soLuongTang);
                ps.setInt(2, idPhuTung);
                return ps.executeUpdate() > 0;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
