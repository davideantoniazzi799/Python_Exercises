# Crea due matrici 2×3:
# A = [[1, 2, 3],
#     [4, 5, 6]]
# B = [[10, 20, 30],
#     [40, 50, 60]]
# 
# Poi:
# - concatenale:
#   - per righe
#   - per colonne
# - stampa entrambe le versioni e la loro shape

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[10, 20, 30],
              [40, 50, 60]])

column_array = np.vstack((a, b))
row_array = np.hstack((a, b))

print("Concatenation by column:", column_array)
print("Shape:", column_array.shape)

print("Concatenation by row:", row_array)
print("Shape:", row_array.shape)