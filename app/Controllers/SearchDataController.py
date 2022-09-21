from tkinter import StringVar, messagebox

from Views.SearchData import SearchData
from Views.Validation import regist_data_invalid_modal
from Models.MainDataModel import MainDataModel
from Models.ValidationModel import date_form_validation, is_num_only, validation_form_data
from Controllers.EditSearchDataController import EditSearchDataController


class SearchDataController():
    def __init__(self, master) -> None:
        self.date = StringVar()
        self.item = StringVar()
        self.price = StringVar()

        self.data = []

        self.model = MainDataModel()
        self.view = SearchData(master)

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
        self.view.form_clear_button.config(command=self.clear_form_data)
        self.view.data_treeview.bind(
            '<<TreeviewSelect>>',
            lambda event: self.display_edit_record_window(event=event))
        self.view.send_data_button.config(command=self.get_data_from_database)

    def add_form_info_to_table(self):
        for ele in self.data:
            self.view.data_treeview.insert(
                parent='', index='end',
                values=(ele[0], ele[1], ele[2], ele[3]))

    def clear_form_data(self):
        self.view.item_entry.delete(0, 'end')
        self.view.price_entry.delete(0, 'end')

    def get_data_from_form(self) -> tuple:
        date, item, price = self.date.get(), self.item.get(), self.price.get()
        form_data = (date, item, price)

        return form_data

    def get_data_from_database(self):
        form_data = self.get_data_from_form()

        isok = validation_form_data(*form_data)

        if isok:
            data = self.model.search_data()

            messagebox.showinfo('データ検索成功', 'データ検索したよ')

            if self.data:
                self.view.data_treeview.detach(
                    *self.view.data_treeview.get_children())
                self.data = data
                self.add_form_info_to_table()
            else:
                self.data = data
                self.add_form_info_to_table()

            print(self.data)
        else:
            regist_data_invalid_modal()

    def display_edit_record_window(self, event):
        EditSearchDataController(self.view.data_treeview)
