# Create a 3×4 matrix with values from 1 to 12.
# Compute:
# - the mean of each row
# - the mean of each column
# 
# Print both results.

import numpy as np

matrix1 = np.arange(1,13).reshape(3,4)

mean_rows = np.round(np.mean(matrix1, axis = 1), 2)
mean_columns = np.round(np.mean(matrix1, axis = 0), 2)

print("Original matrix:")
print(matrix1)
print("Average for each row:", mean_rows)
print("Average for each column:", mean_columns)