class Shop:
    def __init__(self, name):
        self.name = name
        self.goods =[]

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)
class Product:
    _id = 1
    def __init__(self, name, weight, price, id = 1):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = self._id
        Product._id +=1
    def __setattr__(self, key, value):
        if key == 'name':
            if type(value) == str:
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in ('weight', 'price'):
            if isinstance(value, (int, float)) and value > 0:
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'id':
            if isinstance(value, (int)):
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")


    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)

# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price},{p.id}")