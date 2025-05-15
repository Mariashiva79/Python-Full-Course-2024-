# *args= cuando pone el asterisco es porque admite cambio en el número de
# argumentos que le pasas a la función al invocarla.

# def shopping_list(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# shopping_list("bread", "coke", "meat")

# **kwargs= son keyword arguments que puedes modificar y elegir la cantidad de argumentos

# def shipping_label(**kwargs):
#     for keys, values in kwargs.items():
#         print(f"{keys}: {values}")
#
#
# shipping_label(city="Pamplona",
#                street="fake-one, 4",
#                cp="31000",
#                country="Spain")

# se pueden utilizar juntos en una misma función, debe ir primero *args porque es posicional

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "street" in kwargs:
        print(f"{kwargs.get("street")} "
              f"\n{kwargs.get("city")} "
              f"\n{kwargs.get("cp")} "
              f"\n{kwargs.get("country")}")
    elif "road" in kwargs:
        print(f"{kwargs.get("road")} "
              f"\n{kwargs.get("city")} "
              f"\n{kwargs.get("cp")} "
              f"\n{kwargs.get("country")}")



shipping_label("María", "Jiménez", "Mrs.",
               city="Pamplona",
               road="fake, s/n",
               # street="fake-one, 4",
               cp="31000",
               country="Spain")

