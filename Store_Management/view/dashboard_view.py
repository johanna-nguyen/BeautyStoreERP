from tkinter import Label, PhotoImage, Button, Frame


class DashboardView(Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def dashboard_widget(self):
        """Hiển thị dashboard ứng dụng"""
        # Kích thước GUI dashboard
        self.master.geometry('520x520')

        # Tạo giao diện Dashboard
        Label(self, text="Dashboard", font=('Arial', 25)).pack(pady=20)

        # Thêm các nút chức năng vào Dashboard
        # Nút quản lý nhà cung cấp
        self.icon_ql_ncc = PhotoImage(file="image/supplier.png")
        self.btn_ql_ncc = Button(self, text="Suppliers", image=self.icon_ql_ncc, compound="left", width=150, height=50)
        self.btn_ql_ncc.place(x=10, y=100)

        # Nút quản lý sản phẩm
        self.icon_ql_sp = PhotoImage(file="image/products.png")
        self.btn_ql_sp = Button(self, text="Products", image=self.icon_ql_sp, compound="left", width=150, height=50)
        self.btn_ql_sp.place(x=180, y=100)

        # Nút quản lý nhân viên
        self.icon_ql_nv = PhotoImage(file="image/employee.png")
        self.btn_ql_nv = Button(self, text="Employees", image=self.icon_ql_nv, compound="left", width=150, height=50)
        self.btn_ql_nv.place(x=350, y=100)

        # Nút quản lý khách hàng
        self.icon_ql_kh = PhotoImage(file="image/clients.png")
        self.btn_ql_kh = Button(self, text="Customers", image=self.icon_ql_kh, compound="left", width=150, height=50)
        self.btn_ql_kh.place(x=10, y=170)

        # Nút quản lý phiếu nhập
        self.icon_ql_pn = PhotoImage(file="image/import.png")
        self.btn_ql_pn = Button(self, text="Purchase Orders", image=self.icon_ql_pn, compound="left", width=150,
                                height=50)
        self.btn_ql_pn.place(x=180, y=170)

        # Nút quản lý phiếu xuất
        self.icon_ql_px = PhotoImage(file="image/export.png")
        self.btn_ql_px = Button(self, text="Sales Orders", image=self.icon_ql_px, compound="left", width=150, height=50)
        self.btn_ql_px.place(x=350, y=170)

        # Nút quản lý lương
        self.icon_ql_luong = PhotoImage(file="image/salary.png")
        self.btn_ql_luong = Button(self, text="Payroll", image=self.icon_ql_luong, compound="left", width=150,
                                   height=50)
        self.btn_ql_luong.place(x=10, y=250)

        # Nút quản lý tồn kho
        self.icon_ql_kho = PhotoImage(file="image/packages.png")
        self.btn_ql_kho = Button(self, text="Inventory", image=self.icon_ql_kho, compound="left", width=150, height=50)
        self.btn_ql_kho.place(x=180, y=250)

        # Nút thống kê
        self.icon_thong_ke = PhotoImage(file="image/diagram.png")
        self.btn_thong_ke = Button(self, text="Reports", image=self.icon_thong_ke, compound="left", width=150,
                                   height=50)
        self.btn_thong_ke.place(x=350, y=250)

        # Nút đăng xuất
        self.icon_logout = PhotoImage(file="image/logout.png")
        self.btn_logout = Button(self, text="Logout", image=self.icon_logout, compound="left", width=150, height=50)
        self.btn_logout.place(x=180, y=320)