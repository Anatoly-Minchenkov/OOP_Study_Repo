import math
class PathLines:

    def __init__(self, *lines):
        self.line_list = list((LineTo(0, 0),) + lines)
    def add_line(self, line):
        self.line_list.append(line)

    def get_path(self):
        return self.line_list[1:]

    def get_length(self):
        coords_list = [(line.x, line.y) for line in self.line_list]
        x = 0
        for i in range(1, len(self.line_list)):
            x += math.sqrt((coords_list[i][0]-coords_list[i-1][0])**2 + (coords_list[i][1] - coords_list[i-1][1])**2)
        return x
class LineTo:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


# d = LineTo(20, 30)
# dc = LineTo(2032, 330)
# dsd = LineTo(210, 0)
# print(d.x, d.y)

# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# print(p.get_path())
# print(p.get_length())
