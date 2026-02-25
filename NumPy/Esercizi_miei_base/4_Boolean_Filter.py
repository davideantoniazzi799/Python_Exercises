#Create an array with numbers from 1 to 30
#Create a new array containing:
# - numbers greater than 10
# - and divisible by 3
# 
# Print the result

import numpy as np

arr = np.arange(1,31)
arrMask_1 = arr[arr > 10]
arrMask_2 = arrMask_1[arrMask_1 % 3 == 0]
#result = arr[(arr > 10) & (arr % 3 == 0)]

print("Initial array:", arr)
print("Numbers greater than 10 and divisible by 3 in array:", arrMask_2)