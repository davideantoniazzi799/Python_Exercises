# 1. Crea un DataFrame a partire da questo dizionario:
# data = {
#    "name": ["Alice", "Bob", "Charlie"],
#    "age": [25, 30, 35],
#    "score": [85, 90, 88]
#}
# 
# Stampa:
# - il DataFrame
# - le colonne
# - la shape

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "score": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)
print("Columns:",df.columns)
print("Data shape:", df.shape)