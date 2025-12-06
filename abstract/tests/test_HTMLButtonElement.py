import sys
sys.path.append('/home/ivan/python-internal/abstract')
from HTMLButtonElement import HTMLButtonElement


def test_HTMLButtonElement():
    button = HTMLButtonElement()
    assert not button.is_valid()

    button = HTMLButtonElement({'class': 'rounded', 'type': 'submit'})
    assert button.is_valid()

    button = HTMLButtonElement({'name': 'button', 'type': 'button'})
    assert button.is_valid()

    button = HTMLButtonElement({'type': 'button', 'name': 'button'})
    assert button.is_valid()

    button = HTMLButtonElement({'class': 'rounded', 'type': 'link'})
    assert not button.is_valid()

    button = HTMLButtonElement({'class': 'rounded'})
    assert not button.is_valid()

    button = HTMLButtonElement({'class': 'rounded', 'href': 'path/to/file'})
    assert not button.is_valid()

    button = HTMLButtonElement({'type': 'button', 'href': 'path/to/file'})
    assert not button.is_valid()
