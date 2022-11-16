class PhoneBook:
    def __init__(self):
        self.phone_list = []

    def add_phone(self, phone):
        self.phone_list.append(phone)

    def remove_phone(self, indx):
        del self.phone_list[indx]

    def get_phone_list(self):
        return self.phone_list

class PhoneNumber:
    def __init__(self, number, fio):
        if len(str(number)) == 11 and type(number) == int and str(number).isdigit():
            self.number = number
        if type(fio) == str:
            self.fio = fio


# p = PhoneBook()
# p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
# p.add_phone(PhoneNumber(21345678901, "Панда"))
# print(p.get_phone_list())
