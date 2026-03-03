from Store_Management.controller.dashboard_controller import DashboardController
from Store_Management.model.model import Model
from Store_Management.view.view import View


def main() :
        view = View()
        model = Model()

        # Kết nối cơ sở dữ liệu
        #model.connect_db()

        controller = DashboardController(model, view)

        # Chạy ứng dụng
        view.title("Beauty Store ERP")
        view.resizable(False, False)
        view.mainloop()


if __name__ == '__main__':
    main()
