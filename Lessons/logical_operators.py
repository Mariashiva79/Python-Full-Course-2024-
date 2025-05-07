# los operadores son para evaluar multiples condiciones (or, and, not(invierte la condición))

# or

temp = 30
is_raining = True

if temp > 35 or temp < 10 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# and
temp = -6
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("Is is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is SUNNY outside")
    print("But is cold!")
else:
    print("Error")
