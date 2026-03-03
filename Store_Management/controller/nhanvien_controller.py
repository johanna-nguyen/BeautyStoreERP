from tkinter import messagebox, END

from Store_Management.controller.controller import Controller
from Store_Management.model.nhanvien_model import NVModel
from Store_Management.view.nhanvien_view import NVView


class NVController(Controller):
    def __init__(self, model, view, parent_controller=None):
        super().__init__(model, view)
        self.nv_model = NVModel()
        self.dashboard_controller = parent_controller
        self.title = "EMPLOYEES LIST"
        self.headers = ["Employee ID", "Name", "DOB", "Gender", "Job title", "Address", "Phone Number", "Email"]

    def click_ql_nv(self, user_role):
        """Gán sự kiện nút quản lý nhân viên"""
        # Đóng giao diện
        print("Show Employees UI")
        self.dashboard_controller.close_widget()

        # Hiển thị giao diện quản lý nhân viên
        self.nv_view = NVView(self.view)
        self.nv_view.ql_nv_widget()
        self.nv_view.pack(fill="both", expand=True)

        # Gán sự kiện nút quay lại
        self.nv_view.btn_return_nv.config(command=self.dashboard_controller.click_btn_return)

        # Hiển thị dữ liệu lên bảng
        self.load_all_nv()

        # Gắn sự kiện chọn dòng trong bảng
        self.nv_view.tree.bind("<<TreeviewSelect>>", self.select_row_nv)

        # Gắn sự kiện nút thêm nv
        self.nv_view.btn_add_nv.config(command=self.click_add_nv)

        # Gắn sự kiện nút sửa nv
        self.nv_view.btn_update.config(command=self.click_update_nv)

        # Gắn sự kiện nút làm mới nv
        self.nv_view.btn_refresh_nv.config(command=self.click_refresh_nv)

        # Gắn sự kiện nút tìm kiếm nv
        self.nv_view.btn_search_nv.config(command=self.click_search_nv)

        # Gắn sự kiện nút in nv
        self.nv_view.btn_printer_nv.config(command=self.click_print_nv)

        # Gắn sự kiện nút xuất file csv nv
        self.nv_view.btn_csv_nv.config(command=self.click_csv_nv)

        # Gắn sự kiện nút xuất file excel nv
        self.nv_view.btn_excel_nv.config(command=self.click_excel_nv)

        # Gắn sự kiện nút làm mới bảng nv
        self.nv_view.btn_refresh_treeview_nv.config(command=self.update_treeview_nv)

        # Gắn sự kiện nút xóa nv
        self.nv_view.btn_delete.config(command=self.click_delete_nv)

        # Ẩn các nút nếu là staff
        self.hide_buttons_for_staff(user_role)

    def hide_buttons_for_staff(self, user_role):
        """Ẩn các nút Sửa và Xóa nếu người dùng là staff"""
        if user_role == "staff":
            # Kiểm tra các nút và ẩn chúng nếu người dùng là staff
            if hasattr(self.nv_view, 'btn_update') and self.nv_view.btn_update.winfo_exists():
                self.nv_view.btn_update.config(state='disabled')
            if hasattr(self.nv_view, 'btn_delete') and self.nv_view.btn_delete.winfo_exists():
                self.nv_view.btn_delete.config(state='disabled')

    def load_all_nv(self):
        """Lấy toàn bộ dữ liệu nhân viên"""
        # Lấy dữ liệu từ
        raw_data = self.nv_model.get_all_nv()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]

        # Chèn dữ liệu vào bảng Treeview
        for row in data:
            self.nv_view.tree.insert("", "end", values=row)

    def get_data_nv(self):
        """Lấy dữ liệu từ các trường nhập"""
        ma_nv = self.nv_view.entry_ma_nv.get()
        ten_nv = self.nv_view.entry_ten_nv.get()
        ngay_sinh = self.nv_view.entry_ngay_sinh.get()
        gioi_tinh = self.nv_view.gioi_tinh_var.get()
        chuc_vu = self.nv_view.cb_chuc_vu.get()
        dia_chi = self.nv_view.entry_dia_chi_nv.get()
        sdt_nv = self.nv_view.entry_sdt_nv.get()
        email = self.nv_view.entry_email.get()
        return ma_nv, ten_nv, ngay_sinh, gioi_tinh, chuc_vu, dia_chi, sdt_nv, email

    def click_add_nv(self):
        """Sự kiện nhấn nút thêm nhân viên"""
        # Lấy dữ liệu sp từ các trường nhập
        ma_nv, ten_nv, ngay_sinh, gioi_tinh, chuc_vu, dia_chi, sdt_nv, email = self.get_data_nv()

        if ma_nv and ten_nv and ngay_sinh and gioi_tinh and chuc_vu and dia_chi and sdt_nv and email:
            # Gọi phương thức add_nv trong model
            results = self.nv_model.add_nv(ma_nv, ten_nv, ngay_sinh, gioi_tinh, chuc_vu, dia_chi, sdt_nv, email)

            if results:
                messagebox.showinfo("Notification", "Added successfully")
                # Làm mới TreeView
                self.update_treeview_nv()
                self.click_refresh_nv()
            else:
                messagebox.showerror("Error", "Failed to add")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_refresh_nv(self):
        """Sự kiện nhấn nút làm mới các trường dữ liệu"""
        self.nv_view.entry_ma_nv.delete(0, END)
        self.nv_view.entry_ten_nv.delete(0, END)
        self.nv_view.entry_ngay_sinh.delete(0, END)
        self.nv_view.gioi_tinh_var.set("0")
        self.nv_view.cb_chuc_vu.set("Select job title")
        self.nv_view.entry_dia_chi_nv.delete(0, END)
        self.nv_view.entry_sdt_nv.delete(0, END)
        self.nv_view.entry_email.delete(0, END)

    def click_delete_nv(self):
        """Sự kiện nhấn nút xóa nhân viên"""
        selected_item = self.nv_view.tree.selection()
        if selected_item:
            ma_nv = self.nv_view.tree.item(selected_item[0])["values"][0]
            # Gọi phương thức delete_nv trong model
            results = self.nv_model.delete_nv(ma_nv)
            if results:
                messagebox.showinfo("Notification", "Deleted successfully")
                self.update_treeview_nv()
            else:
                messagebox.showerror("Error", "Failed to delete")
            self.click_refresh_nv()
        else:
            messagebox.showwarning("Warning", "Please select a row to delete")

    def update_treeview_nv(self):
        """Cập nhật bảng Treeview sau khi xóa dữ liệu"""
        # Xóa tất cả dữ liệu trong Treeview trước khi cập nhật
        self.clear_treeview()
        # Lấy lại tất cả dữ liệu nhân viên
        self.load_all_nv()

    def select_row_nv(self, event):
        """Chọn một dòng trên bảng Treeview"""
        # Lấy ID của dòng được chọn
        selected_item = self.nv_view.tree.selection()
        if selected_item:
            # Lấy dữ liệu từ dòng được chọn
            values = self.nv_view.tree.item(selected_item[0])["values"]

            # Xóa dữ liệu vào các trường nhập liệu
            self.click_refresh_nv()

            # Đưa dữ liệu vào các trường nhập liệu
            # Mã nv
            self.nv_view.entry_ma_nv.insert(0, values[0])

            # Tên nv
            self.nv_view.entry_ten_nv.insert(0, values[1])

            # Ngày sinh
            self.nv_view.entry_ngay_sinh.insert(0, values[2])

            # Giới tính
            self.nv_view.gioi_tinh_var.set(values[3])

            # Chức vụ
            self.nv_view.cb_chuc_vu.set(values[4])

            # Địa chỉ
            self.nv_view.entry_dia_chi_nv.insert(0, values[5])

            # Số điện thoại
            self.nv_view.entry_sdt_nv.insert(0, values[6])

            # Email
            self.nv_view.entry_email.insert(0, values[7])

    def click_update_nv(self):
        """Sự kiện nhấn nút sửa dữ liệu nhân viên"""
        # Lấy dữ liệu nv từ các trường nhập
        ma_nv, ten_nv, ngay_sinh, gioi_tinh, chuc_vu, dia_chi, sdt_nv, email = self.get_data_nv()

        if ma_nv and ten_nv and ngay_sinh and gioi_tinh and chuc_vu and dia_chi and sdt_nv and email:
            # Gọi phương thức update_nv trong model
            results = self.nv_model.update_nv(ma_nv, ten_nv, ngay_sinh, gioi_tinh, chuc_vu, dia_chi, sdt_nv, email)

            if results:
                messagebox.showinfo("Notification", "Updated successfully")
                # Làm mới TreeView
                self.update_treeview_nv()
                self.click_refresh_nv()
            else:
                messagebox.showerror("Error", "Failed to update")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_search_nv(self):
        """Xử lý sự kiện nhấn nút tìm kiếm nhân viên"""

        # Lấy giá trị từ ô tìm kiếm
        search_text = self.nv_view.entry_search_nv.get()

        # Gọi hàm search_sp trong Model
        raw_data = self.nv_model.search_nv(search_text)

        # Chuyển dữ liệu thành dạng tuple
        results = [tuple(row) for row in raw_data]

        # Xóa dữ liệu trong bảng Treeview
        self.clear_treeview()

        # Hiển thị kết quả lên TreeView
        if results:
            # Thêm kết quả tìm kiếm vào bảng Treeview
            for row in results:
                self.nv_view.tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("Notification", "No results found")

        # Xóa nội dung ô tìm kiếm
        self.nv_view.entry_search_nv.delete(0, "end")

    def get_all_row_nv(self):
        """Lấy dữ liệu từ Treeview nhân viên"""
        return [self.nv_view.tree.item(item, "values") for item in self.nv_view.tree.get_children()]

    def clear_treeview(self):
        """Xóa tất cả dữ liệu trên bảng Treeview"""
        for item in self.nv_view.tree.get_children():
            self.nv_view.tree.delete(item)

    def click_print_nv(self):
        """Sự kiện in danh sách nhân viên"""
        self.click_print(self.title, self.get_all_row_nv(), self.headers)

    def click_csv_nv(self):
        """Sự kiện xuất file CSV"""
        self.click_csv(self.title, self.get_all_row_nv(), self.headers)

    def click_excel_nv(self):
        """Sự kiện xuât file Excel"""
        self.click_excel(self.title, self.get_all_row_nv(), self.headers)