from HTMLElement import HTMLElement


# BEGIN (write your solution here)
class HTMLPairElement(HTMLElement):

    def __init__(self, attributes=None):
    	super().__init__(attributes)
    	self._body = ''

    def __str__(self):
    		attr_line = self._stringify_attributes()
    		tag = self.get_tag_name()
    		body = self.get_text_content()
    		return f'<{tag}{attr_line}>{body}</{tag}>'

    def get_text_content(self):
        return self._body

    def set_text_content(self, body):
    	self._body = body
# END
