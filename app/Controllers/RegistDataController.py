from tkinter import StringVar, messagebox
from unicodedata import category

from Views.RegistData import RegistData
from Views.Validation import regist_data_invalid_modal
from Models.MainDataModel import MainDataModel
from Models.CategoryDataModel import CategoryDataModel
from Models.ValidationModel import date_form_validation, is_num_only, validation_regist_form_data
from Controllers.EditRegistDataController import EditRegistDataController


class RegistDataController():
    def __init__(self, master) -> None:
        self.date = StringVar()
        self.item = StringVar()
        self.price = StringVar()
        self.category = StringVar()

        self.main_data_model = MainDataModel()
        self.category_data_model = CategoryDataModel()

        self.categories = self.category_data_model.get()
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
        
        category_names = [e[1] for e in self.categories]
        category_names.insert(0, '')

        self.view.category_combobox.config(values=category_names, textvariable=self.category)

        self.view.form_input_button.config(command=self.add_form_info_to_table)
        self.view.form_clear_button.config(command=self.clear_form_data)
        self.view.data_treeview.bind(
            '<<TreeviewSelect>>',
            lambda event: self.display_edit_record_window(event=event))
        self.view.send_data_button.config(command=self.send_data_to_database)

    def add_form_info_to_table(self):
        date, item,category, price = self.date.get(), self.item.get(),self.category.get(), self.price.get()

        isok = validation_regist_form_data(date, item, price, category)

        if isok:
            self.view.data_treeview.insert(
                parent='', index='end',
                values=(date, item, category,price))
        else:
            regist_data_invalid_modal()

    def clear_form_data(self):
        self.view.item_entry.delete(0, 'end')
        self.view.price_entry.delete(0, 'end')
        self.view.category_combobox.delete(0, 'end')

    def send_data_to_database(self):
        data = []
        record_ids = self.view.data_treeview.get_children()
        for id in record_ids:
            record_values = self.view.data_treeview.item(id, 'values')

            date, item,category, price = (record_values[0],
                           record_values[1],
                           record_values[2],
                           record_values[3]
                           )

            for ele in self.categories:
                category_id = ele[0]
                category_name = ele[1]
                if category_name == category:
                    category = category_id
                    break
            
            record_data = (date,item, category, price)

            data.append(record_data)

        print(data)

        self.main_data_model.create(data)

        messagebox.showinfo('?????????????????????', '????????????????????????')

        self.view.data_treeview.detach(*self.view.data_treeview.get_children())

    def display_edit_record_window(self, event):
        EditRegistDataController(self.view.data_treeview)

