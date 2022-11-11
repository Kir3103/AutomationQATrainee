class TextCompareModel:

    def __init__(self, first_text, second_text):
        self.__first_text = first_text
        self.__second_text = second_text

    def __eq__(self, other):
        return (self.__first_text, self.__second_text) == \
               (other.__first_text, other.__second_text)

    @property
    def first_text(self):
        return self.__first_text

    @first_text.setter
    def first_text(self, another_first_text):
        self.__first_text = another_first_text

    @property
    def second_text(self):
        return self.__second_text

    @second_text.setter
    def second_text(self, another_second_text):
        self.__second_text = another_second_text
