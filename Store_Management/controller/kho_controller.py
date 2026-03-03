from tkinter import messagebox, END

from Store_Management.controller.controller import Controller
from Store_Management.model.kho_model import KhoModel
from Store_Management.view.kho_view import KhoView


class KhoController(Controller):
    def __init__(self, model, view, parent_controller= None):
        super().__init__(model, view)
        self.kho_model = KhoModel()
        self.dashboard_controller = parent_controller
        self.title = "INVENTORY LIST"
        self.headers = ["Inventory ID", "Product ID", "Product Name", "Unit", "Quantity", "Last Updated"]

    def click_ql_kho(self, user_role):
        """Gán sự kiện nút quản lý kho"""
        # Đóng giao diện
        print("Show Inventory UI")
        self.dashboard_controller.close_widget()

        # Hiển thị giao diện quản lý lương
        self.kho_view = KhoView(self.view)
        self.kho_view.ql_kho_widget()
        self.kho_view.pack(fill="both", expand=True)

        # Gán sự kiện nút quay lại
        self.kho_view.btn_return_kho.config(command=self.dashboard_controller.click_btn_return)

        # Hiển thị dữ liệu lên bảng
        self.load_all_kho()

        # Hiển thị dữ liệu mã sp
        self.kho_view.cb_ma_sp['values'] = self.get_ma_sp()

        # Gán sự kiện khi chọn mã sp
        self.kho_view.cb_ma_sp.bind("<<ComboboxSelected>>", self.on_ma_sp_selected)

        # Gắn sự kiện chọn dòng trong bảng
        self.kho_view.tree.bind("<<TreeviewSelect>>", self.select_row_kho)

        # Gắn sự kiện nút thêm kho
        self.kho_view.btn_add_kho.config(command=self.click_add_kho)

        # Gắn sự kiện nút sửa kho
        self.kho_view.btn_update.config(command=self.click_update_kho)

        # Gắn sự kiện nút làm mới kho
        self.kho_view.btn_refresh_kho.config(command=self.click_refresh_kho)

        # Gắn sự kiện nút tìm kiếm kho
        self.kho_view.btn_search_kho.config(command=self.click_search_kho)

        # Gắn sự kiện nút in kho
        self.kho_view.btn_printer_kho.config(command=self.click_print_kho)

        # Gắn sự kiện nút xuất file csv kho
        self.kho_view.btn_csv_kho.config(command=self.click_csv_kho)

        # Gắn sự kiện nút xuất file excel kho
        self.kho_view.btn_excel_kho.config(command=self.click_excel_kho)

        # Gắn sự kiện nút làm mới bảng kho
        self.kho_view.btn_refresh_treeview_kho.config(command=self.update_treeview_kho)

        # Gắn sự kiện nút xóa kho
        self.kho_view.btn_delete.config(command=self.click_delete_kho)

        # Gắn sự kiện nút tính tồn kho
        self.kho_view.btn_tinh_ton_kho.config(command=self.click_tinh_ton_kho)

        # Ẩn các nút nếu là staff
        self.hide_buttons_for_staff(user_role)

    def hide_buttons_for_staff(self, user_role):
        """Ẩn các nút Sửa và Xóa nếu người dùng là staff"""
        if user_role == "staff":
            # Kiểm tra các nút và ẩn chúng nếu người dùng là staff
            if hasattr(self.kho_view, 'btn_update') and self.kho_view.btn_update.winfo_exists():
                self.kho_view.btn_update.config(state='disabled')
            if hasattr(self.kho_view, 'btn_delete') and self.kho_view.btn_delete.winfo_exists():
                self.kho_view.btn_delete.config(state='disabled')

    def get_ma_sp(self):
        """Lấy toàn bộ dữ liệu mã sản phẩm"""
        # Lấy dữ liệu từ model
        raw_data = self.kho_model.get_ma_sp()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data

    def on_ma_sp_selected(self, event):
        """Sự kiện chọn mã sp"""
        # Lấy sp được chọn
        ma_sp = self.kho_view.cb_ma_sp.get()

        # Lấy tên sp tương ứng
        if ma_sp:
            ten_sp = self.get_ten_sp(ma_sp)
            don_vi = self.get_don_vi(ma_sp)

            # Hiển thị tên sp trong Entry
            self.kho_view.entry_ten_sp.config(state="normal")
            self.kho_view.entry_ten_sp.delete(0, "end")
            self.kho_view.entry_ten_sp.insert(0, ten_sp)
            self.kho_view.entry_ten_sp.config(state="readonly")

            # Hiển thị đơn vị trong Entry
            self.kho_view.entry_don_vi.config(state="normal")
            self.kho_view.entry_don_vi.delete(0, "end")
            self.kho_view.entry_don_vi.insert(0, don_vi)
            self.kho_view.entry_don_vi.config(state="readonly")

    def click_tinh_ton_kho(self):
        """Xử lý sự kiện nút tính tồn kho"""
        # Lấy mã sp
        ma_sp = self.kho_view.cb_ma_sp.get()

        # Gọi phương thức tính tồn kho
        result = self.kho_model.tinh_ton_kho(ma_sp)
        ton_kho = result [0][4]

        # Hiển thị tồn kho lên Entry
        self.kho_view.entry_ton_kho.config(state="normal")
        self.kho_view.entry_ton_kho.delete(0, "end")
        self.kho_view.entry_ton_kho.insert(0, str(ton_kho))
        self.kho_view.entry_ton_kho.config(state="readonly")

    def get_ten_sp(self, ma_sp):
        """Lấy dữ liệu tên sp của bảng"""
        # Lấy dữ liệu từ model
        raw_data = self.kho_model.get_ten_sp(ma_sp)

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data[0][0]

    def get_don_vi(self, ma_sp):
        """Lấy dữ liệu đơn vị của bảng"""
        # Lấy dữ liệu từ model
        raw_data = self.kho_model.get_don_vi(ma_sp)

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data[0][0]

    def load_all_kho(self):
        """Lấy toàn bộ dữ liệu lương"""
        # Lấy dữ liệu từ model
        raw_data = self.kho_model.get_all_kho()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]

        # Chèn dữ liệu vào bảng Treeview
        for row in data:
            self.kho_view.tree.insert("", "end", values=row)

    def get_data_kho(self):
        """Lấy dữ liệu từ các trường nhập"""
        # Lấy và chuyển đổi kiểu dữ liệu từ các trường nhập
        ma_kho = self.kho_view.entry_ma_kho.get()
        ma_sp = self.kho_view.cb_ma_sp.get()
        ten_sp = self.kho_view.entry_ten_sp.get()
        don_vi = self.kho_view.entry_don_vi.get()
        ton_kho = int(self.kho_view.entry_ton_kho.get() or 0)
        ngay_cap_nhat = self.kho_view.entry_ngay_cn.get()
        return ma_kho, ma_sp, ten_sp, don_vi, ton_kho, ngay_cap_nhat

    def click_add_kho(self):
        """Sự kiện nhấn nút thêm kho"""
        # Lấy dữ liệu sp từ các trường nhập
        ma_kho, ma_sp, ten_sp, don_vi, ton_kho, ngay_cap_nhat = self.get_data_kho()

        if ma_kho and ma_sp and ten_sp and don_vi and ton_kho and ngay_cap_nhat:
            # Gọi phương thức add_kho trong model
            results = self.kho_model.add_kho(ma_kho, ma_sp, ten_sp, don_vi, ton_kho, ngay_cap_nhat)

            if results:
                messagebox.showinfo("Notification", "Added successfully")
                # Làm mới TreeView
                self.update_treeview_kho()
                self.click_refresh_kho()
            else:
                messagebox.showerror("Error", "Failed to add")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_refresh_kho(self):
        """Sự kiện nhấn nút làm mới các trường dữ liệu"""
        self.kho_view.entry_ma_kho.delete(0, END)
        self.kho_view.cb_ma_sp.set("Choose Product ID")
        self.Kho_view.entry_ngay_cn.delete(0, END)

        # Reset trường nhập tên sp
        self.kho_view.entry_ten_sp.config(state="normal")
        self.kho_view.entry_ten_sp.delete(0, "end")
        self.kho_view.entry_ten_sp.config(state="readonly")

        # Reset trường nhập đơn vị
        self.kho_view.entry_don_vi.config(state="normal")
        self.kho_view.entry_don_vi.delete(0, "end")
        self.kho_view.entry_don_vi.config(state="readonly")

        # Reset trường nhập tồn kho
        self.kho_view.entry_ton_kho.config(state="normal")
        self.kho_view.entry_ton_kho.delete(0, "end")
        self.kho_view.entry_ton_kho.config(state="readonly")

    def click_delete_kho(self):
        """Sự kiện nhấn nút xóa kho"""
        selected_item = self.kho_view.tree.selection()
        if selected_item:
            ma_kho = self.kho_view.tree.item(selected_item[0])["values"][0]
            # Gọi phương thức delete_luong trong model
            results = self.kho_model.delete_kho(ma_kho)
            if results:
                messagebox.showinfo("Notification", "Deleted successfully")
                self.update_treeview_luong()
            else:
                messagebox.showerror("Error", "Failed to delete")
            self.click_refresh_luong()
        else:
            messagebox.showwarning("Warning", "Please select a row to delete")

    def update_treeview_kho(self):
        """Cập nhật bảng Treeview sau khi xóa dữ liệu"""
        # Xóa tất cả dữ liệu trong Treeview trước khi cập nhật
        self.clear_treeview()
        # Lấy lại tất cả dữ liệu lương
        self.load_all_kho()

    def select_row_kho(self, event):
        """Chọn một dòng trên bảng Treeview"""
        # Lấy ID của dòng được chọn
        selected_item = self.kho_view.tree.selection()
        if selected_item:
            # Lấy dữ liệu từ dòng được chọn
            values = self.kho_view.tree.item(selected_item[0])["values"]

            # Xóa dữ liệu vào các trường nhập liệu
            self.click_refresh_kho()

            # Đưa dữ liệu vào các trường nhập liệu
            # Mã kho
            self.kho_view.entry_ma_kho.insert(0, values[0])

            # Mã sp
            self.kho_view.cb_ma_sp.set(values[1])

            # Tên sp
            ten_sp = values[2]
            self.kho_view.entry_ten_sp.config(state="normal")
            self.kho_view.entry_ten_sp.insert(0, ten_sp)
            self.kho_view.entry_ten_sp.config(state="readonly")

            # Đơn vị
            don_vi = values[3]
            self.kho_view.entry_don_vi.config(state="normal")
            self.kho_view.entry_don_vi.insert(0, don_vi)
            self.kho_view.entry_don_vi.config(state="readonly")

            # Tồn kho
            ton_kho = values[4]
            self.kho_view.entry_ton_kho.config(state="normal")
            self.kho_view.entry_ton_kho.insert(0, ton_kho)
            self.kho_view.entry_ton_kho.config(state="readonly")

            # Ngày cập nhât
            self.kho_view.entry_ngay_cn.insert(0, values[5])

    def click_update_kho(self):
        """Sự kiện nhấn nút sửa dữ liệu kho"""
        # Lấy dữ liệu nv từ các trường nhập
        ma_kho, ma_sp, ten_sp, don_vi, ton_kho, ngay_cap_nhat = self.get_data_kho()

        if ma_kho and ma_sp and ten_sp and don_vi and ton_kho and ngay_cap_nhat:
            # Gọi phương thức update_kho trong model
            results = self.kho_model.update_kho(ma_kho, ma_sp, ten_sp, don_vi, ton_kho, ngay_cap_nhat)

            if results:
                messagebox.showinfo("Notification", "Updated successfully")
                # Làm mới TreeView
                self.update_treeview_kho()
                self.click_refresh_kho()
            else:
                messagebox.showerror("Error", "Failed to update")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_search_kho(self):
        """Xử lý sự kiện nhấn nút tìm kiếm kho"""

        # Lấy giá trị từ ô tìm kiếm
        search_text = self.kho_view.entry_search_kho.get()

        # Gọi hàm search_kho trong Model
        raw_data = self.kho_model.search_kho(search_text)

        # Chuyển dữ liệu thành dạng tuple
        results = [tuple(row) for row in raw_data]

        # Xóa dữ liệu trong bảng Treeview
        self.clear_treeview()

        # Hiển thị kết quả lên TreeView
        if results:
            # Thêm kết quả tìm kiếm vào bảng Treeview
            for row in results:
                self.kho_view.tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("Notification", "No results found")

        # Xóa nội dung ô tìm kiếm
        self.kho_view.entry_search_kho.delete(0, "end")

    def get_all_row_kho(self):
        """Lấy dữ liệu từ Treeview kho"""
        return [self.kho_view.tree.item(item, "values") for item in self.kho_view.tree.get_children()]

    def clear_treeview(self):
        """Xóa tất cả dữ liệu trên bảng Treeview"""
        for item in self.kho_view.tree.get_children():
            self.kho_view.tree.delete(item)

    def click_print_kho(self):
        """Sự kiện in danh sách kho"""
        self.click_print(self.title, self.get_all_row_kho(), self.headers)

    def click_csv_kho(self):
        """Sự kiện xuất file CSV"""
        self.click_csv(self.title, self.get_all_row_kho(), self.headers)

    def click_excel_kho(self):
        """Sự kiện xuất file Excel"""
        self.click_excel(self.title, self.get_all_row_kho(), self.headers)