class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = None
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if type(a) in (int, float) and self.MIN_DIMENSION <= a <= self.MAX_DIMENSION:
            self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        if type(b) in (int, float) and self.MIN_DIMENSION <= b <= self.MAX_DIMENSION:
            self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        if type(c) in (int, float) and self.MIN_DIMENSION <= c <= self.MAX_DIMENSION:
            self.__c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        object.__setattr__(self, key, value)

# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# print(a,b,c)
# d.MAX_DIMENSION = 10  # исключение AttributeError