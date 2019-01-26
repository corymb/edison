from datetime import datetime


def get_date(date_string):
    """
    Takes date in YYYY-MM-DD form,
    returns datetime object
    """
    return datetime.strptime(date_string, '%Y-%m-%d')


def get_time(time_string):
    """
    Takes time in [HH:MM:SS] form,
    returns time object
    """
    return datetime.strptime(time_string, '[%H:%M:%S]').time()
