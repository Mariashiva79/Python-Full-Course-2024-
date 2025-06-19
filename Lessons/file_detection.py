# Python file detection: es un boleano que te dice si existe un archivo o carpeta

import os # hay que importar esto

file_path = "class_methods.py"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")

