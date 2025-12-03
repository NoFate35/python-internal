import sys
print('sys.path', sys.path)
from HTMLDivElement import HTMLDivElement


def test_elements():
    div = HTMLDivElement()
    expected = '<div></div>'
    assert str(div) == expected

    div = HTMLDivElement({'class': 'w-75', 'id': 'wop'})
    expected = '<div class="w-75" id="wop"></div>'
    assert str(div) == expected

    div = HTMLDivElement({'name': 'div', 'data-toggle': 'true'})
    div.set_text_content('Body Text')
    expected = '<div name="div" data-toggle="true">Body Text</div>'
    assert str(div) == expected
