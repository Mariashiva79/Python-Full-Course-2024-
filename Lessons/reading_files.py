# Python reading files (.txt, .json, .csv)

import json
import csv
from xml.etree.ElementTree import indent

file_path = "input.json"

# try:
#   with open(file=file_path, mode="r") as file:
#       content = file.read()
#       print(content)
# except FileExistsError:
#   print("Than file already exist")

try:
    with open(file=file_path, mode="r") as file:
        content = json.load(file)
        print(content)
except FileExistsError:
    print("Than file already exist")

try:
    with open(file=file_path, mode="r") as file:
        content = json.load(file)
        print(content)
except FileExistsError:
    print("Than file already exist")