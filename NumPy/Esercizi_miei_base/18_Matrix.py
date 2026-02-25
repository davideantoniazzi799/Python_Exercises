# Crea una matrice 5 × 5 con numeri casuali tra 1 e 100.
# Ordina ogni riga in ordine crescente.
# Estrai:
# - la prima colonna
# - l’ultima riga
# 
# Stampa tutto.

import numpy as np
from numpy import random

arr = random.randint(1, 100, size = (25)).reshape(5,5)
arr_sorted = np.sort(arr, axis = 1)

print("Original array:", arr)
print("Array sorted by row:", arr_sorted)
print("First column:", arr_sorted[:,0])
print("Last row:", arr_sorted[4,:])