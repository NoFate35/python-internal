from File import File
from errors.FileError import FileError


# BEGIN (write your solution here)
def read_files(paths):
    data = []
    for path in paths:
        file = File(path)
        try:
            file_data = file.read()
            data.append(file_data)
        except FileError:
            data.append(None)
    return data
# END
