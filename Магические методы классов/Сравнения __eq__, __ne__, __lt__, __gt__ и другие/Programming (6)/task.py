class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.m = self.ro*self.volume

    def __eq__(self, other):
        if type(other) in (int, float):
            return self.m == other
        else:
            return self.m == other.m

    def __lt__(self, other):
        if type(other) in (int, float):
            return self.m < other
        else:
            return self.m < other.m
