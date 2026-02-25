# Create two vectors:
# v1 = [1, 2, 3]
# v2 = [4, 5, 6]
# 
# Compute:
# - dot product using np.dot
# - dot product using @
# 
# Print both results.

import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

dot_matrix = np.dot(v1,v2)
dot_matrix2 = v1@v2

print("First result:")
print(dot_matrix)
print("Second result:")
print(dot_matrix2)