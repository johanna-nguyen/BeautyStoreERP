from tkinter import messagebox, END

from Store_Management.controller.controller import Controller
from Store_Management.model.khanhhang_model import KHModel
from Store_Management.view.khachhang_view import KHView


class KHController(Controller):
    def __init__(self, model, view, parent_controller=None):
        super().__init__(model, view)
        self.kh_model = KHModel()
        self.dashboard_controller = parent_controller
        self.title = "CUSTOMERS LIST"
        self.headers = ["Customer ID", "Name", "DOB", "Gender", "Type", "Address", "Phone Number"]

    def click_ql_kh(self, user_role):
        """Gán sự kiện nút quản lý khách hàng"""
        # Đóng giao diện
        print("Show Customer UI")
        self.dashboard_controller.close_widget()

        # Hiển thị giao diện quản lý khách hàng
        self.kh_view = KHView(self.view)
        self.kh_view.ql_kh_widget()
        self.kh_view.pack(fill="both", expand=True)

        # Gán sự kiện nút quay lại
        self.kh_view.btn_return_kh.config(command=self.dashboard_controller.click_btn_return)

        # Hiển thị dữ liệu lên bảng
        self.load_all_kh()

        # Gắn sự kiện chọn dòng trong bảng
        self.kh_view.tree.bind("<<TreeviewSelect>>", self.select_row_kh)

        # Gắn sự kiện nút thêm kh
        self.kh_view.btn_add_kh.config(command=self.click_add_kh)

        # Gắn sự kiện nút sửa kh
        self.kh_view.btn_update.config(command=self.click_update_kh)

        # Gắn sự kiện nút làm mới kh
        self.kh_view.btn_refresh_kh.config(command=self.click_refresh_kh)

        # Gắn sự kiện nút tìm kiếm kh
        self.kh_view.btn_search_kh.config(command=self.click_search_kh)

        # Gắn sự kiện nút in kh
        self.kh_view.btn_printer_kh.config(command=self.click_print_kh)

        # Gắn sự kiện nút xuất file csv kh
        self.kh_view.btn_csv_kh.config(command=self.click_csv_kh)

        # Gắn sự kiện nút xuất file excel kh
        self.kh_view.btn_excel_kh.config(command=self.click_excel_kh)

        # Gắn sự kiện nút làm mới bảng kh
        self.kh_view.btn_refresh_treeview_kh.config(command=self.update_treeview_kh)

        # Gắn sự kiện nút xóa kh
        self.kh_view.btn_delete.config(command=self.click_delete_kh)

        # Ẩn các nút nếu là staff
        self.hide_buttons_for_staff(user_role)

    def hide_buttons_for_staff(self, user_role):
        """Ẩn các nút Sửa và Xóa nếu người dùng là staff"""
        if user_role == "staff":
            # Kiểm tra các nút và ẩn chúng nếu người dùng là staff
            if hasattr(self.kh_view, 'btn_update') and self.kh_view.btn_update.winfo_exists():
                self.kh_view.btn_update.config(state='disabled')
            if hasattr(self.kh_view, 'btn_delete') and self.kh_view.btn_delete.winfo_exists():
                self.kh_view.btn_delete.config(state='disabled')

    def load_all_kh(self):
        """Lấy toàn bộ dữ liệu khách hàng"""
        # Lấy dữ liệu từ model
        raw_data = self.kh_model.get_all_kh()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]

        # Chèn dữ liệu vào bảng Treeview
        for row in data:
            self.kh_view.tree.insert("", "end", values=row)

    def get_data_kh(self):
        """Lấy dữ liệu từ các trường nhập"""
        ma_kh = self.kh_view.entry_ma_kh.get()
        ten_kh = self.kh_view.entry_ten_kh.get()
        ngay_sinh = self.kh_view.entry_ngay_sinh_kh.get()
        gioi_tinh = self.kh_view.gioi_tinh_var_kh.get()
        hang_kh = self.kh_view.cb_hang_kh.get()
        dia_chi = self.kh_view.entry_dia_chi_kh.get()
        sdt_kh = self.kh_view.entry_sdt_kh.get()
        return ma_kh, ten_kh, ngay_sinh, gioi_tinh, hang_kh, dia_chi, sdt_kh

    def click_add_kh(self):
        """Sự kiện nhấn nút thêm khách hàng"""
        # Lấy dữ liệu sp từ các trường nhập
        ma_kh, ten_kh, ngay_sinh, gioi_tinh, hang_kh, dia_chi, sdt_kh = self.get_data_kh()

        if ma_kh and ten_kh and ngay_sinh and gioi_tinh and hang_kh and dia_chi and sdt_kh:
            # Gọi phương thức add_kh trong model
            results = self.kh_model.add_kh(ma_kh, ten_kh, ngay_sinh, gioi_tinh, hang_kh, dia_chi, sdt_kh)

            if results:
                messagebox.showinfo("Notification", "Added successfully")
                # Làm mới TreeView
                self.update_treeview_kh()
                self.click_refresh_kh()
            else:
                messagebox.showerror("Error", "Failed to add")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_refresh_kh(self):
        """Sự kiện nhấn nút làm mới các trường dữ liệu"""
        self.kh_view.entry_ma_kh.delete(0, END)
        self.kh_view.entry_ten_kh.delete(0, END)
        self.kh_view.entry_ngay_sinh_kh.delete(0, END)
        self.kh_view.gioi_tinh_var_kh.set("0")
        self.kh_view.cb_hang_kh.set("Choose type")
        self.kh_view.entry_dia_chi_kh.delete(0, END)
        self.kh_view.entry_sdt_kh.delete(0, END)

    def click_delete_kh(self):
        """Sự kiện nhấn nút xóa khách hàng"""
        selected_item = self.kh_view.tree.selection()
        if selected_item:
            ma_kh = self.kh_view.tree.item(selected_item[0])["values"][0]
            # Gọi phương thức delete_nv trong model
            results = self.kh_model.delete_kh(ma_kh)
            if results:
                messagebox.showinfo("Notification", "Deleted successfully")
                self.update_treeview_kh()
            else:
                messagebox.showerror("Error", "Failed to delete")
            self.click_refresh_kh()
        else:
            messagebox.showwarning("Warning", "Please select a row to delete")

    def update_treeview_kh(self):
        """Cập nhật bảng Treeview sau khi xóa dữ liệu"""
        # Xóa tất cả dữ liệu trong Treeview trước khi cập nhật
        self.clear_treeview()
        # Lấy lại tất cả dữ liệu khách hàng
        self.load_all_kh()

    def select_row_kh(self, event):
        """Chọn một dòng trên bảng Treeview"""
        # Lấy ID của dòng được chọn
        selected_item = self.kh_view.tree.selection()
        if selected_item:
            # Lấy dữ liệu từ dòng được chọn
            values = self.kh_view.tree.item(selected_item[0])["values"]

            # Xóa dữ liệu vào các trường nhập liệu
            self.click_refresh_kh()

            # Đưa dữ liệu vào các trường nhập liệu
            # Mã kh
            self.kh_view.entry_ma_kh.insert(0, values[0])

            # Tên kh
            self.kh_view.entry_ten_kh.insert(0, values[1])

            # Ngày sinh
            self.kh_view.entry_ngay_sinh_kh.insert(0, values[2])

            # Giới tính
            self.kh_view.gioi_tinh_var_kh.set(values[3])

            # Hạng kh
            self.kh_view.cb_hang_kh.set(values[4])

            # Địa chỉ
            self.kh_view.entry_dia_chi_kh.insert(0, values[5])

            # Số điện thoại
            self.kh_view.entry_sdt_kh.insert(0, values[6])

    def click_update_kh(self):
        """Sự kiện nhấn nút sửa dữ liệu khách hàng"""
        # Lấy dữ liệu nv từ các trường nhập
        ma_kh, ten_kh, ngay_sinh, gioi_tinh, hang_kh, dia_chi, sdt_kh = self.get_data_kh()

        if ma_kh and ten_kh and ngay_sinh and gioi_tinh and hang_kh and dia_chi and sdt_kh:
            # Gọi phương thức update_kh trong model
            results = self.kh_model.update_kh(ma_kh, ten_kh, ngay_sinh, gioi_tinh, hang_kh, dia_chi, sdt_kh)

            if results:
                messagebox.showinfo("Notification", "Updated successfully")
                # Làm mới TreeView
                self.update_treeview_kh()
                self.click_refresh_kh()
            else:
                messagebox.showerror("Error", "Failed to update")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_search_kh(self):
        """Xử lý sự kiện nhấn nút tìm kiếm khách hàng"""

        # Lấy giá trị từ ô tìm kiếm
        search_text = self.kh_view.entry_search_kh.get()

        # Gọi hàm search_sp trong Model
        raw_data = self.kh_model.search_kh(search_text)

        # Chuyển dữ liệu thành dạng tuple
        results = [tuple(row) for row in raw_data]

        # Xóa dữ liệu trong bảng Treeview
        self.clear_treeview()

        # Hiển thị kết quả lên TreeView
        if results:
            # Thêm kết quả tìm kiếm vào bảng Treeview
            for row in results:
                self.kh_view.tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("Notification", "No returns found")

        # Xóa nội dung ô tìm kiếm
        self.kh_view.entry_search_kh.delete(0, "end")

    def get_all_row_kh(self):
        """Lấy dữ liệu từ Treeview khách hàng"""
        return [self.kh_view.tree.item(item, "values") for item in self.kh_view.tree.get_children()]

    def clear_treeview(self):
        """Xóa tất cả dữ liệu trên bảng Treeview"""
        for item in self.kh_view.tree.get_children():
            self.kh_view.tree.delete(item)

    def click_print_kh(self):
        """Sự kiện in danh sách khách hàng"""
        self.click_print(self.title, self.get_all_row_kh(), self.headers)

    def click_csv_kh(self):
        """Sự kiện xuất file CSV"""
        self.click_csv(self.title, self.get_all_row_kh(), self.headers)

    def click_excel_kh(self):
        """Sự kiện xuât file Excel"""
        self.click_excel(self.title, self.get_all_row_kh(), self.headers)