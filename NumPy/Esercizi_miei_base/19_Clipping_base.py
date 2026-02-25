# Crea un array con valori da -20 a 50.
# Crea una versione dell’array in cui:
# - tutti i valori < 0 diventano 0
# - tutti i valori > 30 diventano 30
# 
# Stampa array originale e modificato.

import numpy as np

arr = np.arange(-20,51)

arr_clipped = np.clip(arr, 0, 30)

print("Original array:", arr)
print("Clipped array:", arr_clipped)