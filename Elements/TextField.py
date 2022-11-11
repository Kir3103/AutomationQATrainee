from Elements.BaseElement import BaseElements
from LogerUtils import Logger


class TextField(BaseElements):

    def send_keys(self, keys, clear=True):
        element = self.find_element_with_wait()
        if clear:
            element.clear()
            element.send_keys(keys)
        else:
            element.send_keys(keys)
        Logger.info('Input text to: ' + self.name)
