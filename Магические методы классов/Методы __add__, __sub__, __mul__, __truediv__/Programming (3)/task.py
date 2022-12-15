class Lib:
    def __init__(self, book_list=[]):
        self.book_list = book_list

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if type(other) == int:
            del self.book_list[other]
            return self
        else:
            self.book_list.remove(other)
            return self
    def __len__(self):
        return len(self.book_list)
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# b1 = Book('Книга Толяна', "Толян", 1998)
# b2 = Book('Книга Таня', "Таня", 2000)
# library = Lib()
# library = library + b1
# library += b2
# # library -= b2
# print(library.book_list)
# print(len(library))