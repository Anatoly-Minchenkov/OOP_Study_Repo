class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.count = -1

    def ind_check(self, indx):
        if type(indx) == int and 0<= indx <= 4:
            return indx
        else:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.ind_check(item)
        item = list(self.__dict__.keys())[item]
        return self.__dict__[item]
    def __setitem__(self, key, value):
        self.ind_check(key)
        key = list(self.__dict__.keys())[key]
        self.__dict__[key] = value

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= len(list(self.__dict__)) - 2:
            return self.__getitem__(self.count)
        else:
            raise StopIteration


# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# print(pers[3])
# pers[3] = '-10'
# print(pers[4])
# print(len(list(pers.__dict__)))
#
# for i in pers:
#     print(i)