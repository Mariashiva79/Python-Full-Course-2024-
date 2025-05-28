# super() = Función utilizada en un clase hijo para llamar métodos desde
# la clase parent(superclass)

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"This is {self.color} and {'is filled' if self.is_filled else 'is not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        Shape.__init__(self, color, is_filled)
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"The area of the circle is {3.14 * self.radius * self.radius}cm2")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        Shape.__init__(self, color, is_filled)
        self.width = width
    def describe(self):
        super().describe()
        print(f"The area of the square is {self.width * self.width}cm2")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        Shape.__init__(self, color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        super().describe()
        print(f"The area of the triangle is {self.width * self.height / 2}cm2")



circle = Circle("Red", False, 20)
square = Square("Blue", True, 10)
triangle = Triangle("Yellow", False, 7, 8)


circle.describe()
square.describe()
triangle.describe()