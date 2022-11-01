

'''
Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже существует, то
новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать); если связка eng-rus уже
существует, то второй раз ее добавлять не нужно, например:  add('go', 'идти'), add('go', 'идти');
remove(self, eng) - для удаления связки по указанному английскому слову;
translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов, соответствующих
 переводу английского слова, даже если в списке всего одно слово).
'''


class Translator:

    def add(self, eng, rus):
        if 'd' not in self.__dict__:
            self.d = {}
        if eng in self.d and rus not in self.d[eng]:
            self.d[eng] = self.d.get(eng, rus) + f' {rus}'
        elif eng not in self.d:
            self.d[eng] = rus

    def remove(self, eng):
        del self.d[eng]

    def translate(self, eng):
        return list(self.d[eng].split())


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove('car')
print(*tr.translate('go'))



