import os
from errors.NotExistsError import NotExistsError
from errors.NotReadableError import NotReadableError


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        file_path = self.file_path

        # BEGIN (write your solution here)
        if not os.path.exists(file_path):
            raise NotExistsError(f"'{file_path}' does not exist")

        if not os.access(file_path, os.R_OK):
            raise NotReadableError(f"'{file_path}' does not read")

        with open(file_path) as fp:
            return fp.read()
        # END
