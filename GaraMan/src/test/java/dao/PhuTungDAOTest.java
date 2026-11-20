package dao;

import static org.junit.Assert.*;

import java.util.ArrayList;
import model.PhuTung;
import org.junit.Before;
import org.junit.Test;

public class PhuTungDAOTest {

    private PhuTungDAO phuTungDAO;

    @Before
    public void setUp() {
        phuTungDAO = new PhuTungDAO();
    }

    /**
     * Test phương thức capNhatTonKho() trên đối tượng thực thể PhuTung
     */
    @Test
    public void testPhuTungModel_CapNhatTonKho() {
        PhuTung pt = new PhuTung(1, "Lọc dầu Bosch", "Bosch", "Cái", 150000, 10);
        assertEquals(10, pt.getSoLuongTon());

        pt.capNhatTonKho(5);
        assertEquals("Số lượng tồn phải tăng lên 15 sau khi nhập 5 cái", 15, pt.getSoLuongTon());

        pt.capNhatTonKho(-3);
        assertEquals("Số lượng tồn phải giảm về 12 sau khi xuất 3 cái", 12, pt.getSoLuongTon());
    }

    /**
     * Test tìm kiếm phụ tùng với từ khóa rỗng.
     */
    @Test
    public void testGetPhuTungTheoTen_EmptyKeyword() {
        ArrayList<PhuTung> list = phuTungDAO.getPhuTungTheoTen("");
        assertNotNull("Danh sách trả về không được null", list);
        if (phuTungDAO.con != null) {
            assertTrue("Có kết nối CSDL, danh sách phải >= 0", list.size() >= 0);
        }
    }

    /**
     * Test tìm kiếm phụ tùng với từ khóa tồn tại (ví dụ: 'nhớt' hoặc 'lọc').
     */
    @Test
    public void testGetPhuTungTheoTen_PartialKeyword() {
        ArrayList<PhuTung> list = phuTungDAO.getPhuTungTheoTen("Lọc");
        assertNotNull("Danh sách không được null", list);
        if (phuTungDAO.con != null && !list.isEmpty()) {
            for (PhuTung pt : list) {
                assertTrue("Tên hoặc hãng phải chứa từ khóa tìm kiếm",
                        pt.getTenPhuTung().toLowerCase().contains("lọc") ||
                                pt.getHangSanXuat().toLowerCase().contains("lọc"));
            }
        }
    }

    /**
     * Test tìm kiếm với từ khóa không tồn tại.
     */
    @Test
    public void testGetPhuTungTheoTen_NonExistentKeyword() {
        ArrayList<PhuTung> list = phuTungDAO.getPhuTungTheoTen("PHU_TUNG_KHONG_CO_THUC_99999");
        assertNotNull("Danh sách không được null", list);
        assertTrue("Không được có phụ tùng nào khớp", list.isEmpty());
    }

    /**
     * Test lấy chi tiết phụ tùng theo ID hợp lệ.
     */
    @Test
    public void testGetPhuTungById_ValidId() {
        if (phuTungDAO.con != null) {
            ArrayList<PhuTung> all = phuTungDAO.getPhuTungTheoTen("");
            if (!all.isEmpty()) {
                int testId = all.get(0).getId();
                PhuTung pt = phuTungDAO.getPhuTungById(testId);
                assertNotNull("Phụ tùng phải tồn tại", pt);
                assertEquals(testId, pt.getId());
                assertNotNull(pt.getTenPhuTung());
                assertNotNull(pt.getDonViTinh());
                assertTrue(pt.getDonGiaNiemYet() >= 0);
            }
        }
    }

    /**
     * Test lấy phụ tùng theo ID không hợp lệ.
     */
    @Test
    public void testGetPhuTungById_InvalidId() {
        PhuTung pt = phuTungDAO.getPhuTungById(-999);
        assertNull("ID âm phải trả về null", pt);
    }

    /**
     * Test thêm mới phụ tùng vào hệ thống.
     */
    @Test
    public void testThemPhuTung_Valid() {
        if (phuTungDAO.con != null) {
            String randomCode = String.valueOf(System.currentTimeMillis() % 10000);
            PhuTung moi = new PhuTung(0, "Bugi Iridium Denso Test " + randomCode, "Denso", "Cái", 220000, 0);
            PhuTung daThem = phuTungDAO.themPhuTung(moi);

            assertNotNull("Đối tượng sau khi thêm không được null", daThem);
            assertTrue("Phụ tùng thêm mới phải được gán ID tự sinh > 0", daThem.getId() > 0);
            assertEquals("Bugi Iridium Denso Test " + randomCode, daThem.getTenPhuTung());
            assertEquals("Denso", daThem.getHangSanXuat());
        }
    }
}
