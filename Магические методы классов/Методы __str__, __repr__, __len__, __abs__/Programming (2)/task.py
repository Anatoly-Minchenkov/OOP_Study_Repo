class WordString:
    def __init__(self, string = ''):
        self.string = string
    def __len__(self):
        return len(self.string.split())

    def __call__(self, indx):
        if indx < len(self):
            return self._string.split()[indx]
    @property
    def string(self):
        return self._string
    @string.setter
    def string(self, args):
        self._string = args

# words = WordString('Курс по Python    ООП от  Сергея Балакирева')
# words.string = "Курс по Python    ООП от  Сергея Балакирева"
# n = len(words)
# print(n)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")