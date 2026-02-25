# Create a NumPy array with values from 1 to 10.
# Then:
# - add 5 to every element
# - multiply all elements by 2
# 
# Print all arrays.

import numpy as np

arr = np.arange(1,11)

arr_final = 2 * (5 + arr)

print(arr)
print(arr_final)