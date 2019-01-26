from datetime import datetime, time

from log_parser import LogParser


LINE = '<cdunklau> JordiGH: angle brackets'.split()


def test_get_date():
    log_parser = LogParser()
    date = '2019-01-01'
    expected = datetime(year=2019, month=1, day=1)
    assert log_parser._get_date(date) == expected


def test_get_time():
    log_parser = LogParser()
    time_string = '[03:43:05]'
    expected = time(hour=3, minute=43, second=5)
    assert log_parser._get_time(time_string) == expected


def test_get_nick():
    log_parser = LogParser()
    expected = 'cdunklau'
    assert log_parser._get_nick(LINE) == expected


def test_get_recipient():
    log_parser = LogParser()
    expected = 'JordiGH'
    assert log_parser._get_recipient(LINE) == expected


def test_get_recipient_without_recipientp():
    log_parser = LogParser()
    # strips recipient:
    line = [LINE[0]] + LINE[2:]
    assert log_parser._get_recipient(line) is None


def test_get_message():
    log_parser = LogParser()
    expected = ' '.join(LINE[2:])
    assert log_parser._get_message(LINE, recipient='JordiGH') == expected
