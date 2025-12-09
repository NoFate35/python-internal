from abc import abstractmethod


class Logger:
    # BEGIN (write your solution here)
    levels = {
        'DEBUG': 1,
        'INFO': 2,
        'WARNING': 3,
        'ERROR': 4
    }
    def __init__(self, level='INFO'):
        self.level = level
    
    def log(self, level, message):
        pass

    @abstractmethod
    def _write_message(self):
        pass


    # END
