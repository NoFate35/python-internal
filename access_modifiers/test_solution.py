#import sys
#print('sys.path', sys.path)
from HTMLDivElement import HTMLDivElement



def test_HTMLDivElement():
    tag = 'one two'
    div = HTMLDivElement({'tag': tag})
    assert div.get_attribute('tag') == tag

    div.add_tag('small')
    assert div.get_attribute('tag') == 'one two small'

    div.add_tag('small')
    assert div.get_attribute('tag') == 'one two small'

    div.remove_tag('two')
    assert div.get_attribute('tag') == 'one small'

    div.toggle_tag('small')
    assert div.get_attribute('tag') == 'one'

    div.toggle_tag('small')
    assert div.get_attribute('tag') == 'one small'
