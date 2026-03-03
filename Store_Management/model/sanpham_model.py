from Store_Management.model.model import Model


class SPModel(Model):
    def __init__(self):
        super().__init__()

    def get_all_sp(self):
        """Lấy dữ liệu sản phẩm"""
        sql = "SELECT * FROM SANPHAM"
        return self.query(sql)

    def add_sp(self, ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap, gia_ban):
        """Thêm dữ liệu sản phẩm mới"""
        sql = "INSERT INTO SANPHAM (MA_SP, TEN_SP, LOAI, DON_VI, CHI_PHI, GIA_NHAP, GIA_BAN) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap, gia_ban)
        return self.query_params(sql, params)

    def delete_sp(self, ma_sp):
        """Xóa dữ liệu sản phẩm"""
        sql = "DELETE FROM SANPHAM WHERE MA_SP = %s"
        params = (ma_sp,)
        return self.query_params(sql, params)

    def update_sp(self, ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap, gia_ban):
        """Sửa dữ liệu sản phẩm"""
        sql = "UPDATE SANPHAM SET TEN_SP = %s, LOAI = %s, DON_VI = %s, CHI_PHI = %s, GIA_NHAP = %s, GIA_BAN = %s WHERE MA_SP = %s"
        params = (ten_sp, loai_sp, don_vi, chi_phi, gia_nhap, gia_ban, ma_sp)
        return self.query_params(sql, params)

    def search_sp(self, search_text):
        """Tìm kiếm sản phẩm"""
        sql = "SELECT * FROM SANPHAM WHERE MA_SP LIKE %s OR TEN_SP LIKE %s OR LOAI LIKE %s OR DON_VI LIKE %s OR CHI_PHI LIKE %s OR GIA_NHAP LIKE %s OR GIA_BAN LIKE %s"
        search_pattern = f"%{search_text}%"
        params = (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern)
        return self.query_params(sql, params)