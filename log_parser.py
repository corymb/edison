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


def get_nick(line):
    """
    Takes a list based on the line to parse
    returns user's nick
    """
    sender = line[0]
    # strip < and >:
    return sender[1:-1]


def get_recipient(line):
    """
    Takes a list based on the line to parse
    returns recipient's nick if it exists, None if not
    """
    recipient = line[1]
    return recipient[:-1] if recipient.endswith(':') else None
