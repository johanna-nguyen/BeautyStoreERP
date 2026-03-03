from Store_Management.model.model import Model


class KHModel(Model):
    def __init__(self):
        super().__init__()

    def get_all_kh(self):
        """Lấy dữ liệu khách hàng"""
        sql = "SELECT * FROM KHACHHANG"
        return self.query(sql)

    def add_kh(self, ma_kh, ten_kh, ngay_sinh, gioi_tinh, hang_kh, dia_chi, sdt_kh):
        """Thêm dữ liệu khách hàng mới"""
        sql = "INSERT INTO KHACHHANG (MA_KH, TEN_KH, NGAY_SINH, GIOI_TINH, HANG_KH, DIA_CHI, SO_DIEN_THOAI) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (ma_kh, ten_kh, ngay_sinh, gioi_tinh, hang_kh, dia_chi, sdt_kh)
        return self.query_params(sql, params)

    def delete_kh(self, ma_kh):
        """Xóa dữ liệu khách hàng"""
        sql = "DELETE FROM KHACHHANG WHERE MA_KH = %s"
        params = (ma_kh,)
        return self.query_params(sql, params)

    def update_kh(self, ma_kh, ten_kh, ngay_sinh, gioi_tinh, hang_kh, dia_chi, sdt_kh):
        """Sửa dữ liệu khách hàng"""
        sql = "UPDATE KHACHHANG SET TEN_KH = %s, NGAY_SINH = %s, GIOI_TINH = %s, HANG_KH = %s, DIA_CHI = %s, SO_DIEN_THOAI = %s WHERE MA_KH = %s"
        params = (ten_kh, ngay_sinh, gioi_tinh, hang_kh, dia_chi, sdt_kh, ma_kh)
        return self.query_params(sql, params)

    def search_kh(self, search_text):
        """Tìm kiếm khách hàng"""
        sql = "SELECT * FROM KHACHHANG WHERE MA_KH LIKE %s OR TEN_KH LIKE %s OR NGAY_SINH LIKE %s OR GIOI_TINH LIKE %s OR HANG_KH LIKE %s OR DIA_CHI LIKE %s OR SO_DIEN_THOAI LIKE %s"
        search_pattern = f"%{search_text}%"
        params = (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern)
        return self.query_params(sql, params)