# Create a NumPy array with numbers from 1 to 50.
# Then:
# Select only the values that are multiples of 4
# From those values, compute:
# - mean
# - standard deviation
# - maximum
# 
# Print all results.

import numpy as np

arr = np.arange(1,51)
arr_multiple_4 = arr[arr % 4 == 0]

print("Average of the array:", np.round(np.mean(arr_multiple_4), 2))
print("Standard deviation of the array:", np.round(np.std(arr_multiple_4), 2))
print("Maximum value in the array:", np.max(arr_multiple_4))