# multiple inheritance 🐟 una clase puede heredar de varias clases C(A,B)
#                         y también puede haber más niveles un superparent, parent, child


class Clothes:
    def __init__(self, name):
        self.name = name

class Summer(Clothes):
    def summer_time(self):
        print(f"This {self.name} is a summer clothing")

class Winter(Clothes):
    def winter_time(self):
        print(f"This {self.name} is a winter clothing")

class Sweater(Summer, Winter):
    pass

class Trouser(Summer, Winter):
    pass

class Bikini(Summer):
    pass

class Coat(Winter):
    pass

coat1 = Coat("Green_coat")
trouser1 = Trouser("short_trouser")
bikini1 = Bikini("Blue_bikini")

coat1.winter_time()
trouser1.summer_time()
bikini1.summer_time()
