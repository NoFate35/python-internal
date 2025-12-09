from datetime import datetime
from logger import Logger


class FileLogger(Logger):
    # BEGIN (write your solution here)
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
    
    def _write_message(self):
        with open(self.filename, 'w') as file:
            file.write(f"")
    
    def info(self, message):

        self._write_message(self,message)
        print('message', message)

    # END
