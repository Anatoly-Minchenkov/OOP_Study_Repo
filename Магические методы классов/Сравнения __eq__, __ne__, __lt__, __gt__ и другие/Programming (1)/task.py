class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.size = self.a * self.b * self.c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if self.MIN_DIMENSION <= a <= self.MAX_DIMENSION:
            self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        if self.MIN_DIMENSION <= b <= self.MAX_DIMENSION:
            self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        if self.MIN_DIMENSION <= c <= self.MAX_DIMENSION:
            self.__c = c

    def __eq__(self, other):
        self.size = self.a * self.b * self.c
        return self.size == other.size

    def __lt__(self, other):
        self.size = self.a * self.b * self.c
        return self.size < other.size

    def __le__(self, other):
        self.size = self.a * self.b * self.c
        return self.size <= other.size


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


# d2 = Dimensions(10, 10, 10)
# d3 = Dimensions(11, 11, 11)
#
# a = d2 == d3
# b = d2 < d3
# c = d2 <= d3
#
# print(a, b ,c)


lst_shop = []
lst_shop.append(ShopItem('кеды', 1024, Dimensions(40, 30, 120)))
lst_shop.append(ShopItem('зонт', 500.24, Dimensions(10, 20, 50)))
lst_shop.append(ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)))
lst_shop.append(ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)))
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.size)
