class InputDigits:

    def __init__(self, func):
        self.func = func
    def __call__(self, lst, *args, **kwargs):
        nlst = list(map(int, lst.split()))
        return self.func(nlst)


@InputDigits
def input_dg(list):
    return list

res = input_dg(input())

