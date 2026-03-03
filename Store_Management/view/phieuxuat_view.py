from tkinter import Tk, Label, Entry, PhotoImage, Button, Frame, Scrollbar, StringVar, Radiobutton, GROOVE, ttk, RIGHT, \
    Y, VERTICAL, HORIZONTAL, BOTTOM, X, BOTH
from tkinter.ttk import Combobox

from tkcalendar import DateEntry

class PXView (Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def ql_px_widget(self):
        """Hiển thị giao diện quản lý phiếu xuất"""
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

        # Tạo bảng phiếu xuất
        cols = ("ma_px", "ma_kh", "ma_sp", "so_luong", "gia_xuat", "thanh_tien", "nguoi_xuat", "ngay_px")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_px", text="Sales Orders ID")
        self.tree.heading("ma_kh", text="Customer ID")
        self.tree.heading("ma_sp", text="Product ID")
        self.tree.heading("so_luong", text="Quantity")
        self.tree.heading("gia_xuat", text="Sales Price")
        self.tree.heading("thanh_tien", text="Total")
        self.tree.heading("nguoi_xuat", text="Employee ID")
        self.tree.heading("ngay_px", text="Date of sales orders")

        # Kích thước cột
        self.tree.column("ma_px", width=110, stretch=False)
        self.tree.column("ma_kh", width=110, stretch=False)
        self.tree.column("ma_sp", width=110, stretch=False)
        self.tree.column("so_luong", width=110, stretch=False)
        self.tree.column("gia_xuat", width=110, stretch=False)
        self.tree.column("thanh_tien", width=110, stretch=False)
        self.tree.column("nguoi_xuat", width=110, stretch=False)
        self.tree.column("ngay_px", width=110, stretch=False)

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
        self.icon_return_px = PhotoImage(file="image/return.png")
        self.btn_return_px = Button(master=self, text="Back", image=self.icon_return_px, compound="left")
        self.btn_return_px.place(x=20, y=20)

        # Tạo giao diện nhập thông tin phiếu xuất
        # Tạo nhãn tiêu đề
        self.label_px = Label(master=self, text="Sales Order Details", font=('Arial', 25))
        self.label_px.pack(pady=20)

        # Label: Mã phiếu xuất
        self.label_ma_px = Label(master=self, text="Sales Orders ID")
        self.label_ma_px.place(x=50, y=100)

        # Entry: Mã phiếu xuất
        self.entry_ma_px = Entry(master=self, width=30)
        self.entry_ma_px.place(x=150, y=100)

        # Label: Mã khách hàng
        self.label_ma_kh = Label(master=self, text="Customer ID")
        self.label_ma_kh.place(x=50, y=150)

        # Combobox: Mã khách hàng
        self.cb_ma_kh = Combobox(master=self, state="readonly")
        self.cb_ma_kh.place(x=150, y=150)
        self.cb_ma_kh.set("Choose Customer")

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

        # Label: Giá xuất
        self.label_gia_xuat = Label(master=self, text="Sales Price")
        self.label_gia_xuat.place(x=50, y=300)

        # Entry: Giá xuất
        self.entry_gia_xuat = Entry(master=self, width=30)
        self.entry_gia_xuat.place(x=150, y=300)

        # Label: Thành tiền
        self.label_thanh_tien = Label(master=self, text="Total")
        self.label_thanh_tien.place(x=50, y=350)

        # Entry: Thành tiền
        self.entry_thanh_tien = Entry(master=self, width=30)
        self.entry_thanh_tien.place(x=150, y=350)
        self.entry_thanh_tien.config(state="readonly")

        # Nút tính thành tiền
        self.btn_tinh_thanh_tien = Button(master=self, text="Calculate Price", compound="left")
        self.btn_tinh_thanh_tien.place(x=270, y=345)

        # Label: Người xuất
        self.label_nguoi_xuat = Label(master=self, text="Employee ID")
        self.label_nguoi_xuat.place(x=50, y=400)

        # Combobox: Người xuất
        self.cb_nguoi_xuat = Combobox(master=self, state="readonly")
        self.cb_nguoi_xuat.place(x=150, y=400)
        self.cb_nguoi_xuat.set("Choose Employee ID")

        # Label: Ngày phiếu xuất
        self.label_ngay_px = Label(master=self, text="Date of Sales Orders")
        self.label_ngay_px.place(x=50, y=450)

        # Entry: Ngày phiếu xuất
        self.entry_ngay_px = DateEntry(self, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.entry_ngay_px.place(x=150, y=450)

        # Nút thêm phiếu xuất
        self.icon_add_px = PhotoImage(file="image/add.png")
        self.btn_add_px = Button(master=self, text="Add", image=self.icon_add_px, compound="left")
        self.btn_add_px.place(x=50, y=500)

        # Nút sửa phiếu xuất
        self.icon_update_px = PhotoImage(file="image/update.png")
        self.btn_update = Button(self, text="Edit", image=self.icon_update_px, compound="left")
        self.btn_update.place(x=120, y=500)

        # Nút làm mới trường dữ liệu
        self.icon_refresh_px = PhotoImage(file="image/refresh.png")
        self.btn_refresh_px = Button(self, text="Refresh", image=self.icon_refresh_px, compound="left")
        self.btn_refresh_px.place(x=180, y=500)

        # Nút tìm kiếm
        self.icon_search_px = PhotoImage(file="image/search.png")
        self.entry_search_px = Entry(master=self, width=60)
        self.entry_search_px.place(x=370, y=90)
        self.btn_search_px = Button(self, text="Search", image=self.icon_search_px, compound="left")
        self.btn_search_px.place(x=745, y=87)

        # Nút in
        self.icon_printer_px = PhotoImage(file="image/printer.png")
        self.btn_printer_px = Button(self, text="Print", image=self.icon_printer_px, compound="left")
        self.btn_printer_px.place(x=380, y=500)

        # Nút xuất file dạng CSV
        self.icon_csv_px = PhotoImage(file="image/csv.png")
        self.btn_csv_px = Button(self, text="Export CSV", image=self.icon_csv_px, compound="left")
        self.btn_csv_px.place(x=440, y=500)

        # Nút xuất file dạng Excel
        self.icon_excel_px = PhotoImage(file="image/excel.png")
        self.btn_excel_px = Button(self, text="Export Excel", image=self.icon_excel_px, compound="left")
        self.btn_excel_px.place(x=540, y=500)

        # Nút làm mới bảng
        self.icon_refresh_treeview_px = PhotoImage(file="image/refresh.png")
        self.btn_refresh_treeview_px = Button(self, text="Refresh", image=self.icon_refresh_treeview_px,
                                               compound="left")
        self.btn_refresh_treeview_px.place(x=645, y=500)

        # Nút xóa phiếu xuất
        self.icon_delete_px = PhotoImage(file="image/delete.png")
        self.btn_delete = Button(self, text="Delete", image=self.icon_delete_px, compound="left")
        self.btn_delete.place(x=725, y=500)