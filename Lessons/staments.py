# If= hace algo solo si la condición es True,
# else= hace algo más

a = float(input("Enter the first number: "))
b = float(input("Enter the second number:"))

if a > b:
    print("The first number is greater than the second number")
elif a == b:
    print("The first number is equal to the second number")
else:
    print("The second number is greater than the first number")


response = input("Whould you like pizza (Y/N)?: ")

if response == "Y":
    print("Great, here's your pizza")
else:
    print("Okay, no pizza for you")