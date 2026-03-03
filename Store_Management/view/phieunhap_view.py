from tkinter import Tk, Label, Entry, PhotoImage, Button, Frame, Scrollbar, StringVar, Radiobutton, GROOVE, VERTICAL, \
    HORIZONTAL, RIGHT, Y, BOTH, ttk, BOTTOM, X
from tkinter.ttk import Combobox

from tkcalendar import DateEntry

class PNView (Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def ql_pn_widget(self):
        """Hiển thị giao diện quản lý phiếu nhập"""
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

        # Tạo bảng phiếu nhập
        cols = ("ma_pn", "ma_ncc", "ma_sp", "so_luong", "gia_nhap", "thanh_tien", "ngay_pn")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_pn", text="Purchase ID")
        self.tree.heading("ma_ncc", text="Supplier ID")
        self.tree.heading("ma_sp", text="Product ID")
        self.tree.heading("so_luong", text="Quantity")
        self.tree.heading("gia_nhap", text="Purchase Price")
        self.tree.heading("thanh_tien", text="Total")
        self.tree.heading("ngay_pn", text="Date of purchase")

        # Kích thước cột
        self.tree.column("ma_pn", width=110, stretch=False)
        self.tree.column("ma_ncc", width=110, stretch=False)
        self.tree.column("ma_sp", width=110, stretch=False)
        self.tree.column("so_luong", width=110, stretch=False)
        self.tree.column("gia_nhap", width=110, stretch=False)
        self.tree.column("thanh_tien", width=110, stretch=False)
        self.tree.column("ngay_pn", width=110, stretch=False)

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
        self.icon_return_pn = PhotoImage(file="image/return.png")
        self.btn_return_pn = Button(master=self, text="Back", image=self.icon_return_pn, compound="left")
        self.btn_return_pn.place(x=20, y=20)

        # Tạo giao diện nhập thông tin phiếu nhập
        # Tạo nhãn tiêu đề
        self.label_pn = Label(master=self, text="Purchase Details", font=('Arial', 25))
        self.label_pn.pack(pady=20)

        # Label: Mã phiếu nhập
        self.label_ma_pn = Label(master=self, text="Purchase Orders ID")
        self.label_ma_pn.place(x=50, y=100)

        # Entry: Mã phiếu nhập
        self.entry_ma_pn = Entry(master=self, width=30)
        self.entry_ma_pn.place(x=150, y=100)

        # Label: Mã nhà cung cấp
        self.label_ma_ncc = Label(master=self, text="Supplier ID")
        self.label_ma_ncc.place(x=50, y=150)

        # Combobox: Mã nhà cung cấp
        self.cb_ma_ncc = Combobox(master=self, state="readonly")
        self.cb_ma_ncc.place(x=150, y=150)
        self.cb_ma_ncc.set("Choose Supplier ID")

        # Label: Mã sản phẩm
        self.label_ma_sp = Label(master=self, text="Product ID")
        self.label_ma_sp.place(x=50, y=200)

        # Combobox: Mã sản phẩm
        self.cb_ma_sp = Combobox(master=self, state="readonly")
        self.cb_ma_sp.place(x=150, y=200)
        self.cb_ma_sp.set("Choose Product ID")

        # Label: Số lượng
        self.label_so_luong = Label(master=self, text="Quantity")
        self.label_so_luong.place(x=50, y=250)

        # Entry: Số lượng
        self.entry_so_luong = Entry(master=self, width=30)
        self.entry_so_luong.place(x=150, y=250)

        # Label: Giá nhập
        self.label_gia_nhap = Label(master=self, text="Purchase Price")
        self.label_gia_nhap.place(x=50, y=300)

        # Entry: Giá nhập
        self.entry_gia_nhap = Entry(master=self, width=30)
        self.entry_gia_nhap.place(x=150, y=300)

        # Label: Thành tiền
        self.label_thanh_tien = Label(master=self, text="Total")
        self.label_thanh_tien.place(x=50, y=350)

        # Entry: Thành tiền
        self.entry_thanh_tien = Entry(master=self, width=30)
        self.entry_thanh_tien.place(x=150, y=350)
        self.entry_thanh_tien.config(state="readonly")

        # Nút tính thành tiền
        self.btn_tinh_thanh_tien = Button(master=self, text="Calculate", compound="left")
        self.btn_tinh_thanh_tien.place(x=270, y=345)

        # Label: Ngày phiếu nhập
        self.label_ngay_pn = Label(master=self, text="Date of purchase orders")
        self.label_ngay_pn.place(x=50, y=400)

        # Entry: Ngày phiếu nhập
        self.entry_ngay_pn = DateEntry(self, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.entry_ngay_pn.place(x=150, y=400)

        # Nút thêm phiếu nhập
        self.icon_add_pn = PhotoImage(file="image/add.png")
        self.btn_add_pn = Button(master=self, text="Add", image=self.icon_add_pn, compound="left")
        self.btn_add_pn.place(x=50, y=500)

        # Nút sửa phiếu nhập
        self.icon_update_pn = PhotoImage(file="image/update.png")
        self.btn_update = Button(self, text="Edit", image=self.icon_update_pn, compound="left")
        self.btn_update.place(x=120, y=500)

        # Nút làm mới trường dữ liệu
        self.icon_refresh_pn = PhotoImage(file="image/refresh.png")
        self.btn_refresh_pn = Button(self, text="Refresh", image=self.icon_refresh_pn, compound="left")
        self.btn_refresh_pn.place(x=180, y=500)

        # Nút tìm kiếm
        self.icon_search_pn = PhotoImage(file="image/search.png")
        self.entry_search_pn = Entry(master=self, width=60)
        self.entry_search_pn.place(x=370, y=90)
        self.btn_search_pn = Button(self, text="Search", image=self.icon_search_pn, compound="left")
        self.btn_search_pn.place(x=745, y=87)

        # Nút in
        self.icon_printer_pn = PhotoImage(file="image/printer.png")
        self.btn_printer_pn = Button(self, text="Print", image=self.icon_printer_pn, compound="left")
        self.btn_printer_pn.place(x=380, y=500)

        # Nút xuất file dạng CSV
        self.icon_csv_pn = PhotoImage(file="image/csv.png")
        self.btn_csv_pn = Button(self, text="Export CSV", image=self.icon_csv_pn, compound="left")
        self.btn_csv_pn.place(x=440, y=500)

        # Nút xuất file dạng Excel
        self.icon_excel_pn = PhotoImage(file="image/excel.png")
        self.btn_excel_pn = Button(self, text="Export Excel", image=self.icon_excel_pn, compound="left")
        self.btn_excel_pn.place(x=540, y=500)

        # Nút làm mới bảng
        self.icon_refresh_treeview_pn = PhotoImage(file="image/refresh.png")
        self.btn_refresh_treeview_pn = Button(self, text="Refresh", image=self.icon_refresh_treeview_pn,
                                               compound="left")
        self.btn_refresh_treeview_pn.place(x=645, y=500)

        # Nút xóa phiếu nhập
        self.icon_delete_pn = PhotoImage(file="image/delete.png")
        self.btn_delete = Button(self, text="Delete", image=self.icon_delete_pn, compound="left")
        self.btn_delete.place(x=725, y=500)