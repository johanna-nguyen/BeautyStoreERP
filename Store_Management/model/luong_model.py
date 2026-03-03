from Store_Management.model.model import Model


class LuongModel(Model):
    def __init__(self):
        super().__init__()

    def get_all_luong(self):
        """Lấy dữ liệu lương"""
        sql = "SELECT * FROM LUONG"
        return self.query(sql)

    def add_luong(self, ma_luong, ma_nv, chuc_vu, luong_co_ban, doanh_so, so_gio_lam, he_so_chuc_vu, tro_cap, thuong, luong_hang_thang, ngay_tinh_luong):
        """Thêm dữ liệu lương mới"""
        sql = "INSERT INTO LUONG (MA_LUONG, MA_NV, CHUC_VU, LUONG_CO_BAN, DOANH_SO, SO_GIO_LAM, HE_SO_CHUC_VU, TRO_CAP, THUONG, LUONG_HANG_THANG, NGAY_TINH_LUONG) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (ma_luong, ma_nv, chuc_vu, luong_co_ban, doanh_so, so_gio_lam, he_so_chuc_vu, tro_cap, thuong, luong_hang_thang, ngay_tinh_luong)
        return self.query_params(sql, params)

    def delete_luong(self, ma_luong):
        """Xóa dữ liệu lương"""
        sql = "DELETE FROM LUONG WHERE MA_LUONG = %s"
        params = (ma_luong,)
        return self.query_params(sql, params)

    def update_luong(self, ma_luong, ma_nv, chuc_vu, luong_co_ban, doanh_so, so_gio_lam, he_so_chuc_vu, tro_cap, thuong, luong_hang_thang, ngay_tinh_luong):
        """Sửa dữ liệu lương"""
        sql = "UPDATE LUONG SET MA_NV = %s, CHUC_VU = %s, LUONG_CO_BAN = %s, DOANH_SO = %s, SO_GIO_LAM = %s, HE_SO_CHUC_VU = %s, TRO_CAP = %s, THUONG = %s, LUONG_HANG_THANG = %s, NGAY_TINH_LUONG = %s WHERE MA_LUONG = %s"
        params = (ma_nv, chuc_vu, luong_co_ban, doanh_so, so_gio_lam, he_so_chuc_vu, tro_cap, thuong, luong_hang_thang, ngay_tinh_luong, ma_luong)
        return self.query_params(sql, params)

    def search_luong(self, search_text):
        """Tìm kiếm lương"""
        sql = "SELECT * FROM LUONG WHERE MA_LUONG LIKE %s OR MA_NV LIKE %s OR CHUC_VU LIKE %s OR LUONG_CO_BAN LIKE %s OR DOANH_SO LIKE %s OR SO_GIO_LAM LIKE %s OR HE_SO_CHUC_VU LIKE %s OR TRO_CAP LIKE %s OR THUONG LIKE %s OR LUONG_HANG_THANG LIKE %s OR NGAY_TINH_LUONG LIKE %s"
        search_pattern = f"%{search_text}%"
        params = (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern)
        return self.query_params(sql, params)

    def get_ma_nv(self):
        """Lấy dữ liệu mã nhân viên"""
        sql = "SELECT MA_NV FROM NHANVIEN"
        return self.query(sql)

    def get_chuc_vu(self, ma_nv):
        """Lấy dữ liệu chức vụ"""
        sql = "SELECT CHUC_VU FROM NHANVIEN WHERE MA_NV = %s"
        params = (ma_nv,)
        return self.query_params(sql, params)