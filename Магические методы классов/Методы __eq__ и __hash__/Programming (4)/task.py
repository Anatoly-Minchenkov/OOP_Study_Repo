class Dimensions:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        else:
            self.a = a
            self.b = b
            self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))




s_inp = input()

s_inp = s_inp.split(';')
# print(s_inp)
simp = [[float(s) if '.' in s else int(s) for s in x.split()] for x in s_inp]
# print(simp)

lst_dims = [Dimensions(i[0], i[1], i[2]) for i in simp]
# print(lst_dims)
lst_dims = sorted(lst_dims, key=lambda x: hash(x))
# print(lst_dims)
