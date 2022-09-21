from tkinter import NSEW, RIDGE, ttk, Toplevel, CENTER
from Models.ValidationModel import is_num_only, date_form_validation


class EditSearchData(Toplevel):
    def __init__(self, record_values) -> None:
        super().__init__(pady=30)
        self.geometry('600x600')
        self.resizable(width=False, height=False)
        self.title('検索レコードの編集')
        self.grab_set()
        self.focus_set()

        self.record_values = record_values

        self.current_record_frame = ttk.Frame(
            self, padding=10, relief=RIDGE, width=550)
        self.current_record_frame.pack(padx=10, pady=20)

        self.form_frame = ttk.Frame(self, padding=10, relief=RIDGE, width=550)
        self.form_frame.pack()
        self.send_data_button = ttk.Button(self, text='データを更新', width=20)
        self.send_data_button.pack(pady=20)
        self.delete_data_button = ttk.Button(self, text='データを削除', width=20)
        self.delete_data_button.pack()

        self.create_widgets_for_current_record_frame()
        self.create_widgets_for_form_frame()

    def create_widgets_for_current_record_frame(self):
        current_date_label = ttk.Label(
            self.current_record_frame, text='現在のレコード')
        current_date_label.grid(
            row=0, column=0, columnspan=2, sticky=NSEW, padx=100, pady=10)

        current_date_label = ttk.Label(self.current_record_frame, text='年月日')
        current_date_label.grid(row=1, column=0)

        current_item_label = ttk.Label(self.current_record_frame, text='科目')
        current_item_label.grid(row=2, column=0)

        current_price_label = ttk.Label(self.current_record_frame, text='金額')
        current_price_label.grid(row=3, column=0)

        date_label = ttk.Label(self.current_record_frame,
                               text=self.record_values[1], padding=(0, 3))
        item_lable = ttk.Label(self.current_record_frame,
                               text=self.record_values[2], padding=(0, 3))
        price_label = ttk.Label(self.current_record_frame,
                                text=self.record_values[3], padding=(0, 3))

        date_label.grid(row=1, column=1, padx=15)
        item_lable.grid(row=2, column=1)
        price_label.grid(row=3, column=1)

    def create_widgets_for_form_frame(self):
        # 編集フォーム
        form_date_label = ttk.Label(self.form_frame, text='登録するデータを入力してください。')
        form_date_label.grid(row=0, column=0, columnspan=2, padx=50)

        form_date_label = ttk.Label(self.form_frame, text='年月日')
        form_date_label.grid(row=1, column=0)

        form_item_label = ttk.Label(self.form_frame, text='科目')
        form_item_label.grid(row=2, column=0)

        price_label = ttk.Label(self.form_frame, text='金額')
        price_label.grid(row=3, column=0)

        date_only_cmd = self.form_frame.register(date_form_validation)
        num_only_cmd = self.form_frame.register(is_num_only)

        self.date_entry = ttk.Entry(
            self.form_frame,justify=CENTER,
            validate='all', validatecommand=(date_only_cmd, '%S', '%P', '%V'))
        self.date_entry.insert(0, self.record_values[1])
        self.date_entry.grid(row=1, column=1, pady=3)
        self.item_entry = ttk.Entry(
            self.form_frame,  justify=CENTER)
        self.item_entry.insert(0, self.record_values[2])
        self.item_entry.grid(row=2, column=1, pady=3)
        self.price_entry = ttk.Entry(
            self.form_frame,justify=CENTER,
            validate='key', validatecommand=(num_only_cmd, '%S'))
        self.price_entry.insert(0, self.record_values[3])
        self.price_entry.grid(row=3, column=1, pady=3)
