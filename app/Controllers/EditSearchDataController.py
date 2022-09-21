from tkinter import StringVar, messagebox
from Models.MainDataModel import MainDataModel
from Views.EditSearchData import EditSearchData


class EditSearchDataController():
    def __init__(self, record):
        self.record = record
        self.record_treeview_id = self.record.focus()
        self.record_values = self.record.item(self.record_treeview_id)[
            'values']

        self.id = self.record_values[0]
        self.date = StringVar()
        self.item = StringVar()
        self.price = StringVar()

        self.model = MainDataModel()

        self.view = EditSearchData(
            self.record_values
        )

        self.view.date_entry.config(textvariable=self.date)
        self.view.item_entry.config(textvariable=self.item)
        self.view.price_entry.config(textvariable=self.price)
        # self.view..config(textvariable=self.price)

        self.view.send_data_button.config(
            command=self.send_data_to_treeview_and_database)
        self.view.delete_data_button.config(
            command=self.delete_data_from_treeview_and_database)

    def send_data_to_treeview_and_database(self):
        id, date, item, price = (self.id,
                                 self.date.get(),
                                 self.item.get(),
                                 self.price.get())

        self.record.item(self.record_treeview_id,
                         values=(id, date, item, price))
        self.model.edit((date, item, price, id))

        messagebox.showinfo('家計簿編集成功', '家計簿を編集しました。')
        self.view.destroy()

    def delete_data_from_treeview_and_database(self):
        isOk = messagebox.askyesno('レコード削除の確認', 'レコードを本当に削除しますか？')
        if isOk:
            self.model.delete(self.id)
            self.record.detach(self.record_treeview_id)
            messagebox.showinfo('家計簿削除成功', '家計簿を削除しました。')
            self.view.destroy()
