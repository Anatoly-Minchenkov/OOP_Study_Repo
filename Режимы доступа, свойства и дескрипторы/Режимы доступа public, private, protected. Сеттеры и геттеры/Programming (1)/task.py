class Money:
    def __init__(self, money):
        self.__money = money

    @staticmethod
    def __check_money(money):
        if type(money) is int and money >= 0:
            return True
        else:
            return False
    def add_money(self, mn):
        if self.__check_money(mn.get_money()):
            self.__money += mn.get_money()
    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money
    def get_money(self):
        return self.__money

