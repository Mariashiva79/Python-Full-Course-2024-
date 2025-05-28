# Inheritance = Una clase puede heredar los métodos y atributos de otra clase
#               Así se puede reusar código y queda más limpio
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEAW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Uri")
cat = Cat("Zeiss")
mouse = Mouse("Mr.Txuri")

dog.speak()
cat.speak()
print(f"{mouse.name} says: "), mouse.speak()


