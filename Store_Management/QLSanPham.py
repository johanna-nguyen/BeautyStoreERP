from abc import ABC, abstractmethod

class AbcSanPham(ABC):
    @abstractmethod
    def tinh_gia_ban(self):
        pass

class SanPham(AbcSanPham):
    def __init__(self, ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap):
        self._ma_sp = ma_sp
        self._ten_sp = ten_sp
        self._loai_sp = loai_sp
        self._don_vi = don_vi
        self._chi_phi = chi_phi
        self._gia_nhap = gia_nhap
        self._gia_ban = 0

class ChamSocDa(SanPham):
    def __init__(self, ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap):
        super().__init__(ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap)

    def tinh_gia_ban(self):
        gia = self._gia_nhap + self._chi_phi * 1.1 + 0.25 * self._gia_nhap
        self._gia_ban = gia
        return self._gia_ban

class TrangDiem(SanPham):
    def __init__(self, ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap):
        super().__init__(ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap)

    def tinh_gia_ban(self):
        gia = self._gia_nhap + self._chi_phi* 1.2 + 0.3 * self._gia_nhap
        self._gia_ban = gia
        return self._gia_ban

class NuocHoa(SanPham):
    def __init__(self, ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap):
        super().__init__(ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap)

    def tinh_gia_ban(self):
        gia = self._gia_nhap + self._chi_phi * 1.15 + 0.4 * self._gia_nhap
        self._gia_ban = gia
        return self._gia_ban

















