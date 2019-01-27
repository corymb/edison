import os

import mock

from search.file_reader import FileReader


@mock.patch("builtins.open", new_callable=mock.mock_open, read_data='test line')
def test_file_read(file_reader):
    file_reader = FileReader('2019-01-01.log')
    assert file_reader.read_file() == ['test line']


def test_file_reader_gets_environment_variable():
    expected = 'test-dir'
    os.environ['EDISON_LOG_DIRECTORY'] = expected
    file_reader = FileReader('2019-01-01.log')
    assert file_reader._log_directory == expected
