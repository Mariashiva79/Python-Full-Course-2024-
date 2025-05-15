# Se pone un key al argumento a la hora de llamar a la función.
# Ejemplo de key: end=" " , que usamos para poner en horizontal lo que imprimimos.

# def greeting_card(greetings, title, first, last):
#    return f"{greetings} {title}{first} {last}"

# print(greeting_card("Hello", "Mrs.", "Jane", "Pit"))
# print(greeting_card("Hello", title="Mrs.", first="Jane", last="Pit")) # el primero debe ser posicional
# print(greeting_card("Hello", first="Jane", last="Pit", title="Mrs.")) # no importa el orden

# for x in range(1, 11):
#     print(x, end=" ")

def phone_number(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

my_phone = phone_number(1, area=240, first=125, last=5698 )
print(my_phone)
print(1, 2, 3, 4, 5, sep="-")