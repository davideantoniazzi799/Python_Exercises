# Usando il DataFrame dell’esercizio 2:
# Seleziona e stampa:
# - solo la colonna "name"
# - le colonne "name" e "score"
# 
# Stampa:
# - la prima riga usando .iloc
# - la riga con indice 1 usando .loc

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "score": [85, 90, 88]
}

df = pd.DataFrame(data)

print("Column NAME:", df["name"])
print("Columns NAME and SCORE:", df[["name", "score"]])

print("First row:", df.iloc[0])
print("Row with index one:", df.loc[1])