#Apri un file e leggi il contenuto.
# - gestisci il caso in cui il file non esista
# - usa finally per stampare: "Operazione terminata"
import traceback

name_file = "file.txt"

try:
    with open(name_file) as file_input:
        data = file_input.read()
except FileNotFoundError:
    print(f"Error: {name_file} not found.")
    traceback.print_exc()
else:
    print(data)
finally:
    print("Operation terminated.")