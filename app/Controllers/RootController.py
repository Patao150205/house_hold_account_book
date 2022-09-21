# from Models import
from Views.Root import Root
from Controllers.RegistDataController import RegistDataController
from Controllers.SearchDataController import SearchDataController


class RootController():
    def __init__(self, root):
        self.view = Root(root)
        self.regist_data_controller = RegistDataController(
            master=self.view.notebook)
        self.search_data_controller = SearchDataController(
            master=self.view.notebook)

        self.view.create_widgets(
            self.regist_data_controller.view, self.search_data_controller.view)
