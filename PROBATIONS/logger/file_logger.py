from datetime import datetime
from logger import Logger


class FileLogger(Logger):
    # BEGIN (write your solution here)
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
    
    def _write_message(self, message):
        with open(self.filename, 'w') as file:
            file.write(f"{datetime.now()} [{self.level}]: {message}")
    
    def info(self, message):

        self._write_message(message)

    # END
