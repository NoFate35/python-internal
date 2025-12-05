import sys
sys.path.append('/home/ivan/python-internal/exceptions')
from utils import read_files


def test_read_files():
    values = read_files([])
    assert values == []


def test_read_correct_files():
    values = read_files(['/etc/fstab', '/etc/shadow'])
    assert len(values) == 2


def test_read_wrong_files():
    values = read_files(['/etc/shadow', '/opt/asdf'])
    assert (values[1]) is None
