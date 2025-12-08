from lxml import etree


def strip_tags(tag_string):
    parser = etree.HTMLParser()
    tree = etree.fromstring(tag_string, parser)
    return etree.tostring(tree, encoding='unicode', method='text')


class SanitizerStripTagsDecorator:
    def __init__(self, sanitizer):
        self.sanitizer = sanitizer
        #print('self.sanitizer', self.sanitizer)

    # BEGIN (write your solution here)
    def sanitize(self, text):
        clean_text = strip_tags(text)
        stripped_text = self.sanitizer.sanitize(clean_text)
        return stripped_text
    # END
