from HTMLElement import HTMLElement


class HTMLImgElement(HTMLElement):
    ATTRIBUTE_NAMES = ['src']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    
    # END
