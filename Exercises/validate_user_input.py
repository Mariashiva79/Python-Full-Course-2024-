# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

user_name = input("Enter your username: ")

is_correct = True

if len(user_name) > 12:
    print("The username is too long.")
    is_correct = False
if user_name.find(" ") != -1: # .find devuelve un número que es el índice donde se
    # encuentra el primer espacio que detecta.
    print("The username must not contain spaces.")
    is_correct = False
if user_name.isdigit():
    print("The username must not contain digits.")
    is_correct = False
if is_correct:
    print("Your user name is correct")
