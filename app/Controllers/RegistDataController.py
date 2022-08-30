from tkinter import StringVar
from tkinter import messagebox

from Views.RegistData import RegistData
from Models.RegistDataModel import RegistDataModel


class RegistDataController():
    def __init__(self, master) -> None:
        self.date = StringVar()
        self.item = StringVar()
        self.price = StringVar()

        self.view = RegistData(master)
        self.view.date_entry.config(textvariable=self.date)
        self.view.item_entry.config(textvariable=self.item)
        self.view.price_entry.config(textvariable=self.price)
        self.view.form_input_button.config(command=self.add_form_info_to_table)
        self.view.form_clear_button.config(command=self.clear_form_data)

        self.model = RegistDataModel()

    def add_form_info_to_table(self):
        isok = self.model.validation_form_data(
            self.date.get(), self.item.get(), self.price.get())

        if isok:
            pass
        else:
            messagebox.showwarning(
                '形式エラー', 'フォームに正しい入力をしてください。\n\n '
                '年月日:  yyyy/mm/dd \n '
                '科目:     1文字以上 \n'
                '金額:       数字のみ')

    def clear_form_data(self):
        self.view.item_entry.delete(0, 'end')
        self.view.price_entry.delete(0, 'end')

    def send_data_to_database(self):
        messagebox.showinfo('家計簿登録成功', '家計簿に登録しました。')
