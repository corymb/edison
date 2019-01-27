from datetime import datetime, time

from mock import patch

from log_parser import LogParser


DATE = datetime(year=2019, month=1, day=1, hour=20, minute=45, second=34)
DATE_STRING = '2019-01-01'
TIME = '[20:45:34]'
FILENAME = '{}.log'.format(DATE_STRING)
NICK = 'cdunklau'
RECIPIENT = 'JordiGH'
MESSAGE = 'angle brackets'
LINE = '{} <{}> {}: {}'.format(TIME, NICK, RECIPIENT, MESSAGE).split()
LINE_WITHOUT_RECIPIENT = '<{}> {}'.format(NICK, MESSAGE).split()


def test_get_date_from_filename():
    log_parser = LogParser(FILENAME)
    expected = datetime(year=2019, month=1, day=1)
    assert log_parser._get_date_from_filename(FILENAME) == expected


def test_get_time():
    log_parser = LogParser(FILENAME)
    expected = time(hour=20, minute=45, second=34)
    assert log_parser._get_time(TIME) == expected


def test_get_nick():
    log_parser = LogParser(FILENAME)
    expected = 'cdunklau'
    assert log_parser._get_nick(LINE) == expected


def test_get_recipient():
    log_parser = LogParser(FILENAME)
    expected = RECIPIENT
    assert log_parser._get_recipient(LINE) == expected


def test_get_recipient_without_recipient():
    log_parser = LogParser(FILENAME)
    assert log_parser._get_recipient(LINE_WITHOUT_RECIPIENT) is None


def test_get_message():
    log_parser = LogParser(FILENAME)
    expected = MESSAGE
    assert log_parser._get_message(LINE, recipient='JordiGH') == expected


def test_get_message_without_recipient():
    log_parser = LogParser(FILENAME)
    expected = MESSAGE
    assert log_parser._get_message(LINE_WITHOUT_RECIPIENT) == expected


def test_parse_line():
    log_parser = LogParser(FILENAME)
    parsed_data = log_parser._parse_line(LINE)
    assert parsed_data['sent'] == DATE
    assert parsed_data['nick'] == NICK
    assert parsed_data['recipient'] == RECIPIENT
    assert parsed_data['message'] == MESSAGE


@patch('file_reader.FileReader.read_file', lambda x: [' '.join(LINE)])
def test_parse_log():
    log_parser = LogParser(FILENAME)
    parsed_data = log_parser.parse_log_file()[0]
    assert parsed_data['sent'] == DATE
    assert parsed_data['nick'] == NICK
    assert parsed_data['recipient'] == RECIPIENT
    assert parsed_data['message'] == MESSAGE
