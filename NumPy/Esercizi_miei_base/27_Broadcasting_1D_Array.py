# Create:
# matrix = [[1, 2, 3],
#          [4, 5, 6]]
# 
# Create a NumPy array:
# weights = [10, 20, 30]
# 
# Then:
# - multiply each column of the matrix by weights
# - print the result

import numpy as np

matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])
weights = np.array([10, 20, 30])

matrix_weights = matrix * weights

print("Final array:")
print(matrix_weights)