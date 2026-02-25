# Sempre con lo stesso DataFrame:
# Calcola e stampa:
# - la media della colonna "age"
# - il valore massimo della colonna "score"
# 
# Crea una nuova colonna "passed" che vale:
# - True se score >= 88
# - False altrimenti
# 
# Stampa il DataFrame finale

import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "score": [85, 90, 88]
}

df = pd.DataFrame(data)

average_age = round(df["age"].mean(), 2)
max_score = df["score"].max()
df["Passed"] = df["score"] >= 88
#df["Passed"] = np.where(df["score"] >= 88, True, False)

print("Average age: ", average_age)
print("Maximum score: ", max_score)
print("New DataFrame:")
print(df)