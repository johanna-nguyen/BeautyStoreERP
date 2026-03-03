from Store_Management.model.model import Model


class ThongKeModel(Model):
    def __init__(self):
        super().__init__()

    # THỐNG KÊ DOANH THU
    def doanh_thu_theo_thang(self, thang):
        """Tính doanh thu theo tháng"""
        sql = """
                SELECT MONTH(NGAY_XUAT) AS THANG, SUM(THANH_TIEN) AS DOANH_THU
                FROM PHIEUXUAT
                WHERE MONTH(NGAY_XUAT) = %s
                GROUP BY MONTH(NGAY_XUAT)
            """
        params = (thang,)
        return self.query_params(sql, params)

    def doanh_thu_theo_nam(self, nam):
        """Tính doanh thu theo năm"""
        sql = """
                SELECT YEAR(NGAY_XUAT) AS NAM, SUM(THANH_TIEN) AS DOANH_THU
                FROM PHIEUXUAT
                WHERE YEAR(NGAY_XUAT) = %s
                GROUP BY YEAR(NGAY_XUAT)
            """
        params = (nam,)
        return self.query_params(sql, params)

    def doanh_thu_theo_ma_sp(self, ma_sp):
        """Tính doanh thu theo mã sản phẩm"""
        sql = """
                SELECT MA_SP, SUM(THANH_TIEN) AS DOANH_THU
                FROM PHIEUXUAT
                WHERE MA_SP = %s
                GROUP BY MA_SP
            """
        params = (ma_sp,)
        return self.query_params(sql, params)

    def doanh_thu_theo_loai_sp(self, loai_sp):
        """Tính doanh thu theo loại sản phẩm"""
        sql = """
                SELECT SP.LOAI, SUM(PX.THANH_TIEN) AS DOANH_THU
                FROM PHIEUXUAT PX
                INNER JOIN SANPHAM SP ON PX.MA_SP = SP.MA_SP
                WHERE SP.LOAI = %s
                GROUP BY SP.LOAI
            """
        params = (loai_sp,)
        return self.query_params(sql, params)

    def doanh_thu_theo_ma_nv(self, ma_nv):
        """Tính doanh thu theo người xuất - mã nhân viên"""
        sql = """
                SELECT NGUOI_XUAT, SUM(THANH_TIEN) AS DOANH_THU
                FROM PHIEUXUAT
                WHERE NGUOI_XUAT = %s
                GROUP BY NGUOI_XUAT
            """
        params = (ma_nv,)
        return self.query_params(sql, params)

    # THỐNG KÊ SẢN PHẨM
    def top_san_pham_ban_chay(self):
        """Top sản phẩm bán chạy"""
        sql = """
                SELECT SP.MA_SP, SP.TEN_SP, SUM(SO_LUONG) AS TONG_SO_LUONG_BAN
                FROM PHIEUXUAT PX
                JOIN SANPHAM SP ON PX.MA_SP = SP.MA_SP
                GROUP BY SP.MA_SP, SP.TEN_SP
                ORDER BY TONG_SO_LUONG_BAN DESC
            """
        return self.query(sql)

    # THỐNG KÊ NHÂN VIÊN
    def top_nhan_vien(self):
        """Top nhân viên có doanh số cao nhất"""
        sql = """
                SELECT PX.NGUOI_XUAT, NV.TEN_NV, SUM(PX.THANH_TIEN) AS TONG_DOANH_SO
                FROM PHIEUXUAT PX
                JOIN NHANVIEN NV ON PX.NGUOI_XUAT = NV.MA_NV
                GROUP BY PX.NGUOI_XUAT, NV.TEN_NV
                ORDER BY TONG_DOANH_SO DESC;
                """
        return self.query(sql)

    # THỐNG KÊ KHÁCH HÀNG
    def top_khach_hang(self):
        """Top khách hàng đã mua nhiều nhất"""
        sql = """
                SELECT KH.MA_KH, KH.TEN_KH, SUM(PX.THANH_TIEN) AS TONG_SO_TIEN
                FROM PHIEUXUAT PX
                JOIN KHACHHANG KH ON KH.MA_KH = PX.MA_KH
                GROUP BY KH.MA_KH, KH.TEN_KH
                ORDER BY TONG_SO_TIEN DESC;
                """
        return self.query(sql)

    # THỐNG KÊ NHÀ CUNG CẤP
    def top_nha_cung_cap(self):
        """Top nhà cung câp nhận hàng nhiều nhất"""
        sql = """
                SELECT NCC.MA_NCC, NCC.TEN_NCC, SUM(PN.SO_LUONG) AS TONG_SO_LUONG_NHAP
                FROM PHIEUNHAP PN
                JOIN NHACUNGCAP NCC ON PN.MA_NCC = NCC.MA_NCC
                GROUP BY NCC.MA_NCC, NCC.TEN_NCC
                ORDER BY TONG_SO_LUONG_NHAP DESC;
                """
        return self.query(sql)

    # THỐNG KÊ LƯƠNG
    def tk_luong(self):
        """Thống kê lương"""
        sql = """
                SELECT NV.MA_NV, NV.TEN_NV, SUM(L.LUONG_HANG_THANG) AS TONG_LUONG
                FROM LUONG L
                JOIN NHANVIEN NV ON NV.MA_NV = L.MA_NV
                GROUP BY NV.MA_NV, NV.TEN_NV
                ORDER BY TONG_LUONG DESC;
                """
        return self.query(sql)

    def get_ma_sp(self):
        """Lấy dữ liệu mã sản phẩm"""
        sql = "SELECT MA_SP FROM SANPHAM"
        return self.query(sql)

    def get_ma_nv(self):
        """Lấy dữ liệu mã nhân viên"""
        sql = "SELECT MA_NV FROM NHANVIEN"
        return self.query(sql)