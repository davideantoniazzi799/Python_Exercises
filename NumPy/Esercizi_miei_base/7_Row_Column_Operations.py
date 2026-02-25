# Using the 3x4 array from Exercise 1:
#
# Compute and print:
# - the sum of each row
# - the sum of each column

import numpy as np

arr = np.arange(1,13)
arr_2D = arr.reshape(3,4)

sum_rows = np.sum(arr_2D, axis = 1)
sum_columns = np.sum(arr_2D, axis = 0)

print("Total for each row in array:", sum_rows)
print("Total for each column in array:", sum_columns)