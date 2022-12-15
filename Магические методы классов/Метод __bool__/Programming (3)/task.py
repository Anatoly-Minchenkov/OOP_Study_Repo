class Ellipse:
    def __init__(self, *args):
        if len(args) >= 1:
            self.x1 = args[0]
        if len(args) >= 2:
            self.y1 = args[1]
        if len(args) >= 3:
            self.x2 = args[2]
        if len(args) >= 4:
            self.y2 = args[3]

    def __bool__(self):
        return all([getattr(self, 'x1', False), getattr(self, 'y1', False), getattr(self, 'x2', False), getattr(self, 'y2', False)])

    def get_coords(self):
        if bool(self):
            return (self.x1, self.y1, self.x2, self.y2)
        else:
            raise AttributeError('нет координат для извлечения')
# el1 = Ellipse()
# el2 = Ellipse(1,2,3, 4)
# print(bool(el1), bool(el2))
# print(el2.get_coords())

lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(2, 3, 4, 5)]
for i in lst_geom:
    if i:
        i.get_coords()
