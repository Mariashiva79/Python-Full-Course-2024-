# para comprobar si un valor o variable está en una secuencia
# (string, list, tuple, set, or dictionary)
# 1. in
# 2. not in

# word = "HORSE"
# letter = input("Enter the letter: ").upper()
# if letter in word:
#     print(f"{letter} is in secret word")
# else:
#     print(f"{letter} is not in word")

# students = {"Sandy", "Jane", "Liz", "Monica"}
#
# student = input("Enter the name of a student: ")
#
# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} is not a student")

grades = {"Sandy": "A",
         "Jane": "B",
         "Liz": "C",
         "Monica": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student} have grade: {grades[student]}")
else:
    print(f"{student} is not a student")