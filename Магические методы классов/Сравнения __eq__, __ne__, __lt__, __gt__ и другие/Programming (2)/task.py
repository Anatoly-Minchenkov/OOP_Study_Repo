# эти строчки не менять
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

new_stich = []

for i in stich:
    a = []
    for j in i.split():
        j = j.strip('–?!,.;')
        if j:
            a.append(j)
    new_stich.append(a)
#
class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

lst_text = []
lst_text.append(StringText(new_stich[0]))
lst_text.append(StringText(new_stich[1]))
lst_text.append(StringText(new_stich[2]))
lst_text.append(StringText(new_stich[3]))
lst_text.append(StringText(new_stich[4]))
lst_text.append(StringText(new_stich[5]))
lst_text.append(StringText(new_stich[6]))

lst_text_sorted = sorted(lst_text, key = lambda x: len(x), reverse=True)
lst_text_sorted = [' '.join(x.lst_words) for x in lst_text_sorted]
# print(lst_text_sorted)
