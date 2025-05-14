# En las funciones se pueden poder argumentos por defecto, así reducimos el número de
# argumentos al invocarla

# def net_price(list_prize, discount= 0.15, tax= 0.21):
#    return list_prize * (1 - discount) * (1 + tax)

# print(net_price(500)) # los demás argumentos tienen valores por defecto
# print(net_price(500, 0)) # Aumque tenga por defecto, lo calcula con lo que le doy

import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!!")

count(10)