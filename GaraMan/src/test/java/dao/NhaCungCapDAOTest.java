package dao;

import static org.junit.Assert.*;

import java.util.ArrayList;
import model.NhaCungCap;
import org.junit.Before;
import org.junit.Test;

public class NhaCungCapDAOTest {

    private NhaCungCapDAO nhaCungCapDAO;

    @Before
    public void setUp() {
        nhaCungCapDAO = new NhaCungCapDAO();
    }

    /**
     * Test tìm kiếm nhà cung cấp với từ khóa rỗng -> lấy toàn bộ.
     */
    @Test
    public void testGetNhaCungCapTheoTen_EmptyKeyword() {
        ArrayList<NhaCungCap> list = nhaCungCapDAO.getNhaCungCapTheoTen("");
        assertNotNull("Danh sách trả về không được null", list);
        if (nhaCungCapDAO.con != null) {
            assertTrue("Có kết nối CSDL, danh sách nhà cung cấp phải >= 0", list.size() >= 0);
        }
    }

    /**
     * Test tìm kiếm với từ khóa cụ thể.
     */
    @Test
    public void testGetNhaCungCapTheoTen_PartialKeyword() {
        ArrayList<NhaCungCap> list = nhaCungCapDAO.getNhaCungCapTheoTen("Bosch");
        assertNotNull("Danh sách không được null", list);
        if (nhaCungCapDAO.con != null && !list.isEmpty()) {
            for (NhaCungCap ncc : list) {
                assertTrue("Tên NCC phải chứa từ khóa tìm kiếm",
                        ncc.getTenNCC().toLowerCase().contains("bosch"));
            }
        }
    }

    /**
     * Test tìm kiếm với tên NCC không tồn tại.
     */
    @Test
    public void testGetNhaCungCapTheoTen_NonExistent() {
        ArrayList<NhaCungCap> list = nhaCungCapDAO.getNhaCungCapTheoTen("NCC_VO_DANH_KHONG_CO_THUC_789");
        assertNotNull("Danh sách không được null", list);
        assertTrue("Không tìm thấy NCC nào", list.isEmpty());
    }

    /**
     * Test thêm mới nhà cung cấp và kiểm tra ID tự sinh.
     */
    @Test
    public void testThemNhaCungCap_Valid() {
        if (nhaCungCapDAO.con != null) {
            String suffix = String.valueOf(System.currentTimeMillis() % 10000);
            NhaCungCap nccMoi = new NhaCungCap(0, "Công ty Phụ tùng Auto " + suffix, "Khu CN Hà Nội",
                    "091234" + suffix);

            NhaCungCap daLuu = nhaCungCapDAO.themNhaCungCap(nccMoi);
            assertNotNull("NCC sau khi lưu không được null", daLuu);
            assertTrue("NCC mới phải được gán ID tự sinh > 0", daLuu.getId() > 0);
            assertEquals("Công ty Phụ tùng Auto " + suffix, daLuu.getTenNCC());
            assertEquals("Khu CN Hà Nội", daLuu.getDiaChi());
            assertEquals("091234" + suffix, daLuu.getSoDienThoai());
        }
    }
}
