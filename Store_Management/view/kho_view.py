from tkinter import Label, Entry, PhotoImage, Button, Frame, Scrollbar, ttk, GROOVE, VERTICAL, HORIZONTAL, RIGHT, Y, \
    BOTTOM, X, BOTH
from tkinter.ttk import Combobox

from tkcalendar import DateEntry


class KhoView (Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def ql_kho_widget(self):
        """Hiển thị giao diện quản lý kho"""

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

        # Tạo bảng kho
        cols = ("ma_kho","ma_sp", "ten_sp", "don_vi", "ton_kho", "ngay_cap_nhat")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=10)

        # Tiêu đề các cột
        self.tree.heading("ma_kho", text="Inventory ID")
        self.tree.heading("ma_sp", text="Product ID")
        self.tree.heading("ten_sp", text="Product Name")
        self.tree.heading("don_vi", text="Unit")
        self.tree.heading("ton_kho", text="Quantity")
        self.tree.heading("ngay_cap_nhat", text="Last Updated")

        # Kích thước cột
        self.tree.column("ma_kho", width=110, stretch=False)
        self.tree.column("ma_sp", width=110, stretch=False)
        self.tree.column("ten_sp", width=110, stretch=False)
        self.tree.column("don_vi", width=110, stretch=False)
        self.tree.column("ton_kho", width=110, stretch=False)
        self.tree.column("ngay_cap_nhat", width=110, stretch=False)

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
        self.icon_return_kho = PhotoImage(file="image/return.png")
        self.btn_return_kho = Button(master=self, text="Back", image=self.icon_return_kho, compound="left")
        self.btn_return_kho.place(x=20, y=20)

        # Tạo giao diện nhập thông tin kho
        # Tạo nhãn tiêu đề
        self.label_ncc = Label(master=self, text="Inventory Details", font=('Arial', 25))
        self.label_ncc.pack(pady=20)

        # Label: Mã kho
        self.label_ma_kho = Label(master=self, text="Inventory ID")
        self.label_ma_kho.place(x=50, y=100)

        # Entry: Mã kho
        self.entry_ma_kho= Entry(master=self, width=30)
        self.entry_ma_kho.place(x=150, y=100)

        # Label: Mã sp
        self.label_ma_sp= Label(master=self, text="Product ID")
        self.label_ma_sp.place(x=50, y=150)

        # Combo: Mã sp
        self.cb_ma_sp = Combobox(master=self)
        self.cb_ma_sp.place(x=150, y=150)
        self.cb_ma_sp.set("Choose Product ID")

        # Label: Tên sp
        self.label_ten_sp = Label(master=self, text="Product Name")
        self.label_ten_sp.place(x=50, y=200)

        # Entry: Tên sp
        self.entry_ten_sp = Entry(master=self, width=30)
        self.entry_ten_sp.place(x=150, y=200)
        self.entry_ten_sp.config(state="readonly")

        # Label: Đơn vị
        self.label_don_vi = Label(master=self, text="Unit")
        self.label_don_vi.place(x=50, y=250)

        # Entry: Đơn vị
        self.entry_don_vi = Entry(master=self, width=30)
        self.entry_don_vi.place(x=150, y=250)
        self.entry_don_vi.config(state="readonly")

        # Label: Tồn kho
        self.label_ton_kho = Label(master=self, text="Quantity")
        self.label_ton_kho.place(x=50, y=300)

        # Entry: Tồn kho
        self.entry_ton_kho = Entry(master=self, width=20)
        self.entry_ton_kho.place(x=150, y=300)
        self.entry_ton_kho.config(state="readonly")

        # Nút tính tồn kho
        self.btn_tinh_ton_kho = Button(master=self, text="Calculate", compound="left")
        self.btn_tinh_ton_kho.place(x=270, y=298)

        # Label: Ngày cập nhật
        self.label_ngay_cn = Label(master=self, text="Last Updated")
        self.label_ngay_cn.place(x=50, y=350)

        # Entry: Ngày cập nhật
        self.entry_ngay_cn = DateEntry(self, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.entry_ngay_cn.place(x=150, y=350)

        # Nút thêm tồn kho
        self.icon_add_kho = PhotoImage(file="image/add.png")
        self.btn_add_kho = Button(master=self, text="Add", image=self.icon_add_kho, compound="left")
        self.btn_add_kho.place(x=50, y=380)

        # Nút sửa kho
        self.icon_update_kho = PhotoImage(file="image/update.png")
        self.btn_update = Button(self, text="Edit", image=self.icon_update_kho, compound="left")
        self.btn_update.place(x=120, y=380)

        # Nút làm mới trường dữ liệu
        self.icon_refresh_kho = PhotoImage(file="image/refresh.png")
        self.btn_refresh_kho = Button(self, text="Refresh", image=self.icon_refresh_kho, compound="left")
        self.btn_refresh_kho.place(x=180, y=380)

        # Nút tìm kiếm
        self.icon_search_kho = PhotoImage(file="image/search.png")
        self.entry_search_kho = Entry(master=self, width=60)
        self.entry_search_kho.place(x=370, y=90)
        self.btn_search_kho = Button(self, text="Search", image=self.icon_search_kho, compound="left")
        self.btn_search_kho.place(x=745, y=87)

        # Nút in
        self.icon_printer_kho = PhotoImage(file="image/printer.png")
        self.btn_printer_kho = Button(self, text="Print", image=self.icon_printer_kho, compound="left")
        self.btn_printer_kho.place(x=380, y=380)

        # Nút xuất file dạng CSV
        self.icon_csv_kho = PhotoImage(file="image/csv.png")
        self.btn_csv_kho = Button(self, text="Export CSV", image=self.icon_csv_kho, compound="left")
        self.btn_csv_kho.place(x=440, y=380)

        # Nút xuất file dạng Excel
        self.icon_excel_kho = PhotoImage(file="image/excel.png")
        self.btn_excel_kho = Button(self, text="Export Excel", image=self.icon_excel_kho, compound="left")
        self.btn_excel_kho.place(x=540, y=380)

        # Nút làm mới bảng
        self.icon_refresh_treeview_kho = PhotoImage(file="image/refresh.png")
        self.btn_refresh_treeview_kho = Button(self, text="Refresh", image=self.icon_refresh_treeview_kho,
                                               compound="left")
        self.btn_refresh_treeview_kho.place(x=645, y=380)

        # Nút xóa kho
        self.icon_delete_kho = PhotoImage(file="image/delete.png")
        self.btn_delete = Button(self, text="Delete", image=self.icon_delete_kho, compound="left")
        self.btn_delete.place(x=725, y=380)