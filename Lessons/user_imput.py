# input() es para que el usuario meta un input, devuelve un string

name = input("What is your name?: ")
age = int(input("How old are you?: ")) # le decimos que sea un integer para que devuelva un número

age += 1

print(f"Your name is {name}")
print(f"You are {age} years old")
print("HAPPY BIRTHDAY!!")
