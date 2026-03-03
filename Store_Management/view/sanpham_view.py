from tkinter import Label, Entry, PhotoImage, Button, Frame, GROOVE, Scrollbar, HORIZONTAL, VERTICAL, ttk, RIGHT, Y, \
    BOTTOM, X, BOTH, StringVar, Radiobutton
from tkinter.ttk import Combobox


class SPView (Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def ql_sp_widget(self):
        """Hiển thị giao diện quản lý sản phẩm"""
        # Kích thước GUI đăng nhập
        self.master.geometry('870x560')

        # Tạo Frame chứa giao diện
        # Thêm viền cho Frame
        self.main_frame = Frame(self, bd=2, relief=GROOVE)
        # Vị trí Frame
        self.main_frame.place(x=20, y=50, width=820, height=490)

        # Tạo Frame con để chứa Treeview và Scrollbars
        self.frame = Frame(self.main_frame, bd=2, relief=GROOVE)
        self.frame.place(x=350, y=70, width=450, height=370)

        # Tạo bảng sản phẩm
        cols = ("ma_sp", "ten_sp", "loai", "don_vi", "chi_phi", "gia_nhap", "gia_ban")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_sp", text="Product ID")
        self.tree.heading("ten_sp", text="Product Name")
        self.tree.heading("loai", text="Category")
        self.tree.heading("don_vi", text="Unit")
        self.tree.heading("chi_phi", text="Cost")
        self.tree.heading("gia_nhap", text="Purchase Price")
        self.tree.heading("gia_ban", text="Selling Price")

        # Kích thước cột
        self.tree.column("ma_sp", width=110, stretch=False)
        self.tree.column("ten_sp", width=110, stretch=False)
        self.tree.column("loai", width=110, stretch=False)
        self.tree.column("don_vi", width=110, stretch=False)
        self.tree.column("chi_phi", width=110, stretch=False)
        self.tree.column("gia_nhap", width=110, stretch=False)
        self.tree.column("gia_ban", width=110, stretch=False)

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

        # Nút quay lại dashboard
        self.icon_return_sp = PhotoImage(file="image/return.png")
        self.btn_return_sp = Button(master=self, text="Back", image=self.icon_return_sp, compound="left")
        self.btn_return_sp.place(x=20, y=20)

        # Tạo giao diện nhập thông tin sản phẩm
        # Tạo nhãn tiêu đề
        self.label_sp = Label(master=self, text="Products Details", font=('Arial', 25))
        self.label_sp.pack(pady=20)

        # Label: Mã sp
        self.label_ma_sp = Label(master=self, text="Product ID")
        self.label_ma_sp.place(x=50, y=100)

        # Entry: Mã sp
        self.entry_ma_sp = Entry(master=self, width=30)
        self.entry_ma_sp.place(x=150, y=100)

        # Label: Tên sp
        self.label_ten_sp = Label(master=self, text="Product Name")
        self.label_ten_sp.place(x=50, y=150)

        # Entry: Tên sp
        self.entry_ten_sp = Entry(master=self, width=30)
        self.entry_ten_sp.place(x=150, y=150)

        # Label: Loại
        self.label_loai_sp = Label(master=self, text="Category")
        self.label_loai_sp.place(x=50, y=200)

        # Biến liên kết để lưu loại sản phẩm
        self.loai_sp_var = StringVar(value="0")

        # Radio Buttons: Loại sp
        self.rb_cham_soc_da = Radiobutton(self, text="Skin Care", variable=self.loai_sp_var, value="Skin Care")
        self.rb_cham_soc_da.place(x=150, y=200)

        self.rb_trang_diem = Radiobutton(self, text="Makeup",  variable=self.loai_sp_var, value="Makeup")
        self.rb_trang_diem.place(x=150, y=230)

        self.rb_nuoc_hoa = Radiobutton(self, text="Parfum", variable=self.loai_sp_var, value="Parfum")
        self.rb_nuoc_hoa.place(x=150, y=260)

        # Label: Đơn vị
        self.label_loai_sp = Label(master=self, text="Unit")
        self.label_loai_sp.place(x=50, y=310)

        # ComboBox: Đơn vị
        self.cb_don_vi_sp = Combobox(master=self, state="readonly", values=["Unit","Box","Bottle","Ml"])
        self.cb_don_vi_sp.place(x=150, y=310)
        self.cb_don_vi_sp.set("Chose unit")

        # Label: Chi phí
        self.label_chi_phi_sp = Label(master=self, text="Cost")
        self.label_chi_phi_sp.place(x=50, y=360)

        # Entry: Chi phí
        self.entry_chi_phi_sp = Entry(master=self, width=30)
        self.entry_chi_phi_sp.place(x=150, y=360)

        # Label: Giá nhập
        self.label_gia_nhap_sp = Label(master=self, text="Purchase Price")
        self.label_gia_nhap_sp.place(x=50, y= 410)

        # Entry: Giá nhập
        self.entry_gia_nhap_sp = Entry(master=self, width=30)
        self.entry_gia_nhap_sp.place(x=150, y=410)

        # Label: Giá bán
        self.label_gia_ban_sp = Label(master=self, text="Selling Price")
        self.label_gia_ban_sp.place(x=50, y=460)

        # Entry: Giá bán
        self.entry_gia_ban_sp = Entry(master=self, width=20)
        self.entry_gia_ban_sp.place(x=150, y=460)
        self.entry_gia_ban_sp.config(state="readonly")

        # Nút tính giá bán
        self.btn_tinh_gia_ban_sp = Button(master=self, text="Calculate Price", compound="left")
        self.btn_tinh_gia_ban_sp.place(x=280, y=455)

        # Nút thêm sp
        self.icon_add_sp = PhotoImage(file="image/add.png")
        self.btn_add_sp = Button(master=self, text="Add", image=self.icon_add_sp, compound="left")
        self.btn_add_sp.place(x=50, y=500)

        # Nút sửa sp
        self.icon_update_sp = PhotoImage(file="image/update.png")
        self.btn_update = Button(self, text="Edit", image=self.icon_update_sp, compound="left")
        self.btn_update.place(x=120, y=500)

        # Nút làm mới trường dữ liệu
        self.icon_refresh_sp = PhotoImage(file="image/refresh.png")
        self.btn_refresh_sp = Button(self, text="Refresh", image=self.icon_refresh_sp, compound="left")
        self.btn_refresh_sp.place(x=180, y=500)

        # Nút tìm kiếm
        self.icon_search_sp = PhotoImage(file="image/search.png")
        self.entry_search_sp = Entry(master=self, width=60)
        self.entry_search_sp.place(x=370, y=90)
        self.btn_search_sp = Button(self, text="Search", image=self.icon_search_sp, compound="left")
        self.btn_search_sp.place(x=745, y=87)

        # Nút in
        self.icon_printer_sp = PhotoImage(file="image/printer.png")
        self.btn_printer_sp = Button(self, text="Print", image=self.icon_printer_sp, compound="left")
        self.btn_printer_sp.place(x=380, y=500)

        # Nút xuất file dạng CSV
        self.icon_csv_sp = PhotoImage(file="image/csv.png")
        self.btn_csv_sp = Button(self, text="Export CSV", image=self.icon_csv_sp, compound="left")
        self.btn_csv_sp.place(x=440, y=500)

        # Nút xuất file dạng Excel
        self.icon_excel_sp = PhotoImage(file="image/excel.png")
        self.btn_excel_sp = Button(self, text="Export Excel", image=self.icon_excel_sp, compound="left")
        self.btn_excel_sp.place(x=540, y=500)

        # Nút làm mới bảng
        self.icon_refresh_treeview_sp = PhotoImage(file="image/refresh.png")
        self.btn_refresh_treeview_sp = Button(self, text="Refresh", image=self.icon_refresh_treeview_sp,
                                               compound="left")
        self.btn_refresh_treeview_sp.place(x=645, y=500)

        # Nút xóa sp
        self.icon_delete_sp = PhotoImage(file="image/delete.png")
        self.btn_delete = Button(self, text="Delete", image=self.icon_delete_sp, compound="left")
        self.btn_delete.place(x=725, y=500)