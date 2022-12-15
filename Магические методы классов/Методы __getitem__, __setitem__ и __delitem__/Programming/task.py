class Record:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getitem__(self, item):
        if not isinstance(item, int) or item >= len(self.__dict__):
            raise IndexError('неверный индекс поля')

        return getattr(self, list(self.__dict__)[item])


    def __setitem__(self, key, value):
        if not isinstance(key, int) or key >= len(self.__dict__):
            raise IndexError('неверный индекс поля')
        setattr(self, list(self.__dict__)[key], value)
#
# r = Record(pk=1, title='Python ООП', author='Балакирев')
# print(r.__dict__)
# print(r[2])
# r[2] = 'ТОля'
# print(r[2])