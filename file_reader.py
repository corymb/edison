class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename) as f:
            return f.readlines()
