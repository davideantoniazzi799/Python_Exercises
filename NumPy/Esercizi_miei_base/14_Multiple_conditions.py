# Create a NumPy array with numbers from 1 to 100.
# Select only the values that are:
# - greater than 20
# - less than 80
# - divisible by 5 or divisible by 7
# 
# Print the resulting array.

import numpy as np

arr = np.arange(1,101)

arr_final = arr[(arr > 20) & (arr < 80) & ((arr % 5 == 0) | (arr % 7 == 0))]

print("Final array", arr_final)