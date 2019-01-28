from datetime import datetime

from search.file_reader import FileReader


IGNORE_PATTERNS = '***'  # should be an iterable, but we only need to match one pattern (O(n) vs O(n2)


class LogParser:
    """
    Groups log parsing functionality.

    Methods or attributes not prefixed with '_' should be considered a public
    interface.
    """
    def __init__(self, filename):
        self._filename = filename
        self._date = self._get_date_from_filename(filename)
        self._reader = FileReader(filename)
        self._ignore_patterns = IGNORE_PATTERNS

    def parse_log_file(self):
        log_file = self._reader.read_file()
        acc = []
        for l in log_file:
            line = self._parse_line(l.split())
            if line:
                acc.append(line)
        return acc

    def _parse_line(self, line):
        if self._ignore_patterns in line:
            return None

        time = self._get_time(line[0])
        recipient = self._get_recipient(line)
        return dict(
            sent=datetime.combine(self._date, time),
            nick=self._get_nick(line),
            recipient=recipient,
            message=self._get_message(line, recipient)
        )

    def _get_date_from_filename(self, filename):
        """
        Takes filename
        returns corresponding datetime object
        """
        date_string = filename[:-4]
        return datetime.strptime(date_string, '%Y-%m-%d')

    def _get_time(self, time_string):
        """
        Takes time in [HH:MM:SS] form,
        returns time object
        """
        return datetime.strptime(time_string, '[%H:%M:%S]').time()

    def _get_nick(self, line):
        """
        Takes a list based on the line to parse
        returns user's nick
        """
        sender = line[1]
        # strip < and >:
        return sender[1:-1]

    def _get_recipient(self, line):
        """
        Takes a list based on the line to parse
        returns recipient's nick if it exists, None if not
        """
        recipient = line[2]
        return recipient[:-1] if recipient.endswith(':') else None

    def _get_message(self, line, recipient=None):
        """
        Takes a list based on the line to parse
        returns message string excluding recipient if not None
        """
        # Strip timestamp:
        line = line[1:]
        # Strip recipient nick from message if it's in there:
        if recipient and recipient + ':' in line:
            line = line[2:]
        return ' '.join(line)
