# Python weight converter

weight = float(input("Would you like to know your weight in pounds or kilograms?! Enter your weight: "))

unit = input("Choose your unit (K or L): ")

if unit == "K":
    result = weight * 2.20462
    unit = "kg"
    print(f"Your weight is {round(result, 3)}{unit}")
elif unit == "L":
    result = weight / 2.20462
    unit = "lbs"
    print(f"Your weight is {round(result, 3)}{unit}")
else:
    print("Ups!! Something went wrong!! Enter a valid number and/or unit (K or L)")
