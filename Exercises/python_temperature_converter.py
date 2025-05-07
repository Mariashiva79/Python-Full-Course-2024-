# Pasa de grados Cº a grados Fº

print("Welcome to the temperature converter!!")

response = input("You need converted to (ºC or ºF): ")

if response == "ºF":
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{round(celsius, 2)}ºC are {round(fahrenheit, 2)}ºF")
elif response == "ºC":
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{round(fahrenheit, 2)}ºF are {round(celsius, 2)}ºC")
else:
    print("Ups!! Something went wrong!!")

print("Thank you for using our temperature converter!!")