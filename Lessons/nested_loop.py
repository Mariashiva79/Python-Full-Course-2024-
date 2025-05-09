# un loop puede ir dentro de otro loop

rows = int(input("Enter # of rows: "))
columns = int(input("Enter # of columns: "))
symbol = (input("Enter symbol: "))

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
