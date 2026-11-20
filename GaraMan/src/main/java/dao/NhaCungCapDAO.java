package dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import model.NhaCungCap;

public class NhaCungCapDAO extends DAO {

    public NhaCungCapDAO() {
        super();
    }

    public ArrayList<NhaCungCap> getNhaCungCapTheoTen(String ten) {
        ArrayList<NhaCungCap> list = new ArrayList<>();
        String sql = "SELECT * FROM tblNhaCungCap WHERE tenNCC LIKE ?";

        try {
            if (con == null || con.isClosed()) {
                con = getConnection();
            }
            if (con != null) {
                PreparedStatement ps = con.prepareStatement(sql);
                String pattern = "%" + (ten != null ? ten.trim() : "") + "%";
                ps.setString(1, pattern);
                ResultSet rs = ps.executeQuery();

                while (rs.next()) {
                    NhaCungCap ncc = new NhaCungCap();
                    ncc.setId(rs.getInt("id"));
                    ncc.setTenNCC(rs.getString("tenNCC"));
                    ncc.setDiaChi(rs.getString("diaChi"));
                    ncc.setSoDienThoai(rs.getString("soDienThoai"));
                    list.add(ncc);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return list;
    }

    public NhaCungCap themNhaCungCap(NhaCungCap ncc) {
        String sql = "INSERT INTO tblNhaCungCap (tenNCC, diaChi, soDienThoai) VALUES (?, ?, ?)";

        try {
            if (con == null || con.isClosed()) {
                con = getConnection();
            }
            if (con != null) {
                PreparedStatement ps = con.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
                ps.setString(1, ncc.getTenNCC());
                ps.setString(2, ncc.getDiaChi());
                ps.setString(3, ncc.getSoDienThoai());

                int affected = ps.executeUpdate();
                if (affected > 0) {
                    ResultSet rs = ps.getGeneratedKeys();
                    if (rs.next()) {
                        ncc.setId(rs.getInt(1));
                    }
                    return ncc;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}
