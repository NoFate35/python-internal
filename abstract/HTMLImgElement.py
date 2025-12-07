from HTMLElement import HTMLElement


class HTMLImgElement(HTMLElement):
    ATTRIBUTE_NAMES = ['src']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    def is_valid(self):
    	attributes = self.get_attributes()
    	attribute_names = self.get_attribute_names()
    	return set(attributes.keys()).issubset(set(attribute_names))
    # END
