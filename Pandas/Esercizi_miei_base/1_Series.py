# Crea una Series Pandas con questi valori:
# [10, 20, 30, 40, 50]
# Stampa:
# - la Series
# - il suo tipo
# - i suoi valori (.values)
# - il suo indice (.index)

import pandas as pd

ds = [10, 20, 30, 40, 50]

series = pd.Series(ds)

print("Data series:")
print(series)
print("Data type:", type(series))
print("Series values:", series.values)
print("Data indexes:", series.index)
print("Data dtype:", series.dtype)