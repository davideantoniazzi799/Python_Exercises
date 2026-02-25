#Genera una password casuale composta da 8 caratteri (usa random).

import random

list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
password = ""

for i in range(8):
    letter = random.choice(list_letters)
    password += letter

print(f"Your password is: {password}")