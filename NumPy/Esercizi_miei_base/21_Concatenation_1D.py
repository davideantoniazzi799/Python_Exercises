# Crea due array NumPy:
# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30]

# Poi:
# - concatenali in un unico array
# - stampa:
#   - l’array finale
#   - la sua lunghezza
#   - il suo tipo di dato

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30])

arr = np.concatenate((a, b))

print("Concatenated array:", arr)
print("Length:", np.size(arr))
print("Data type:", arr.dtype)