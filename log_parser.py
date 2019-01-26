from datetime import datetime


def get_date(date_string):
    """
    Takes date in YYYY-MM-DD form,
    returns datetime objects
    """
    return datetime.strptime(date_string, '%Y-%m-%d')
