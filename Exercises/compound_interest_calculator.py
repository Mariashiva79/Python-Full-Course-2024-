# ⭐ compound interest calculator 💵 la formula es A = P(1 + r/n)ᵗ
# A = final amount
# P = initial principal balance
# r = inerest rate
# t = number of time periods elapsed

principal = 0
time = 0
rate = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("The amount can´t be a negative number or zero.")

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("The rate can´t be a negative number or zero.")

while time <= 0:
    time = int(input("Enter the time in months: "))
    if time <= 0:
        print("The time can´t be a negative number or zero.")

amount = (principal * (1 + rate / 100))**time # en el tutorial lo pone diferente = principal * pow((1 + rate / 100), time)
print(f"With principal ${principal:.2f}, a rate of {rate:.2f}% and {time} month of time, the final amount is: ${amount:.2f}")