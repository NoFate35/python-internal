from HTMLElement import HTMLElement


class HTMLDivElement(HTMLElement):
    # BEGIN (write your solution here)
    _params = {
        'name': 'div',
        'pair': True,
    }
    def __init__(self):
    	self.text = ''
 
    def set_text_content(self, text):
    	self.text = text

    def get_text_content(self):
    	return self.text
    # END
