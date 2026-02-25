#Create two matrices:
# A = [[1, 2],
#     [3, 4],
#     [5, 6]]
# 
# B = [[10, 20],
#     [30, 40]]
# 
# Then:
# - compute the matrix multiplication
# - print the result and its shape

import numpy as np

a = np.array([[1, 2],
              [3, 4],
              [5, 6]])

b = np.array([[10, 20],
              [30, 40]])

final_result = a @ b

print("Matrix product:")
print(final_result)
print("Shape:", final_result.shape)