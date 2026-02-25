#Create a 4×4 matrix with values from 1 to 16.
# 
# Then:
# - subtract row_means from each row using broadcasting
# 
# Print:
# - original matrix
# - row means
# - centered matrix

import numpy as np

matrix = np.arange(1,17).reshape(4,4)
row_means = np.mean(matrix, axis = 1)
row_means_reshaped = np.reshape(row_means, (4,1))
#row_means = matrix.mean(axis=1, keepdims=True)
centered_matrix = matrix - row_means_reshaped

print("Original matrix:")
print(matrix)
print("Rows mean:", row_means)
print("Centered matrix:")
print(centered_matrix)