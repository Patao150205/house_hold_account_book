from email import message
from tkinter import StringVar, messagebox
from Views.EditRegistData import EditRegistData


class EditRegistDataController():
    def __init__(self, record):
        self.record = record
        self.record_id = self.record.focus()
        self.record_values = self.record.item(self.record_id)[
            'values']

        self.date = StringVar()
        self.item = StringVar()
        self.price = StringVar()

        self.view = EditRegistData(
            self.record_values,
            self.date, self.item, self.price,
        )

        self.view.send_data_button.config(command=self.send_data_to_treeview)
        self.view.delete_data_button.config(
            command=self.delete_data_from_treeview)

    def send_data_to_treeview(self):
        date, item, price = self.date.get(), self.item.get(), self.price.get()
        temp = self.record.item(self.record_id, "values")
        print(temp)
        print(date, item, price)
        data = (date, item, price)
        self.record.item(self.record_id, values=data)
        messagebox.showinfo('家計簿編集成功', '家計簿を編集しました。')
        self.view.destroy()

    def delete_data_from_treeview(self):
        isOk = messagebox.askyesno('レコード削除の確認', 'レコードを本当に削除しますか？')

        if isOk:
            self.record.detach(self.record_id)
            self.view.destroy()
