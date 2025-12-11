from abc import abstractmethod


class Logger:
    # BEGIN (write your solution here)
   
    def __init__(self, level):
        self.level = level
        self.current = "INFO"
        self._levels = {
        'DEBUG': 1,
        'INFO': 2,
        'WARNING': 3,
        'ERROR': 4
    }

    @abstractmethod
    def _write_message(self):
        pass

    def info(self, message):
    	if self._levels[self.level] <= self._levels[self.current]:
              self._write_message(message)

    def warning(self, message):
    	if self._levels[self.level] > self._levels[self.current]:
            self.current = self.level
            self._write_message(message)
    # END
