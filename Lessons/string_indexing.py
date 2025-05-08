# indexing = acceder a los elementos o a una secuencia usando [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

#print(credit_number[0])
#print(credit_number[:6]) # si no pones start, empieza por el 0
#print(credit_number[5:9])
#print(credit_number[10:])
#print(credit_number[::2])

last_digits = credit_number[-4:] # con el número negativo vas hacia atrás desde el final del index
print(f"XXXX-XXXX-XXXX-{last_digits}")

