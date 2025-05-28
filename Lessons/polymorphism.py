# Polymorphism es poly (muchas) morphism (formas)

from abc import ABC, abstractmethod

# Esta línea de código importa la clase `ABC` (Abstract Base Class) del
# módulo `abc` (Abstract Base Classes).
# Las clases abstractas en Python son una forma de definir una clase base que:
#       1. No puede ser instanciada directamente
#       2. Define una interfaz común que las clases hijas deben implementar

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

class Triangle(Shape):
    def __init__(self, base, heigh):
        self.base = base
        self.heigh = heigh
    def area(self):
        return self.base * self.heigh * 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)


shapes = [Circle(5), Square(6), Triangle(8, 5), Pizza("Pepperoni", 6)]

for shape in shapes:
    print(f"{shape.area()}cm2")