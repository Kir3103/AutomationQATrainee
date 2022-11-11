class StringUtils:

    @staticmethod
    def get_quant_players(text_from_page, index_word, del_symbol, new_symbol):
        return int(text_from_page.split()[index_word].replace(del_symbol, new_symbol))
