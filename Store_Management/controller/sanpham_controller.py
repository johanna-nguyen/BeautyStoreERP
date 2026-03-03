from tkinter import messagebox, END

from Store_Management.controller.controller import Controller
from Store_Management.model.sanpham_model import SPModel
from Store_Management.view.sanpham_view import SPView


class SPController(Controller):
    def __init__(self, model, view, parent_controller=None):
        super().__init__(model, view)
        self.sp_model = SPModel()
        self.dashboard_controller = parent_controller
        self.title = "PRODUCT LIST"
        self.headers = ["Product ID", "Name", "Category", "Unit", "Cost", "Purchase Price", "Selling Price"]

    def click_ql_sp(self, user_role):
        """Gán sự kiện nút quản lý sản phẩm"""
        # Đóng giao diện
        print("Show Product UI")
        self.dashboard_controller.close_widget()

        # Hiển thị giao diện quản lý sản phẩm
        self.sp_view = SPView(self.view)
        self.sp_view.ql_sp_widget()
        self.sp_view.pack(fill="both", expand=True)

        # Gán sự kiện nút quay lại
        self.sp_view.btn_return_sp.config(command=self.dashboard_controller.click_btn_return)

        # Hiển thị dữ liệu lên bảng
        self.load_all_sp()

        # Gắn sự kiện chọn dòng trong bảng
        self.sp_view.tree.bind("<<TreeviewSelect>>", self.select_row_sp)

        # Gắn sự kiện nút thêm sp
        self.sp_view.btn_add_sp.config(command=self.click_add_sp)

        # Gắn sự kiện nút sửa sp
        self.sp_view.btn_update.config(command=self.click_update_sp)

        # Gắn sự kiện nút làm mới sp
        self.sp_view.btn_refresh_sp.config(command=self.click_refresh_sp)

        # Gắn sự kiện nút tìm kiếm sp
        self.sp_view.btn_search_sp.config(command=self.click_search_sp)

        # Gắn sự kiện nút in sp
        self.sp_view.btn_printer_sp.config(command=self.click_print_sp)

        # Gắn sự kiện nút xuất file csv sp
        self.sp_view.btn_csv_sp.config(command=self.click_csv_sp)

        # Gắn sự kiện nút xuất file excel sp
        self.sp_view.btn_excel_sp.config(command=self.click_excel_sp)

        # Gắn sự kiện nút làm mới bảng sp
        self.sp_view.btn_refresh_treeview_sp.config(command=self.update_treeview_sp)

        # Gắn sự kiện nút xóa sp
        self.sp_view.btn_delete.config(command=self.click_delete_sp)

        # Gắn sự kiện nút tính giá bán sp
        self.sp_view.btn_tinh_gia_ban_sp.config(command=self.click_tinh_gia_ban)

        # Ẩn các nút nếu là staff
        self.hide_buttons_for_staff(user_role)

    def hide_buttons_for_staff(self, user_role):
        """Ẩn các nút Sửa và Xóa nếu người dùng là staff"""
        if user_role == "staff":
            # Kiểm tra các nút và ẩn chúng nếu người dùng là staff
            if hasattr(self.sp_view, 'btn_update') and self.sp_view.btn_update.winfo_exists():
                self.sp_view.btn_update.config(state='disabled')
            if hasattr(self.sp_view, 'btn_delete') and self.sp_view.btn_delete.winfo_exists():
                self.sp_view.btn_delete.config(state='disabled')

    def click_tinh_gia_ban(self):
        """Xử lý sự kiện nút tính giá bán"""
        try:
            # Lấy dữ liệu từ các trường nhập
            ma_sp = self.sp_view.entry_ma_sp.get()
            ten_sp = self.sp_view.entry_ten_sp.get()
            loai_sp = self.sp_view.loai_sp_var.get()
            don_vi = self.sp_view.cb_don_vi_sp.get()
            chi_phi = int(self.sp_view.entry_chi_phi_sp.get())
            gia_nhap = int(self.sp_view.entry_gia_nhap_sp.get())

            # Tạo object tương ứng
            if loai_sp == "Skin Care":
                sp = ChamSocDa(ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap)
            elif loai_sp == "Makeup":
                sp = TrangDiem(ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap)
            elif loai_sp == "Parfum":
                sp = NuocHoa(ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap)

            # Gọi phương thức tính giá bán
            gia_ban = sp.tinh_gia_ban()

            # Hiển thị giá bán lên Entry giá
            self.sp_view.entry_gia_ban_sp.config(state="normal")
            self.sp_view.entry_gia_ban_sp.delete(0, "end")
            self.sp_view.entry_gia_ban_sp.insert(0, str(gia_ban))
            self.sp_view.entry_gia_ban_sp.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Error", "Please enter valid information")

    def load_all_sp(self):
        """Lấy toàn bộ dữ liệu sản phẩm"""
        # Lấy dữ liệu từ
        raw_data = self.sp_model.get_all_sp()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]

        # Chèn dữ liệu vào bảng Treeview
        for row in data:
            self.sp_view.tree.insert("", "end", values=row)

    def get_data_sp(self):
        """Lấy dữ liệu từ các trường nhập"""
        ma_sp = self.sp_view.entry_ma_sp.get()
        ten_sp = self.sp_view.entry_ten_sp.get()
        loai_sp = self.sp_view.loai_sp_var.get()
        don_vi = self.sp_view.cb_don_vi_sp.get()
        chi_phi = int(self.sp_view.entry_chi_phi_sp.get())
        gia_nhap = int(self.sp_view.entry_gia_nhap_sp.get())
        gia_ban = float(self.sp_view.entry_gia_ban_sp.get())
        return ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap, gia_ban

    def click_add_sp(self):
        """Sự kiện nhấn nút thêm sản phẩm"""
        # Lấy dữ liệu sp từ các trường nhập
        ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap, gia_ban = self.get_data_sp()

        if ma_sp and ten_sp and loai_sp and don_vi and chi_phi and gia_nhap and gia_ban:
            # Gọi phương thức thêm sp trong model
            results = self.sp_model.add_sp(ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap, gia_ban)
            if results:
                messagebox.showinfo("Notification", "Added successfully")
                # Làm mới TreeView
                self.update_treeview_sp()
                self.click_refresh_sp()
            else:
                messagebox.showerror("Error", "Failed to add")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_refresh_sp(self):
        """Sự kiện nhấn nút làm mới các trường dữ liệu"""
        self.sp_view.entry_ma_sp.delete(0, END)
        self.sp_view.entry_ten_sp.delete(0, END)
        self.sp_view.loai_sp_var.set("0")
        self.sp_view.cb_don_vi_sp.set("Chose unit")
        self.sp_view.entry_chi_phi_sp.delete(0, END)
        self.sp_view.entry_gia_nhap_sp.delete(0, END)
        self.sp_view.entry_gia_ban_sp.config(state="normal")
        self.sp_view.entry_gia_ban_sp.delete(0, END)
        self.sp_view.entry_gia_ban_sp.config(state="readonly")

    def click_delete_sp(self):
        """Sự kiện nhấn nút xóa sản phẩm"""
        selected_item = self.sp_view.tree.selection()
        if selected_item:
            ma_sp = self.sp_view.tree.item(selected_item[0])["values"][0]
            # Gọi phương thức delete_sp trong model
            results = self.sp_model.delete_sp(ma_sp)
            if results:
                messagebox.showinfo("Notification", "Deleted successfully")
                self.update_treeview_sp()
            else:
                messagebox.showerror("Error", "Failed to delete")
            self.click_refresh_sp()
        else:
            messagebox.showwarning("Warning", "Please select a row to delete")

    def update_treeview_sp(self):
        """Cập nhật bảng Treeview sau khi xóa dữ liệu"""
        # Xóa tất cả dữ liệu trong Treeview trước khi cập nhật
        self.clear_treeview()
        # Lấy lại tất cả dữ liệu sản phẩm
        self.load_all_sp()

    def select_row_sp(self, event):
        """Chọn một dòng trên bảng Treeview"""
        # Lấy ID của dòng được chọn
        selected_item = self.sp_view.tree.selection()
        if selected_item:
            # Lấy dữ liệu từ dòng được chọn
            values = self.sp_view.tree.item(selected_item[0])["values"]

            # Xóa dữ liệu vào các trường nhập liệu
            self.click_refresh_sp()

            # Đưa dữ liệu vào các trường nhập liệu
            # Mã sp
            self.sp_view.entry_ma_sp.insert(0, values[0])

            # Tên sp
            self.sp_view.entry_ten_sp.insert(0, values[1])

            # Loại
            self.sp_view.loai_sp_var.set(values[2])

            # Đơn vị
            self.sp_view.cb_don_vi_sp.set(values[3])

            # Chi phí
            self.sp_view.entry_chi_phi_sp.insert(0, values[4])

            # Giá nhập
            self.sp_view.entry_gia_nhap_sp.insert(0, values[5])

            # Giá bán
            self.sp_view.entry_gia_ban_sp.config(state="normal")
            self.sp_view.entry_gia_ban_sp.insert(0, values[6])
            self.sp_view.entry_gia_ban_sp.config(state="readonly")

    def click_update_sp(self):
        """Sự kiện nhấn nút sửa dữ liệu sản phẩm"""
        # Lấy dữ liệu sp từ các trường nhập
        ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap, gia_ban = self.get_data_sp()

        if ma_sp and ten_sp and loai_sp and don_vi and chi_phi and gia_nhap and gia_ban:
            # Gọi phương thức update_sp trong model
            results = self.sp_model.update_sp(ma_sp, ten_sp, loai_sp, don_vi, chi_phi, gia_nhap, gia_ban)

            if results:
                messagebox.showinfo("Notification", "Updated successfully")
                # Làm mới TreeView
                self.update_treeview_sp()
                self.click_refresh_sp()
            else:
                messagebox.showerror("Error", "Failed to update")
        else:
            messagebox.showwarning("Warning", "Please fill in all required information")

    def click_search_sp(self):
        """Xử lý sự kiện nhấn nút tìm kiếm sản phẩm"""
        # Lấy giá trị từ ô tìm kiếm
        search_text = self.sp_view.entry_search_sp.get()

        # Gọi hàm search_sp trong Model
        raw_data = self.sp_model.search_sp(search_text)

        # Chuyển dữ liệu thành dạng tuple
        results = [tuple(row) for row in raw_data]

        # Xóa dữ liệu trong bảng Treeview
        self.clear_treeview()

        # Hiển thị kết quả lên TreeView
        if results:
            # Thêm kết quả tìm kiếm vào bảng Treeview
            for row in results:
                self.sp_view.tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("Notification", "No results found")

        # Xóa nội dung ô tìm kiếm
        self.sp_view.entry_search_sp.delete(0, "end")

    def get_all_row_sp(self):
        """Lấy dữ liệu từ Treeview sản phẩm"""
        return [self.sp_view.tree.item(item, "values") for item in self.sp_view.tree.get_children()]

    def clear_treeview(self):
        """Xóa tất cả dữ liệu trên bảng Treeview"""
        for item in self.sp_view.tree.get_children():
            self.sp_view.tree.delete(item)

    def click_print_sp(self):
        """Sự kiện in danh sách sản phẩm"""
        self.click_print(self.title, self.get_all_row_sp(), self.headers)

    def click_csv_sp(self):
        """Sự kiện xuất file CSV"""
        self.click_csv(self.title, self.get_all_row_sp(), self.headers)

    def click_excel_sp(self):
        """Sự kiện xuât file Excel"""
        self.click_excel(self.title, self.get_all_row_sp(), self.headers)