from datetime import datetime
from logger import Logger


class ConsoleLogger(Logger):
    # BEGIN (write your solution here)
    def __init__(self, level = "INFO"):
        super().__init__(level)
    
    def _write_message(self, message):
        print(f"{datetime.now()} [{self.level}]: {message}")
    # END
