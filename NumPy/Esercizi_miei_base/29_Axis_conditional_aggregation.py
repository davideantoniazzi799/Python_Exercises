# Using the same 3×4 matrix:
# - compute the sum of values > 5 for each column
# 
# Hint: use boolean masking + axis.

import numpy as np

matrix1 = np.arange(1,13).reshape(3,4)

mask_matrix = np.where(matrix1 > 5, matrix1, 0)
sum_columns = np.sum(mask_matrix, axis = 0)

print("Original matrix:")
print(matrix1)
print("Sum of the values > 5 for each column:", sum_columns)