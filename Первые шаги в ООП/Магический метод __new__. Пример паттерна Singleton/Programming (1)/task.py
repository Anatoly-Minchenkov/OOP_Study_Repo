class SingletonFive:
    __instance = None
    __count = 0

    def __new__(cls, name, *args, **kwargs):
        cls.name = name
        if int(cls.name) <= 4:
            cls.__instance = super().__new__(cls)
        return cls.__instance


objs = [SingletonFive(str(n)) for n in range(10)]