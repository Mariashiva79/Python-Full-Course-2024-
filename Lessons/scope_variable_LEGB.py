# variable scope = es cuando la variable es visible y accesible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# (este es el orden en que hace "caso" al valor que le damos a una variable (LEGB))

from math import e

# def func1():    # si en esta función pusiera print(b) daría error porque no puede acceder a b
#     a = 1
#     print(a)
#
# def func2():    # cada función ve solo lo que tiene dentro.
#     b = 2
#     print(b)
#
# func1()
# func2()

# def func1():
#     x = 1
#     def func2(): # aquí estamos utilizando "Local" para imprimir x
#         x = 2
#         print(x)
#     func2()
#
# func1()

# def func1():
#     x = 1
#     def func2(): # aquí estamos utilizando "Enclosed" para imprimir x
#         print(x)
#     func2()
#
# func1()

# def func1():
#     x = 1
#     print(x)
#
# def func2():
#     x = 2
#     print(x)
#
# x = 3  # aunque le demos un nuevo valor a x fuera de las funciones, primero utiliza la "local"
#
# func1()
# func2()

# def func1():
#     print(x)
#
# def func2():
#     print(x)
#
# x = 3  # Ahora utiliza este valor porque en local no hemos determinado otro.
#
# func1()
# func2()

def func1():
    print(e)

e = 3  # Built-in, ahora elige el 3 aunque esté declarado antes la "e" porque primero elige lo local

func1()