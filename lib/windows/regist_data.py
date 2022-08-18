  
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import datetime

from lib import validation  
from lib.windows.edit_record_form import set_record_bind

def display_regist_data_window(parent):		
    regist_data_window = ttk.Frame(parent, padding=(0,20))
    regist_data_window.pack()

	# フォーム フレーム
    def input_form_info_to_table(date, item, price):
        isOK =  validation.validation_regist_form(date=date,item=item, price=price)

        if isOK:
            data_treeview.insert(parent='', index='end',
                                values=(date, item, price))
        else:
            messagebox.showwarning('形式エラー', 'フォームに正しい入力をしてください。\n\n 年月日:  yyyy/mm/dd \n 科目:     1文字以上 \n金額:       数字のみ')   

    
    def clear_entry_info(*entries):
        for entry in entries:
           entry.delete(0, 'end') 


    form_frame = ttk.Frame(regist_data_window, padding=10)
    form_frame.pack()

    date_label = ttk.Label(form_frame, text='登録するデータを入力してください。')
    date_label.grid(row=0, column=0, columnspan=2)

    date_label = ttk.Label(form_frame, text='年月日')
    date_label.grid(row=1, column=0)

    item_label = ttk.Label(form_frame, text='科目')
    item_label.grid(row=2, column=0)

    price_label = ttk.Label(form_frame, text='金額')
    price_label.grid(row=3, column=0)

    date = StringVar()
    item = StringVar()
    price = StringVar()

    today = datetime.date.today()
    formated_date = today.strftime('%Y/%m/%d')

    date_only_cmd = form_frame.register(validation.date_form)
    num_only_cmd = form_frame.register(validation.is_num_only)

    date_entry = ttk.Entry(form_frame, textvariable=date, justify=CENTER, validate='all', validatecommand=(date_only_cmd, '%S','%P', '%V'))
    date_entry.insert(0, formated_date)
    date_entry.grid(row=1, column=1, pady=3)
    item_entry = ttk.Entry(form_frame, textvariable=item, justify=CENTER )
    item_entry.grid(row=2, column=1, pady=3)
    price_entry = ttk.Entry(form_frame, textvariable=price, justify=CENTER, validate='key', validatecommand=(num_only_cmd, '%S'))
    price_entry.grid(row=3, column=1, pady=3)

    form_button_frame = ttk.Frame(regist_data_window, padding=[0, 0, 0, 40])
    form_button_frame.pack()

    form_clear_button = ttk.Button(form_button_frame, text='クリア', command=lambda: clear_entry_info(item_entry, price_entry))
    form_input_button = ttk.Button(form_button_frame, text='追加',
                                   command=lambda: input_form_info_to_table(
                                       date.get(), item.get(), price.get()))

    form_clear_button.pack(side=LEFT, padx=5)
    form_input_button.pack(side=LEFT, padx=5)

    # データ表示フレーム
    display_data_frame = ttk.Frame(regist_data_window, borderwidth=2, relief=RIDGE)
    display_data_frame.pack()


    columns = ('date', 'item', 'price')

    table_frame = ttk.Frame(display_data_frame)
    table_frame.pack()


    data_treeview = ttk.Treeview(
        table_frame, columns=columns, height=15)


    data_scrollbar = Scrollbar(table_frame, orient=VERTICAL,width=16, command=data_treeview.yview)
    data_treeview['yscrollcommand'] = data_scrollbar.set

    # レコード選択
    set_record_bind(data_treeview)

    data_treeview.column('#0', width=0, stretch=False)
    data_treeview.column('date', width=80)
    data_treeview.column('item', width=200)
    data_treeview.column('price', width=80)

    data_treeview.heading('#0', text='')
    data_treeview.heading('date', text='年月日')
    data_treeview.heading('item', text='科目')
    data_treeview.heading('price', text='金額')

    data_treeview.grid(column=0, row=0)
    data_scrollbar.grid(column=1, row=0, sticky='news')

    # 送信ボタン
    def send_data_to_database():
        messagebox.showinfo('家計簿登録成功', '家計簿に登録しました。')

    send_data_button = ttk.Button(regist_data_window ,text='データを送信', padding=(20, 20), command=send_data_to_database)
    send_data_button.pack()

    return regist_data_window