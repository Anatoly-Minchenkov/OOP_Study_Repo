class RadiusVector:
    def __init__(self, *args):
        self.coords = [i for i in args]

    def __getitem__(self, item):
        if isinstance(item, slice):
            return tuple(self.coords[item])
        else:
            return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value


