class HTMLElement:
    def __init__(self):
        self.body = None

    def set_text_content(self, body):
    	self.body = body

    @classmethod
    def get_params(cls):
        return cls._params

    # BEGIN (write your solution here)
    def __str__(self):
    	params = self.get_params()
    	if params['pair']:
    		text = self.get_text_content()
    		return f"<{params['name']}>{text}</{params['name']}>"
    	return f'<{params['name']}>'
    # END