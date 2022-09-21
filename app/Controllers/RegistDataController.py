from tkinter import StringVar, messagebox

from Views.RegistData import RegistData
from Views.Validation import regist_data_invalid_modal
from Models.RegistDataModel import RegistDataModel
from Models.ValidationModel import date_form_validation, is_num_only, validation_form_data
from Controllers.EditRegistDataController import EditRegistDataController


class RegistDataController():
    def __init__(self, master) -> None:
        self.date = StringVar()
        self.item = StringVar()
        self.price = StringVar()

        self.model = RegistDataModel()
        self.view = RegistData(master)

        date_only_cmd = self.view.form_frame.register(
            date_form_validation)
        num_only_cmd = self.view.form_frame.register(
            is_num_only)

        self.view.date_entry.config(
            textvariable=self.date, validate='all',
            validatecommand=(date_only_cmd, '%S', '%P', '%V'))
        self.view.set_default_date()
        self.view.item_entry.config(textvariable=self.item)
        self.view.price_entry.config(
            textvariable=self.price,
            validate='key',
            validatecommand=(num_only_cmd, '%S'))
        self.view.form_input_button.config(command=self.add_form_info_to_table)
        self.view.form_clear_button.config(command=self.clear_form_data)
        self.view.data_treeview.bind(
            '<<TreeviewSelect>>',
            lambda event: self.display_edit_record_window(event=event))
        self.view.send_data_button.config(command=self.send_data_to_database)

    def add_form_info_to_table(self):
        date, item, price = self.date.get(), self.item.get(), self.price.get()

        isok = validation_form_data(date, item, price)

        if isok:
            self.view.data_treeview.insert(
                parent='', index='end',
                values=(date, item, price))
        else:
            regist_data_invalid_modal()

    def clear_form_data(self):
        self.view.item_entry.delete(0, 'end')
        self.view.price_entry.delete(0, 'end')

    def send_data_to_database(self):
        data = []
        record_ids = self.view.data_treeview.get_children()
        for id in record_ids:
            record_values = self.view.data_treeview.item(id, 'values')
            record_data = (record_values[0],
                           record_values[1],
                           record_values[2])

            data.append(record_data)

        self.model.create(data)

        messagebox.showinfo('データ登録成功', 'データ登録したよ')

        self.view.data_treeview.detach(*self.view.data_treeview.get_children())

    def display_edit_record_window(self, event):
        EditRegistDataController(self.view.data_treeview)
