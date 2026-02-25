# Create a NumPy array with numbers from 1 to 24 and reshape it into a 4×6 matrix.
# Then:
# - Compute the sum of each row
# - Compute the mean of each column
# - Find the maximum value of the entire matrix
# 
# Print all results.

import numpy as np

arr = np.arange(1,25).reshape(4,6)

sum_rows = np.sum(arr, axis = 1)
mean_columns = np.mean(arr, axis = 0)
max_value = np.max(arr)

print(f"Sum of the rows: {sum_rows}")
print(f"Mean of each colum: {mean_columns}")
print(f"Max: {max_value}")