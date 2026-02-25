# Create two arrays:
# a = [1, 2, 3]
# b = [4, 5, 6]
# Then:
# - stack them by rows
# - stack them by columns
# 
# Print:
# - resulting arrays
# - their shapes

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vstack_array = np.vstack((a,b))
hstack_array = np.hstack((a,b))

print("Original arrays:")
print(a)
print(b)
print("Concatenation by rows:", vstack_array)
print("Shape:", vstack_array.shape)
print("Concatenation by columns:", hstack_array)
print("Shape:", hstack_array.shape)