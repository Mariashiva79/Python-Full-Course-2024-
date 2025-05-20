# Se importan módulos que ya existen, matemáticos por ejemplo,
# que tienen las funciones integradas

# import math
#
# print(math.pi)

# print(help("modules")) # imprime un listado de módulos

# print(help("math")) # imprime lo que contiene el módulo math

# import math as m
#
# from math import pi
#
# print(m.e)
# print(pi)

# O se crean módulos en otros archivos y se importan

import example_modules as em

result = em.square(3)
print(result)

print(em.pi)