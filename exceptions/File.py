import os
from errors.NotExistsError import NotExistsError
from errors.NotReadableError import NotReadableError


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        file_path = self.file_path

        # BEGIN (write your solution here)
        
        # END
        with open(file_path, 'r') as file:
            return file.read()
