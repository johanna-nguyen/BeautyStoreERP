from Store_Management.model.model import Model


class NccModel(Model):
    def __init__(self):
        super().__init__()

    def get_all_ncc(self):
        """Lấy dữ liệu nhà cung cấp"""
        sql = "SELECT * FROM NHACUNGCAP"
        return self.query(sql)


    def add_ncc(self, ma_ncc, ten_ncc, dia_chi, sdt):
        """Thêm dữ liệu nhà cung cấp mới"""
        sql = "INSERT INTO NHACUNGCAP (MA_NCC, TEN_NCC, DIA_CHI, SO_DIEN_THOAI) VALUES (%s, %s, %s, %s)"
        params = (ma_ncc, ten_ncc, dia_chi, sdt)
        return self.query_params(sql, params)


    def delete_ncc(self, ma_ncc):
        """Xóa dữ liệu nhà cung cấp"""
        sql = "DELETE FROM NHACUNGCAP WHERE MA_NCC = %s"
        params = (ma_ncc,)
        return self.query_params(sql, params)


    def update_ncc(self, ma_ncc, ten_ncc, dia_chi, sdt):
        """Sửa dữ liệu nhà cung cấp"""
        sql = "UPDATE NHACUNGCAP SET TEN_NCC = %s, DIA_CHI = %s, SO_DIEN_THOAI = %s  WHERE MA_NCC = %s"
        params = (ten_ncc, dia_chi, sdt, ma_ncc)
        return self.query_params(sql, params)


    def search_ncc(self, search_text):
        """Tìm kiếm nhà cung cấp"""
        sql = "SELECT * FROM NHACUNGCAP WHERE MA_NCC LIKE %s OR TEN_NCC LIKE %s OR DIA_CHI LIKE %s OR SO_DIEN_THOAI LIKE %s"
        search_pattern = f"%{search_text}%"
        params = (search_pattern, search_pattern, search_pattern, search_pattern)
        return self.query_params(sql, params)