import os


class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self._log_directory = self._get_log_directory()

    def read_file(self):
        with open(self._log_directory + self.filename) as f:
            return f.readlines()

    def _get_log_directory(self):
        """
        Get environment variable or just guess at 'logs/' for now
        """
        return os.getenv('EDISON_LOG_DIRECTORY', 'logs/')
