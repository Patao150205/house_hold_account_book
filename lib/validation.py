import re

from tkinter import messagebox
from tkinter import ttk

def is_num_only(text: str):
  return text.isdigit()

def is_yyyy_mm_dd_only(text: str):
	if re.match('^[0-9]{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$', text):
			return True
	else:
		  return False

def date_form(letter: str,text: str, input_action):
	if input_action == 'key':
		if re.match('[0-9/]', letter):
			return True
		else:
			return False
	elif input_action == 'focusout':
		if is_yyyy_mm_dd_only(text):
			return True
		else:
			messagebox.showwarning('エラー', '日付をyyyy/mm/dd形式で入力してください。')
			return False
	else:
		return False

def validation_regist_form(date,item, price):
	return is_yyyy_mm_dd_only(date) and item and is_num_only(price)