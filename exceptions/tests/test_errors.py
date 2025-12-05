import sys
sys.path.append('/home/ivan/python-internal/exceptions')
from errors.NotExistsError import NotExistsError

from errors.NotReadableError import NotReadableError
from errors.FileError import FileError


def test_NotExistsError():
    error = NotExistsError()
    assert isinstance(error, FileError)


def test_NotReadableError():
    error = NotReadableError()
    assert isinstance(error, FileError)
