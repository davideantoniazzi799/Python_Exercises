# Crea questo array:
# [10, 20, np.nan, 30, np.nan, 40]
# 
# Calcola:
# - il numero di valori NaN
# - la media ignorando i NaN
# 
# Stampa i risultati.

import numpy as np

arr = np.array([10, 20, np.nan, 30, np.nan, 40])

print("Total NaN values:", np.sum(np.isnan(arr)))
print("Average without NaN values:", round(np.nanmean(arr), 2))