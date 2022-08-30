from tkinter import ttk


class Root():
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('家計簿アプリ')
        self.root.geometry('700x700')
        self.root.resizable(width=False, height=False)
        self.notebook = ttk.Notebook(self.root, width=650, height=650)

    def create_widgets(self, regist_data_view):
        tab_search = ttk.Frame(self.notebook)

        self.notebook.add(regist_data_view, text='家計簿登録')
        self.notebook.add(tab_search, text='家計簿検索')

        self.notebook.pack(padx=10, pady=10)
