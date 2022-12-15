class TableValues:
    def __init__(self, rows = 0, cols = 0, type_data = int):
        self.rows =rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]

    def check_index(self, ind):
        if type(ind[0]) != int or type(ind[1]) != int or ind[0] > self.rows - 1 or ind[1] > self.cols - 1:
            raise IndexError('неверный индекс')

    def check_value(self, value):
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')

    def __setitem__(self, key, value):
        self.check_index(key)
        self.check_value(value)
        self.table[key[0]][key[1]].data = value

    def __getitem__(self, item):
        self.check_index(item)
        return self.table[item[0]][item[1]].data

    def __iter__(self):
        for row in self.table:
            yield (x.data for x in row)

class Cell:
    def __init__(self, data = 0):
        self.data = data
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data


# t = TableValues(2, 5)
# print(t.table)
# t[1, 1] = 23
# print(t.table[1][1].data)
# a = t[1, 1]
# print(a)
# for row in t:
#     for value in row:
#         print(value)