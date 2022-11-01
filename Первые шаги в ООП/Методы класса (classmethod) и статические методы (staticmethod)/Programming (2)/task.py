from string import ascii_lowercase, digits
    
class CardCheck:
    
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    
    @classmethod
    def check_card_number(cls, number, lengh = 4, spliter = '-'):
        if len(number.split(spliter)) == lengh:
            for i in number.split(spliter):
                if len(i) == lengh:
                    for j in i:
                        if not j.isdigit():
                            return False
                else:
                    return False
        else:
            return False
        return True
        
    
    @classmethod
    def check_name(cls, name, lengh = 2, spliter = ' '):
        if len(name.split(spliter)) == 2:
            for i in name.split(spliter):
                if len(i):
                    for j in i:
                        if not j in cls.CHARS_FOR_NAME:
                            return False
                else:
                    return False
        else:
            return False
        return True
        



