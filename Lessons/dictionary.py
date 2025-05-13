# dictionary = colección de parejas de {clave: valor}
#              Es ordenable y se puede cambiar. No puede haber duplicados.

capitals = {"USA" : "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India")) # Imprime el valor de la key que le proporcionas
# capitals.update({"England": "London"}) # Añade una capital
# capitals.update({"China": "Pekin"}) # Actualiza el valor de la llave si ya existe
# capitals.pop("China") # Borra China
# capitals.popitem() # Borra el último elemento
# capitals.clear() # Borra el contenido

# keys = capitals.keys() # Saca las keys
# for key in capitals.keys():
#   print(key)

# value = capitals.values() # Saca los valores
# for value in capitals.values():
#  print(value)

items = capitals.items() # Saca todos los items
for key, value in capitals.items():
    print(f"{key}: {value}")
