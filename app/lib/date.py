import datetime


def get_current_yyyy_mm_dd():
    today = datetime.date.today()
    formated_date = today.strftime('%Y/%m/%d')

    return formated_date
