#Apri un file data.txt e leggilo.
# - se il file non esiste → messaggio di errore
# - se tutto va bene → stampa il contenuto usando else

try:
    with open("data.txt") as file_input:
        data = file_input.read()
except FileNotFoundError:
    print("File does not exist.")
else:
    print(data)