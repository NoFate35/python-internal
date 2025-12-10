from datetime import datetime
from logger import Logger


class FileLogger(Logger):
    # BEGIN (write your solution here)
    def __init__(self, filename, level = "INFO"):
        super().__init__(level)
        self.filename = filename
    
    def _write_message(self, message):
        try:
            with open(self.filename, 'w') as file:
            	file.write(f"{datetime.now()} [{self.level}]: {message}")
        except Exception:
        	print("Ошибка записи в файл")
    


    # END
