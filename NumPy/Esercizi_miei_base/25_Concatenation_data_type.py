# Crea un array:
# [1.2, 3.5, 6.7, 8.9]
# 
# Poi:
# - convertilo in:
#   - array di interi
#
# - crea un secondo array:
#     [100, 200]
# 
# - concatena i due array
#
# - stampa:
#   - array finale
#   - tipo di dato finale

import numpy as np

arr_1 = np.array([1.2, 3.5, 6.7, 8.9])
arr_2 = np.array([100, 200])

arr_1_Int = np.round(arr_1).astype(int)

arrConc = np.concatenate((arr_1_Int, arr_2))

print("Final array:", arrConc)
print("Data type:", arrConc.dtype)