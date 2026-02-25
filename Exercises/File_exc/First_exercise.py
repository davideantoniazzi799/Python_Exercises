#Scrivere un programma che:
# 1 - Apre un file chiamato testo.txt
# 2 - Legge tutto il contenuto
# 3 - Lo stampa sullo schermo

"""
file = open("testo.txt")
content = file.read()
print(content)
file.close()
"""

with open("testo.txt") as file:
    content = file.read()
    print(content)