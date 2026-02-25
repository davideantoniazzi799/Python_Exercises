# Crea un array NumPy con 20 valori equidistanti tra 0 e 1 (inclusi).
# Calcola:
# - media
# - minimo
# - massimo
# 
# Stampa l’array e i risultati.

import numpy as np

arr = np.linspace(0,1,20)

print("Array:", arr)
print("Average:", np.round(np.mean(arr), 2))
print("Minimum value:", np.min(arr))
print("Maximum value:", np.max(arr))