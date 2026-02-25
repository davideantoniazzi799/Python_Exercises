# Crea questo array:
# [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# 
# Usa NumPy per ottenere:
# - i valori unici
# - quante volte ciascun valore appare
# 
# Stampa ogni valore con la sua frequenza.

import numpy as np

arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

arr_values, arr_counts = np.unique(arr, return_counts=True)

for i in range(0, np.size(arr_values)):
    print(f"Number {arr_values[i]}: frequency {arr_counts[i]}")

#for value, count in zip(arr_values, arr_counts):
#    print(f"Number {value}: frequency {count}")