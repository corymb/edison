from datetime import datetime

from log_parser import get_date


def test_get_date():
    date = '2019-01-01'
    expected = datetime(year=2019, month=1, day=1)
    assert get_date(date) == expected


def test_get_time():
    pass


def test_get_nick():
    pass


def test_get_recipient():
    pass


def test_get_message():
    pass
