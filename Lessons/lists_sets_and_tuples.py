# lists, sets, and tuples 🍎
# Collection = una variable utilizada para que almacene multiples valores.
#    List = [] es ordenable y cambiable, puede contener duplicados
#    Set = {} NO se puede ordenar y es inmutable, se puede añadir o borra. NO puede haber duplicados.
#    Tuple = () es ordenable y cambiable. Puede tener duplicados. Es el más rápido.

# List []
# fruits = ["coconut", "banana", "apple", "banana"]

# print(fruits[2])
# print(len(fruits))
# print("coconut" in fruits) # este devuelve un booleano
# print(dir(fruits))
# print(fruits.count("banana"))

# for fruit in fruits:
#    print(fruit[4]) # imprime la letra en el puesto número 4 de cada palabra
#    print(fruit.upper())
#    print(fruit.lower())

# print(fruits.append("mango"))
# print(fruits.pop()) # imprime el último elemento de la lista en []

# Set {}

# fruits = {"coconut", "banana", "apple", "banana"} # solo imprime una "banana" porque no puede haber duplicados

# print(fruits[2]) # en Set no funciona
# print(len(fruits))
# print("coconut" in fruits) # este devuelve un booleano
# print(dir(fruits))
# print(fruits.count("banana")) # en Set no funciona

# for fruit in fruits:
#    print(fruit[4]) # imprime la letra en el puesto número 4 de cada palabra
#    print(fruit.upper())
#    print(fruit.lower())

# print(fruits.append("mango")) # en Set no funciona
# print(fruits.pop()) # imprime el último elemento de la lista en [], en Set no funciona
# print(fruits.clear())

# Tuple ()

fruits = ("coconut", "banana", "apple", "banana")

# print(fruits)
# print(len(fruits))
# print("coconut" in fruits) # este devuelve un booleano
# print(dir(fruits))
# print(fruits.count("banana"))

for fruit in fruits:
#    print(fruit[4]) # imprime la letra en el puesto número 4 de cada palabra
    print(fruit.upper())
#    print(fruit.lower())

# print(fruits.append("mango")) # en Set no funciona
# print(fruits.pop()) # imprime el último elemento de la lista en [], en Set no funciona y en Tuple tampoco