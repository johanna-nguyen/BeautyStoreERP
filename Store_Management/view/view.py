from tkinter import Tk

from Store_Management.view.login_view import LoginView


class View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.resizable(width=False, height=False)
        self.login_view = LoginView(self)
        self.login_view.pack(fill="both", expand=True)



