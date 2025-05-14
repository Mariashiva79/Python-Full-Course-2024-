# function = A block of reusable code
#            place () after function name to invoke it

# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!!")
#     print(f"You are {age} years old!")
#     print("Happy birthday!!")
#     print()
#
# happy_birthday("Naia",16)
# happy_birthday("Anne", 13)


# def display_invoice(username, amount, due_date):
#    print(f"The invoice of {username}")
#    print(f"Total amount ${amount:.2f}, is due: {due_date}")

# display_invoice("UPNA", 350.80, "01/02")

# def add(x, y):
#    z = x + y
#    return z

# def subtract(x, y):
#    z = x - y
#    return z

# def multply(x, y):
#    z = x * y
#    return z

# def divide(x, y):
#    z = x / y
#    return z

# print(add(6,7))
# print(subtract(6,7))
# print(multply(6,7))
# print(divide(6,7))

def create_name(first, last):
   first = first.capitalize()
   last = last.capitalize()
   return first + " " + last

full_name = create_name("maria", "jiménez")
print(full_name)

