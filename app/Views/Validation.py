from tkinter import messagebox


def regist_data_invalid_modal():
    messagebox.showwarning(
        '形式エラー', 'フォームに正しい入力をしてください。\n\n '
        '年月日:  yyyy/mm/dd \n '
        '科目:     1文字以上 \n'
        '金額:       数字のみ')


def invalid_date_modal():
    messagebox.showwarning('エラー', '日付をyyyy/mm/dd形式で入力してください。')
