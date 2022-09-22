from tkinter import StringVar, messagebox
from Models.CategoryDataModel import CategoryDataModel

from Views.SearchData import SearchData
from Views.Validation import regist_data_invalid_modal
from Models.MainDataModel import MainDataModel
from Models.ValidationModel import date_form_validation, is_num_only, validation_search_form_data
from Controllers.EditSearchDataController import EditSearchDataController


class SearchDataController():
    def __init__(self, master) -> None:
        self.date_from = StringVar()
        self.date_to = StringVar()
        self.item = StringVar()
        self.price = StringVar()
        self.category = StringVar()

        self.data = []

        self.main_data_model = MainDataModel()
        self.category_data_model = CategoryDataModel()

        self.categories = self.category_data_model.get()
        self.view = SearchData(master)

        date_only_cmd = self.view.form_frame.register(
            date_form_validation)
        num_only_cmd = self.view.form_frame.register(
            is_num_only)

        self.view.date_from_entry.config(
            textvariable=self.date_from, validate='all',
            validatecommand=(date_only_cmd, '%S', '%P', '%V'))
        self.view.date_to_entry.config(
            textvariable=self.date_to, validate='all',
            validatecommand=(date_only_cmd, '%S', '%P', '%V'))
        self.view.set_default_date()
        # self.view.item_entry.config(textvariable=self.item)
        # self.view.category_combobox.config(values=[e[1] for e in self.categories], textvariable=self.category)
        # self.view.price_entry.config(
        #     textvariable=self.price,
        #     validate='key',
        #     validatecommand=(num_only_cmd, '%S'))
        # self.view.form_clear_button.config(command=self.clear_form_data)
        self.view.data_treeview.bind(
            '<<TreeviewSelect>>',
            lambda event: self.display_edit_record_window(event=event))
        self.view.send_data_button.config(command=self.get_data_from_database)

    def add_form_info_to_table(self):
        for ele in self.data:
            self.view.data_treeview.insert(
                parent='', index='end',
                values=(ele[0], ele[1], ele[2], ele[3]))

    # def clear_form_data(self):
    #     self.view.item_entry.delete(0, 'end')
    #     self.view.price_entry.delete(0, 'end')
    #     self.view.category_combobox.delete(0, 'end')

    def get_data_from_database(self):
        # date_from,date_to ,item, price, category = self.date_from.get(),self.date_to.get(), self.item.get(), self.price.get(), self.category.get()
        # form_data = [date_from,date_to ,item, category, price]
        date_from,date_to = self.date_from.get(),self.date_to.get()
        form_data = (date_from,date_to)

        isok = validation_search_form_data(date_from=date_from,date_to=date_to)
        if isok:
            # for ele in self.categories:
            #     category_id = ele[0]
            #     category_name = ele[1]
            #     if category_name == category:
            #         form_data[2] = category_id
            #         break
        
            data = self.main_data_model.search_data(where=form_data)
            print(data)

            messagebox.showinfo('データ検索成功', 'データ検索したよ')

            # if self.data:
            #     self.view.data_treeview.detach(
            #         *self.view.data_treeview.get_children())
            #     self.data = data
            #     self.add_form_info_to_table()
            # else:
            #     self.data = data
            #     self.add_form_info_to_table()

            # print(self.data)
        else:
            regist_data_invalid_modal()

    def display_edit_record_window(self, event):
        EditSearchDataController(self.view.data_treeview)
