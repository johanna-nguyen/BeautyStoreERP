from tkinter import messagebox, END

from Store_Management.controller.controller import Controller
from Store_Management.model.phieunhap_model import PNModel
from Store_Management.view.phieunhap_view import PNView


class PNController(Controller):
    def __init__(self, model, view, parent_controller=None):
        super().__init__(model, view)
        self.pn_model = PNModel()
        self.dashboard_controller = parent_controller
        self.title = "PURCHASE ORDERS LIST"
        self.headers =  ["Purchase Orders ID", "Supplier ID", "Product ID", "Quantity", "Purchase Price", "Total", "Date of purchase orders"]

    def click_ql_pn(self, user_role):
        """Gán sự kiện nút quản lý phiếu nhập"""
        # Đóng giao diện
        print("Show Purchase Orders UI")
        self.dashboard_controller.close_widget()

        # Hiển thị giao diện quản lý phiếu nhập
        self.pn_view = PNView(self.view)
        self.pn_view.ql_pn_widget()
        self.pn_view.pack(fill="both", expand=True)

        # Gán sự kiện nút quay lại
        self.pn_view.btn_return_pn.config(command=self.dashboard_controller.click_btn_return)

        # Hiển thị dữ liệu lên bảng
        self.load_all_pn()

        # Hiển thị dữ liệu mã ncc
        self.pn_view.cb_ma_ncc['values'] = self.get_ma_ncc()

        # Hiển thị dữ liệu mã sp
        self.pn_view.cb_ma_sp['values'] = self.get_ma_sp()

        # Gắn sự kiện chọn dòng trong bảng
        self.pn_view.tree.bind("<<TreeviewSelect>>", self.select_row_pn)

        # Gắn sự kiện nút thêm phiếu nhập
        self.pn_view.btn_add_pn.config(command=self.click_add_pn)

        # Gắn sự kiện nút sửa phiếu nhập
        self.pn_view.btn_update.config(command=self.click_update_pn)

        # Gắn sự kiện nút làm mới phiếu nhập
        self.pn_view.btn_refresh_pn.config(command=self.click_refresh_pn)

        # Gắn sự kiện nút tìm kiếm phiếu nhập
        self.pn_view.btn_search_pn.config(command=self.click_search_pn)

        # Gắn sự kiện nút in phiếu nhập
        self.pn_view.btn_printer_pn.config(command=self.click_print_pn)

        # Gắn sự kiện nút xuất file csv phiếu nhập
        self.pn_view.btn_csv_pn.config(command=self.click_csv_pn)

        # Gắn sự kiện nút xuất file excel phiếu nhập
        self.pn_view.btn_excel_pn.config(command=self.click_excel_pn)

        # Gắn sự kiện nút làm mới bảng phiếu nhập
        self.pn_view.btn_refresh_treeview_pn.config(command=self.update_treeview_pn)

        # Gắn sự kiện nút xóa phiếu nhập
        self.pn_view.btn_delete.config(command=self.click_delete_pn)

        # Gắn sự kiện nút tính thành tiền
        self.pn_view.btn_tinh_thanh_tien.config(command=self.click_tinh_thanh_tien)

        # Ẩn các nút nếu là staff
        self.hide_buttons_for_staff(user_role)

    def hide_buttons_for_staff(self, user_role):
        """Ẩn các nút Sửa và Xóa nếu người dùng là staff"""
        if user_role == "staff":
            # Kiểm tra các nút và ẩn chúng nếu người dùng là staff
            if hasattr(self.pn_view, 'btn_update') and self.pn_view.btn_update.winfo_exists():
                self.pn_view.btn_update.config(state='disabled')
            if hasattr(self.pn_view, 'btn_delete') and self.pn_view.btn_delete.winfo_exists():
                self.pn_view.btn_delete.config(state='disabled')


    def click_tinh_thanh_tien(self):
        """Xử lý sự kiện nút tính thành tiền"""
        try:
            # Lấy và chuyển đổi kiểu dữ liệu từ các trường nhập
            gia_nhap = float(self.pn_view.entry_gia_nhap.get() or 0.0)
            so_luong = int(self.pn_view.entry_so_luong.get() or 0)

            # Tính thành tiền
            thanh_tien = gia_nhap * so_luong

            # Hiển thị thành tiền lên Entry
            self.pn_view.entry_thanh_tien.config(state="normal")
            self.pn_view.entry_thanh_tien.delete(0, "end")
            self.pn_view.entry_thanh_tien.insert(0,str(thanh_tien))
            self.pn_view.entry_thanh_tien.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Error", "Please enter valid information")

    def get_ma_ncc(self):
        """Lấy toàn bộ dữ liệu mã nhà cung cấp từ bảng"""
        # Lấy dữ liệu từ model
        raw_data = self.pn_model.get_ma_ncc()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data

    def get_ma_sp(self):
        """Lấy toàn bộ dữ liệu mã sản phẩm từ bảng"""
        # Lấy dữ liệu từ model
        raw_data = self.pn_model.get_ma_sp()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data # Lấy dữ liệu pn từ các trường nhập

    def load_all_pn(self):
        """Lấy toàn bộ dữ liệu phiếu nhập"""
        # Lấy dữ liệu từ model
        raw_data = self.pn_model.get_all_pn()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]

        # Chèn dữ liệu vào bảng Treeview
        for row in data:
            self.pn_view.tree.insert("", "end", values=row)

    def get_data_pn(self):
        """Lấy dữ liệu từ các trường nhập"""
        # Lấy và chuyển đổi kiểu dữ liệu từ các trường nhập
        ma_pn = self.pn_view.entry_ma_pn.get()
        ma_ncc = self.pn_view.cb_ma_ncc.get()
        ma_sp = self.pn_view.cb_ma_sp.get()
        so_luong = int(self.pn_view.entry_so_luong.get() or 0)
        gia_nhap = float(self.pn_view.entry_gia_nhap.get() or 0.0)
        thanh_tien = float(self.pn_view.entry_thanh_tien.get() or 0.0)
        ngay_pn = self.pn_view.entry_ngay_pn.get()
        return ma_pn, ma_ncc, ma_sp, so_luong, gia_nhap, thanh_tien, ngay_pn

    def click_add_pn(self):
        """Sự kiện nhấn nút thêm phiếu nhập"""
        # Lấy dữ liệu pn từ các trường nhập
        ma_pn, ma_ncc, ma_sp, so_luong, gia_nhap, thanh_tien, ngay_pn = self.get_data_pn()

        if ma_pn and ma_ncc and ma_sp and so_luong and gia_nhap and thanh_tien and ngay_pn:
            # Gọi phương thức add_pn trong model
            results = self.pn_model.add_pn(ma_pn, ma_ncc, ma_sp, so_luong, gia_nhap, thanh_tien, ngay_pn)

            if results:
                messagebox.showinfo("Notification", "Added successfully")
                # Làm mới TreeView
                self.update_treeview_pn()
                self.click_refresh_pn()
            else:
                messagebox.showerror("Lỗi", "Failed to add")
        else:
            messagebox.showwarning("Cảnh báo", "Please fill in all required information")

    def click_refresh_pn(self):
        """Sự kiện nhấn nút làm mới các trường dữ liệu"""
        self.pn_view.entry_ma_pn.delete(0, END)
        self.pn_view.cb_ma_ncc.set("Choose Supplier ID")
        self.pn_view.cb_ma_sp.set("Choose Product ID")
        self.pn_view.entry_so_luong.delete(0, END)
        self.pn_view.entry_gia_nhap.delete(0, END)
        self.pn_view.entry_ngay_pn.delete(0, END)

        # Reset trường nhập thành tiền
        self.pn_view.entry_thanh_tien.config(state="normal")
        self.pn_view.entry_thanh_tien.delete(0, "end")
        self.pn_view.entry_thanh_tien.config(state="readonly")

    def click_delete_pn(self):
        """Sự kiện nhấn nút xóa phiếu nhập"""
        selected_item = self.pn_view.tree.selection()
        if selected_item:
            ma_pn = self.pn_view.tree.item(selected_item[0])["values"][0]
            # Gọi phương thức delete_pn trong model
            results = self.pn_model.delete_pn(ma_pn)
            if results:
                messagebox.showinfo("Notification", "Delete successfully")
                self.update_treeview_pn()
            else:
                messagebox.showerror("Error", "Failed to delete")
            self.click_refresh_pn()
        else:
            messagebox.showwarning("Warning", "Please select a row to delete")

    def update_treeview_pn(self):
        """Cập nhật bảng Treeview sau khi xóa dữ liệu"""
        # Xóa tất cả dữ liệu trong Treeview trước khi cập nhật
        self.clear_treeview()
        # Lấy lại tất cả dữ liệu phiếu nhập
        self.load_all_pn()

    def select_row_pn(self, event):
        """Chọn một dòng trên bảng Treeview"""
        # Lấy ID của dòng được chọn
        selected_item = self.pn_view.tree.selection()
        if selected_item:
            # Lấy dữ liệu từ dòng được chọn
            values = self.pn_view.tree.item(selected_item[0])["values"]

            # Xóa dữ liệu vào các trường nhập liệu
            self.click_refresh_pn()

            # Đưa dữ liệu vào các trường nhập liệu
            # Mã phiếu nhập
            self.pn_view.entry_ma_pn.insert(0, values[0])

            # Mã ncc
            self.pn_view.cb_ma_ncc.set(values[1])

            # Mã sp
            self.pn_view.cb_ma_sp.set(values[2])

            # Số lượng
            self.pn_view.entry_so_luong.insert(0, values[3])

            # Giá nhập
            self.pn_view.entry_gia_nhap.insert(0, values[4])

            # Thành tiền
            self.pn_view.entry_thanh_tien.config(state="normal")
            self.pn_view.entry_thanh_tien.insert(0, values[5])
            self.pn_view.entry_thanh_tien.config(state="readonly")

            # Ngày phiếu nhập
            self.pn_view.entry_ngay_pn.insert(0, values[6])

    def click_update_pn(self):
        """Sự kiện nhấn nút sửa dữ liệu phiếu nhập"""
        # Lấy dữ liệu pn từ các trường nhập
        ma_pn, ma_ncc, ma_sp, so_luong, gia_nhap, thanh_tien, ngay_pn = self.get_data_pn()

        if ma_pn and ma_ncc and ma_sp and so_luong and gia_nhap and thanh_tien and ngay_pn:
            # Gọi phương thức update_pn trong model
            results = self.pn_model.update_pn(ma_pn, ma_ncc, ma_sp, so_luong, gia_nhap, thanh_tien, ngay_pn)

            if results:
                messagebox.showinfo("Notification", "Updated successfully")
                # Làm mới TreeView
                self.update_treeview_pn()
                self.click_refresh_pn()
            else:
                messagebox.showerror("Error", "Failed to update")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_search_pn(self):
        """Xử lý sự kiện nhấn nút tìm kiếm phiếu nhập"""
        # Lấy giá trị từ ô tìm kiếm
        search_text = self.pn_view.entry_search_pn.get()

        # Gọi hàm search_sp trong Model
        raw_data = self.pn_model.search_pn(search_text)

        # Chuyển dữ liệu thành dạng tuple
        results = [tuple(row) for row in raw_data]

        # Xóa dữ liệu trong bảng Treeview
        self.clear_treeview()

        # Hiển thị kết quả lên TreeView
        if results:
            # Thêm kết quả tìm kiếm vào bảng Treeview
            for row in results:
                self.pn_view.tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("Notification", "No results found")

        # Xóa nội dung ô tìm kiếm
        self.view.entry_search_pn.delete(0, "end")

    def get_all_row_pn(self):
        """Lấy dữ liệu từ Treeview phiếu nhập"""
        return [self.pn_view.tree.item(item, "values") for item in self.pn_view.tree.get_children()]

    def clear_treeview(self):
        """Xóa tất cả dữ liệu trên bảng Treeview"""
        for item in self.pn_view.tree.get_children():
            self.pn_view.tree.delete(item)

    def click_print_pn(self):
        """Sự kiện in danh sách phiếu nhập"""
        self.click_print(self.title, self.get_all_row_pn(), self.headers)

    def click_csv_pn(self):
        """Sự kiện xuất file CSV"""
        self.click_csv(self.title, self.get_all_row_pn(), self.headers)

    def click_excel_pn(self):
        """Sự kiện xuât file Excel"""
        self.click_excel(self.title, self.get_all_row_pn(), self.headers)