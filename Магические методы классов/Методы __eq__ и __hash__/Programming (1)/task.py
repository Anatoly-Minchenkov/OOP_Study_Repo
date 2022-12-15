import sys

class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)

# считывание списка из входного потока
lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

shop_items = {}
for i in lst_in:
    key = ShopItem(i.split(':')[0], i.split()[-2], i.split()[-1])
    shop_items.setdefault(key, [key, 0])[1] += 1
    # print(shop_items)

