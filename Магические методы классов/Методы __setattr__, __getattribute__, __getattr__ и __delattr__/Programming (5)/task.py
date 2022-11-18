class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if isinstance(radius, (int, float)):
            if radius > 0:
                self.__radius = radius
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False


# circle = Circle(10.5, 7, 22)
# circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# x, y = circle.x, circle.y
# res = circle.name # False, т.к. атрибут name не существует