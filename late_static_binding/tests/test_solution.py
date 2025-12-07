import sys
sys.path.append('/data/data/com.termux/files/home/python-internal/late_static_binding')
from HTMLBrElement import HTMLBrElement
from HTMLDivElement import HTMLDivElement


def test_solution():
    hr = HTMLBrElement()
    expected = '<br>'
    assert expected == str(hr)

    element = HTMLDivElement()
    element.set_text_content('hello!')
    expected = '<div>hello!</div>'
    assert expected == str(element)

    element = HTMLDivElement()
    expected = '<div></div>'
    assert expected == str(element)


def test_set_params():
    element = HTMLDivElement()
    element._params = {
        'name': 'foo',
    }
    assert element._params == {
        'name': 'foo',
    }
    assert str(element) == '<div></div>'
