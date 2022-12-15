import random# функция для генерации целых случайных значений в диапазоне [a; b]


# здесь объявляйте класс RandomPassword
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        self.passwd = ''.join([random.choice(self.psw_chars) for _ in range(random.randrange(self.min_length, self.max_length))])
        return self.passwd

min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rnd() for i in range(3)]
# print(lst_pass)
# print(psw)
# print(type(rnd.lst_pass))