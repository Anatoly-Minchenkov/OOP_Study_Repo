import string
from random import choice
class EmailValidator:

    CANUSED = string.ascii_letters + string.digits + '@._'
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        return choice(['tolik', 'asfasf', 'asgwgwg', 'segsegs', 'rgwrgwgw']) + '@gmail.com'
    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email) is False:
            return False
        check = email.split('@')
        if len(check) == 2 and len(check[0]) <= 100 and len(check[1]) <=50 and '.' in check[1]:
            for i in range(len(email)):
                if email[i] not in cls.CANUSED:
                    return False
                if email[i] == '.':
                    if email[i-1] == '.' or email[i+1] == '.':
                        return False
            return True
        else:
            return False


    @staticmethod
    def __is_email_str(email):
        return type(email) is str

#
# assert EmailValidator.check_email('sc..lib@list.ru') == False
# assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
# assert EmailValidator.check_email('name.surname@mail.com') == True
# assert EmailValidator.check_email(1342) == False
# assert EmailValidator.check_email('a+a@m.c') == False
# # assert EmailValidator.check_email('aabda..kkk@m.c') == False
# assert EmailValidator.check_email('aaaa@bbb..cc') == False
# assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
# assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
# assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
# assert EmailValidator.check_email('name.surnamemail.com') == False
# assert EmailValidator.check_email('name@mail') == False
#
# res = EmailValidator.get_random_email()
# print(res)