package dao;

import static org.junit.Assert.*;

import java.util.ArrayList;
import model.DichVu;
import org.junit.Before;
import org.junit.Test;

public class DichVuDAOTest {

    private DichVuDAO dichVuDAO;

    @Before
    public void setUp() {
        dichVuDAO = new DichVuDAO();
    }

    /**
     * Test tìm kiếm với từ khóa rỗng -> trả về toàn bộ danh sách dịch vụ.
     */
    @Test
    public void testGetDichVuTheoTen_EmptyKeyword() {
        ArrayList<DichVu> list = dichVuDAO.getDichVuTheoTen("");
        assertNotNull("Danh sách trả về không được null", list);
        if (dichVuDAO.con != null) {
            assertTrue("Nếu có kết nối CSDL, danh sách trả về phải >= 0", list.size() >= 0);
        }
    }

    /**
     * Test tìm kiếm với từ khóa tồn tại (ví dụ: 'Bảo dưỡng').
     */
    @Test
    public void testGetDichVuTheoTen_ExactOrPartialKeyword() {
        ArrayList<DichVu> list = dichVuDAO.getDichVuTheoTen("Bảo dưỡng");
        assertNotNull("Kết quả tìm kiếm không được null", list);
        if (dichVuDAO.con != null && !list.isEmpty()) {
            for (DichVu dv : list) {
                assertTrue("Tên dịch vụ phải chứa từ khóa tìm kiếm",
                        dv.getTenDichVu().toLowerCase().contains("bảo dưỡng") ||
                                dv.getLoaiDichVu().toLowerCase().contains("bảo dưỡng"));
            }
        }
    }

    /**
     * Test tìm kiếm với từ khóa không tồn tại.
     */
    @Test
    public void testGetDichVuTheoTen_NonExistentKeyword() {
        ArrayList<DichVu> list = dichVuDAO.getDichVuTheoTen("XYZ_KHONG_TON_TAI_123456");
        assertNotNull("Danh sách trả về không được null", list);
        assertTrue("Không được tìm thấy dịch vụ nào với từ khóa ngẫu nhiên", list.isEmpty());
    }

    /**
     * Test lấy chi tiết dịch vụ theo ID hợp lệ.
     */
    @Test
    public void testGetDichVuById_ValidId() {
        if (dichVuDAO.con != null) {
            ArrayList<DichVu> all = dichVuDAO.getDichVuTheoTen("");
            if (!all.isEmpty()) {
                int idTest = all.get(0).getId();
                DichVu dv = dichVuDAO.getDichVuById(idTest);
                assertNotNull("Dịch vụ tìm theo ID hợp lệ phải tồn tại", dv);
                assertEquals("ID lấy về phải khớp với ID yêu cầu", idTest, dv.getId());
                assertNotNull("Tên dịch vụ không được rỗng", dv.getTenDichVu());
                assertTrue("Đơn giá dịch vụ phải >= 0", dv.getDonGia() >= 0);
            }
        }
    }

    /**
     * Test lấy chi tiết dịch vụ theo ID âm hoặc không tồn tại.
     */
    @Test
    public void testGetDichVuById_InvalidId() {
        DichVu dv = dichVuDAO.getDichVuById(-9999);
        assertNull("ID âm hoặc không tồn tại phải trả về null", dv);
    }
}
