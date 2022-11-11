import random
import string

from LogerUtils import Logger


class StringUtils:

    @staticmethod
    def get_text_with_slice(text_to_change: str, number_of_slice: int):
        return text_to_change.split()[number_of_slice]

    @staticmethod
    def generate_random_string():
        letters = string.ascii_lowercase
        random_string = ''.join(random.sample(letters, 10))
        Logger.info(f'Generate random string: {random_string}')
        return random_string
