class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # def __check(self, x, y):
    #     if type(x) in (float, int):
    #         self.__x = x
    #     if type(y) in (float, int):
    #         self.__y = y

    def get_coords(self):
        return (self.__x, self.__y)


class Rectangle:

    def __init__(self, *args):
        if len(args) == 4:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])
        else:
            self.__sp = (args[0])
            self.__ep = (args[1])
    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return (self.__sp, self.__ep)

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coord()} {self.__ep.get_coord()}")

rect = Rectangle(Point(0, 0), Point(20, 34))
# rect2 = Rectangle(1, 2, 3, 4)
# #
# print(rect.get_coords())
# print(rect.draw())
#
# print(rect2.get_coords())
# print(rect2.draw())