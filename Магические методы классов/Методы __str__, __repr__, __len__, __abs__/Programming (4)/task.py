class Complex:
    def __init__(self, real, img):
        self.__real = self.__img = 0
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        if type(real) in (int, float):
            self.__real = real
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        if type(img) in (int, float):
            self.__img = img
        else:
            raise ValueError("Неверный тип данных.")
    def __abs__(self):
        return (self.real * self.real + self.img * self.img)**0.5
cmp = Complex(7, 8)
cmp.img = 4
cmp.real = 3
c_abs = abs(cmp)
# print(c_abs)
# print(cmp.__dict__)