package dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import model.DichVu;

public class DichVuDAO extends DAO {

    public DichVuDAO() {
        super();
    }

    public ArrayList<DichVu> getDichVuTheoTen(String tuKhoa) {
        ArrayList<DichVu> list = new ArrayList<>();
        String sql = "SELECT * FROM tblDichVu WHERE tenDichVu LIKE ?";

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
                    DichVu dv = new DichVu();
                    dv.setId(rs.getInt("id"));
                    dv.setTenDichVu(rs.getString("tenDichVu"));
                    dv.setLoaiDichVu(rs.getString("loaiDichVu"));
                    dv.setDonGia(rs.getDouble("donGia"));
                    dv.setThoiGianBaoHanh(rs.getString("thoiGianBaoHanh"));
                    list.add(dv);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return list;
    }

    /**
     * Lấy thông tin chi tiết dịch vụ theo mã ID
     * 
     * @param id mã dịch vụ
     * @return đối tượng DichVu
     */
    public DichVu getDichVuById(int id) {
        DichVu dv = null;
        String sql = "SELECT * FROM tblDichVu WHERE id = ?";

        try {
            if (con == null || con.isClosed()) {
                con = getConnection();
            }
            if (con != null) {
                PreparedStatement ps = con.prepareStatement(sql);
                ps.setInt(1, id);
                ResultSet rs = ps.executeQuery();

                if (rs.next()) {
                    dv = new DichVu();
                    dv.setId(rs.getInt("id"));
                    dv.setTenDichVu(rs.getString("tenDichVu"));
                    dv.setLoaiDichVu(rs.getString("loaiDichVu"));
                    dv.setDonGia(rs.getDouble("donGia"));
                    dv.setThoiGianBaoHanh(rs.getString("thoiGianBaoHanh"));
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return dv;
    }
}
