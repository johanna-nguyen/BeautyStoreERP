from tkinter import Tk, Label, Entry, PhotoImage, Button, Frame, Scrollbar, StringVar, Radiobutton, GROOVE, ttk, \
    VERTICAL, HORIZONTAL, RIGHT, Y, BOTTOM, X, BOTH
from tkinter.ttk import Combobox

from tkcalendar import DateEntry


class NVView (Frame):
    def __init__(self, parent):
        super().__init__(parent)


    def ql_nv_widget(self):
        """Hiển thị giao diện quản lý nhân viên"""
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

        # Tạo bảng nhân viên
        cols = ("ma_nv", "ten_nv", "ngay_sinh", "gioi_tinh", "chuc_vu", "dia_chi", "sdt_nv", "email")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_nv", text="Employee ID")
        self.tree.heading("ten_nv", text="Name")
        self.tree.heading("ngay_sinh", text="DOB")
        self.tree.heading("gioi_tinh", text="Gender")
        self.tree.heading("chuc_vu", text="Job title")
        self.tree.heading("dia_chi", text="Address")
        self.tree.heading("sdt_nv", text="Phone Number")
        self.tree.heading("email", text="Email")

        # Kích thước cột
        self.tree.column("ma_nv", width=110, stretch=False)
        self.tree.column("ten_nv", width=110, stretch=False)
        self.tree.column("ngay_sinh", width=110, stretch=False)
        self.tree.column("gioi_tinh", width=110, stretch=False)
        self.tree.column("chuc_vu", width=110, stretch=False)
        self.tree.column("dia_chi", width=110, stretch=False)
        self.tree.column("sdt_nv", width=110, stretch=False)
        self.tree.column("email", width=110, stretch=False)

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
        self.icon_return_nv = PhotoImage(file="image/return.png")
        self.btn_return_nv = Button(master=self, text="Back", image=self.icon_return_nv, compound="left")
        self.btn_return_nv.place(x=20, y=20)

        # Tạo giao diện nhập thông tin nhân viên
        # Tạo nhãn tiêu đề
        self.label_nv = Label(master=self, text="Employees Details", font=('Arial', 25))
        self.label_nv.pack(pady=20)

        # Label: Mã nv
        self.label_ma_nv = Label(master=self, text="Employee ID")
        self.label_ma_nv.place(x=50, y=100)

        # Entry: Mã nv
        self.entry_ma_nv = Entry(master=self, width=30)
        self.entry_ma_nv.place(x=150, y=100)

        # Label: Tên nv
        self.label_ten_nv= Label(master=self, text="Name")
        self.label_ten_nv.place(x=50, y=150)

        # Entry: Tên nv
        self.entry_ten_nv = Entry(master=self, width=30)
        self.entry_ten_nv.place(x=150, y=150)

        # Label: Ngày sinh
        self.label_ngay_sinh = Label(master=self, text="DOB")
        self.label_ngay_sinh.place(x=50, y=200)

        # Entry: Ngày sinh
        self.entry_ngay_sinh = DateEntry(self, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.entry_ngay_sinh.place(x=150, y=200)

        # Label: Giới tính
        self.label_gioi_tinh = Label(master=self, text="Gender")
        self.label_gioi_tinh.place(x=50, y=250)

        # Biến liên kết để lưu giới tính
        self.gioi_tinh_var = StringVar(value="0")

        # Radio Buttons: Giới tính
        self.rb_gioi_tinh_nu = Radiobutton(self, text="Male", variable=self.gioi_tinh_var, value="Male")
        self.rb_gioi_tinh_nu.place(x=150, y=250)

        self.rb_gioi_tinh_nam = Radiobutton(self, text="Female", variable=self.gioi_tinh_var, value="Female")
        self.rb_gioi_tinh_nam.place(x=210, y=250)

        # Label: Chức vụ
        self.label_chuc_vu = Label(master=self, text="Job title")
        self.label_chuc_vu.place(x=50, y=300)

        # ComboBox: Chức vụ
        self.cb_chuc_vu = Combobox(master=self, state="readonly",values=["Manager", "Cashier", "Sale Staff"])
        self.cb_chuc_vu.place(x=150, y=300)
        self.cb_chuc_vu.set("Select job title")

        # Label: Địa chỉ
        self.label_dia_chi_nv = Label(master=self, text="Address")
        self.label_dia_chi_nv.place(x=50, y=350)

        # Entry: Địa chỉ
        self.entry_dia_chi_nv = Entry(master=self, width=30)
        self.entry_dia_chi_nv.place(x=150, y=350)

        # Label: Sdt
        self.label_sdt_nv = Label(master=self, text="Phone Number")
        self.label_sdt_nv.place(x=50, y=400)

        # Entry: Sdt
        self.entry_sdt_nv = Entry(master=self, width=30)
        self.entry_sdt_nv.place(x=150, y=400)

        # Label: Email
        self.label_email = Label(master=self, text="Email")
        self.label_email.place(x=50, y=450)

        # Entry: Email
        self.entry_email = Entry(master=self, width=30)
        self.entry_email.place(x=150, y=450)

        # Nút thêm nv
        self.icon_add_nv = PhotoImage(file="image/add.png")
        self.btn_add_nv = Button(master=self, text="Thêm", image=self.icon_add_nv, compound="left")
        self.btn_add_nv.place(x=50, y=500)

        # Nút sửa nv
        self.icon_update_nv = PhotoImage(file="image/update.png")
        self.btn_update = Button(self, text="Sửa", image=self.icon_update_nv, compound="left")
        self.btn_update.place(x=120, y=500)

        # Nút làm mới trường dữ liệu
        self.icon_refresh_nv = PhotoImage(file="image/refresh.png")
        self.btn_refresh_nv = Button(self, text="Refresh", image=self.icon_refresh_nv, compound="left")
        self.btn_refresh_nv.place(x=180, y=500)

        # Nút tìm kiếm
        self.icon_search_nv = PhotoImage(file="image/search.png")
        self.entry_search_nv = Entry(master=self, width=60)
        self.entry_search_nv.place(x=370, y=90)
        self.btn_search_nv = Button(self, text="Search", image=self.icon_search_nv, compound="left")
        self.btn_search_nv.place(x=745, y=87)

        # Nút in
        self.icon_printer_nv = PhotoImage(file="image/printer.png")
        self.btn_printer_nv = Button(self, text="Print", image=self.icon_printer_nv, compound="left")
        self.btn_printer_nv.place(x=380, y=500)

        # Nút xuất file dạng CSV
        self.icon_csv_nv = PhotoImage(file="image/csv.png")
        self.btn_csv_nv = Button(self, text="Export CSV", image=self.icon_csv_nv, compound="left")
        self.btn_csv_nv.place(x=440, y=500)

        # Nút xuất file dạng Excel
        self.icon_excel_nv = PhotoImage(file="image/excel.png")
        self.btn_excel_nv = Button(self, text="Export Excel", image=self.icon_excel_nv, compound="left")
        self.btn_excel_nv.place(x=540, y=500)

        # Nút làm mới bảng
        self.icon_refresh_treeview_nv = PhotoImage(file="image/refresh.png")
        self.btn_refresh_treeview_nv = Button(self, text="Refresh", image=self.icon_refresh_treeview_nv,
                                              compound="left")
        self.btn_refresh_treeview_nv.place(x=645, y=500)

        # Nút xóa sp
        self.icon_delete_nv = PhotoImage(file="image/delete.png")
        self.btn_delete = Button(self, text="Delete", image=self.icon_delete_nv, compound="left")
        self.btn_delete.place(x=725, y=500)