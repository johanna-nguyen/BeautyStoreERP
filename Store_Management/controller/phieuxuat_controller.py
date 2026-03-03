from tkinter import messagebox, END

from Store_Management.controller.controller import Controller
from Store_Management.model.phieuxuat_model import PXModel
from Store_Management.view.phieuxuat_view import PXView


class PXController(Controller):
    def __init__(self, model, view, parent_controller = None):
        super().__init__(model, view)
        self.px_model = PXModel()
        self.dashboard_controller = parent_controller
        self.title = "SALES ORDER LIST"
        self.headers = ["Sales Orders ID", "Customer ID", "Product ID", "Quantity", "Sales Price", "Total", "Employee ID"
                          "Date of sales orders"]


    def click_ql_px(self, user_role):
        """Gán sự kiện nút quản lý phiếu xuất"""
        # Đóng giao diện
        print("Show Sales Orders UI")
        self.dashboard_controller.close_widget()

        # Hiển thị giao diện quản lý phiếu xuaats
        self.px_view = PXView(self.view)
        self.px_view.ql_px_widget()
        self.px_view.pack(fill="both", expand=True)

        # Gán sự kiện nút quay lại
        self.px_view.btn_return_px.config(command=self.dashboard_controller.click_btn_return)

        # Hiển thị dữ liệu lên bảng
        self.load_all_px()

        # Hiển thị dữ liệu mã khách hàng
        self.px_view.cb_ma_kh['values'] = self.get_ma_kh()

        # Hiển thị dữ liệu mã sp
        self.px_view.cb_ma_sp['values'] = self.get_ma_sp()

        # Hiển thị dữ liệu mã nv
        self.px_view.cb_nguoi_xuat['values'] = self.get_ma_nv()

        # Gắn sự kiện chọn dòng trong bảng
        self.px_view.tree.bind("<<TreeviewSelect>>", self.select_row_px)

        # Gắn sự kiện nút thêm phiếu xuất
        self.px_view.btn_add_px.config(command=self.click_add_px)

        # Gắn sự kiện nút sửa phiếu xuất
        self.px_view.btn_update.config(command=self.click_update_px)

        # Gắn sự kiện nút làm mới phiếu xuất
        self.px_view.btn_refresh_px.config(command=self.click_refresh_px)

        # Gắn sự kiện nút tìm kiếm phiếu xuất
        self.px_view.btn_search_px.config(command=self.click_search_px)

        # Gắn sự kiện nút in phiếu xuất
        self.px_view.btn_printer_px.config(command=self.click_print_px)

        # Gắn sự kiện nút xuất file csv phiếu xuất
        self.px_view.btn_csv_px.config(command=self.click_csv_px)

        # Gắn sự kiện nút xuất file excel phiếu xuất
        self.px_view.btn_excel_px.config(command=self.click_excel_px)

        # Gắn sự kiện nút làm mới bảng phiếu xuất
        self.px_view.btn_refresh_treeview_px.config(command=self.update_treeview_px)

        # Gắn sự kiện nút xóa phiếu xuất
        self.px_view.btn_delete.config(command=self.click_delete_px)

        # Gắn sự kiện nút tính thành tiền
        self.px_view.btn_tinh_thanh_tien.config(command=self.click_tinh_thanh_tien)

        # Ẩn các nút nếu là staff
        self.hide_buttons_for_staff(user_role)

    def hide_buttons_for_staff(self, user_role):
        """Ẩn các nút Sửa và Xóa nếu người dùng là staff"""
        if user_role == "staff":
            # Kiểm tra các nút và ẩn chúng nếu người dùng là staff
            if hasattr(self.px_view, 'btn_update') and self.px_view.btn_update.winfo_exists():
                self.px_view.btn_update.config(state='disabled')
            if hasattr(self.px_view, 'btn_delete') and self.px_view.btn_delete.winfo_exists():
                self.px_view.btn_delete.config(state='disabled')

    def click_tinh_thanh_tien(self):
        """Xử lý sự kiện nút tính thành tiền"""
        try:
            # Lấy và chuyển đổi kiểu dữ liệu từ các trường nhập
            gia_xuat = float(self.px_view.entry_gia_xuat.get() or 0.0)
            so_luong = int(self.px_view.entry_so_luong.get() or 0)

            # Tính thành tiền
            thanh_tien = gia_xuat * so_luong

            # Hiển thị thành tiền lên Entry
            self.px_view.entry_thanh_tien.config(state="normal")
            self.px_view.entry_thanh_tien.delete(0, "end")
            self.px_view.entry_thanh_tien.insert(0, str(thanh_tien))
            self.px_view.entry_thanh_tien.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Error", "Please enter valid information")

    def get_ma_kh(self):
        """Lấy toàn bộ dữ liệu mã khách hàng từ bảng"""
        # Lấy dữ liệu từ model
        raw_data = self.px_model.get_ma_kh()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data

    def get_ma_sp(self):
        """Lấy toàn bộ dữ liệu mã sản phẩm từ bảng"""
        # Lấy dữ liệu từ model
        raw_data = self.px_model.get_ma_sp()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data

    def get_ma_nv(self):
        """Lấy toàn bộ dữ liệu mã nhân viên từ bảng"""
        # Lấy dữ liệu từ model
        raw_data = self.px_model.get_ma_nv()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data

    def load_all_px(self):
        """Lấy toàn bộ dữ liệu phiếu xuất"""
        # Lấy dữ liệu từ model
        raw_data = self.px_model.get_all_px()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]

        # Chèn dữ liệu vào bảng Treeview
        for row in data:
            self.px_view.tree.insert("", "end", values=row)

    def get_data_px(self):
        """Lấy dữ liệu từ các trường nhập"""
        # Lấy và chuyển đổi kiểu dữ liệu từ các trường nhập
        ma_px = self.px_view.entry_ma_px.get()
        ma_kh = self.px_view.cb_ma_kh.get()
        ma_sp = self.px_view.cb_ma_sp.get()
        so_luong = int(self.px_view.entry_so_luong.get() or 0)
        gia_xuat = float(self.px_view.entry_gia_xuat.get() or 0.0)
        thanh_tien = float(self.px_view.entry_thanh_tien.get() or 0.0)
        nguoi_xuat = self.px_view.cb_nguoi_xuat.get()
        ngay_px = self.px_view.entry_ngay_px.get()
        return ma_px, ma_kh, ma_sp, so_luong, gia_xuat, thanh_tien, nguoi_xuat, ngay_px

    def click_add_px(self):
        """Sự kiện nhấn nút thêm phiếu xuất"""
        # Lấy dữ liệu pn từ các trường nhập
        ma_px, ma_kh, ma_sp, so_luong, gia_xuat, thanh_tien, nguoi_xuat, ngay_px = self.get_data_px()

        if ma_px and ma_kh and ma_sp and so_luong and gia_xuat and thanh_tien and nguoi_xuat and ngay_px:
            # Gọi phương thức add_px trong model
            results = self.px_model.add_px(ma_px, ma_kh, ma_sp, so_luong, gia_xuat, thanh_tien, nguoi_xuat, ngay_px)

            if results:
                messagebox.showinfo("Notification", "Added successfully")
                # Làm mới TreeView
                self.update_treeview_px()
                self.click_refresh_px()
            else:
                messagebox.showerror("Error", "Faile to add")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_refresh_px(self):
        """Sự kiện nhấn nút làm mới các trường dữ liệu"""
        self.px_view.entry_ma_px.delete(0, END)
        self.px_view.cb_ma_kh.set("Choose Customer ID")
        self.px_view.cb_ma_sp.set("Choose Product ID")
        self.px_view.entry_so_luong.delete(0, END)
        self.px_view.entry_gia_xuat.delete(0, END)
        self.px_view.entry_ngay_px.delete(0, END)
        self.px_view.cb_nguoi_xuat.set("Choose Employee ID")

        # Reset trường nhập thành tiền
        self.px_view.entry_thanh_tien.config(state="normal")
        self.px_view.entry_thanh_tien.delete(0, "end")
        self.px_view.entry_thanh_tien.config(state="readonly")

    def click_delete_px(self):
        """Sự kiện nhấn nút xóa phiếu xuất"""
        selected_item = self.px_view.tree.selection()
        if selected_item:
            ma_px = self.px_view.tree.item(selected_item[0])["values"][0]
            # Gọi phương thức delete_px trong model
            results = self.px_model.delete_px(ma_px)
            if results:
                messagebox.showinfo("Notification", "Delete successfully")
                self.update_treeview_px()
            else:
                messagebox.showerror("Error", "Failed to delete")
            self.click_refresh_px()
        else:
            messagebox.showwarning("Warning", "Please select a row to delete")

    def update_treeview_px(self):
        """Cập nhật bảng Treeview sau khi xóa dữ liệu"""
        # Xóa tất cả dữ liệu trong Treeview trước khi cập nhật
        self.clear_treeview()
        # Lấy lại tất cả dữ liệu phiếu xuất
        self.load_all_px()

    def select_row_px(self, event):
        """Chọn một dòng trên bảng Treeview"""
        # Lấy ID của dòng được chọn
        selected_item = self.px_view.tree.selection()
        if selected_item:
            # Lấy dữ liệu từ dòng được chọn
            values = self.px_view.tree.item(selected_item[0])["values"]

            # Xóa dữ liệu vào các trường nhập liệu
            self.click_refresh_px()

            # Đưa dữ liệu vào các trường nhập liệu
            # Mã phiếu xuất
            self.px_view.entry_ma_px.insert(0, values[0])

            # Mã kh
            self.px_view.cb_ma_kh.set(values[1])

            # Mã sp
            self.px_view.cb_ma_sp.set(values[2])

            # Số lượng
            self.px_view.entry_so_luong.insert(0, values[3])

            # Giá xuất
            self.px_view.entry_gia_xuat.insert(0, values[4])

            # Thành tiền
            self.px_view.entry_thanh_tien.config(state="normal")
            self.px_view.entry_thanh_tien.insert(0, values[5])
            self.px_view.entry_thanh_tien.config(state="readonly")

            # Người xuất
            self.px_view.cb_nguoi_xuat.set(values[6])

            # Ngày phiếu xuất
            self.px_view.entry_ngay_px.insert(0, values[7])

    def click_update_px(self):
        """Sự kiện nhấn nút sửa dữ liệu phiếu xuất"""
        # Lấy dữ liệu pn từ các trường nhập
        ma_px, ma_kh, ma_sp, so_luong, gia_xuat, thanh_tien, nguoi_xuat, ngay_px = self.get_data_px()

        if ma_px and ma_kh and ma_sp and so_luong and gia_xuat and thanh_tien and nguoi_xuat and ngay_px:
            # Gọi phương thức update_pn trong model
            results = self.px_model.update_px(ma_px, ma_kh, ma_sp, so_luong, gia_xuat, thanh_tien, nguoi_xuat, ngay_px)

            if results:
                messagebox.showinfo("Notification", "Edit successfully")
                # Làm mới TreeView
                self.update_treeview_px()
                self.click_refresh_px()
            else:
                messagebox.showerror("Error", "Failed to edit")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_search_px(self):
        """Xử lý sự kiện nhấn nút tìm kiếm phiếu xuất"""
        # Lấy giá trị từ ô tìm kiếm
        search_text = self.px_view.entry_search_px.get()

        # Gọi hàm search_sp trong Model
        raw_data = self.px_model.search_px(search_text)

        # Chuyển dữ liệu thành dạng tuple
        results = [tuple(row) for row in raw_data]

        # Xóa dữ liệu trong bảng Treeview
        self.clear_treeview()

        # Hiển thị kết quả lên TreeView
        if results:
            # Thêm kết quả tìm kiếm vào bảng Treeview
            for row in results:
                self.px_view.tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("Notification", "No results found")

        # Xóa nội dung ô tìm kiếm
        self.px_view.entry_search_px.delete(0, "end")

    def get_all_row_px(self):
        """Lấy dữ liệu từ Treeview phiếu nhập"""
        return [self.px_view.tree.item(item, "values") for item in self.px_view.tree.get_children()]

    def clear_treeview(self):
        """Xóa tất cả dữ liệu trên bảng Treeview"""
        for item in self.px_view.tree.get_children():
            self.px_view.tree.delete(item)

    def click_print_px(self):
        """Sự kiện in danh sách phiếu xuất"""
        self.click_print(self.title, self.get_all_row_px(), self.headers)

    def click_csv_px(self):
        """Sự kiện xuất file CSV"""
        self.click_csv(self.title, self.get_all_row_px(), self.headers)

    def click_excel_px(self):
        """Sự kiện xuât file Excel"""
        self.click_excel(self.title, self.get_all_row_px(), self.headers)