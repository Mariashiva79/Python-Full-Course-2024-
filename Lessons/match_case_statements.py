# Match-case stament (switch): Es una alternativa a los elif, queda más limpio

# def days_week(day):
#     if day == 1:
#         print("It´s Monday")
#     elif day == 2:
#         print("It´s Tuesday")
#     elif day == 3:
#         print("It´s wednesday")
#     elif day == 4:
#         print("It´s Thursday")
#     elif day == 5:
#         print("It´s Friday")
#     elif day == 6:
#         print("It´s Saturday")
#     elif day == 7:
#         print("It´s Sunday")
#     else:
#         print("It´s invalid day")
#
# days_week(7)

# def days_week(day):
#     match day:
#         case 1:
#             print("It´s Monday")
#         case 2:
#             print("It´s Tuesday")
#         case 3:
#             print("It´s wednesday")
#         case 4:
#             print("It´s Thursday")
#         case 5:
#             print("It´s Friday")
#         case 6:
#             print("It´s Saturday")
#         case 7:
#             print("It´s Sunday")
#         case _:
#             print("It´s invalid day")
#
# days_week(5)


# def days_weekend(day):
#     match day:
#         case "Monday":
#             return False
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thursday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return True
#         case "Sunday":
#             return True
#         case _:
#             print("It´s invalid day")
#
# print(days_weekend("Sunday"))

def days_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:
            return "It´s invalid day"

print(days_weekend("pizza"))