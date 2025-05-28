# class variables 🎓, las clases pueden tener variables que afectan a todos
#                       sus atributos, se ponen fuera de la función

class Cat:
    adopt_center = "Ikatz" # estas variables afectan a todos los atributos, cat1, cat2, etc o Cat
    num_of_cats = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Cat.num_of_cats += 1

cat1 = Cat("Mitxi", 3)
cat2 = Cat("Zeiss", 7)
cat3 = Cat("Garfield", 3)
cat4 = Cat("Tom", 2)
cat5 = Cat("Silvestre", 6)


print(cat1.name)
print(f"{cat2.name} has {cat2.age} years old")
print(cat3.num_of_cats)
print(f"\nIn {Cat.adopt_center} there are {Cat.num_of_cats} cats in adoption")


