from tkinter import *
from tkinter import ttk

def display_error_modal(parent, title, geometry, message):
	error_modal = Toplevel(parent)
	error_modal.title(title)
	error_modal.geometry(geometry)
	error_modal.grab_set()

	ttk.Label(error_modal, text=message)

	error_modal.mainloop()