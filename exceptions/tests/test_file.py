import pytest
import sys
sys.path.append('/home/ivan/python-internal/exceptions')
from File import File
from errors.NotExistsError import NotExistsError
from errors.NotReadableError import NotReadableError


def test_read():
    file = File('/etc/fstab')
    assert file.read() is not False


def test_NotExistsError():
    file = File('/etc/foobar')
    with pytest.raises(NotExistsError):
        file.read()


def test_NotReadableError():
    file = File('/etc/shadow')
    with pytest.raises(NotReadableError):
        file.read()
