from tkinter import Entry, messagebox
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from Store_Management.controller.controller import Controller
from Store_Management.model.thongke_model import ThongKeModel
from Store_Management.view.thongke_view import ThongKeView


class ThongKeController (Controller):
    def __init__(self, model, view, parent_controller=None):
        super().__init__(model, view)
        self.tk_model = ThongKeModel()
        self.dashboard_controller = parent_controller

    def close_widget_tk(self):
        """Sự kiện đóng giao diện thống kê"""
        for widget in self.tk_view.winfo_children():
            widget.destroy()

    def get_ma_sp(self):
        """Lấy dữ liệu mã sp của bảng"""
        # Lấy dữ liệu từ model
        raw_data = self.tk_model.get_ma_sp()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data[0][0]

    def get_ma_nv(self):
        """Lấy dữ liệu mã nv của bảng"""
        # Lấy dữ liệu từ model
        raw_data = self.tk_model.get_ma_nv()

        # Chuyển dữ liệu thành dạng tuple
        data = [tuple(row) for row in raw_data]
        return data[0][0]

    def click_thong_ke(self):
        """Gán sự kiện nút thống kê"""
        # Đóng giao diện
        print("Show Report UI")
        self.dashboard_controller.close_widget()

        # Hiển thị giao diện thống kê
        self.tk_view = ThongKeView(self.view)
        self.tk_view.thong_ke_widget()
        self.tk_view.pack(fill="both", expand=True)

        # Gán sự kiện nút quay lại dashboard
        self.tk_view.btn_return_tk.config(command=self.dashboard_controller.click_btn_return)

        # Sự kiện nút thống kê doanh thu
        self.tk_view.btn_tk_doanh_thu.config(command=self.click_tk_doanh_thu)

        # Sự kiện nút thống kê sản phẩm
        self.tk_view.btn_tk_sp.config(command=self.click_tk_san_pham)

        # Sự kiện nút thống kê nhân viên
        self.tk_view.btn_tk_nv.config(command=self.click_tk_nhan_vien)

        # Sự kiện nút thống kê lương
        self.tk_view.btn_tk_luong.config(command=self.click_tk_luong)

        # Sự kiện nút thống kê khách hàng
        self.tk_view.btn_tk_kh.config(command=self.click_tk_khach_hang)

        # Sự kiện nút thống kê nhà cung cấp
        self.tk_view.btn_tk_ncc.config(command=self.click_tk_nha_cung_cap)

    # THỐNG KÊ DOANH THU
    def click_tk_doanh_thu(self):
        """Hiển thị giao diện thống kê doanh thu"""
        # Đóng giao diện
        self.close_widget_tk()

        # Hiển thị giao diện thống kê doanh thu
        self.tk_view.tk_doanh_thu_widget()

        # Hiển thị mã sp
        self.tk_view.cb_ma_sp['values'] = self.get_ma_sp()

        # Hiển thị dữ liệu mã nv
        self.tk_view.cb_ma_nv['values'] = self.get_ma_nv()

        # Gán sự kiện nút quay lại
        self.tk_view.btn_return.config(command=self.dashboard_controller.click_btn_return)

        # Sự kiện nút làm mới
        self.tk_view.btn_refresh.config(command=self.reset_fields)

        # Sự kiện tính doanh thu theo tháng
        self.tk_view.cb_doanh_thu_theo_thang.bind("<<ComboboxSelected>>", lambda event: self.doanh_thu_theo_thang())

        # Sự kiện tính doanh thu theo năm (sử dụng sự kiện FocusOut hoặc nhấn Enter)
        self.tk_view.entry_doanh_thu_theo_nam.bind("<FocusOut>", lambda event: self.doanh_thu_theo_nam())
        self.tk_view.entry_doanh_thu_theo_nam.bind("<Return>", lambda event: self.doanh_thu_theo_nam())

        # Sự kiện tính doanh thu theo mã sp
        self.tk_view.cb_ma_sp.bind("<<ComboboxSelected>>", lambda event: self.doanh_thu_theo_ma_sp())

        # Sự kiện tính doanh thu theo loại sp
        self.tk_view.cb_loai_sp.bind("<<ComboboxSelected>>", lambda event: self.doanh_thu_theo_loai_sp())

        # Sự kiện tính doanh thu theo mã nv
        self.tk_view.cb_ma_nv.bind("<<ComboboxSelected>>", lambda event: self.doanh_thu_theo_ma_nv())

        loai_sp_list = ["Skin Care", "Makeup", "Parfum"]
        self.tk_view.btn_show_diagram.config(command=lambda: self.hien_thi_so_do_doanh_thu_theo_loai_sp(loai_sp_list))

    def reset_fields(self):
        """Đặt lại tất cả các trường về trạng thái 'normal' và xóa dữ liệu"""
        # Dictionary chứa các ComboBox và giá trị mặc định của chúng
        combobox_defaults = {
            self.tk_view.cb_doanh_thu_theo_thang: "Choose month",
            self.tk_view.cb_ma_sp: "Choose Product ID",
            self.tk_view.cb_loai_sp: "Choose Product Type",
            self.tk_view.cb_ma_nv: "Choose Employee ID"
        }

        # Đặt trạng thái và xóa dữ liệu cho Entry
        self.tk_view.entry_doanh_thu_theo_nam.config(state="normal")
        self.tk_view.entry_doanh_thu_theo_nam.delete(0, "end")

        self.tk_view.entry_doanh_thu.config(state="normal")
        self.tk_view.entry_doanh_thu.delete(0, "end")
        self.tk_view.entry_doanh_thu.config(state="disabled")

        # Đặt trạng thái và giá trị mặc định cho ComboBox
        for combobox, default_value in combobox_defaults.items():
            combobox.config(state="normal")
            combobox.set(default_value)

    def update_fields(self, exclude_widget=None):
        """Cập nhật trạng thái của các trường, ngoại trừ widget được chỉ định"""
        fields = [
            self.tk_view.cb_doanh_thu_theo_thang,
            self.tk_view.entry_doanh_thu_theo_nam,
            self.tk_view.cb_ma_sp,
            self.tk_view.cb_loai_sp,
            self.tk_view.cb_ma_nv
        ]
        for field in fields:
            if field == exclude_widget:
                # Bật widget được chọn
                if isinstance(field, Entry):
                    field.config(state="normal")
                if isinstance(field, Combobox):
                    field.config(state="readonly")
            else:
                # Vô hiệu hóa các widget khác
                if isinstance(field, Entry):
                    field.config(state="readonly")
                if isinstance(field, Combobox):
                    field.config(state="disabled")

    def doanh_thu_theo_nam(self):
        """Tính doanh thu theo năm"""
        nam_str = self.tk_view.entry_doanh_thu_theo_nam.get()
        # Kiểm tra định dạng hợp lệ
        if nam_str.isdigit() and len(nam_str) == 4:
            nam = int(nam_str)
            result = self.tk_model.doanh_thu_theo_nam(nam)

            # Kiểm tra kết quả và gán doanh thu
            doanh_thu = result[0][1] if result else 0

            # Hiển thị doanh thu lên Entry
            self.tk_view.entry_doanh_thu.config(state="normal")
            self.tk_view.entry_doanh_thu.delete(0, "end")
            self.tk_view.entry_doanh_thu.insert(0, str(doanh_thu))
            self.tk_view.entry_doanh_thu.config(state="readonly")

            # Gọi hàm update_fields để cập nhật trạng thái các trường khác
            self.update_fields(exclude_widget=self.tk_view.entry_doanh_thu_theo_nam)

        else:
            # Nếu năm không hợp lệ, hiển thị thông báo lỗi
            messagebox.showinfo("Warning", "Please enter a valid year (e.g., 2026)")

    def doanh_thu_theo_thang(self):
        """Tính doanh thu theo tháng"""
        try:
            # Lấy giá trị tháng từ Combobox
            thang = int(self.tk_view.cb_doanh_thu_theo_thang.get())
            result = self.tk_model.doanh_thu_theo_thang(thang)

            # Kiểm tra kết quả và gán doanh thu
            doanh_thu = result[0][1] if result else 0

            # Hiển thị doanh thu lên Entry
            self.tk_view.entry_doanh_thu.config(state="normal")
            self.tk_view.entry_doanh_thu.delete(0, "end")
            self.tk_view.entry_doanh_thu.insert(0, str(doanh_thu))
            self.tk_view.entry_doanh_thu.config(state="readonly")

            # Gọi hàm update_fields để cập nhật trạng thái các trường khác
            self.update_fields(exclude_widget=self.tk_view.cb_doanh_thu_theo_thang)

        except ValueError:
            messagebox.showinfo("Warning", "Please select a valid month")

    def doanh_thu_theo_ma_sp(self):
        """Tính doanh thu theo mã sp"""
        # Lấy dữ liệu mã sp trong trường nhập dữ liệu
        ma_sp = self.tk_view.cb_ma_sp.get()

        # Gọi phương thức trong model
        result = self.tk_model.doanh_thu_theo_ma_sp(ma_sp)

        # Kiểm tra kết quả và gán doanh thu
        doanh_thu = result[0][1] if result else 0

        # Hiển thị doanh thu lên Entry
        self.tk_view.entry_doanh_thu.config(state="normal")
        self.tk_view.entry_doanh_thu.delete(0, "end")
        self.tk_view.entry_doanh_thu.insert(0, str(doanh_thu))
        self.tk_view.entry_doanh_thu.config(state="readonly")

        # Gọi hàm update_fields để cập nhật trạng thái các trường khác
        self.update_fields(exclude_widget=self.tk_view.cb_ma_sp)

    def doanh_thu_theo_loai_sp(self):
        """Tính doanh thu theo loại sp"""
        # Lấy dữ liệu mã sp trong trường nhập dữ liệu
        loai_sp = self.tk_view.cb_loai_sp.get()

        # Gọi phương thức trong model
        result = self.tk_model.doanh_thu_theo_loai_sp(loai_sp)

        # Kiểm tra kết quả và gán doanh thu
        doanh_thu = result[0][1] if result else 0

        # Hiển thị doanh thu lên Entry
        self.tk_view.entry_doanh_thu.config(state="normal")
        self.tk_view.entry_doanh_thu.delete(0, "end")
        self.tk_view.entry_doanh_thu.insert(0, str(doanh_thu))
        self.tk_view.entry_doanh_thu.config(state="readonly")

        # Gọi hàm update_fields để cập nhật trạng thái các trường khác
        self.update_fields(exclude_widget=self.tk_view.cb_loai_sp)

    def lay_doanh_thu_theo_loai_sp(self, loai_sp):
        """Lấy doanh thu từ Model cho một loại sản phẩm"""
        result = self.tk_model.doanh_thu_theo_loai_sp(loai_sp)
        return result[0][1] if result else 0

    def doanh_thu_theo_ma_nv(self):
        """Tính doanh thu theo mã nv"""
        # Lấy dữ liệu mã sp trong trường nhập dữ liệu
        ma_nv = self.tk_view.cb_ma_nv.get()

        # Gọi phương thức trong model
        result = self.tk_model.doanh_thu_theo_ma_nv(ma_nv)

        # Kiểm tra kết quả và gán doanh thu
        doanh_thu = result[0][1] if result else 0

        # Hiển thị doanh thu lên Entry
        self.tk_view.entry_doanh_thu.config(state="normal")
        self.tk_view.entry_doanh_thu.delete(0, "end")
        self.tk_view.entry_doanh_thu.insert(0, str(doanh_thu))
        self.tk_view.entry_doanh_thu.config(state="readonly")

        # Gọi hàm update_fields để cập nhật trạng thái các trường khác
        self.update_fields(exclude_widget=self.tk_view.cb_ma_nv)

    def hien_thi_so_do_doanh_thu_theo_loai_sp(self, loai_sp_list):
        """Hiển thị sơ đồ doanh thu theo loại sản phẩm trên Frame"""
        # Lấy dữ liệu doanh thu cho từng loại sản phẩm
        doanh_thu_data = []
        for loai_sp in loai_sp_list:
            doanh_thu = self.lay_doanh_thu_theo_loai_sp(loai_sp)
            doanh_thu_data.append(doanh_thu)

        # Tạo figure và biểu đồ
        fig = Figure(figsize=(4.5, 2.5), dpi=100)  # Kích thước khớp với Frame
        ax = fig.add_subplot(111)
        ax.bar(loai_sp_list, doanh_thu_data, color="skyblue")
        ax.set_title("Doanh thu theo loại sản phẩm", fontsize=10, fontweight="bold")
        ax.set_xlabel("Loại sản phẩm", fontsize=8)
        ax.set_ylabel("Doanh thu (VNĐ)", fontsize=8)
        ax.tick_params(axis="x", labelrotation=360, labelsize=7)

        # Tạo canvas từ figure và nhúng vào Frame
        canvas = FigureCanvasTkAgg(fig, master=self.tk_view.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

        # Xóa các widget cũ trong frame (nếu có)
        #self.dashboard_controller.close_widget()

    # THỐNG KÊ SẢN PHẨM
    def click_tk_san_pham(self):
        """Hiển thị giao diện thống kê sản phẩm"""
        # Đóng giao diện
        self.close_widget_tk()

        # Hiển thị giao diện thống kê sản phẩm
        self.tk_view.tk_san_pham_widget()

        # Hiển thị top 10 sản phẩm
        self.top_san_pham_ban_chay()

        # Gán sự kiện nút quay lại
        self.tk_view.btn_return.config(command=self.dashboard_controller.click_btn_return)

    def top_san_pham_ban_chay(self):
        """Hiển thị top sản phẩm bán chạy trên TreeView"""
        try:
            # Gọi hàm từ model để lấy dữ liệu
            raw_data = self.tk_model.top_san_pham_ban_chay()
            data = [tuple(row) for row in raw_data]

            # Xóa dữ liệu cũ trên Treeview
            for row in self.tk_view.tree.get_children():
                self.tk_view.tree.delete(row)

            # Thêm dữ liệu mới vào Treeview
            for row in data:
                self.tk_view.tree.insert("", "end", values=row)
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu top sản phẩm: {e}")

    # THỐNG KÊ NHÂN VIÊN
    def click_tk_nhan_vien(self):
        """Hiển thị giao diện thống kê nhân viên"""
        # Đóng giao diện
        self.close_widget_tk()

        # Hiển thị giao diện thống kê nhân viên
        self.tk_view.tk_nhan_vien_widget()

        # Hiển thị top nhân viên có doanh số cao nhất
        self.top_nhan_vien()

        # Gán sự kiện nút quay lại
        self.tk_view.btn_return.config(command=self.dashboard_controller.click_btn_return)

    def top_nhan_vien(self):
        """Hiển thị top nhân viên có doanh số cao nhất trên TreeView"""
        try:
            # Gọi hàm từ model để lấy dữ liệu
            raw_data = self.tk_model.top_nhan_vien()
            data = [tuple(row) for row in raw_data]

            # Xóa dữ liệu cũ trên Treeview
            for row in self.tk_view.tree.get_children():
                self.tk_view.tree.delete(row)

            # Thêm dữ liệu mới vào Treeview
            for row in data:
                self.tk_view.tree.insert("", "end", values=row)
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu top nhân viên: {e}")

    # THỐNG KÊ KHÁCH HÀNG
    def click_tk_khach_hang(self):
        """Hiển thị giao diện thống kê khách hàng"""
        # Đóng giao diện
        self.close_widget_tk()

        # Hiển thị giao diện thống kê khách hàng
        self.tk_view.tk_khach_hang_widget()

        # Hiển thị top khách hàng đã mua nhiều nhất
        self.top_khach_hang()

        # Gán sự kiện nút quay lại
        self.tk_view.btn_return.config(command=self.dashboard_controller.click_btn_return)

    def top_khach_hang(self):
        """Hiển thị top khách hàng đã mua nhiều nhất trên TreeView"""
        try:
            # Gọi hàm từ model để lấy dữ liệu
            raw_data = self.tk_model.top_khach_hang()
            data = [tuple(row) for row in raw_data]

            # Xóa dữ liệu cũ trên Treeview
            for row in self.tk_view.tree.get_children():
                self.tk_view.tree.delete(row)

            # Thêm dữ liệu mới vào Treeview
            for row in data:
                self.tk_view.tree.insert("", "end", values=row)
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu top khách hàng: {e}")

    # THỐNG KÊ NHÀ CUNG CẤP
    def click_tk_nha_cung_cap(self):
        """Hiển thị giao diện thống kê nhà cung cấp"""
        # Đóng giao diện
        self.close_widget_tk()

        # Hiển thị giao diện thống kê nhà cung cấp
        self.tk_view.tk_nha_cung_cap_widget()

        # Hiển thị top nhà cung cấp có số lượng nhập hàng nhiều nhất
        self.top_nha_cung_cap()

        # Gán sự kiện nút quay lại
        self.tk_view.btn_return.config(command=self.dashboard_controller.click_btn_return)

    def top_nha_cung_cap(self):
        """Hiển thị top nhà cung cấp có số lượng nhập hàng nhiều nhất trên TreeView"""
        try:
            # Gọi hàm từ model để lấy dữ liệu
            raw_data = self.tk_model.top_nha_cung_cap()
            data = [tuple(row) for row in raw_data]

            # Xóa dữ liệu cũ trên Treeview
            for row in self.tk_view.tree.get_children():
                self.tk_view.tree.delete(row)

            # Thêm dữ liệu mới vào Treeview
            for row in data:
                self.tk_view.tree.insert("", "end", values=row)
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu top nhà cung cấp: {e}")

    # THỐNG KÊ LƯƠNG
    def click_tk_luong(self):
        """Hiển thị giao diện thống kê lương"""
        # Đóng giao diện
        self.close_widget_tk()

        # Hiển thị giao diện thống kê lương
        self.tk_view.tk_luong_widget()

        # Hiển thị tổng số lương đã trả nhân viên
        self.tk_luong()

        # Gán sự kiện nút quay lại
        self.tk_view.btn_return.config(command=self.dashboard_controller.click_btn_return)

    def tk_luong(self):
        """Hiển thị tổng số lương đã trả nhân viên trên TreeView"""
        try:
            # Gọi hàm từ model để lấy dữ liệu
            raw_data = self.tk_model.tk_luong()
            data = [tuple(row) for row in raw_data]

            # Xóa dữ liệu cũ trên Treeview
            for row in self.tk_view.tree.get_children():
                self.tk_view.tree.delete(row)

            # Thêm dữ liệu mới vào Treeview
            for row in data:
                self.tk_view.tree.insert("", "end", values=row)
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu thống kê lương: {e}")