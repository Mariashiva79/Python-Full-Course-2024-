# 2D collections ⬜ Hacer listas de listas, [[], [], []]
# por ejemplo para realizar un teclado de teléfono:

num_rows = ((1,2,3),
            (4,5,6),
            (7,8,9),
            ("*", 0, "#"))

for row in num_rows:
    for num in row:
        print(num, end=" ")
    print()