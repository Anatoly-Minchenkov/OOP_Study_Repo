class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []
        self.current_weight = 0

    def add_thing(self, thing):
        if self.max_weight - self.get_total_weight() >= thing.weight:
            self.__things.append(thing)
            self.current_weight += thing.weight

    def remove_thing(self, indx):
        self.current_weight -= self.__things[indx].weight
        del self.__things[indx]

    def get_total_weight(self):
        return self.current_weight

    @property
    def things(self):
        return self.__things


class Name_descript:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str:
            return setattr(instance, self.name, value)


class Weight_descrip:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if isinstance(value, (float, int)):
            return setattr(instance, self.name, value)


class Thing:
    name = Name_descript()
    weight = Weight_descrip()

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

# bag = Bag(1000)
# bag.add_thing(Thing("Книга по Python", 100))
# bag.add_thing(Thing("Котелок", 500))
# bag.add_thing(Thing("Спички", 20))
# bag.add_thing(Thing("Бумага", 100))
# w = bag.get_total_weight()
# print(w)
# for t in bag.things:
#     print(f"{t.name}: {t.weight}")
