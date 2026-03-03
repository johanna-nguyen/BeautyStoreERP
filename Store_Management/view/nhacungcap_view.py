from tkinter import Tk, Label, Entry, PhotoImage, Button, Frame, GROOVE, HORIZONTAL, Scrollbar, VERTICAL, ttk, RIGHT, Y, \
    BOTTOM, X, BOTH



class NccView (Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def ql_ncc_widget(self):
        """Hiển thị giao diện quản lý nhà cung cấp"""

        # Kích thước GUI đăng nhập
        self.master.geometry('870x450')

        # Tạo Frame chứa giao diện
        # Thêm viền cho Frame
        self.main_frame = Frame(self, bd=2, relief=GROOVE)

        # Vị trí Frame
        self.main_frame.place(x=20, y=50, width=820, height=370)

        # Tạo Frame con để chứa Treeview và Scrollbars
        self.frame = Frame(self.main_frame, bd=2, relief=GROOVE)
        self.frame.place(x=350, y=70, width=450, height=250)

        # Tạo bảng nhà cung cấp
        cols = ("ma_ncc", "ten_ncc", "dia_chi", "sdt")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=10)

        # Tiêu đề các cột
        self.tree.heading("ma_ncc", text="Supplier ID")
        self.tree.heading("ten_ncc", text="Supplier Name")
        self.tree.heading("dia_chi", text="Address")
        self.tree.heading("sdt", text="Phone Number")

        # Kích thước cột
        self.tree.column("ma_ncc", width=110, stretch=False)
        self.tree.column("ten_ncc", width=110, stretch=False)
        self.tree.column("dia_chi", width=110, stretch=False)
        self.tree.column("sdt", width=110, stretch=False)

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
        self.icon_return_ncc = PhotoImage(file="image/return.png")
        self.btn_return_ncc = Button(master=self, text="Back", image=self.icon_return_ncc, compound="left")
        self.btn_return_ncc.place(x=20, y=20)

        # Tạo giao diện nhập thông tin nhà cung cấp
        # Tạo nhãn tiêu đề
        self.label_ncc = Label(master=self, text="Supplies Detail", font=('Arial', 25))
        self.label_ncc.pack(pady=20)

        # Mã ncc
        self.label_ma_ncc = Label(master=self, text="Supplier ID")
        self.label_ma_ncc.place(x=50, y=100)
        self.entry_ma_ncc = Entry(master=self, width=30)
        self.entry_ma_ncc.place(x=150, y=100)

        # Tên ncc
        self.label_ten_ncc = Label(master=self, text="Supplier Name")
        self.label_ten_ncc.place(x=50, y=150)
        self.entry_ten_ncc = Entry(master=self, width=30)
        self.entry_ten_ncc.place(x=150, y=150)

        # Địa chỉ ncc
        self.label_dia_chi_ncc = Label(master=self, text="Address")
        self.label_dia_chi_ncc.place(x=50, y=200)
        self.entry_dia_chi_ncc = Entry(master=self, width=30)
        self.entry_dia_chi_ncc.place(x=150, y=200)

        # Số điện thoại ncc
        self.label_sdt_ncc = Label(master=self, text="Phone Number")
        self.label_sdt_ncc.place(x=50, y=250)
        self.entry_sdt_ncc = Entry(master=self, width=30)
        self.entry_sdt_ncc.place(x=150, y=250)

        # Nút thêm ncc
        self.icon_add_ncc = PhotoImage(file="image/add.png")
        self.btn_add_ncc = Button(master=self, text="Add", image=self.icon_add_ncc, compound="left")
        self.btn_add_ncc.place(x=50, y=380)

        # Nút sửa ncc
        self.icon_update_ncc = PhotoImage(file="image/update.png")
        self.btn_update = Button(self, text="Edit", image=self.icon_update_ncc, compound="left")
        self.btn_update.place(x=120, y=380)

        # Nút làm mới trường dữ liệu
        self.icon_refresh_ncc = PhotoImage(file="image/refresh.png")
        self.btn_refresh_ncc = Button(self, text="Refresh", image=self.icon_refresh_ncc, compound="left")
        self.btn_refresh_ncc.place(x=180, y=380)

        # Nút tìm kiếm
        self.icon_search_ncc = PhotoImage(file="image/search.png")
        self.entry_search_ncc = Entry(master=self, width=60)
        self.entry_search_ncc.place(x=370, y=90)
        self.btn_search_ncc = Button(self, text="Search", image=self.icon_search_ncc, compound="left")
        self.btn_search_ncc.place(x=745, y=87)

        # Nút in
        self.icon_printer_ncc = PhotoImage(file="image/printer.png")
        self.btn_printer_ncc = Button(self, text="Print", image=self.icon_printer_ncc, compound="left")
        self.btn_printer_ncc.place(x=380, y=380)

        # Nút xuất file dạng CSV
        self.icon_csv_ncc = PhotoImage(file="image/csv.png")
        self.btn_csv_ncc = Button(self, text="Export CSV", image=self.icon_csv_ncc, compound="left")
        self.btn_csv_ncc.place(x=440, y=380)

        # Nút xuất file dạng Excel
        self.icon_excel_ncc = PhotoImage(file="image/excel.png")
        self.btn_excel_ncc = Button(self, text="Export Excel", image=self.icon_excel_ncc, compound="left")
        self.btn_excel_ncc.place(x=540, y=380)

        # Nút làm mới bảng
        self.icon_refresh_treeview_ncc = PhotoImage(file="image/refresh.png")
        self.btn_refresh_treeview_ncc = Button(self, text="Refresh", image=self.icon_refresh_treeview_ncc,
                                               compound="left")
        self.btn_refresh_treeview_ncc.place(x=645, y=380)

        # Nút xóa ncc
        self.icon_delete_ncc = PhotoImage(file="image/delete.png")
        self.btn_delete = Button(self, text="Delete", image=self.icon_delete_ncc, compound="left")
        self.btn_delete.place(x=725, y=380)