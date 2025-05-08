# format specifiers es para añadir a la variable un formato concreto al llamarlo con f{} (:+, :.2f, :<, :>,
# o varios juntos (:+,>,.5f, ,30)

price1 = 3000.14159
price2 = -9520.45
price3 = 12000.34

#print(f"The price1 is ${price1:.2f}") # siendo el ": .2f" el número de decimales que queremos ver
#print(f"The price2 is ${price2:.2f}")
#print(f"The price3 is ${price3:.2f}")

print(f"The price1 is ${price1:10}") # siendo el número 10 el número de espacios que va a ocupar desde los :
print(f"The price2 is ${price2:010}") # rellena con 0 los espacios sin caracteres
print(f"The price3 is ${price3:<10}") # lo justifica a la izquierda

print(f"The price1 is ${price1:^10}") # centra el numero en el espacio que tiene de 10 espacios
print(f"The price2 is ${price2:>10}") # lo justifica o alinea a la derecha
print(f"The price3 is ${price3:<10}") # lo justifica o alinea a la izquierda

print(f"The price1 is ${price1:+}") # para que muestre el signo
print(f"The price2 is ${price2: }") # un espacio para dejar un sitio para el signo, en positivos " ", en negativos "-"
print(f"The price3 is ${price3:,}") # para que ponga , a los millares

print(f"The price1 is ${price1:+,.2f}") # se pueden juntar varios (con signo, 2 decimales y coma en millares)
print(f"The price2 is ${price2:>+}")
print(f"The price3 is ${price3:,.0f}")