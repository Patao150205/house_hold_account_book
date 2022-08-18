from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from lib import validation  

def set_record_bind(data_treeview):
	global treeview 
	treeview = data_treeview
	data_treeview.bind('<<TreeviewSelect>>',display_edit_record_form)

def display_edit_record_form(event):
	edit_record_window = Toplevel()
	edit_record_window.geometry('400x400')
	edit_record_window.resizable(width=False, height=False)
	edit_record_window.title('レコードの編集')
	edit_record_window.grab_set()
	edit_record_window.focus_set()

	record_id = treeview.focus()
	record_values = treeview.item(record_id)['values']

	current_record_frame = ttk.Frame(edit_record_window)
	current_record_frame.pack(padx=10, pady=20)

	current_date_label = ttk.Label(current_record_frame, text='現在のレコード')
	current_date_label.grid(row=0, column=0, columnspan=2)
	
	current_date_label = ttk.Label(current_record_frame, text='年月日')
	current_date_label.grid(row=1, column=0)

	current_item_label = ttk.Label(current_record_frame, text='科目')
	current_item_label.grid(row=2, column=0)

	current_price_label = ttk.Label(current_record_frame, text='金額')
	current_price_label.grid(row=3, column=0)

	date_label = ttk.Label(current_record_frame, text=record_values[0], padding=(0, 3))
	item_lable = ttk.Label(current_record_frame, text=record_values[1], padding=(0, 3))
	price_label = ttk.Label(current_record_frame, text=record_values[2], padding=(0, 3))

	date_label.grid(row=1, column=1, padx=60)
	item_lable.grid(row=2, column=1)
	price_label.grid(row=3, column=1)

	# 編集フォーム
	form_frame = ttk.Frame(edit_record_window, padding=10)
	form_frame.pack()

	form_date_label = ttk.Label(form_frame, text='登録するデータを入力してください。')
	form_date_label.grid(row=0, column=0, columnspan=2)

	form_date_label = ttk.Label(form_frame, text='年月日')
	form_date_label.grid(row=1, column=0)

	form_item_label = ttk.Label(form_frame, text='科目')
	form_item_label.grid(row=2, column=0)

	price_label = ttk.Label(form_frame, text='金額')
	price_label.grid(row=3, column=0)

	date_only_cmd = form_frame.register(validation.date_form)
	num_only_cmd = form_frame.register(validation.is_num_only)

	date = StringVar()
	item = StringVar()
	price = StringVar()

	date_entry = ttk.Entry(form_frame, textvariable=date, justify=CENTER, validate='all', validatecommand=(date_only_cmd, '%S','%P', '%V'))
	date_entry.insert(0, record_values[0])
	date_entry.grid(row=1, column=1, pady=3)
	item_entry = ttk.Entry(form_frame, textvariable=item, justify=CENTER )
	item_entry.insert(0, record_values[1])
	item_entry.grid(row=2, column=1, pady=3)
	price_entry = ttk.Entry(form_frame, textvariable=price, justify=CENTER, validate='key', validatecommand=(num_only_cmd, '%S'))
	price_entry.insert(0, record_values[2])
	price_entry.grid(row=3, column=1, pady=3)

	  # 送信ボタン
	def send_data_to_database():
		messagebox.showinfo('家計簿登録成功', '家計簿に登録しました。')
		edit_record_window.destroy()

	send_data_button = ttk.Button(edit_record_window ,text='データを送信', padding=(20, 20), command=send_data_to_database)
	send_data_button.pack()

	edit_record_window.mainloop()