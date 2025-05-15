# list comprehension = Es para crear listas en python
# de manera más concisa y fácil que las listas tradicionales
# [expression for value in iterable if condition] FORMULA para hacer las listas

numbers = [-1, 2, -3, 4, -5, 6, -7, 8]

# doubles = [x * 2 for x in range(1, 11)]
# triples = [x * 3 for x in range(1, 11)]
# print(triples)

# fruits = ["banana", "orange", "apple", "watermelon"]
# fruits_capitalize = [fruit.upper() for fruit in fruits]
# print(fruits_capitalize)

positive_num = [num for num in numbers if num >= 0]
negative_num = [num for num in numbers if num <= 0]
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 == 1]

print(odd_num)