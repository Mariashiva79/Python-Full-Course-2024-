# La fórmula es c = raiz cuadrada(a al cuadrado + b al cuadrado)
import math

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The area of the triangle is {round (c, 2)}")
