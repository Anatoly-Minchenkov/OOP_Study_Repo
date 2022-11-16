class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = 0
        self.__y = 0
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) in (int, float) and self.MIN_COORD <= x <= self.MAX_COORD:
            self.__x = x




    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) in (int, float) and self.MIN_COORD <= y <= self.MAX_COORD:
            self.__y = y


    @staticmethod
    def norm2(vector):
        x = vector.__x
        y = vector.__y
        return x * x + y * y

# v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
# v2 = RadiusVector2D(-1000, 25424242)       # радиус-вектор с координатами (1; 0)
# v3 = RadiusVector2D(1, 23)
# print(v1.x, v1.y)
# print(v2.x, v2.y)
# print(v3.x, v3.y)
#
# r = RadiusVector2D(10, 20)
# r.x = 'a'
# r.y = (1, 2)
# print(r.x, r.y)
