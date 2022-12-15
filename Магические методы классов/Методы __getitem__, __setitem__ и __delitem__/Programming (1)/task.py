class Track:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.segms = []

    def add_point(self, x, y, speed):
        self.segms.append([(x, y), speed])

    def __getitem__(self, item):
        if not isinstance(item, int) or not 0 <= item < len(self.segms):
            raise IndexError('некорректный индекс')
        return self.segms[item][0], self.segms[item][1]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or not 0 <= key < len(self.segms):
            raise IndexError('некорректный индекс')
        self.segms[key][1] = value


# tr = Track(10, -5.4)
# tr.add_point(20, 0, 100)
# tr.add_point(50, -20, 80)
# coord, speed = tr[0]
# print(coord, speed)
# tr[0] = 999
# coord, speed = tr[0]
# print(coord, speed)


