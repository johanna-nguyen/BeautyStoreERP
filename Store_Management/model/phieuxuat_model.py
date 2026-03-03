from Store_Management.model.model import Model


class PXModel(Model):
    def __init__(self):
        super().__init__()

    def get_all_px(self):
        """Lấy dữ liệu phiếu xuất"""
        sql = "SELECT * FROM PHIEUXUAT"
        return self.query(sql)

    def add_px(self, ma_px, ma_kh, ma_sp, so_luong, gia_xuat, thanh_tien, nguoi_xuat, ngay_px):
        """Thêm dữ liệu phiếu xuất mới"""
        sql = "INSERT INTO PHIEUXUAT (MA_PX, MA_KH, MA_SP, SO_LUONG, GIA_XUAT, THANH_TIEN, NGUOI_XUAT, NGAY_XUAT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (ma_px, ma_kh, ma_sp, so_luong, gia_xuat, thanh_tien, nguoi_xuat, ngay_px)
        return self.query_params(sql, params)

    def delete_px(self, ma_px):
        """Xóa dữ liệu phiếu nhập"""
        sql = "DELETE FROM PHIEUXUAT WHERE MA_PX = %s"
        params = (ma_px,)
        return self.query_params(sql, params)

    def update_px(self, ma_px, ma_kh, ma_sp, so_luong, gia_xuat, thanh_tien, nguoi_xuat, ngay_px):
        """Sửa dữ liệu phiếu xuất"""
        sql = "UPDATE PHIEUXUAT SET MA_KH = %s, MA_SP = %s, SO_LUONG = %s, GIA_XUAT = %s, THANH_TIEN = %s, NGUOI_XUAT = %s, NGAY_XUAT = %s WHERE MA_PX = %s"
        params = (ma_kh, ma_sp, so_luong, gia_xuat, thanh_tien, nguoi_xuat, ngay_px, ma_px)
        return self.query_params(sql, params)

    def search_px(self, search_text):
        """Tìm kiếm phiếu xuất"""
        sql = "SELECT * FROM PHIEUXUAT WHERE MA_PX LIKE %s OR MA_KH LIKE %s OR MA_SP LIKE %s OR SO_LUONG LIKE %s OR GIA_XUAT LIKE %s OR THANH_TIEN LIKE %s OR NGUOI_XUAT LIKE %s OR NGAY_XUAT LIKE %s"
        search_pattern = f"%{search_text}%"
        params = (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern,  search_pattern)
        return self.query_params(sql, params)

    def get_ma_kh(self):
        """Lấy dữ liệu mã khách hàng"""
        sql = "SELECT MA_KH FROM KHACHHANG"
        return self.query(sql)

    def get_ma_sp(self):
        """Lấy dữ liệu mã sản phẩm"""
        sql = "SELECT MA_SP FROM SANPHAM"
        return self.query(sql)

    def get_ma_nv(self):
        """Lấy dữ liệu mã nhân viên"""
        sql = "SELECT MA_NV FROM NHANVIEN"
        return self.query(sql)

