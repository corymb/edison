from datetime import datetime


class LogParser:
    """
    Groups log parsing functionality.
    Methods not prefixed with '_' should be considered a public interface
    """
    def _get_date(self, date_string):
        """
        Takes date in YYYY-MM-DD form,
        returns datetime object
        """
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
        sender = line[0]
        # strip < and >:
        return sender[1:-1]

    def _get_recipient(self, line):
        """
        Takes a list based on the line to parse
        returns recipient's nick if it exists, None if not
        """
        recipient = line[1]
        return recipient[:-1] if recipient.endswith(':') else None

    def _get_message(self, line, recipient=None):
        """
        Takes a list based on the line to parse
        returns message string excluding recipient if not None
        """
        # Strip recipient nick from message if it's in there:
        if recipient and recipient + ':' in line:
            line = line[2:]
        return ' '.join(line)
