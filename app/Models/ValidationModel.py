import re

from Views.Validation import invalid_date_modal


def validation_regist_form_data(date, item, price, category):
    result = is_yyyy_mm_dd_only(
        date) and item and category and is_num_only(price)

    return result

def validation_search_form_data(date_from, date_to):
    result_date_from = is_yyyy_mm_dd_only(date_from)
    result_date_to = is_yyyy_mm_dd_only(date_to)
    result = result_date_from and result_date_to

    print(result_date_from, date_to, result)
    return result


def is_num_only(text: str):
    return text.isdigit()


def is_yyyy_mm_dd_only(text: str):
    is_match = re.match(
        '^[0-9]{4}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$',
        text)
    print(is_match)
    if is_match:
        return True
    else:
        return False


def date_form_validation(letter: str, text: str, input_action):
    if input_action == 'key':
        if re.match('[0-9/]', letter):
            return True
        else:
            return False
    elif input_action == 'focusout':
        if is_yyyy_mm_dd_only(text):
            return True
        else:
            invalid_date_modal()
            return False
    else:
        return False
