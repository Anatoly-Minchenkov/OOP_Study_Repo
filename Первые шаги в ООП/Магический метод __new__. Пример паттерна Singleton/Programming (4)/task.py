class Factory:
    def build_sequence(self):
        self.ls = []
        return self.ls
    def build_number(self, item):
        self.item = item
        return float(self.item)
        

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())