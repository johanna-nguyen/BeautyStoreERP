from tkinter import Tk, Label, Entry, PhotoImage, Button, Frame, Scrollbar, StringVar, Radiobutton, GROOVE, ttk, RIGHT, \
    Y, VERTICAL, HORIZONTAL, BOTTOM, X, BOTH
from tkinter.ttk import Combobox

from tkcalendar import DateEntry

class ThongKeView (Frame):
    def __init__(self, parent):
        super().__init__(parent)

    # THỐNG KÊ
    def thong_ke_widget(self):
        """Hiển thị giao diện"""
        # Kích thước GUI dashboard
        self.master.geometry('520x520')

        # Tạo giao diện
        Label(self, text="Report", font=('Arial', 25)).pack(pady=20)

        # Nút quay lại dashboard
        self.icon_return_tk = PhotoImage(file="image/return.png")
        self.btn_return_tk = Button(master=self, text="Back", image=self.icon_return_tk, compound="left")
        self.btn_return_tk.place(x=20, y=20)

        # Nút thống kê nhà cung cấp
        self.icon_tk_ncc = PhotoImage(file="image/supplier.png")
        self.btn_tk_ncc = Button(self, text="Supplier", image=self.icon_tk_ncc, compound="left",
                                 width=150, height=50)
        self.btn_tk_ncc.place(x=10, y=100)

        # Nút thống kê sản phẩm
        self.icon_tk_sp = PhotoImage(file="image/products.png")
        self.btn_tk_sp = Button(self, text="Thống kê sản phẩm", image=self.icon_tk_sp, compound="left", width=150,
                                height=50)
        self.btn_tk_sp.place(x=180, y=100)

        # Nút thống kê nhân viên
        self.icon_tk_nv = PhotoImage(file="image/employee.png")
        self.btn_tk_nv = Button(self, text="Thống kê nhân viên", image=self.icon_tk_nv, compound="left", width=150,
                                height=50)
        self.btn_tk_nv.place(x=350, y=100)

        # Nút thống kê khách hàng
        self.icon_tk_kh = PhotoImage(file="image/clients.png")
        self.btn_tk_kh = Button(self, text="Thống kê khách hàng", image=self.icon_tk_kh, compound="left", width=150,
                                height=50)
        self.btn_tk_kh.place(x=10, y=170)

        # Nút thống kê doanh thu
        self.icon_tk_doanh_thu = PhotoImage(file="image/income.png")
        self.btn_tk_doanh_thu = Button(self, text="Thống kê doanh thu", image=self.icon_tk_doanh_thu, compound="left", width=150,
                                height=50)
        self.btn_tk_doanh_thu.place(x=180, y=170)

        # Nút thống kê lương
        self.icon_tk_luong = PhotoImage(file="image/salary.png")
        self.btn_tk_luong = Button(self, text="Thống kê lương", image=self.icon_tk_luong, compound="left", width=150,
                                   height=50)
        self.btn_tk_luong.place(x=350, y=170)

    # THỐNG KÊ DOANH THU

    def tk_doanh_thu_widget(self):
        """Hiển thị giao diện thống kê doanh thu"""
        # Kích thước GUI đăng nhập
        self.master.geometry('870x500')

        # Tạo Frame chứa giao diện
        # Thêm viền cho Frame
        self.main_frame = Frame(self, bd=2, relief=GROOVE)

        # Vị trí Frame
        self.main_frame.place(x=20, y=50, width=820, height=440)

        # Tạo Frame con để chứa Treeview và Scrollbars
        self.frame = Frame(self.main_frame, bd=2, relief=GROOVE)
        self.frame.place(x=350, y=20, width=450, height=370)

        # Tạo nhãn tiêu đề
        self.label_tk = Label(master=self, text="Thống kê doanh thu", font=('Arial', 25))
        self.label_tk.pack(pady=20)

        # Nút quay lại dashboard
        self.icon_return = PhotoImage(file="image/return.png")
        self.btn_return = Button(master=self, text="Quay lại", image=self.icon_return, compound="left")
        self.btn_return.place(x=20, y=20)

        # Label: Doanh thu theo tháng
        self.label_doanh_thu_theo_thang = Label(master=self, text="Doanh thu theo tháng")
        self.label_doanh_thu_theo_thang.place(x=50, y=100)

        # Combobox: Doanh thu theo tháng
        self.months = [str(month) for month in range(1, 12)]
        self.cb_doanh_thu_theo_thang = Combobox(master=self, values=self.months)
        self.cb_doanh_thu_theo_thang.set("Chọn tháng")
        self.cb_doanh_thu_theo_thang.place(x=180, y=100)

        # Label: Doanh thu theo năm
        self.label_doanh_thu_theo_nam = Label(master=self, text="Doanh thu theo năm")
        self.label_doanh_thu_theo_nam.place(x=50, y=150)

        # Entry: Doanh thu theo năm
        self.entry_doanh_thu_theo_nam = Entry(master=self, width=20)
        self.entry_doanh_thu_theo_nam.place(x=180, y=150)

        # Label: Theo mã sản phẩm
        self.label_ma_sp = Label(master=self, text="Mã sản phẩm")
        self.label_ma_sp.place(x=50, y=200)

        # Combo: Theo mã sản phẩm
        self.cb_ma_sp = Combobox(master=self)
        self.cb_ma_sp.place(x=180, y=200)
        self.cb_ma_sp.set("Chọn mã sản phẩm")

        # Label: Theo loại sản phẩm
        self.label_loai_sp = Label(master=self, text="Loại sản phẩm")
        self.label_loai_sp.place(x=50, y=250)

        # Combo: Theo loại sản phẩm
        self.loai_sp = ["Chăm sóc da", "Trang điểm", "Nước hoa"]
        self.cb_loai_sp = Combobox(master=self, values=self.loai_sp)
        self.cb_loai_sp.place(x=180, y=250)
        self.cb_loai_sp.set("Chọn loại sản phẩm")

        # Label: Theo mã nhân viên
        self.label_ma_nv = Label(master=self, text="Mã nhân viên")
        self.label_ma_nv.place(x=50, y=300)

        # Combo: Theo mã nhân viên
        self.cb_ma_nv = Combobox(master=self)
        self.cb_ma_nv.place(x=180, y=300)
        self.cb_ma_nv.set("Chọn mã nhân viên")

        # Label: Doanh thu
        self.label_doanh_thu = Label(master=self, text="Doanh thu")
        self.label_doanh_thu.place(x=50, y=350)

        # Entry: Doanh thu
        self.entry_doanh_thu = Entry(master=self, width=20,  fg="red", font=("", 10, "bold"))
        self.entry_doanh_thu.place(x=180, y=350)
        self.entry_doanh_thu.config(state="readonly")

        # Nút làm mới các trường dữ liệu
        self.icon_refresh= PhotoImage(file="image/refresh.png")
        self.btn_refresh = Button(self, text="Làm mới", image=self.icon_refresh, compound="left")
        self.btn_refresh.place(x=50, y=380)

        # Nút xem sơ đồ
        self.icon_show_diagram = PhotoImage(file="image/diagram_small.png")
        self.btn_show_diagram = Button(self, text="Xem sơ đồ", image=self.icon_show_diagram, compound="left")
        self.btn_show_diagram.place(x=540, y=450)

    # THỐNG KÊ SẢN PHẨM
    def tk_san_pham_widget(self):
        """Hiển thị giao diện thống kê sản phẩm"""
        # Kích thước GUI đăng nhập
        self.master.geometry('870x500')

        # Tạo Frame chứa giao diện
        # Thêm viền cho Frame
        self.main_frame = Frame(self, bd=2, relief=GROOVE)

        # Vị trí Frame
        self.main_frame.place(x=20, y=50, width=820, height=440)

        # Tạo Frame con để chứa Treeview và Scrollbars
        self.frame = Frame(self.main_frame, bd=2, relief=GROOVE)
        self.frame.place(x=30, y=20, width=750, height=400)

        # Tạo nhãn tiêu đề
        self.label_tk = Label(master=self, text="Top sản phẩm bán chạy", font=('Arial', 25))
        self.label_tk.pack(pady=20)

        # Nút quay lại dashboard
        self.icon_return = PhotoImage(file="image/return.png")
        self.btn_return = Button(master=self, text="Quay lại", image=self.icon_return, compound="left")
        self.btn_return.place(x=20, y=20)

        # Tạo bảng top sản phẩm bán chạy
        cols = ("ma_sp", "ten_sp", "tong_so_luong_ban")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_sp", text="Mã sản phẩm")
        self.tree.heading("ten_sp", text="Tên sản phẩm")
        self.tree.heading("tong_so_luong_ban", text="Tổng số lượng bán")

        # Kích thước cột
        self.tree.column("ma_sp", width=250, stretch=False)
        self.tree.column("ten_sp", width=250, stretch=False)
        self.tree.column("tong_so_luong_ban", width=250, stretch=False)

        # Tạo Scrollbar dọc
        self.scrollbar_y = Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        # Tạo Scrollbar ngang
        self.scrollbar_x = Scrollbar(self.frame, orient=HORIZONTAL, command=self.tree.xview)
        self.scrollbar_x.pack(side=BOTTOM, fill=X)

        # Liên kết Treeview với Scrollbar
        self.tree.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # Thêm Treeview vào Frame
        self.tree.pack(fill=BOTH, expand=True)

    # THỐNG KÊ NHÂN VIÊN
    def tk_nhan_vien_widget(self):
        """Hiển thị giao diện thống kê nhân viên"""
        # Kích thước GUI đăng nhập
        self.master.geometry('870x500')

        # Tạo Frame chứa giao diện
        # Thêm viền cho Frame
        self.main_frame = Frame(self, bd=2, relief=GROOVE)

        # Vị trí Frame
        self.main_frame.place(x=20, y=50, width=820, height=440)

        # Tạo Frame con để chứa Treeview và Scrollbars
        self.frame = Frame(self.main_frame, bd=2, relief=GROOVE)
        self.frame.place(x=30, y=20, width=750, height=400)

        # Tạo nhãn tiêu đề
        self.label_tk = Label(master=self, text="Top nhân viên bán hàng hiệu quả", font=('Arial', 25))
        self.label_tk.pack(pady=20)

        # Nút quay lại dashboard
        self.icon_return = PhotoImage(file="image/return.png")
        self.btn_return = Button(master=self, text="Quay lại", image=self.icon_return, compound="left")
        self.btn_return.place(x=20, y=20)

        # Tạo bảng top nhân viên có doanh số cao nhất
        cols = ("ma_nv", "ten_nv", "tong_doanh_so")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_nv", text="Mã nhân viên")
        self.tree.heading("ten_nv", text="Tên nhân viên")
        self.tree.heading("tong_doanh_so", text="Tổng doanh số")

        # Kích thước cột
        self.tree.column("ma_nv", width=250, stretch=False)
        self.tree.column("ten_nv", width=250, stretch=False)
        self.tree.column("tong_doanh_so", width=250, stretch=False)

        # Tạo Scrollbar dọc
        self.scrollbar_y = Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        # Tạo Scrollbar ngang
        self.scrollbar_x = Scrollbar(self.frame, orient=HORIZONTAL, command=self.tree.xview)
        self.scrollbar_x.pack(side=BOTTOM, fill=X)

        # Liên kết Treeview với Scrollbar
        self.tree.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # Thêm Treeview vào Frame
        self.tree.pack(fill=BOTH, expand=True)

    # THỐNG KÊ LƯƠNG
    def tk_luong_widget(self):
        """Hiển thị giao diện thống kê lương"""
        # Kích thước GUI đăng nhập
        self.master.geometry('870x500')

        # Tạo Frame chứa giao diện
        # Thêm viền cho Frame
        self.main_frame = Frame(self, bd=2, relief=GROOVE)

        # Vị trí Frame
        self.main_frame.place(x=20, y=50, width=820, height=440)

        # Tạo Frame con để chứa Treeview và Scrollbars
        self.frame = Frame(self.main_frame, bd=2, relief=GROOVE)
        self.frame.place(x=30, y=20, width=750, height=400)

        # Tạo nhãn tiêu đề
        self.label_tk = Label(master=self, text="Thống kê lương", font=('Arial', 25))
        self.label_tk.pack(pady=20)

        # Nút quay lại dashboard
        self.icon_return = PhotoImage(file="image/return.png")
        self.btn_return = Button(master=self, text="Quay lại", image=self.icon_return, compound="left")
        self.btn_return.place(x=20, y=20)

        # Tạo bảng thống kê lương
        cols = ("ma_nv", "ten_nv", "tong_luong")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_nv", text="Mã nhân viên")
        self.tree.heading("ten_nv", text="Tên nhân viên")
        self.tree.heading("tong_luong", text="Tổng lương")

        # Kích thước cột
        self.tree.column("ma_nv", width=250, stretch=False)
        self.tree.column("ten_nv", width=250, stretch=False)
        self.tree.column("tong_luong", width=250, stretch=False)

        # Tạo Scrollbar dọc
        self.scrollbar_y = Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        # Tạo Scrollbar ngang
        self.scrollbar_x = Scrollbar(self.frame, orient=HORIZONTAL, command=self.tree.xview)
        self.scrollbar_x.pack(side=BOTTOM, fill=X)

        # Liên kết Treeview với Scrollbar
        self.tree.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # Thêm Treeview vào Frame
        self.tree.pack(fill=BOTH, expand=True)

    # THỐNG KÊ KHÁCH HÀNG
    def tk_khach_hang_widget(self):
        """Hiển thị giao diện thống kê khách hàng"""
        # Kích thước GUI đăng nhập
        self.master.geometry('870x500')

        # Tạo Frame chứa giao diện
        # Thêm viền cho Frame
        self.main_frame = Frame(self, bd=2, relief=GROOVE)

        # Vị trí Frame
        self.main_frame.place(x=20, y=50, width=820, height=440)

        # Tạo Frame con để chứa Treeview và Scrollbars
        self.frame = Frame(self.main_frame, bd=2, relief=GROOVE)
        self.frame.place(x=30, y=20, width=750, height=400)

        # Tạo nhãn tiêu đề
        self.label_tk = Label(master=self, text="Top khách hàng mua nhiều nhất", font=('Arial', 25))
        self.label_tk.pack(pady=20)

        # Nút quay lại dashboard
        self.icon_return = PhotoImage(file="image/return.png")
        self.btn_return = Button(master=self, text="Quay lại", image=self.icon_return, compound="left")
        self.btn_return.place(x=20, y=20)

        # Tạo bảng top khách hàng mua nhiều nhất
        cols = ("ma_kh", "ten_kh", "tong_so_tien")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_kh", text="Mã khách hàng")
        self.tree.heading("ten_kh", text="Tên khách hàng")
        self.tree.heading("tong_so_tien", text="Tổng số tiền đã mua")

        # Kích thước cột
        self.tree.column("ma_kh", width=250, stretch=False)
        self.tree.column("ten_kh", width=250, stretch=False)
        self.tree.column("tong_so_tien", width=250, stretch=False)

        # Tạo Scrollbar dọc
        self.scrollbar_y = Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        # Tạo Scrollbar ngang
        self.scrollbar_x = Scrollbar(self.frame, orient=HORIZONTAL, command=self.tree.xview)
        self.scrollbar_x.pack(side=BOTTOM, fill=X)

        # Liên kết Treeview với Scrollbar
        self.tree.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # Thêm Treeview vào Frame
        self.tree.pack(fill=BOTH, expand=True)

    # THỐNG KÊ NHÀ CUNG CẤP
    def tk_nha_cung_cap_widget(self):
        """Hiển thị giao diện thống kê nhà cung cấp"""
        # Kích thước GUI đăng nhập
        self.master.geometry('870x500')

        # Tạo Frame chứa giao diện
        # Thêm viền cho Frame
        self.main_frame = Frame(self, bd=2, relief=GROOVE)

        # Vị trí Frame
        self.main_frame.place(x=20, y=50, width=820, height=440)

        # Tạo Frame con để chứa Treeview và Scrollbars
        self.frame = Frame(self.main_frame, bd=2, relief=GROOVE)
        self.frame.place(x=30, y=20, width=750, height=400)

        # Tạo nhãn tiêu đề
        self.label_tk = Label(master=self, text="Top nhà cung cấp nhập hàng nhiều nhất", font=('Arial', 25))
        self.label_tk.pack(pady=20)

        # Nút quay lại dashboard
        self.icon_return = PhotoImage(file="image/return.png")
        self.btn_return = Button(master=self, text="Quay lại", image=self.icon_return, compound="left")
        self.btn_return.place(x=20, y=20)

        # Tạo bảng top nhà cung cấp nhập hàng nhiều nhất
        cols = ("ma_ncc", "ten_ncc", "tong_so_luong_nhap")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_ncc", text="Mã nhà cung cấp")
        self.tree.heading("ten_ncc", text="Tên nhà cung cấp")
        self.tree.heading("tong_so_luong_nhap", text="Tổng số lượng nhập")

        # Kích thước cột
        self.tree.column("ma_ncc", width=250, stretch=False)
        self.tree.column("ten_ncc", width=250, stretch=False)
        self.tree.column("tong_so_luong_nhap", width=250, stretch=False)

        # Tạo Scrollbar dọc
        self.scrollbar_y = Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        self.scrollbar_y.pack(side=RIGHT, fill=Y)

        # Tạo Scrollbar ngang
        self.scrollbar_x = Scrollbar(self.frame, orient=HORIZONTAL, command=self.tree.xview)
        self.scrollbar_x.pack(side=BOTTOM, fill=X)

        # Liên kết Treeview với Scrollbar
        self.tree.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        # Thêm Treeview vào Frame
        self.tree.pack(fill=BOTH, expand=True)

