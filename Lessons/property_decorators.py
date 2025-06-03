# @property sirve para añadir algo a los atributos de una clase, también hay
#           para escribir más métodos para el atributo o borrar

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width < 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height < 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width is delete")

    @height.deleter
    def height(self):
        del self._height
        print("Height is delete")




rectangle = Rectangle(3, 8)


print(rectangle.width)
print(rectangle.height)

del rectangle.height
del rectangle.width