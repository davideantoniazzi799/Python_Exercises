# Create a NumPy array containing the numbers from 1 to 10
# Print:
# - the array
# - its type
# - its shape

import numpy as np

arr = np.arange(1,11)

print(arr)
print(type(arr))
print(arr.shape)
print('Numero di dimensioni:', arr.ndim)