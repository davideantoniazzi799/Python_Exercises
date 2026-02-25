#Scrivi un programma che:
# 1 - Apre story.txt
# 2 - Legge tutto il contenuto
# 3 - Conta quante parole totali ci sono
# 4 - Stampa: Il file contiene X parole.

with open("story.txt") as file:
    data = file.read()
    w = data.split()
    print(f"File has {len(w)} words.")