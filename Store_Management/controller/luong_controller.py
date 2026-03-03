from tkinter import messagebox, END

from Store_Management.QLLuong import NVBanHang, NVThuNgan, NVQuanLy
from Store_Management.controller.controller import Controller
from Store_Management.model.luong_model import LuongModel
from Store_Management.view.luong_view import LuongView


class LuongController(Controller):
    def __init__(self, model, view, parent_controller = None):
        super().__init__(model, view)
        self.luong_model = LuongModel()
        self.dashboard_controller = parent_controller
        self.title = "PAYROLL LIST"
        self.headers = ["Salary ID", "Employee ID", "Job Title", "Base Salary", "Sales Revenue", "Working Hour","Role Coefficient", "Allowance", "Performance Bonus", "Monthly Salary", "Payroll Date"]

    def click_ql_luong(self, user_role):
        """Gán sự kiện nút quản lý lương"""
        # Đóng giao diện
        print("Show Payroll UI")
        self.dashboard_controller.close_widget()

        # Hiển thị giao diện quản lý lương
        self.luong_view = LuongView(self.view)
        self.luong_view.ql_luong_widget()
        self.luong_view.pack(fill="both", expand=True)

        # Gán sự kiện nút quay lại
        self.luong_view.btn_return_luong.config(command=self.dashboard_controller.click_btn_return)

        # Hiển thị dữ liệu lên bảng
        self.load_all_luong()

        # Hiển thị dữ liệu mã nv
        self.luong_view.cb_ma_nv['values'] = self.get_ma_nv()

        # Gán sự kiện khi chọn mã nhân viên
        self.luong_view.cb_ma_nv.bind("<<ComboboxSelected>>", self.on_ma_nv_selected)

        # Gắn sự kiện chọn dòng trong bảng
        self.luong_view.tree.bind("<<TreeviewSelect>>", self.select_row_luong)

        # Gắn sự kiện nút thêm lương
        self.luong_view.btn_add_luong.config(command=self.click_add_luong)

        # Gắn sự kiện nút sửa lương
        self.luong_view.btn_update.config(command=self.click_update_luong)

        # Gắn sự kiện nút làm mới lương
        self.luong_view.btn_refresh_luong.config(command=self.click_refresh_luong)

        # Gắn sự kiện nút tìm kiếm lương
        self.luong_view.btn_search_luong.config(command=self.click_search_luong)

        # Gắn sự kiện nút in lương
        self.luong_view.btn_printer_luong.config(command=self.click_print_luong)

        # Gắn sự kiện nút xuất file csv lương
        self.luong_view.btn_csv_luong.config(command=self.click_csv_luong)

        # Gắn sự kiện nút xuất file excel lương
        self.luong_view.btn_excel_luong.config(command=self.click_excel_luong)

        # Gắn sự kiện nút làm mới bảng lương
        self.luong_view.btn_refresh_treeview_luong.config(command=self.update_treeview_luong)

        # Gắn sự kiện nút xóa lương
        self.luong_view.btn_delete.config(command=self.click_delete_luong)

        # Gắn sự kiện nút tính lương hàng tháng
        self.luong_view.btn_tinh_luong_ht.config(command=self.click_tinh_luong_ht)

        # Ẩn các nút nếu là staff
        self.hide_buttons_for_staff(user_role)

    def hide_buttons_for_staff(self, user_role):
        """Ẩn các nút Sửa và Xóa nếu người dùng là staff"""
        if user_role == "staff":
            # Kiểm tra các nút và ẩn chúng nếu người dùng là staff
            if hasattr(self.luong_view, 'btn_update') and self.luong_view.btn_update.winfo_exists():
                self.luong_view.btn_update.config(state='disabled')
            if hasattr(self.luong_view, 'btn_delete') and self.luong_view.btn_delete.winfo_exists():
                self.luong_view.btn_delete.config(state='disabled')

    def reset_fields_state(self):
        """Đóng các trường nhập dữ liệu"""
        self.luong_view.entry_he_so_chuc_vu.config(state="disabled")
        self.luong_view.entry_thuong.config(state="disabled")
        self.luong_view.entry_doanh_so.config(state="disabled")
        self.luong_view.entry_tro_cap.config(state="disabled")
        self.luong_view.entry_so_gio_lam.config(state="disabled")

    def on_ma_nv_selected(self, event):
        """Sự kiện chọn mã nhân viên"""
        # Lấy mã nhân viên được chọn
        ma_nv = self.luong_view.cb_ma_nv.get()

        # Lấy chức vụ tương ứng
        if ma_nv:
            chuc_vu = self.get_chuc_vu(ma_nv)

            # Hiển thị chức vụ trong Entry
            self.luong_view.entry_chuc_vu.config(state="normal")
            self.luong_view.entry_chuc_vu.delete(0, "end")
            self.luong_view.entry_chuc_vu.insert(0, chuc_vu)
            self.luong_view.entry_chuc_vu.config(state="readonly")

            # Reset lại các trường khi chọn mã nv
            self.reset_fields_state()

        # Kiểm tra chức vụ và điều chỉnh các trường khác
        if chuc_vu == "Manager":
            self.luong_view.entry_he_so_chuc_vu.config(state="normal")
            self.luong_view.entry_thuong.config(state="normal")
        if chuc_vu == "Sale Staff":
            self.luong_view.entry_doanh_so.config(state="normal")
            self.luong_view.entry_tro_cap.config(state="normal")
        if chuc_vu == "Cashier":
            self.luong_view.entry_so_gio_lam.config(state="normal")
            self.luong_view.entry_thuong.config(state="normal")

    def click_tinh_luong_ht(self):
        """Xử lý sự kiện nút tính lương hàng tháng"""
        try:
            # Lấy và chuyển đổi kiểu dữ liệu từ các trường nhập
            ma_luong = self.luong_view.entry_ma_luong.get()
            ma_nv = self.luong_view.cb_ma_nv.get()
            chuc_vu = self.luong_view.entry_chuc_vu.get()
            luong_cb = float(self.luong_view.entry_luong_cb.get() or 0.0)
            doanh_so = float(self.luong_view.entry_doanh_so.get() or 0.0)
            so_gio_lam = int(self.luong_view.entry_so_gio_lam.get() or 0)
            he_so_chuc_vu = float(self.luong_view.entry_he_so_chuc_vu.get() or 0.0)
            tro_cap = float(self.luong_view.entry_tro_cap.get() or 0.0)
            thuong = float(self.luong_view.entry_thuong.get() or 0.0)
            ngay_tinh_luong = self.luong_view.entry_ngay_tinh_luong.get()

            # Tạo object tương ứng với chức vụ
            if chuc_vu == "Sale Staff":
                nv = NVBanHang(ma_luong, ma_nv, chuc_vu, luong_cb, doanh_so, tro_cap, ngay_tinh_luong)
            elif chuc_vu == "Cashier":
                nv = NVThuNgan(ma_luong, ma_nv, chuc_vu, luong_cb, so_gio_lam, thuong, ngay_tinh_luong)
            elif chuc_vu == "Manager":
                nv = NVQuanLy(ma_luong, ma_nv, chuc_vu, luong_cb, he_so_chuc_vu, thuong, ngay_tinh_luong)
            else:
                messagebox.showerror("Error", "Invalid Job Title")
                return

            # Gọi phương thức tính lương hàng tháng
            luong_ht = nv.tinh_luong_ht()

            # Hiển thị lương ht lên Entry lương ht
            self.luong_view.entry_luong_ht.config(state="normal")
            self.luong_view.entry_luong_ht.delete(0, "end")
            self.luong_view.entry_luong_ht.insert(0, str(luong_ht))
            self.luong_view.entry_luong_ht.config(state="readonly")

        except Exception as e:
            messagebox.showerror("Error", "Please enter valid information")

    def get_ma_nv(self):
        """Lấy toàn bộ dữ liệu mã nhân viên của bảng nhân viên"""
        # Lấy dữ liệu từ model
        raw_data = self.luong_model.get_ma_nv()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data

    def get_chuc_vu(self, ma_nv):
        """Lấy dữ liệu chức vụ của bảng nhân viên"""
        # Lấy dữ liệu từ model
        raw_data = self.luong_model.get_chuc_vu(ma_nv)

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data[0][0]

    def load_all_luong(self):
        """Lấy toàn bộ dữ liệu lương"""
        # Lấy dữ liệu từ model
        raw_data = self.luong_model.get_all_luong()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]

        # Chèn dữ liệu vào bảng Treeview
        for row in data:
            self.luong_view.tree.insert("", "end", values=row)

    def get_data_luong(self):
        """Lấy dữ liệu từ các trường nhập"""
        # Lấy và chuyển đổi kiểu dữ liệu từ các trường nhập
        ma_luong = self.luong_view.entry_ma_luong.get()
        ma_nv = self.luong_view.cb_ma_nv.get()
        chuc_vu = self.luong_view.entry_chuc_vu.get()
        luong_cb = float(self.luong_view.entry_luong_cb.get() or 0.0)
        doanh_so = float(self.luong_view.entry_doanh_so.get() or 0.0)
        so_gio_lam = int(self.luong_view.entry_so_gio_lam.get() or 0)
        he_so_chuc_vu = float(self.luong_view.entry_he_so_chuc_vu.get() or 0.0)
        tro_cap = float(self.luong_view.entry_tro_cap.get() or 0.0)
        thuong = float(self.luong_view.entry_thuong.get() or 0.0)
        luong_ht = float(self.luong_view.entry_luong_ht.get() or 0.0)
        ngay_tinh_luong = self.luong_view.entry_ngay_tinh_luong.get()
        return ma_luong, ma_nv, chuc_vu, luong_cb, doanh_so, so_gio_lam, he_so_chuc_vu, tro_cap, thuong, luong_ht, ngay_tinh_luong

    def click_add_luong(self):
        """Sự kiện nhấn nút thêm lương"""
        # Lấy dữ liệu sp từ các trường nhập
        ma_luong, ma_nv, chuc_vu, luong_cb, doanh_so, so_gio_lam, he_so_chuc_vu, tro_cap, thuong, luong_ht, ngay_tinh_luong = self.get_data_luong()

        if ma_luong or ma_nv or chuc_vu or luong_cb or doanh_so or so_gio_lam or he_so_chuc_vu or tro_cap or thuong or luong_ht or ngay_tinh_luong:
            # Gọi phương thức add_luong trong model
            results = self.luong_model.add_luong(ma_luong, ma_nv, chuc_vu, luong_cb, doanh_so, so_gio_lam, he_so_chuc_vu,
                                           tro_cap, thuong, luong_ht, ngay_tinh_luong)

            if results:
                messagebox.showinfo("Notification", "Added successfully")
                # Làm mới TreeView
                self.update_treeview_luong()
                self.click_refresh_luong()
                self.reset_fields_state()
            else:
                messagebox.showerror("Erro", "Failed to add")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_refresh_luong(self):
        """Sự kiện nhấn nút làm mới các trường dữ liệu"""
        self.luong_view.entry_ma_luong.delete(0, END)
        self.luong_view.cb_ma_nv.set("Choose Employee ID")
        self.luong_view.entry_luong_cb.delete(0, END)
        self.luong_view.entry_doanh_so.delete(0, END)
        self.luong_view.entry_so_gio_lam.delete(0, END)
        self.luong_view.entry_he_so_chuc_vu.delete(0, END)
        self.luong_view.entry_tro_cap.delete(0, END)
        self.luong_view.entry_thuong.delete(0, END)
        self.luong_view.entry_ngay_tinh_luong.delete(0, END)

        # Reset trường nhập chức vụ
        self.luong_view.entry_chuc_vu.config(state="normal")
        self.luong_view.entry_chuc_vu.delete(0, "end")
        self.luong_view.entry_chuc_vu.config(state="readonly")

        # Reset trường nhập lương hàng tháng
        self.luong_view.entry_luong_ht.config(state="normal")
        self.luong_view.entry_luong_ht.delete(0, "end")
        self.luong_view.entry_luong_ht.config(state="readonly")

        self.reset_fields_state()

    def click_delete_luong(self):
        """Sự kiện nhấn nút xóa lương"""
        selected_item = self.view.tree.selection()
        if selected_item:
            ma_luong = self.luong_view.tree.item(selected_item[0])["values"][0]
            # Gọi phương thức delete_luong trong model
            results = self.luong_model.delete_luong(ma_luong)
            if results:
                messagebox.showinfo("Notification", "Deleted successfully")
                self.update_treeview_luong()
            else:
                messagebox.showerror("Error", "Failed to delete")
            self.click_refresh_luong()
        else:
            messagebox.showwarning("Warning", "Please select a row to delete")

    def update_treeview_luong(self):
        """Cập nhật bảng Treeview sau khi xóa dữ liệu"""
        # Xóa tất cả dữ liệu trong Treeview trước khi cập nhật
        self.clear_treeview()
        # Lấy lại tất cả dữ liệu lương
        self.load_all_luong()

    def select_row_luong(self, event):
        """Chọn một dòng trên bảng Treeview"""
        # Lấy ID của dòng được chọn
        selected_item = self.luong_view.tree.selection()
        if selected_item:
            # Lấy dữ liệu từ dòng được chọn
            values = self.luong_view.tree.item(selected_item[0])["values"]

            # Xóa dữ liệu vào các trường nhập liệu
            self.click_refresh_luong()

            # Đưa dữ liệu vào các trường nhập liệu

            # Mã lương
            self.luong_view.entry_ma_luong.insert(0, values[0])

            # Mã nv
            self.luong_view.cb_ma_nv.set(values[1])

            # Chức vụ
            chuc_vu = values[2]
            self.luong_view.entry_chuc_vu.config(state="normal")
            self.luong_view.entry_chuc_vu.insert(0,chuc_vu)
            self.luong_view.entry_chuc_vu.config(state="readonly")

            # Bật các trường dựa trên chức vụ
            if chuc_vu == "Manager":
                # Hệ số chức vụ
                self.luong_view.entry_he_so_chuc_vu.config(state="normal")
                self.luong_view.entry_he_so_chuc_vu.insert(0, values[6])

                # Thưởng
                self.luong_view.entry_thuong.config(state="normal")
                self.luong_view.entry_thuong.insert(0, values[8])
            if chuc_vu == "Sale Staff":
                # Doanh số
                self.luong_view.entry_doanh_so.config(state="normal")
                self.luong_view.entry_doanh_so.insert(0, values[4])

                # Trợ cấp
                self.luong_view.entry_tro_cap.config(state="normal")
                self.luong_view.entry_tro_cap.insert(0, values[7])

            if chuc_vu == "Cashier":
                # Số giờ làm
                self.luong_view.entry_so_gio_lam.config(state="normal")
                self.luong_view.entry_so_gio_lam.insert(0, values[5])

                # Thưởng
                self.luong_view.entry_thuong.config(state="normal")
                self.luong_view.entry_thuong.insert(0, values[8])

            # Lương cơ bản
            self.luong_view.entry_luong_cb.insert(0, values[3])

            # Lương hàng tháng
            self.luong_view.entry_so_gio_lam.config(state="normal")
            self.luong_view.entry_luong_ht.insert(0, values[9])

            # Ngày tính lương
            self.luong_view.entry_ngay_tinh_luong.insert(0, values[10])

    def click_update_luong(self):
        """Sự kiện nhấn nút sửa dữ liệu lương"""
        # Lấy dữ liệu nv từ các trường nhập
        ma_luong, ma_nv, chuc_vu, luong_co_ban, doanh_so, so_gio_lam, he_so_chuc_vu, tro_cap, thuong, luong_ht, ngay_tinh_luong = self.get_data_luong()

        if ma_luong or ma_nv or chuc_vu or luong_co_ban or doanh_so or so_gio_lam or he_so_chuc_vu or tro_cap or thuong or luong_ht or ngay_tinh_luong:
            # Gọi phương thức update_luong trong model
            results = self.luong_model.update_luong(ma_luong, ma_nv, chuc_vu, luong_co_ban, doanh_so, so_gio_lam, he_so_chuc_vu,
                                              tro_cap, thuong, luong_ht, ngay_tinh_luong)

            if results:
                messagebox.showinfo("Notification", "Updated successfully")
                # Làm mới TreeView
                self.update_treeview_luong()
                self.click_refresh_luong()
            else:
                messagebox.showerror("Error", "Failed to update")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_search_luong(self):
        """Xử lý sự kiện nhấn nút tìm kiếm lương"""

        # Lấy giá trị từ ô tìm kiếm
        search_text = self.luong_view.entry_search_luong.get()

        # Gọi hàm search_sp trong Model
        raw_data = self.luong_model.search_luong(search_text)

        # Chuyển dữ liệu thành dạng tuple
        results = [tuple(row) for row in raw_data]

        # Xóa dữ liệu trong bảng Treeview
        self.clear_treeview()

        # Hiển thị kết quả lên TreeView
        if results:
            # Thêm kết quả tìm kiếm vào bảng Treeview
            for row in results:
                self.luong_view.tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("Notification", "No results found")

        # Xóa nội dung ô tìm kiếm
        self.luong_view.entry_search_luong.delete(0, "end")

    def get_all_row_luong(self):
        """Lấy dữ liệu từ Treeview lương"""
        return [self.luong_view.tree.item(item, "values") for item in self.luong_view.tree.get_children()]

    def clear_treeview(self):
        """Xóa tất cả dữ liệu trên bảng Treeview"""
        for item in self.luong_view.tree.get_children():
            self.luong_view.tree.delete(item)

    def click_print_luong(self):
        """Sự kiện in danh sách lương"""
        self.click_print(self.title, self.get_all_row_luong(), self.headers)

    def click_csv_luong(self):
        """Sự kiện xuất file CSV"""
        self.click_csv(self.title, self.get_all_row_luong(), self.headers)

    def click_excel_luong(self):
        """Sự kiện xuât file Excel"""
        self.click_excel(self.title, self.get_all_row_luong(), self.headers)