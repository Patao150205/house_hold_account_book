from tkinter import Scrollbar, VERTICAL, CENTER, LEFT, RIDGE
from tkinter import ttk

from lib.date import get_current_yyyy_mm_dd


class SearchData(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master=master, padding=(0, 20))
        self.pack()

        # master is Notebook
        self.master = master
        self.form_frame = ttk.Frame(self, padding=10)
        self.form_frame.pack()
        self.form_button_frame = ttk.Frame(self, padding=(0, 0, 0, 40))
        self.form_button_frame.pack()
        self.data_display_frame = ttk.Frame(self, borderwidth=2, relief=RIDGE)
        self.data_display_frame.pack()
        self.send_data_button_frame = ttk.Frame(self)
        self.send_data_button_frame.pack()

        self.create_widgets_for_form_frame()
        # self.create_widgets_for_form_button_frame()
        self.create_widgets_for_display_frame()
        self.create_widgets_for_send_data_button_frame()

    def create_widgets_for_form_frame(self):
        description_label = ttk.Label(
            self.form_frame, text='検索するデータを入力してください。')
        description_label.grid(row=0, column=0, columnspan=2)

        date_from_label = ttk.Label(self.form_frame, text='年月日(from)')
        date_from_label.grid(row=1, column=0)
        date_to_label = ttk.Label(self.form_frame, text='年月日(to)')
        date_to_label.grid(row=2, column=0)
        # item_label = ttk.Label(self.form_frame, text='科目')
        # item_label.grid(row=3, column=0)

        # price_label = ttk.Label(self.form_frame, text='金額')
        # price_label.grid(row=4, column=0)

        # category_label = ttk.Label(self.form_frame, text='内訳')
        # category_label.grid(row=5, column=0)

        self.date_from_entry = ttk.Entry(
            self.form_frame, justify=CENTER, validate='all')
        self.date_from_entry.grid(row=1, column=1, pady=3)
        self.date_to_entry = ttk.Entry(
            self.form_frame, justify=CENTER, validate='all')
        self.date_to_entry.grid(row=2, column=1, pady=3)
        # self.item_entry = ttk.Entry(
        #     self.form_frame, justify=CENTER)
        # self.item_entry.grid(row=3, column=1, pady=3)
        # self.price_entry = ttk.Entry(
        #     self.form_frame, justify=CENTER, validate='key')
        # self.price_entry.grid(row=4, column=1, pady=3)
        # self.category_combobox = ttk.Combobox(self.form_frame,justify=CENTER, height=15,  state='readonly')
        # self.category_combobox.grid(row=5, column=1, pady=3)

    # def create_widgets_for_form_button_frame(self):
    #     self.form_clear_button = ttk.Button(
    #         self.form_button_frame, text='クリア')

    #     self.form_clear_button.pack()

    def create_widgets_for_display_frame(self):
        columns = ('id', 'date', 'item','category', 'price')

        table_frame = ttk.Frame(self.data_display_frame)
        table_frame.pack()

        self.data_treeview = ttk.Treeview(
            table_frame, columns=columns, height=25)

        # レコード選択
        self.data_treeview.column('#0', width=0, stretch=False)
        self.data_treeview.column('id', width=0, stretch=False)
        self.data_treeview.column('date', width=80)
        self.data_treeview.column('item', width=250)
        self.data_treeview.column('category', width=80)
        self.data_treeview.column('price', width=80)

        self.data_treeview.heading('#0', text='')
        self.data_treeview.heading('id', text='ID')
        self.data_treeview.heading('date', text='年月日')
        self.data_treeview.heading('item', text='科目')
        self.data_treeview.heading('category', text='内訳')
        self.data_treeview.heading('price', text='金額')

        self.data_treeview.grid(column=0, row=0)

        data_scrollbar = Scrollbar(
            table_frame, orient=VERTICAL, width=16,
            command=self.data_treeview.yview)
        self.data_treeview['yscrollcommand'] = data_scrollbar.set
        data_scrollbar.grid(column=1, row=0, sticky='news')

    def create_widgets_for_send_data_button_frame(self):
        self.send_data_button = ttk.Button(self, text='データを検索', width=20)
        self.send_data_button.pack(pady=20)
        s = ttk.Style()
        # s.theme_use('classic')
        s.configure('MyWidget.TButton', foreground='red', background='blue')
        self.dashboard_button = ttk.Button(self, text='ダッシュボード起動', style='MyWidget.TButton', width=20)
        self.dashboard_button.pack(pady=0)

    def set_default_date(self):
        today = get_current_yyyy_mm_dd()
        print(today)
        self.date_from_entry.insert(0, today)
        self.date_to_entry.insert(0, today)
