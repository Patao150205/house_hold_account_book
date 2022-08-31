# from Models import
from Views.Root import Root
from Controllers.RegistDataController import RegistDataController


class RootController():
    def __init__(self, root):
        self.view = Root(root)
        self.regist_data_controller = RegistDataController(
            master=self.view.notebook)

        self.view.create_widgets(self.regist_data_controller.view)
