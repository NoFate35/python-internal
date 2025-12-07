from Sanitizer import Sanitizer
from SanitizerStripTagsDecorator import SanitizerStripTagsDecorator
from Application import Application


def test_Application():
    sanitizer = Sanitizer()
    decorated = SanitizerStripTagsDecorator(sanitizer)
    app = Application(decorated)
    assert app.run('<p>text<p>') == 'text'
    assert app.run('  <hr>   another text ') == 'another text'
