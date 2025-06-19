# Para escribir en archivos (.txt, .json, .csv)
import json
import csv
from os import write

# employees=["Patrick", "Eugene", "Carla", "Rosa"]
# employee= {
#    "name": "Patrick",
#    "age": 39,
#    "job": "cook",
# }

employee =[["Name", "Age", "Job"],
           ["Martha", 34, "cook"],
           ["Bob", 36, "doctor"],
           ["Joe", 42, "actor"]]

txt_data = "I can write files with Python"

file_path = "output.csv" # se puede poner así y se incluye en el proyecto
# o indicarle la ruta
# file_path = "/home/mjimenez/output.txt"

# try:
#    with open(file=file_path, mode="a") as file:  # la w es de write, si pones x, r, a, no es para escribir.
#        for employee in employees:
#            file.write(f"\n" + employee)
#        print(f"The file '{file_path}' was created")
# except FileExistsError:
#    print("The file already exist")

# with open(file_path, mode="w") as file:
#    json.dump(employee, file, indent=4) # esto es para ver el json mejor, le pone espacios
#    print(f"The file '{file_path}' was created")

try:
    with open(file=file_path, mode="w") as file:
        write = csv.writer(file)
        for row in employee:
            write.writerow(row)
        print(f"The csv file '{file_path}' was created")
except FileExistsError:
    print("The file already exist")

