#Simula una risorsa (es: file o connessione):
# - stampa "Risorsa aperta"
# - genera volutamente un errore
# - usa finally per stampare "Risorsa chiusa"

import traceback

name_file = "file.txt"

try:
    print("Source opened.")
    with open(name_file) as file_input:
        data = file_input.read()
except FileNotFoundError:
    print(f"Error: {name_file} not found.")
    traceback.print_exc()
else:
    print(data)
finally:
    print("Source closed.")