from tkinter import Tk, Label, Entry, PhotoImage, Button, Frame, Scrollbar, StringVar, Radiobutton, ttk, VERTICAL, \
    RIGHT, Y, HORIZONTAL, BOTTOM, X, BOTH, GROOVE
from tkinter.ttk import Combobox

from tkcalendar import DateEntry

class LuongView (Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def ql_luong_widget(self):
        """Hiển thị giao diện quản lý lương"""
        # Kích thước GUI đăng nhập
        self.master.geometry('870x710')

        # Tạo Frame chứa giao diện
        # Thêm viền cho Frame
        self.main_frame = Frame(self, bd=2, relief=GROOVE)
        # Vị trí Frame
        self.main_frame.place(x=20, y=50, width=820, height=650)

        # Tạo Frame con để chứa Treeview và Scrollbars
        self.frame = Frame(self.main_frame, bd=2, relief=GROOVE)
        self.frame.place(x=350, y=70, width=450, height=520)

        # Tạo bảng lương
        cols = ("ma_luong", "ma_nv", "chuc_vu", "luong_co_ban", "doanh_so", "so_gio_lam", "he_so_chuc_vu", "tro_cap", "thuong", "luong_hang_thang", "ngay_tinh_luong")
        self.tree = ttk.Treeview(master=self.frame, columns=cols, show="headings", height=100)

        # Tiêu đề các cột
        self.tree.heading("ma_luong", text="Salary ID")
        self.tree.heading("ma_nv", text="Employee ID")
        self.tree.heading("chuc_vu", text="Job Title")
        self.tree.heading("luong_co_ban", text="Base Salary")
        self.tree.heading("doanh_so", text="Sales Revenue")
        self.tree.heading("so_gio_lam", text="Working Hour")
        self.tree.heading("he_so_chuc_vu", text="Role Coefficient")
        self.tree.heading("tro_cap", text="Allowance")
        self.tree.heading("thuong", text="Performance Bonus")
        self.tree.heading("luong_hang_thang", text="Monthly Salary")
        self.tree.heading("ngay_tinh_luong", text="Payroll Date")

        # Kích thước cột
        self.tree.column("ma_luong", width=110, stretch=False)
        self.tree.column("ma_nv", width=110, stretch=False)
        self.tree.column("chuc_vu", width=110, stretch=False)
        self.tree.column("luong_co_ban", width=110, stretch=False)
        self.tree.column("doanh_so", width=110, stretch=False)
        self.tree.column("so_gio_lam", width=110, stretch=False)
        self.tree.column("he_so_chuc_vu", width=110, stretch=False)
        self.tree.column("tro_cap", width=110, stretch=False)
        self.tree.column("thuong", width=110, stretch=False)
        self.tree.column("luong_hang_thang", width=110, stretch=False)
        self.tree.column("ngay_tinh_luong", width=110, stretch=False)

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
        self.icon_return_luong = PhotoImage(file="image/return.png")
        self.btn_return_luong = Button(master=self, text="Back", image=self.icon_return_luong, compound="left")
        self.btn_return_luong.place(x=20, y=20)

        # Tạo giao diện nhập thông tin lương
        # Tạo nhãn tiêu đề
        self.label_nv = Label(master=self, text="Payroll Details", font=('Arial', 25))
        self.label_nv.pack(pady=20)

        # Label: Mã lương
        self.label_ma_luong = Label(master=self, text="Salary ID")
        self.label_ma_luong.place(x=50, y=100)

        # Entry: Mã lương
        self.entry_ma_luong = Entry(master=self, width=30)
        self.entry_ma_luong.place(x=150, y=100)

        # Label: Mã nv
        self.label_ma_nv = Label(master=self, text="Employedd ID")
        self.label_ma_nv.place(x=50, y=150)

        # Combobox: Mã nv
        self.cb_ma_nv = Combobox(master=self, state="readonly")
        self.cb_ma_nv.place(x=150, y=150)
        self.cb_ma_nv.set("Chọn mã nhân viên")

        # Label: Chức vụ
        self.label_chuc_vu = Label(master=self, text="Job Title")
        self.label_chuc_vu.place(x=50, y=200)

        # Entry: Chức vụ
        self.entry_chuc_vu = Entry(master=self, width=30)
        self.entry_chuc_vu.place(x=150, y=200)
        self.entry_chuc_vu.config(state="readonly")

        # Label: Lương cơ bản
        self.label_luong_cb = Label(master=self, text="Base Salary")
        self.label_luong_cb.place(x=50, y=250)

        # Entry: Lương cơ bản
        self.entry_luong_cb = Entry(master=self, width=30)
        self.entry_luong_cb.place(x=150, y=250)

        # Label: Doanh số
        self.label_doanh_so = Label(master=self, text="Sales Revenue")
        self.label_doanh_so.place(x=50, y=300)

        # Entry: Doanh số
        self.entry_doanh_so = Entry(master=self, width=30)
        self.entry_doanh_so.place(x=150, y=300)
        self.entry_doanh_so.config(state="readonly")

        # Label: Số giờ làm
        self.label_so_gio_lam = Label(master=self, text="Working Hour")
        self.label_so_gio_lam.place(x=50, y=350)

        # Entry: Số giờ làm
        self.entry_so_gio_lam = Entry(master=self, width=30)
        self.entry_so_gio_lam.place(x=150, y=350)
        self.entry_so_gio_lam.config(state="readonly")

        # Label: Hệ số chức vụ
        self.label_he_so_chuc_vu = Label(master=self, text="Role Coefficient")
        self.label_he_so_chuc_vu.place(x=50, y=400)

        # Entry: Hệ số chức vụ
        self.entry_he_so_chuc_vu = Entry(master=self, width=30)
        self.entry_he_so_chuc_vu.place(x=150, y=400)
        self.entry_he_so_chuc_vu.config(state="readonly")

        # Label: Trợ cấp
        self.label_tro_cap = Label(master=self, text="Allowance")
        self.label_tro_cap.place(x=50, y= 450)

        # Entry: Trợ cấp
        self.entry_tro_cap = Entry(master=self, width=30)
        self.entry_tro_cap.place(x=150, y=450)
        self.entry_tro_cap.config(state="readonly")

        # Label: Thưởng
        self.label_thuong = Label(master=self, text="Performance Bonus")
        self.label_thuong.place(x=50, y=500)

        # Entry: Thưởng
        self.entry_thuong = Entry(master=self, width=30)
        self.entry_thuong.place(x=150, y=500)
        self.entry_thuong.config(state="readonly")

        # Label: Lương hàng tháng
        self.label_luong_ht = Label(master=self, text="Monthly Salary")
        self.label_luong_ht.place(x=50, y=550)

        # Entry: Lương hàng tháng
        self.entry_luong_ht = Entry(master=self, width=18)
        self.entry_luong_ht.place(x=150, y=550)
        self.entry_luong_ht.config(state="readonly")

        # Nút tính lương hàng tháng
        self.btn_tinh_luong_ht = Button(master=self, text="Calculate Salary", compound="left")
        self.btn_tinh_luong_ht.place(x=270, y=550)

        # Label: Ngày tính lương
        self.label_ngay_tinh_luong = Label(master=self, text="Payroll Date")
        self.label_ngay_tinh_luong.place(x=50, y=600)

        # Entry: Ngày tính lương
        self.entry_ngay_tinh_luong = DateEntry(self, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.entry_ngay_tinh_luong.place(x=150, y=600)

        # Nút thêm lương
        self.icon_add_luong = PhotoImage(file="image/add.png")
        self.btn_add_luong = Button(master=self, text="Add", image=self.icon_add_luong, compound="left")
        self.btn_add_luong.place(x=50, y=650)

        # Nút sửa lương
        self.icon_update_luong = PhotoImage(file="image/update.png")
        self.btn_update = Button(self, text="Edit", image=self.icon_update_luong, compound="left")
        self.btn_update.place(x=120, y=650)

        # Nút làm mới trường dữ liệu
        self.icon_refresh_luong = PhotoImage(file="image/refresh.png")
        self.btn_refresh_luong = Button(self, text="Refresh", image=self.icon_refresh_luong, compound="left")
        self.btn_refresh_luong.place(x=180, y=650)

        # Nút tìm kiếm
        self.icon_search_luong = PhotoImage(file="image/search.png")
        self.entry_search_luong = Entry(master=self, width=60)
        self.entry_search_luong.place(x=370, y=90)
        self.btn_search_luong = Button(self, text="Search", image=self.icon_search_luong, compound="left")
        self.btn_search_luong.place(x=745, y=87)

        # Nút in
        self.icon_printer_luong = PhotoImage(file="image/printer.png")
        self.btn_printer_luong = Button(self, text="Print", image=self.icon_printer_luong, compound="left")
        self.btn_printer_luong.place(x=380, y=650)

        # Nút xuất file dạng CSV
        self.icon_csv_luong = PhotoImage(file="image/csv.png")
        self.btn_csv_luong = Button(self, text="Export CSV", image=self.icon_csv_luong, compound="left")
        self.btn_csv_luong.place(x=440, y=650)

        # Nút xuất file dạng Excel
        self.icon_excel_luong = PhotoImage(file="image/excel.png")
        self.btn_excel_luong = Button(self, text="Export Excel", image=self.icon_excel_luong, compound="left")
        self.btn_excel_luong.place(x=540, y=650)

        # Nút làm mới bảng
        self.icon_refresh_treeview_luong = PhotoImage(file="image/refresh.png")
        self.btn_refresh_treeview_luong = Button(self, text="Refresh", image=self.icon_refresh_treeview_luong,
                                               compound="left")
        self.btn_refresh_treeview_luong.place(x=645, y=650)

        # Nút xóa lương
        self.icon_delete_luong = PhotoImage(file="image/delete.png")
        self.btn_delete = Button(self, text="Delete", image=self.icon_delete_luong, compound="left")
        self.btn_delete.place(x=725, y=650)