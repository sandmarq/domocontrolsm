"""

"""
import datetime
import locale
import time
from calendar import different_locale, month_name, day_name


def get_time():
    """
    get present time
    :return: time
    """
    return time.strftime("%H:%M:%S")


def get_month_name(month_no, loclg):
    """
    get the right month name from translation
    :param month_no:
    :param loclg:
    :return:
    """
    with different_locale(loclg) as encoding:
        s = month_name[month_no]
        if encoding is not None:
            s = s.decode(encoding)
        return s


def get_day_name(day_no, loclg):
    """
    get the right day name from translation
    :param day_no:
    :param loclg:
    :return:
    """
    with different_locale(loclg) as encoding:
        s = day_name[day_no]
        if encoding is not None:
            s = s.decode(encoding)
        return s


def get_date():
    """
    get the present date
    :return: return the present date
    """
    day_name1 = get_day_name(datetime.datetime.today().weekday(), locale.getdefaultlocale()[0] + "." \
                             + locale.getdefaultlocale()[1]).capitalize()
    month_name1 = get_month_name(datetime.datetime.today().month, locale.getdefaultlocale()[0] + "." \
                                 + locale.getdefaultlocale()[1]).capitalize()
    if locale.getdefaultlocale()[0][0:2] == 'fr':
        str_date = day_name1 + ", le " + str(datetime.datetime.today().day) + " " + month_name1 + " " \
                   + str(datetime.datetime.today().year)
        return str_date
    else:
        str_date = day_name1 + ", " + month_name1 + " " + str(datetime.datetime.today().day) + " " \
                   + str(datetime.datetime.today().year)
        return str_date
