from lxml import etree


def strip_tags(tag_string):
    parser = etree.HTMLParser()
    tree = etree.fromstring(tag_string, parser)
    return etree.tostring(tree, encoding='unicode', method='text')


class SanitizerStripTagsDecorator:
    def __init__(self, sanitizer):
        self.sanitizer = sanitizer

    # BEGIN (write your solution here)
    pass
    # END
