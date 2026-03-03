from tkinter import Label, Entry, PhotoImage, Button, Frame




class LoginView (Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_widget()

    def init_widget(self):
        """Hiển thị giao diện đăng nhập"""
        # Kích thước GUI đăng nhập
        self.master.geometry('460x300')

        # Tạo nhãn tiêu đề
        self.label_login = Label(master=self, text="Login", font=('Arial', 25))
        self.label_login.place(x=170, y=20)

        # Tên đăng nhập
        self.label_user = Label(master=self, text="Username")
        self.label_user.place(x=50, y=100)
        self.entry_user = Entry(master=self, width=30)
        self.entry_user.place(x=150, y=100)

        # Mật khẩu
        self.label_pw = Label(master=self, text="Password")
        self.label_pw.place(x=50, y=150)
        self.entry_pw = Entry(master=self, width=30, show="*")
        self.entry_pw.place(x=150, y=150)

        # Nút đăng nhập

        self.icon_login = PhotoImage(file="image/login.png")
        self.btn_login = Button(self, text="Login", image=self.icon_login, compound="left")
        self.btn_login.place(x=50, y=200)