# Usando lo stesso DataFrame:
# Seleziona solo le persone con:
# - age > 26
# 
# Seleziona solo le persone con:
# - score >= 88
# 
# Stampa i risultati

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "score": [85, 90, 88]
}

df = pd.DataFrame(data)

print("People older than 26:", df[df["age"] > 26])
print("People that scored at least 88:", df[df["score"] >= 88])