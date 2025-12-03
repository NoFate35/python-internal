class HTMLElement:
    def __init__(self, attributes=None):
        if attributes is None:
            self.attributes = {}
        else:
            self.attributes = attributes

    def get_attribute(self, key):
        return self.attributes.get(key)

    # BEGIN (write your solution here)
    def _stringify_tags(self, tags):
            return ' '.join(tags)
    def get_tags(self):
        attribute = self.get_attribute('tag')
        return attribute.split(' ')

    def add_tag(self, tag_name):
        string_attrs = self.get_tags()
        if tag_name not in string_attrs:
            string_attrs.append(tag_name)
        self.attributes['tag'] = self._stringify_tags(string_attrs)

    def remove_tag(self, tag_name):
        string_attrs = self.get_tags()
        if tag_name in string_attrs:
            string_attrs.remove(tag_name)
        self.attributes['tag'] = self._stringify_tags(string_attrs)
    
    def toggle_tag(self, tag_name):
        string_attrs = self.get_tags()
        if tag_name in string_attrs:
            self.remove_tag(tag_name)
        else:
            self.add_tag(tag_name)
    # END
