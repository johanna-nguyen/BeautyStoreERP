from tkinter import Tk, Label, Entry, PhotoImage, Button, Frame, Scrollbar, StringVar, Radiobutton, ttk, GROOVE, \
    VERTICAL, RIGHT, Y, HORIZONTAL, BOTTOM, X, BOTH
from tkinter.ttk import Combobox

from tkcalendar import DateEntry


class KHView (Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def ql_kh_widget(self):
        """Hiển thị giao diện quản lý khách hàng"""
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

        # Tạo bảng khách hàng
        cols = ("ma_kh", "ten_kh", "ngay_sinh_kh", "gioi_tinh_kh", "hang_kh", "dia_chi_kh", "sdt_kh")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_kh", text="Customer ID")
        self.tree.heading("ten_kh", text="Name")
        self.tree.heading("ngay_sinh_kh", text="DOB")
        self.tree.heading("gioi_tinh_kh", text="Gender")
        self.tree.heading("hang_kh", text="Type")
        self.tree.heading("dia_chi_kh", text="Address")
        self.tree.heading("sdt_kh", text="Phone Number")

        # Kích thước cột
        self.tree.column("ma_kh", width=110, stretch=False)
        self.tree.column("ten_kh", width=110, stretch=False)
        self.tree.column("ngay_sinh_kh", width=110, stretch=False)
        self.tree.column("gioi_tinh_kh", width=110, stretch=False)
        self.tree.column("hang_kh", width=110, stretch=False)
        self.tree.column("dia_chi_kh", width=110, stretch=False)
        self.tree.column("sdt_kh", width=110, stretch=False)

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
        self.icon_return_kh = PhotoImage(file="image/return.png")
        self.btn_return_kh = Button(master=self, text="Quay lại", image=self.icon_return_kh, compound="left")
        self.btn_return_kh.place(x=20, y=20)

        # Tạo giao diện nhập thông tin khách hàng
        # Tạo nhãn tiêu đề
        self.label_kh = Label(master=self, text="Customers Details", font=('Arial', 25))
        self.label_kh.pack(pady=20)

        # Label: Mã kh
        self.label_ma_kh = Label(master=self, text="Customer ID")
        self.label_ma_kh.place(x=50, y=100)

        # Entry: Mã kh
        self.entry_ma_kh = Entry(master=self, width=30)
        self.entry_ma_kh.place(x=150, y=100)

        # Label: Tên kh
        self.label_ten_kh= Label(master=self, text="Name")
        self.label_ten_kh.place(x=50, y=150)

        # Entry: Tên kh
        self.entry_ten_kh = Entry(master=self, width=30)
        self.entry_ten_kh.place(x=150, y=150)

        # Label: Ngày sinh
        self.label_ngay_sinh_kh = Label(master=self, text="DOB")
        self.label_ngay_sinh_kh.place(x=50, y=200)

        # Entry: Ngày sinh
        self.entry_ngay_sinh_kh = DateEntry(self, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.entry_ngay_sinh_kh.place(x=150, y=200)

        # Label: Giới tính
        self.label_gioi_tinh_kh = Label(master=self, text="Gender")
        self.label_gioi_tinh_kh.place(x=50, y=250)

        # Biến liên kết để lưu giới tính
        self.gioi_tinh_var_kh = StringVar(value="0")

        # Radio Buttons: Giới tính
        self.rb_gioi_tinh_nu = Radiobutton(self, text="Nam", variable=self.gioi_tinh_var_kh, value="Male")
        self.rb_gioi_tinh_nu.place(x=150, y=250)

        self.rb_gioi_tinh_nam = Radiobutton(self, text="Nữ", variable=self.gioi_tinh_var_kh, value="Female")
        self.rb_gioi_tinh_nam.place(x=210, y=250)

        # Label: Hạng kh
        self.label_hang_kh= Label(master=self, text="Type")
        self.label_hang_kh.place(x=50, y=300)

        # ComboBox: Hạng kh
        self.cb_hang_kh = Combobox(master=self, state="readonly",values=["Beauty Starter", "Beauty Lover", "Beauty Expert", "Beauty Queen"])
        self.cb_hang_kh.place(x=150, y=300)
        self.cb_hang_kh.set("Chose type")

        # Label: Địa chỉ
        self.label_dia_chi_kh = Label(master=self, text="Address")
        self.label_dia_chi_kh.place(x=50, y=350)

        # Entry: Địa chỉ
        self.entry_dia_chi_kh = Entry(master=self, width=30)
        self.entry_dia_chi_kh.place(x=150, y=350)

        # Label: Sdt
        self.label_sdt_kh = Label(master=self, text="Phone Number")
        self.label_sdt_kh.place(x=50, y=400)

        # Entry: Sdt
        self.entry_sdt_kh = Entry(master=self, width=30)
        self.entry_sdt_kh.place(x=150, y=400)

        # Nút thêm kh
        self.icon_add_kh = PhotoImage(file="image/add.png")
        self.btn_add_kh = Button(master=self, text="Add", image=self.icon_add_kh, compound="left")
        self.btn_add_kh.place(x=50, y=500)

        # Nút sửa kh
        self.icon_update_kh = PhotoImage(file="image/update.png")
        self.btn_update = Button(self, text="Edit", image=self.icon_update_kh, compound="left")
        self.btn_update.place(x=120, y=500)

        # Nút làm mới trường dữ liệu
        self.icon_refresh_kh = PhotoImage(file="image/refresh.png")
        self.btn_refresh_kh = Button(self, text="Refresh", image=self.icon_refresh_kh, compound="left")
        self.btn_refresh_kh.place(x=180, y=500)

        # Nút tìm kiếm
        self.icon_search_kh = PhotoImage(file="image/search.png")
        self.entry_search_kh = Entry(master=self, width=60)
        self.entry_search_kh.place(x=370, y=90)
        self.btn_search_kh = Button(self, text="Search", image=self.icon_search_kh, compound="left")
        self.btn_search_kh.place(x=745, y=87)

        # Nút in
        self.icon_printer_kh = PhotoImage(file="image/printer.png")
        self.btn_printer_kh = Button(self, text="Print", image=self.icon_printer_kh, compound="left")
        self.btn_printer_kh.place(x=380, y=500)

        # Nút xuất file dạng CSV
        self.icon_csv_kh = PhotoImage(file="image/csv.png")
        self.btn_csv_kh = Button(self, text="Export CSV", image=self.icon_csv_kh, compound="left")
        self.btn_csv_kh.place(x=440, y=500)

        # Nút xuất file dạng Excel
        self.icon_excel_kh = PhotoImage(file="image/excel.png")
        self.btn_excel_kh = Button(self, text="Export Excel", image=self.icon_excel_kh, compound="left")
        self.btn_excel_kh.place(x=540, y=500)

        # Nút làm mới bảng
        self.icon_refresh_treeview_kh = PhotoImage(file="image/refresh.png")
        self.btn_refresh_treeview_kh = Button(self, text="Refresh", image=self.icon_refresh_treeview_kh,
                                              compound="left")
        self.btn_refresh_treeview_kh.place(x=645, y=500)

        # Nút xóa kh
        self.icon_delete_kh = PhotoImage(file="image/delete.png")
        self.btn_delete = Button(self, text="Delete", image=self.icon_delete_kh, compound="left")
        self.btn_delete.place(x=725, y=500)