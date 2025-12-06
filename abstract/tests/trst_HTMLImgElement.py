from HTMLImgElement import HTMLImgElement


def test_HTMLImgElement():
    img = HTMLImgElement()
    assert img.is_valid()

    img = HTMLImgElement({'class': 'rounded', 'src': 'path/to/file'})
    assert img.is_valid()

    img = HTMLImgElement({'class': 'rounded', 'href': 'path/to/file'})
    assert not img.is_valid()
