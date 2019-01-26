from datetime import datetime, time

from log_parser import get_date, get_time, get_nick, get_recipient


LINE = '<cdunklau> JordiGH: angle brackets'.split()


def test_get_date():
    date = '2019-01-01'
    expected = datetime(year=2019, month=1, day=1)
    assert get_date(date) == expected


def test_get_time():
    time_string = '[03:43:05]'
    expected = time(hour=3, minute=43, second=5)
    assert get_time(time_string) == expected


def test_get_nick():
    expected = 'cdunklau'
    assert get_nick(LINE) == expected


def test_get_recipient():
    expected = 'JordiGH'
    assert get_recipient(LINE) == expected

def test_get_recipient_without_recipientp():
    # strips recipient:
    line = [LINE[0]] + LINE[2:]
    assert get_recipient(line) == None

def test_get_message():
    pass
