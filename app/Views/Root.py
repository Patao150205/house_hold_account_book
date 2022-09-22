from tkinter import ttk
from tkinter.tix import Tk


class Root():
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('家計簿アプリ')
        self.root.minsize(width=1000, height=800)
        # self.root.resizable(width=False, height=False)
        self.notebook = ttk.Notebook(self.root, width=950, height=750)

    def create_widgets(self, regist_data_view, search_data_view):
        self.help_frame = ttk.Frame()
        self.dashboard_frame = ttk.Frame()
        self.settings_others_frame = ttk.Frame()
        self.notebook.add(regist_data_view, text='家計簿登録')
        self.notebook.add(search_data_view, text='家計簿検索')
        self.notebook.add(self.dashboard_frame, text='ダッシュボード')
        self.notebook.add(self.settings_others_frame, text='設定・その他')
        self.notebook.add(self.help_frame, text='　ヘルプ　')
        # self.notebook.select(self.dashboard_frame)

        self.notebook.pack(padx=10, pady=10)
