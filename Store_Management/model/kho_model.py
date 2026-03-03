from Store_Management.model.model import Model


class KhoModel(Model):
    def __init__(self):
        super().__init__()

    def get_all_kho(self):
        """Lấy dữ liệu kho"""
        sql = "SELECT * FROM KHO"
        return self.query(sql)

    def add_kho(self, ma_kho, ma_sp, ten_sp, don_vi, ton_kho, ngay_cap_nhat):
        """Thêm dữ liệu kho mới"""
        sql = "INSERT INTO KHO (MA_KHO, MA_SP, TEN_SP, DON_VI, TON_KHO, NGAY_CAP_NHAT) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (ma_kho, ma_sp, ten_sp, don_vi, ton_kho, ngay_cap_nhat)
        return self.query_params(sql, params)

    def delete_kho(self, ma_kho):
        """Xóa dữ liệu kho"""
        sql = "DELETE FROM KHO WHERE MA_KHO = %s"
        params = (ma_kho,)
        return self.query_params(sql, params)

    def update_kho(self, ma_kho, ma_sp, ten_sp, don_vi, ton_kho, ngay_cap_nhat):
        """Sửa dữ liệu kho"""
        sql = "UPDATE KHO SET MA_SP = %s, TEN_SP = %s, DON_VI = %s, TON_KHO = %s, NGAY_CAP_NHAT = %s WHERE MA_KHO = %s"
        params = (ma_sp, ten_sp, don_vi, ton_kho, ngay_cap_nhat, ma_kho)
        return self.query_params(sql, params)

    def search_kho(self, search_text):
        """Tìm kiếm lương"""
        sql = "SELECT * FROM KHO WHERE MA_KHO LIKE %s OR MA_SP LIKE %s OR TEN_SP LIKE %s OR DON_VI LIKE %s OR TON_KHO LIKE %s OR NGAY_CAP_NHAT LIKE %s"
        search_pattern = f"%{search_text}%"
        params = (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern)
        return self.query_params(sql, params)

    def get_ten_sp(self, ma_sp):
        """Lấy dữ liệu tên sp"""
        sql = "SELECT TEN_SP FROM SANPHAM WHERE MA_SP = %s"
        params = (ma_sp,)
        return self.query_params(sql, params)

    def get_don_vi(self, ma_sp):
        """Lấy dữ liệu đơn vị"""
        sql = "SELECT DON_VI FROM SANPHAM WHERE MA_SP = %s"
        params = (ma_sp,)
        return self.query_params(sql, params)

    def tinh_ton_kho(self, ma_sp):
        """Tính số lượng hàng tồn kho"""
        sql = """SELECT sp.MA_SP, sp.TEN_SP, COALESCE(SUM(pn.SO_LUONG), 0) AS TONG_NHAP, COALESCE(SUM(px.SO_LUONG), 0) AS TONG_XUAT,COALESCE(SUM(pn.SO_LUONG), 0) - COALESCE(SUM(px.SO_LUONG), 0) AS TON_KHO
               FROM SANPHAM sp
               LEFT JOIN PHIEUNHAP pn ON sp.MA_SP = pn.MA_SP
               LEFT JOIN PHIEUXUAT px ON sp.MA_SP = px.MA_SP
               WHERE sp.MA_SP = %s
               GROUP BY sp.MA_SP, sp.TEN_SP"""
        params = (ma_sp,)
        return self.query_params(sql, params)

    def get_ma_sp(self):
        """Lấy dữ liệu mã sản phẩm"""
        sql = "SELECT MA_SP FROM SANPHAM"
        return self.query(sql)