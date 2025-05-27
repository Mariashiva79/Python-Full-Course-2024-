#  encryption program 🔐 utilizando dos bibliotecas, random y string

import random
import string

chars = " " + string.digits + string.punctuation + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key:   {key}")

# ENCRYPTING

original_message = input("Enter a message to encrypt: ")
encrypt_message = ""

for letter in original_message:
    index = chars.index(letter) # esto busca el lugar de cada letra del mensaje original en chars
    encrypt_message += key[index]
    # aquí dice que pase por key y coga los carácteres situados en el número que marque el index y los añada

print(f"The encrypt message: {encrypt_message}")

# DECRYPTING

encrypt_message  = input("Enter a message to decrypt: ")
original_message= ""

for letter in encrypt_message:
    index = key.index(letter) # esto busca el lugar de cada letra del mensaje en key
    original_message += chars[index]
    # aquí dice que pase por chars y coga los carácteres situados en el número que marque el index y los añada

print(f"The original message: {original_message}")
