# Python calculator

import math

print("Python Calculator!!")

num1 = float(input("Enter first number: "))

operator = input("Enter an operator (+ - * /): ")

num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(f"The result is {round(result, 3)}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is {round(result, 3)}")
elif operator == "*":
    result = num1 * num2
    print(f"The result is {round(result, 3)}")
elif operator == "/":
    result = num1 / num2
    print(f"The result is {round(result, 3)}")
else:
    print("Ups!! Something went wrong!!")



