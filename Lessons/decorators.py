# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

def add_chocolate(func):
    def wrapper():
        print("*You add chocolate 🍫*")
        func()
    return wrapper


def add_sprinkles(func):
    def wrapper():
        print("*You add sprinkles 🧁*")
        func()
    return wrapper

@add_sprinkles
@add_chocolate
def get_ice_cream():
    print("Here is your ice cream 🍦")

get_ice_cream()

