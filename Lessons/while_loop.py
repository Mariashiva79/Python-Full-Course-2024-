# while loop = se ejecuta algo WHILE alguna condición se cumpla

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") # IMPORTANTE darle una salida al loop, sino será un loop infinito

print(f"Hello {name}!!")

food = input("Enter your favorite food (q to quit): ")

while not food == "q": # mientras NO se ponga "q" no sale del loop
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print("Invalid number")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")
