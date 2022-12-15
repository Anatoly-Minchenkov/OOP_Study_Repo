class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        return setattr(instance, self.name, value)

class CellInteger:
    value = IntegerValue()
    def __init__(self, start_value = 0):
        self.value = start_value

class TableValues:

    rows = IntegerValue()
    cols = IntegerValue
    def __init__(self, row, cols, cell = None):
        if not cell:
            raise ValueError('параметр cell не указан')

        self.rows = row
        self.cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for j in range(row))


    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value