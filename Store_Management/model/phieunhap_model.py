from Store_Management.model.model import Model


class PNModel(Model):
    def __init__(self):
        super().__init__()

    def get_all_pn(self):
        """Lấy dữ liệu phiếu nhập"""
        sql = "SELECT * FROM PHIEUNHAP"
        return self.query(sql)

    def add_pn(self, ma_pn, ma_ncc, ma_sp, so_luong, gia_nhap, thanh_tien, ngay_pn):
        """Thêm dữ liệu phiếu nhập mới"""
        sql = "INSERT INTO PHIEUNHAP (MA_PN, MA_NCC, MA_SP, SO_LUONG, GIA_NHAP, THANH_TIEN, NGAY_PN) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (ma_pn, ma_ncc, ma_sp, so_luong, gia_nhap, thanh_tien, ngay_pn)
        return self.query_params(sql, params)

    def delete_pn(self, ma_pn):
        """Xóa dữ liệu phiếu nhập"""
        sql = "DELETE FROM PHIEUNHAP WHERE MA_PN = %s"
        params = (ma_pn,)
        return self.query_params(sql, params)

    def update_pn(self, ma_pn, ma_ncc, ma_sp, so_luong, gia_nhap, thanh_tien, ngay_pn):
        """Sửa dữ liệu phiếu nhập"""
        sql = "UPDATE PHIEUNHAP SET MA_NCC = %s, MA_SP = %s, SO_LUONG = %s, GIA_NHAP = %s, THANH_TIEN = %s, NGAY_PN = %s WHERE MA_PN = %s"
        params = (ma_ncc, ma_sp, so_luong, gia_nhap, thanh_tien, ngay_pn, ma_pn)
        return self.query_params(sql, params)

    def search_pn(self, search_text):
        """Tìm kiếm phiếu nhập"""
        sql = "SELECT * FROM PHIEUNHAP WHERE MA_PN LIKE %s OR MA_NCC LIKE %s OR MA_SP LIKE %s OR SO_LUONG LIKE %s OR GIA_NHAP LIKE %s OR THANH_TIEN LIKE %s OR NGAY_PN LIKE %s"
        search_pattern = f"%{search_text}%"
        params = (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern, search_pattern)
        return self.query_params(sql, params)

    def get_ma_ncc(self):
        """Lấy dữ liệu mã nhà cung cấp"""
        sql = "SELECT MA_NCC FROM NHACUNGCAP"
        return self.query(sql)

    def get_ma_sp(self):
        """Lấy dữ liệu mã sản phẩm"""
        sql = "SELECT MA_SP FROM SANPHAM"
        return self.query(sql)