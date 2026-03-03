from tkinter import messagebox, END, ttk

from Store_Management.controller.controller import Controller
from Store_Management.model.nhacungcap_model import NccModel
from Store_Management.view.nhacungcap_view import NccView


class NccController(Controller):
    def __init__(self, model, view, parent_controller=None):
        super().__init__(model, view)
        self.ncc_model = NccModel()
        self.dashboard_controller = parent_controller
        self.title = "SUPPLIER LIST"
        self.headers = ["Supplier ID", "Name", "Address", "Phone Number"]

    def click_ql_ncc(self, user_role):
        """Gán sự kiện nút quản lý nhà cung cấp"""
        # Đóng giao diện
        print("Show Supplier UI")
        self.dashboard_controller.close_widget()


        # Hiển thị giao diện quản lý nhà cung cấp
        self.ncc_view = NccView(self.view)
        self.ncc_view.ql_ncc_widget()
        self.ncc_view.pack(fill="both", expand=True)

        # Gán sự kiện nút quay lại dashboard
        self.ncc_view.btn_return_ncc.config(command=self.dashboard_controller.click_btn_return)

        # Hiển thị dữ liệu lên bảng
        self.load_all_ncc()

        # Gắn sự kiện chọn dòng trong bảng
        self.ncc_view.tree.bind("<<TreeviewSelect>>", self.select_row_ncc)

        # Gắn sự kiện nút thêm ncc
        self.ncc_view.btn_add_ncc.config(command=self.click_add_ncc)

        # Gắn sự kiện nút sửa ncc
        self.ncc_view.btn_update.config(command=self.click_update_ncc)

        # Gắn sự kiện nút làm mới ncc
        self.ncc_view.btn_refresh_ncc.config(command=self.click_refresh_ncc)

        # Gắn sự kiện nút tìm kiếm ncc
        self.ncc_view.btn_search_ncc.config(command=self.click_search_ncc)

        # Gắn sự kiện nút in ncc
        self.ncc_view.btn_printer_ncc.config(command=self.click_print_ncc)

        # Gắn sự kiện nút xuất file csv ncc
        self.ncc_view.btn_csv_ncc.config(command=self.click_csv_ncc)

        # Gắn sự kiện nút xuất file excel ncc
        self.ncc_view.btn_excel_ncc.config(command=self.click_excel_ncc)

        # Gắn sự kiện nút làm mới bảng ncc
        self.ncc_view.btn_refresh_treeview_ncc.config(command=self.update_treeview_ncc)

        # Gắn sự kiện nút xóa ncc
        self.ncc_view.btn_delete.config(command=self.click_delete_ncc)

        # Ẩn các nút nếu là staff
        self.hide_buttons_for_staff(user_role)

    def hide_buttons_for_staff(self, user_role):
        """Ẩn các nút Sửa và Xóa nếu người dùng là staff"""
        if user_role == "staff":
            # Kiểm tra các nút và ẩn chúng nếu người dùng là staff
            if hasattr(self.ncc_view, 'btn_update') and self.ncc_view.btn_update.winfo_exists():
                self.ncc_view.btn_update.config(state='disabled')
            if hasattr(self.ncc_view, 'btn_delete') and self.ncc_view.btn_delete.winfo_exists():
                self.ncc_view.btn_delete.config(state='disabled')

    def load_all_ncc(self):
        """Lấy toàn bộ dữ liệu nhà cung cấp"""
        # Lấy dữ liệu từ ncc
        raw_data = self.ncc_model.get_all_ncc()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]

        # Chèn dữ liệu vào bảng Treeview
        for row in data:
            self.ncc_view.tree.insert("", "end", values=row)

    def get_data_ncc(self):
        """Lấy dữ liệu sản phẩm từ các trường"""
        ma_ncc = self.ncc_view.entry_ma_ncc.get()
        ten_ncc = self.ncc_view.entry_ten_ncc.get()
        dia_chi = self.ncc_view.entry_dia_chi_ncc.get()
        sdt = self.ncc_view.entry_sdt_ncc.get()
        return ma_ncc, ten_ncc, dia_chi, sdt

    def click_add_ncc(self):
        """Sự kiện nhấn nút thêm nhà cung cấp"""
        # Lấy dữ liệu từ các trường
        ma_ncc, ten_ncc, dia_chi, sdt = self.get_data_ncc()

        if ma_ncc and ten_ncc and dia_chi and sdt:
            # Gọi phương thức thêm nhà cung cấp trong model
            results = self.ncc_model.add_ncc(ma_ncc, ten_ncc, dia_chi, sdt)
            if results:
                messagebox.showinfo("Notification", "Added successfully")
                # Làm mới TreeView
                self.update_treeview_ncc()
                self.click_refresh_ncc()
            else:
                messagebox.showerror("Error", "Failed to add")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_refresh_ncc(self):
        """Sự kiện nhấn nút làm mới các trường dữ liệu"""
        self.ncc_view.entry_ma_ncc.delete(0, END)
        self.ncc_view.entry_ten_ncc.delete(0, END)
        self.ncc_view.entry_dia_chi_ncc.delete(0, END)
        self.ncc_view.entry_sdt_ncc.delete(0, END)

    def click_delete_ncc(self):
        """Sự kiện nhấn nút xóa nhà cung cấp"""
        selected_item = self.ncc_view.tree.selection()
        if selected_item:
            ma_ncc = self.ncc_view.tree.item(selected_item[0])["values"][0]
            # Gọi phương thức delete_ncc trong model
            results = self.ncc_model.delete_ncc(ma_ncc)
            if results:
                messagebox.showinfo("Notification", "Deleted successfully")
                self.update_treeview_ncc()
            else:
                messagebox.showerror("Error", "Failed to delete")
            self.click_refresh_ncc()
        else:
            messagebox.showwarning("Warning", "Please select a row to delete")

    def update_treeview_ncc(self):
        """Cập nhật bảng Treeview sau khi xóa dữ liệu"""
        # Xóa tất cả dữ liệu trong Treeview trước khi cập nhật
        self.clear_treeview()
        # Lấy lại tất cả dữ liệu nhà cung cấp
        self.load_all_ncc()

    def select_row_ncc(self, event):
        """Chọn một dòng trên bảng Treeview"""
        # Lấy ID của dòng được chọn
        selected_item = self.ncc_view.tree.selection()
        if selected_item:
            # Lấy dữ liệu từ dòng được chọn
            values = self.ncc_view.tree.item(selected_item[0])["values"]

            # Xóa dữ liệu các trường
            self.click_refresh_ncc()

            # Đưa dữ liệu vào các trường nhập liệu
            # Mã nhà cung cấp
            self.ncc_view.entry_ma_ncc.insert(0, values[0])

            # Tên nhà cung cấp
            self.ncc_view.entry_ten_ncc.insert(0, values[1])

            # Địa chỉ
            self.ncc_view.entry_dia_chi_ncc.insert(0, values[2])

            # Số điện thoại
            self.ncc_view.entry_sdt_ncc.insert(0, values[3])

    def click_update_ncc(self):
        """Sự kiện nhấn nút sửa dữ liệu nhà cung cấp"""
        # Lấy dữ liệu từ các trường nhập liệu
        ma_ncc, ten_ncc, dia_chi, sdt = self.get_data_ncc()

        if ma_ncc and ten_ncc and dia_chi and sdt:
            # Gọi phương thức update_ncc trong model
            results = self.ncc_model.update_ncc(ma_ncc, ten_ncc, dia_chi, sdt)

            if results:
                messagebox.showinfo("Notification", "Updated successfully")
                # Làm mới TreeView
                self.update_treeview_ncc()
                self.click_refresh_ncc()
            else:
                messagebox.showerror("Error", "Failed to update")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_search_ncc(self):
        """Xử lý sự kiện nhấn nút tìm kiếm nhà cung cấp"""
        # Lấy giá trị từ ô tìm kiếm
        search_text = self.ncc_view.entry_search_ncc.get()

        # Gọi hàm search_ncc trong Model
        raw_data = self.ncc_model.search_ncc(search_text)

        # Chuyển dữ liệu thành dạng tuple
        results = [tuple(row) for row in raw_data]

        # Xóa dữ liệu trong bảng Treeview
        self.clear_treeview()

        # Hiển thị kết quả lên TreeView
        if results:
            # Thêm kết quả tìm kiếm vào bảng Treeview
            for row in results:
                self.ncc_view.tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("Notification", "No results found")
        # Xóa nội dung ô tìm kiếm
        self.ncc_view.entry_search_ncc.delete(0, "end")


    def click_print_ncc(self):
        """Sự kiện in danh sách nhà cung cấp"""
        self.click_print(self.title, self.get_all_row_ncc(), self.get_column_headers_ncc())


    def get_all_row_ncc(self):
        """Lấy dữ liệu từ Treeview nhà cung cấp"""
        return [self.ncc_view.tree.item(item, "values") for item in self.ncc_view.tree.get_children()]

    def clear_treeview(self):
        """Xóa tất cả dữ liệu trên bảng Treeview"""
        for item in self.ncc_view.tree.get_children():
            self.ncc_view.tree.delete(item)

    def click_csv_ncc(self):
        """Sự kiện xuất file CSV"""
        self.click_csv(self.title, self.get_all_row_ncc(), self.headers)

    def click_excel_ncc(self):
        """Sự kiện xuât file Excel"""
        self.click_excel(self.title, self.get_all_row_ncc(), self.headers)
