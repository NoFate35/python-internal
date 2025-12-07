
from HTMLElement import HTMLElement


class HTMLButtonElement(HTMLElement):
    ATTRIBUTE_NAMES = ['type']
    TYPE_NAMES = ['button', 'submit', 'reset']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    def is_valid(self):
    	attributes = self.get_attributes()
    	attribute_names = self.get_attribute_names()
    	if set(attributes.keys()).issubset(set(attribute_names)):
    		type = attributes.get('type')
    		if type:
    			return type in self.TYPE_NAMES
    # END
