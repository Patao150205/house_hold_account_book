

from tkinter import *
from tkinter import ttk

from lib.windows import regist_data

def main():
    root = Tk()
    root.title('家計簿アプリ')

    root.geometry('700x700')
    root.resizable(width=False, height=False)

    notebook =  ttk.Notebook(root, width=650, height=650)
    tab_input = regist_data.display_regist_data_window(notebook)
    tab_search = ttk.Frame(notebook)

    print(tab_input)

    notebook.add(tab_input, text='家計簿登録')
    notebook.add(tab_search, text='家計簿検索')

    notebook.pack(padx=10, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
