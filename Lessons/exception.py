# exception = Para que un evento no interrumpa el flujo de un programa
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally
#             Exception (incluye todas las excepciones, pero no especifica qué ha fallado)

# number = int(input("Enter a number: "))
# print(1 / number)

# Si no ponemos excepciones el programa se romperá si el usuario mete un 0
# escribe un string o un valor erroneo, etc. por esto tenemos que manejar los
# errores de manera controlada

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can´t divide by zero IDIOT!!") # De esta forma no rompe el flujo, sino que saca este mensaje
except ValueError:
    print("Enter only numbers, please")
except Exception:
    print("Something went wrong!")
finally:    # finally se ejecuta siempre, haya una excepción o no
    print("Do something to clean")