from dotenv import load_dotenv
import os
import sys
from tkinter import messagebox

from Store_Management.controller.controller import Controller
from Store_Management.controller.khachhang_controller import KHController
from Store_Management.controller.kho_controller import KhoController
from Store_Management.controller.luong_controller import LuongController
from Store_Management.controller.nhacungcap_controller import NccController
from Store_Management.controller.nhanvien_controller import NVController
from Store_Management.controller.phieunhap_controller import PNController
from Store_Management.controller.phieuxuat_controller import PXController
from Store_Management.controller.sanpham_controller import SPController
from Store_Management.controller.thongke_controller import ThongKeController
from Store_Management.view.dashboard_view import DashboardView


class DashboardController(Controller):
    def __init__(self, model, view):
        super().__init__(model, view)

        # Gán sự kiện nút login
        self.view.login_view.btn_login.config(command=self.click_login)

    def close_widget(self):
        """Đóng giao diện"""
        for widget in self.view.winfo_children():
            widget.destroy()

    def click_btn_return(self):
        """Sự kiện nút quay lại"""
        # Đóng giao diện
        self.close_widget()

        # Hiển thị lại giao diện dashboard và sử dụng user_role đã lưu
        self.show_dashboard()

    def click_logout(self):
        """Sự kiện nút logout hoát ứng dụng."""
        response = messagebox.askyesno("Confirmation", "Are you sure you want to exit?")
        if response:
            # Đóng toàn bộ chương trình
            sys.exit()

    def click_login(self):
        """Sự kiện nút đãng nhập"""
        load_dotenv()
        ADMIN = os.getenv("ADMIN_USERNAME")
        STAFF = os.getenv("STAFF_USERNAME")
        PASSWORD = os.getenv("PASSWORD")

        username = self.view.login_view.entry_user.get()
        password = self.view.login_view.entry_pw.get()

        if username == ADMIN and password == PASSWORD:
            self.view.user_role = "admin"
            print("Logged in as admin")


        elif username == STAFF and password == PASSWORD:
            self.view.user_role = "staff"
            print("Logged in as staff")

        else:
            messagebox.showerror("Error", "Invalid username or password")
            return

        self.close_widget()
        self.show_dashboard()

    def show_dashboard(self):
        print("Show Dashboard")
        """Sự kiện hiển thị giao diện dashboard và gán sự kiện cho các nút"""
        user_role = self.view.user_role  # Lấy user_role từ view

        # Hiển thị giao diện dashboard
        self.view.dashboard_view= DashboardView(self.view)
        self.view.dashboard_view.pack(fill="both", expand=True)
        self.view.dashboard_view.dashboard_widget()

        # Giao diện nhà cung cấp
        self.ncc_controller = NccController(self.model, self.view, parent_controller=self)

        # Giao diện sản phẩm
        self.sp_controller = SPController(self.model, self.view, parent_controller=self)

        # Giao diện nhân viên
        self.nv_controller = NVController(self.model, self.view, parent_controller=self)

        # Giao diện quản lý lương
        self.luong_controller = LuongController(self.model, self.view, parent_controller=self)

        # Giao diện khách hàng
        self.kh_controller = KHController(self.model, self.view, parent_controller=self)

        # Giao diện phiếu nhập
        self.pn_controller = PNController(self.model, self.view, parent_controller=self)

        # Giao diện phiếu xuất
        self.px_controller = PXController(self.model, self.view, parent_controller=self)

        # Giao diện kho
        self.kho_controller = KhoController(self.model, self.view, parent_controller=self)

        # Giao diện thống kê
        self.tk_controller = ThongKeController(self.model, self.view, parent_controller=self)

        # Gán sự kiện cho các nút trong dashboard
        # Nút nhà cung cấp
        if hasattr(self.view.dashboard_view, 'btn_ql_ncc'):
            self.view.dashboard_view.btn_ql_ncc.config(command=lambda: self.ncc_controller.click_ql_ncc(user_role))

        # Nút sản phẩm
        if hasattr(self.view.dashboard_view, 'btn_ql_sp'):
            self.view.dashboard_view.btn_ql_sp.config(command=lambda: self.sp_controller.click_ql_sp(user_role))

        # Nút nhân viên
        if hasattr(self.view.dashboard_view, 'btn_ql_nv'):
            self.view.dashboard_view.btn_ql_nv.config(command=lambda: self.nv_controller.click_ql_nv(user_role))


        if hasattr(self.view.dashboard_view, 'btn_ql_luong'):
            self.view.dashboard_view.btn_ql_luong.config(command=lambda: self.luong_controller.click_ql_luong(user_role))

        # Nút khách hàng
        if hasattr(self.view.dashboard_view, 'btn_ql_kh'):
            self.view.dashboard_view.btn_ql_kh.config(command=lambda: self.kh_controller.click_ql_kh(user_role))

        # Nút phiếu nhập
        if hasattr(self.view.dashboard_view, 'btn_ql_pn'):
            self.view.dashboard_view.btn_ql_pn.config(command=lambda: self.pn_controller.click_ql_pn(user_role))

        # Nút phiếu xuất
        if hasattr(self.view.dashboard_view, 'btn_ql_px'):
            self.view.dashboard_view.btn_ql_px.config(command=lambda: self.px_controller.click_ql_px(user_role))

        # Nút kho
        if hasattr(self.view.dashboard_view, 'btn_ql_kho'):
            self.view.dashboard_view.btn_ql_kho.config(command=lambda: self.kho_controller.click_ql_kho(user_role))

        # Nút thống kê
        if hasattr(self.view.dashboard_view, 'btn_thong_ke'):
            self.view.dashboard_view.btn_thong_ke.config(command=self.tk_controller.click_thong_ke)

        # Nút đăng xuất
        if hasattr(self.view.dashboard_view, 'btn_logout'):
            self.view.dashboard_view.btn_logout.config(command=self.click_logout)

        # Ẩn các nút Sửa và Xóa nếu người dùng là staff
        self.hide_buttons_for_staff(user_role)