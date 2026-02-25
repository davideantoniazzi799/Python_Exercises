# Data una lista [10, 20, 30], chiedi all’utente un indice e stampa il valore.
# Gestisci:
# - indice fuori range
# - input non numerico

input_list = [10, 20, 30]

try:
    index_request = int(input("Please, provide an index: "))
except ValueError:
    print("The index must be a number.")
except IndexError:
    print("Index out of range. It must be in range [0-2].")
else:
    print(f"You selected the number {input_list[index_request]}")
