from tkinter import *
from tkinter import ttk

root = Tk()
root.title('家計簿アプリ')

root.geometry('700x700')
root.resizable(width=False, height=False)

# フォーム フレーム


def input_


form_frame = ttk.Frame(root, padding=10)
form_frame.pack()

date_label = ttk.Label(form_frame, text='年月日')
date_label.grid(row=0, column=0)

item_label = ttk.Label(form_frame, text='科目')
item_label.grid(row=1, column=0)

price_label = ttk.Label(form_frame, text='金額')
price_label.grid(row=2, column=0)

date = StringVar()
item = StringVar()
price = StringVar()

date_entry = ttk.Entry(form_frame, textvariable=date,
                       background='white')
date_entry.grid(row=0, column=1, pady=3)
item_entry = ttk.Entry(form_frame, textvariable=item)
item_entry.grid(row=1, column=1, pady=3)
price_entry = ttk.Entry(form_frame, textvariable=price)
price_entry.grid(row=2, column=1, pady=3)

form_button_frame = ttk.Frame(root, padding=[0, 0, 0, 40])
form_button_frame.pack()

form_clear_button = ttk.Button(form_button_frame, text='クリア')
form_input_button = ttk.Button(form_button_frame, text='追加', command=lambda: print(
    date.get(), item.get(), price.get()))

form_clear_button.pack(side=LEFT, padx=5)
form_input_button.pack(side=LEFT, padx=5)

# データ表示フレーム
display_data_frame = ttk.Frame(root, borderwidth=2, relief=RIDGE)
display_data_frame.pack()

columns = ('date', 'item', 'price')

data_treeview = ttk.Treeview(display_data_frame, columns=columns, height=10)

data_treeview.column('#0', width=0, stretch=False)
data_treeview.column('date', width=80)
data_treeview.column('item', width=200)
data_treeview.column('price', width=80)

data_treeview.heading('#0', text='')
data_treeview.heading('date', text='年月日')
data_treeview.heading('item', text='科目')
data_treeview.heading('price', text='金額')

data_treeview.insert(parent='', index='end',
                     values=('2022/06/09', '歯磨き粉', 150))
data_treeview.insert(parent='', index='end',
                     values=('2022/06/09', 'たまねぎ', 150))

data_treeview.pack()

root.mainloop()
