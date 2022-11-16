
class Book:

    def __init__(self, author, title, price):
        self.__author = self.__set_author(author)
        self.__title = self.__set_title(title)
        self.__price = self.__set_price(price)
    def __set_title(self, title):
        return title

    def __set_author(self, author):
        return author

    def __set_price(self, price):
        return price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price






