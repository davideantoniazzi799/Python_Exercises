# Create an array with values from 1 to 10.
# 
# Then:
# - assign it to a new variable (without .copy())
# - modify one element in the new variable
# - print both arrays
# 
# Repeat the same using .copy() and compare the results.

import numpy as np

arr = np.arange(1,11)

arr2 = arr
arr2[0] = 100

arr_copy = np.copy(arr)
arr_copy[5] = 100

print("Original array:", arr)
print("Modified array:", arr2) #both original and modified arrays change
print("Copied array", arr_copy) #only the copied array changes