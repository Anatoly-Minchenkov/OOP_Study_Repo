class TriangleChecker:
    def __init__(self, a, b, c):
        self.lst = [a, b, c]

    def is_triangle(self):
        for i in self.lst:
            if type(i) not in (int, float) or i <= 0:
                return 1
        if max(self.lst) >= sum(self.lst) - max(self.lst):
            return 2
        else:
            return 3

a, b, c = map(int, input().split()) # эту строчку не менять
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())