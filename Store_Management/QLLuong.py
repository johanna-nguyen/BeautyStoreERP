from abc import ABC, abstractmethod

class AbcNhanVien(ABC):
    @abstractmethod
    def tinh_luong_ht(self):
        pass

class NhanVien(AbcNhanVien):
    def __init__(self, ma_luong, ma_nv, chuc_vu, luong_cb, ngay_tinh_luong):
        self._ma_luong = ma_luong
        self._ma_nv = ma_nv
        self._chuc_vu = chuc_vu
        self._luong_cb = luong_cb
        self.ngay_tinh_luong = ngay_tinh_luong
        self._luong_ht = 0

class NVBanHang(NhanVien):
    def __init__(self, ma_luong, ma_nv, chuc_vu, luong_cb, doanh_so, tro_cap, ngay_tinh_luong):
        super().__init__( ma_luong, ma_nv, chuc_vu, luong_cb, ngay_tinh_luong)
        self.__doanh_so = doanh_so
        self.__tro_cap = tro_cap

    def tinh_luong_ht(self):
        luong = self._luong_cb + self.__doanh_so * 0.02 + self.__tro_cap
        self._luong_ht = luong
        return self._luong_ht

class NVThuNgan(NhanVien):
    def __init__(self, ma_luong, ma_nv, chuc_vu, luong_cb, so_gio_lam, thuong, ngay_tinh_luong):
        super().__init__(ma_luong, ma_nv, chuc_vu, luong_cb, ngay_tinh_luong)
        self.__so_gio_lam = so_gio_lam
        self.__thuong = thuong

    def tinh_luong_ht(self):
        luong = self._luong_cb + self.__so_gio_lam * 50_000 + self.__thuong
        self._luong_ht = luong
        return self._luong_ht

class NVQuanLy(NhanVien):
    def __init__(self, ma_luong, ma_nv, chuc_vu, luong_cb, he_so_chuc_vu, thuong, ngay_tinh_luong):
        super().__init__(ma_luong, ma_nv, chuc_vu, luong_cb, ngay_tinh_luong)
        self.__he_so_chuc_vu = he_so_chuc_vu
        self.__thuong = thuong

    def tinh_luong_ht(self):
        luong = self._luong_cb * self.__he_so_chuc_vu + self.__thuong
        self._luong_ht = luong
        return self._luong_ht

















