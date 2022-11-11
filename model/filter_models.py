class FilterModel:

    def __init__(self, game_name, hero_name, rarity, search_phrase):
        self.__game_name = game_name
        self.__hero_name = hero_name
        self.__rarity = rarity
        self.__search_phrase = search_phrase

    def __eq__(self, other):
        return (self.__game_name, self.__hero_name, self.__rarity, self.__search_phrase) \
               == (other.__game_name, other.__hero_name, other.__rarity, other.__search_phrase)

    @property
    def game_name(self):
        return self.__game_name

    @game_name.setter
    def game_name(self, another_game_name):
        self.__game_name = another_game_name

    @property
    def hero_name(self):
        return self.__hero_name

    @hero_name.setter
    def hero_name(self, another_hero_name):
        self.__hero_name = another_hero_name

    @property
    def rarity(self):
        return self.__rarity

    @rarity.setter
    def rarity(self, another_rarity):
        self.__rarity = another_rarity

    @property
    def search_phrase(self):
        return self.__search_phrase

    @search_phrase.setter
    def search_phrase(self, another_search_phrase):
        self.__search_phrase = another_search_phrase
