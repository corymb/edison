from datetime import datetime, time

from log_parser import get_date, get_time


def test_get_date():
    date = '2019-01-01'
    expected = datetime(year=2019, month=1, day=1)
    assert get_date(date) == expected


def test_get_time():
    time_string = '[03:43:05]'
    expected = time(hour=3, minute=43, second=5)
    assert get_time(time_string) == expected


def test_get_nick():
    pass


def test_get_recipient():
    pass


def test_get_message():
    pass
