class ListMath:
    def __init__(self, lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []
        self.repair(self._lst)
    def repair(self, lst):
        self.lst_math = [x for x in lst if type(x) in(int, float)]

    def __add__(self, other):
        return ListMath(list(map(lambda x: x + other, self.lst_math)))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return ListMath(list(map(lambda x: x - other, self.lst_math)))

    def __rsub__(self, other):
        return ListMath(list(map(lambda x: other - x, self.lst_math)))

    def __mul__(self, other):
        return ListMath(list(map(lambda x: x * other, self.lst_math)))

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return ListMath(list(map(lambda x: x / other, self.lst_math)))
    def __rtruediv__(self, other):
        return self / other

# lst = ListMath([1, "abc", -5, 7.68, True])
# print(lst.lst_math)
# lst = lst + 76
# print(lst.lst_math)
# lst = 6.5 + lst
# print(lst.lst_math)
# lst += 76.7
# print(lst.lst_math)
# lst = lst - 76
# print(lst.lst_math)
# lst = 7.0 - lst
# print(lst.lst_math)
# lst -= 76.3
# print(lst.lst_math)
# lst = lst * 5
# print(lst.lst_math)
# lst = 5 * lst
# print(lst.lst_math)
# lst *= 5.54
# print(lst.lst_math)
# lst = lst / 13
# print(lst.lst_math)
# lst = 3 / lst
# print(lst.lst_math)
# lst /= 13.0
# print(lst.lst_math)