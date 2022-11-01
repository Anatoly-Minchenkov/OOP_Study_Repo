class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):

        return list((map(lambda x: f'{x.name}: {x.price}', self.goods)))


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('kek', 100))
cart.add(TV('lol', 500))
cart.add(Table('stol', 700))
cart.add(Notebook('asus', 1000))
cart.add(Notebook('dell', 200))
cart.add(Cup('kruzka', 90000))
cart.get_list()