from tkinter import Scrollbar, VERTICAL, CENTER, LEFT, RIDGE
from tkinter import ttk
import datetime


class RegistData(ttk.Frame):
    def __init__(self, notebook) -> None:
        super().__init__(master=notebook, padding=(0, 20))
        self.pack()

        self.form_frame = ttk.Frame(self, padding=10)
        self.form_frame.pack()
        self.form_button_frame = ttk.Frame(self, padding=(0, 0, 0, 40))
        self.form_button_frame.pack()
        self.data_display_frame = ttk.Frame(self, borderwidth=2, relief=RIDGE)
        self.data_display_frame.pack()
        self.send_data_button_frame = ttk.Frame(self, padding=(20, 20))
        self.send_data_button_frame.pack()

        self.create_widgets_for_form_frame()
        self.create_widgets_for_form_button_frame()
        self.create_widgets_for_display_frame()
        self.create_widgets_for_send_data_button_frame()

    def create_widgets_for_form_frame(self):
        description_label = ttk.Label(
            self.form_frame, text='登録するデータを入力してください。')
        description_label.grid(row=0, column=0, columnspan=2)

        date_label = ttk.Label(self.form_frame, text='年月日')
        date_label.grid(row=1, column=0)

        item_label = ttk.Label(self.form_frame, text='科目')
        item_label.grid(row=2, column=0)

        price_label = ttk.Label(self.form_frame, text='金額')
        price_label.grid(row=3, column=0)

        today = datetime.date.today()
        formated_date = today.strftime('%Y/%m/%d')

        self.date_entry = ttk.Entry(
            self.form_frame, justify=CENTER, validate='all')
        self.date_entry.insert(0, formated_date)
        self.date_entry.grid(row=1, column=1, pady=3)
        self.item_entry = ttk.Entry(
            self.form_frame, justify=CENTER)
        self.item_entry.grid(row=2, column=1, pady=3)
        self.price_entry = ttk.Entry(
            self.form_frame, justify=CENTER, validate='key')
        self.price_entry.grid(row=3, column=1, pady=3)

    def create_widgets_for_form_button_frame(self):
        self.form_clear_button = ttk.Button(
            self.form_button_frame, text='クリア')
        self.form_input_button = ttk.Button(self.form_button_frame, text='追加')

        self.form_clear_button.pack(side=LEFT, padx=5)
        self.form_input_button.pack(side=LEFT, padx=5)

    def create_widgets_for_display_frame(self):
        columns = ('date', 'item', 'price')

        table_frame = ttk.Frame(self.data_display_frame)
        table_frame.pack()

        self.data_treeview = ttk.Treeview(
            table_frame, columns=columns, height=15)

        # レコード選択
        self.data_treeview.column('#0', width=0, stretch=False)
        self.data_treeview.column('date', width=80)
        self.data_treeview.column('item', width=200)
        self.data_treeview.column('price', width=80)

        self.data_treeview.heading('#0', text='')
        self.data_treeview.heading('date', text='年月日')
        self.data_treeview.heading('item', text='科目')
        self.data_treeview.heading('price', text='金額')

        self.data_treeview.grid(column=0, row=0)

        data_scrollbar = Scrollbar(
            table_frame, orient=VERTICAL, width=16,
            command=self.data_treeview.yview)
        self.data_treeview['yscrollcommand'] = data_scrollbar.set
        data_scrollbar.grid(column=1, row=0, sticky='news')

    def create_widgets_for_send_data_button_frame(self):
        send_data_button = ttk.Button(self, text='データを送信')
        send_data_button.pack()

        # 送信ボタン
        # def send_data_to_database():
        # 		messagebox.showinfo('家計簿登録成功', '家計簿に登録しました。')
