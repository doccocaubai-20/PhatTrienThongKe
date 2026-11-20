package dao;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Date;
import model.ChiTietNhap;
import model.HoaDonNhap;
import model.NhaCungCap;
import model.NVKho;
import model.PhuTung;
import org.junit.Before;
import org.junit.Test;

public class HoaDonNhapDAOTest {

    private HoaDonNhapDAO hoaDonNhapDAO;

    @Before
    public void setUp() {
        hoaDonNhapDAO = new HoaDonNhapDAO();
    }

    /**
     * Test phương thức tính thành tiền của ChiTietNhap.
     */
    @Test
    public void testChiTietNhap_TinhThanhTien() {
        PhuTung pt = new PhuTung(1, "Lọc dầu", "Bosch", "Cái", 150000, 10);
        ChiTietNhap ct = new ChiTietNhap(0, 10, 120000, pt, null);

        double thanhTien = ct.tinhThanhTien();
        assertEquals(1200000.0, thanhTien, 0.001);
        assertEquals(1200000.0, ct.getThanhTien(), 0.001);
    }

    /**
     * Test phương thức tính tổng tiền của HoaDonNhap.
     */
    @Test
    public void testHoaDonNhap_TinhTongTien() {
        HoaDonNhap hdn = new HoaDonNhap();
        PhuTung pt1 = new PhuTung(1, "Lọc dầu", "Bosch", "Cái", 150000, 10);
        PhuTung pt2 = new PhuTung(2, "Bugi", "Denso", "Cái", 200000, 20);

        ChiTietNhap ct1 = new ChiTietNhap(0, 5, 100000, pt1, hdn); // 500.000
        ChiTietNhap ct2 = new ChiTietNhap(0, 4, 150000, pt2, hdn); // 600.000

        hdn.themChiTiet(ct1);
        hdn.themChiTiet(ct2);

        assertEquals(2, hdn.getDsChiTietNhap().size());
        assertEquals(1100000.0, hdn.getTongTien(), 0.001);
        assertEquals(1100000.0, hdn.tinhTongTien(), 0.001);
    }

    /**
     * Test lưu hóa đơn với đầu vào null hoặc danh sách rỗng -> phải trả về false.
     */
    @Test
    public void testLuuHoaDonNhap_InvalidInput() {
        assertFalse("Hóa đơn null phải trả về false", hoaDonNhapDAO.luuHoaDonNhap(null));

        HoaDonNhap hdnEmpty = new HoaDonNhap();
        hdnEmpty.setNhaCungCap(new NhaCungCap(1, "NCC Test", "Hà Nội", "0123456789"));
        assertFalse("Hóa đơn không có chi tiết phải trả về false", hoaDonNhapDAO.luuHoaDonNhap(hdnEmpty));
    }

    /**
     * Test tra cứu hóa đơn theo ID không tồn tại.
     */
    @Test
    public void testGetHoaDonNhapById_InvalidId() {
        HoaDonNhap hdn = hoaDonNhapDAO.getHoaDonNhapById(-9999);
        assertNull("Hóa đơn ID không tồn tại phải trả về null", hdn);
    }

    /**
     * Test lưu hóa đơn hoàn chỉnh vào CSDL (Transaction: hóa đơn + chi tiết + cập
     * nhật kho).
     */
    @Test
    public void testLuuHoaDonNhap_SuccessTransaction() {
        if (hoaDonNhapDAO.con != null) {
            // Lấy 1 NCC và 1 Phụ tùng có sẵn
            NhaCungCapDAO nccDAO = new NhaCungCapDAO();
            PhuTungDAO ptDAO = new PhuTungDAO();

            ArrayList<NhaCungCap> listNCC = nccDAO.getNhaCungCapTheoTen("");
            ArrayList<PhuTung> listPT = ptDAO.getPhuTungTheoTen("");

            if (!listNCC.isEmpty() && !listPT.isEmpty()) {
                NhaCungCap ncc = listNCC.get(0);
                PhuTung pt = listPT.get(0);
                int tonKhoTruoc = pt.getSoLuongTon();

                NVKho nvKho = new NVKho();
                nvKho.setId(1);
                nvKho.setHoTen("Thủ kho test");

                HoaDonNhap hdn = new HoaDonNhap(0, new Date(), ncc, nvKho);
                ChiTietNhap ct = new ChiTietNhap(0, 5, 80000, pt, hdn);
                hdn.themChiTiet(ct);

                boolean thanhCong = hoaDonNhapDAO.luuHoaDonNhap(hdn);
                assertTrue("Giao dịch lưu hóa đơn nhập phải thành công", thanhCong);
                assertTrue("Hóa đơn mới phải có ID tự sinh > 0", hdn.getId() > 0);

                // Kiểm tra truy vấn lại hóa đơn vừa lưu
                HoaDonNhap hdnDaLuu = hoaDonNhapDAO.getHoaDonNhapById(hdn.getId());
                assertNotNull("Hóa đơn vừa lưu phải truy vấn ra được", hdnDaLuu);
                assertEquals(hdn.getTongTien(), hdnDaLuu.getTongTien(), 0.001);
                assertFalse("Danh sách chi tiết không được rỗng", hdnDaLuu.getDsChiTietNhap().isEmpty());

                // Kiểm tra số lượng tồn kho phụ tùng đã được tự động cộng dồn thêm 5
                PhuTung ptSau = ptDAO.getPhuTungById(pt.getId());
                assertEquals("Tồn kho phải được cộng thêm 5", tonKhoTruoc + 5, ptSau.getSoLuongTon());
            }
        }
    }
}
