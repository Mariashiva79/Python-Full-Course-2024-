# Programa para exponer un menú al usuario, que elija la comida y calcular el total, utilizando el diccionario.

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("****** MENU *******")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("*******************")

while True:
    food = input(f"Choose your food (q to quit): ").lower()
    if food == "q":
            break
    elif food in menu.keys():
        cart.append(food)
#    elif menu.get(food) is not None:
#            cart.append(food)
    else:
        print(f"{food} is not in the menu")
for food in cart:
        total += menu.get(food)

print("\n****** TICKET *******")

for item in cart:
    print(f"{item:10}: ${menu.get(item):.2f}")
print("------------------")
print(f"{"TOTAL":10}: ${total:.2f}")

print("**********************")
