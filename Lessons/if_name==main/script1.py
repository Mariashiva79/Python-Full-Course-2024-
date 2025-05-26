# __name__ contiene dentro el string __main__, por eso cuando se hace if __name__ == "__main__" hay
#                                              que indicar que main es un string.
# Si no se pone el if __name__ == "__main__" y se importa (from script1 import *) al script2, se
#                                            imprime lo que hay en el archivo script1

from script2 import *

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    favorite_drink("kas")
    print("Goodbye!!")

if __name__ == '__main__':
    main()


