class GameModel:

    def __init__(self, game_name, release_date, price):
        self.__game_name = game_name
        self.__release_date = release_date
        self.__price = price

    def __eq__(self, other):
        return (self.__game_name, self.__release_date, self.__price) \
               == (other.__game_name, other.__release_date, other.__price)

    @property
    def game_name(self):
        return self.__game_name

    @game_name.setter
    def game_name(self, another_game_name):
        self.__game_name = another_game_name

    @property
    def release_date(self):
        return self.__release_date

    @release_date.setter
    def release_date(self, another_release_date):
        self.__release_date = another_release_date

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, another_price):
        self.__price = another_price
