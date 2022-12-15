class Model:
    def query(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def __str__(self):
        if self.__dict__:
            mod = 'Model: '
            a = []

            for key, value in self.__dict__.items():
                a.append(f'{key} = {value}')

            return mod + ', '.join(a)
        else:
            return 'Model'
#
# model = Model()
# model.query(id=1, fio='Sergey', old=33)
# print(model)