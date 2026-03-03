from Store_Management.model.model import Model


class NVModel(Model):
    def __init__(self):
        super().__init__()

    def get_all_nv(self):
        """Lấy dữ liệu nhân viên"""
        sql = "SELECT * FROM NHANVIEN"
        return self.query(sql)

    def add_nv(self, ma_nv, ten_nv, ngay_sinh, gioi_tinh, chuc_vu, dia_chi, sdt_nv, email):
        """Thêm dữ liệu sản phẩm mới"""
        sql = "INSERT INTO NHANVIEN (MA_NV, TEN_NV, NGAY_SINH, GIOI_TINH, CHUC_VU, DIA_CHI, SO_DIEN_THOAI, EMAIL) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (ma_nv, ten_nv, ngay_sinh, gioi_tinh, chuc_vu, dia_chi, sdt_nv, email)
        return self.query_params(sql, params)

    def delete_nv(self, ma_nv):
        """Xóa dữ liệu nhân viên"""
        sql = "DELETE FROM NHANVIEN WHERE MA_NV = %s"
        params = (ma_nv,)
        return self.query_params(sql, params)

    def update_nv(self, ma_nv, ten_nv, ngay_sinh, gioi_tinh, chuc_vu, dia_chi, sdt_nv, email):
        """Sửa dữ liệu nhân viên"""
        sql = "UPDATE NHANVIEN SET TEN_NV = %s, NGAY_SINH = %s, GIOI_TINH = %s, CHUC_VU = %s, DIA_CHI = %s, SO_DIEN_THOAI = %s, EMAIL = %s  WHERE MA_NV = %s"
        params = (ten_nv, ngay_sinh, gioi_tinh, chuc_vu, dia_chi, sdt_nv, email, ma_nv)
        return self.query_params(sql, params)
    
    def search_nv(self, search_text):
        """Tìm kiếm nhân viên"""
        sql = "SELECT * FROM NHANVIEN WHERE MA_NV LIKE %s OR TEN_NV LIKE %s OR NGAY_SINH LIKE %s OR GIOI_TINH LIKE %s OR CHUC_VU LIKE %s OR DIA_CHI LIKE %s OR SO_DIEN_THOAI LIKE %s OR EMAIL LIKE %s"
        search_pattern = f"%{search_text}%"
        params = (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern)
        return self.query_params(sql, params)