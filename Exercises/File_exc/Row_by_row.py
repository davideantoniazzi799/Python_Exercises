#Scrivi un programma che:
# 1 - Apre il file poem.txt
# 2 - Legge una riga alla volta
# 3 - Stampa ogni riga senza creare righe vuote extra

with open("poem.txt") as file:
    for line in file:
        print(line, end="")