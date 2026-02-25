# Crea due array:
# a = [10, 20, 30, 40]
# b = [2, 4, 5, 8]
# 
# Poi:
# - dividi a per b elemento per elemento
# - arrotonda il risultato a 2 decimali
# - stampa l’array risultante

import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([2, 4, 5, 8])
my_list = []

for i in range(0, np.size(a)):
    my_list.append(round(a[i]/b[i], 2))

final_array = np.array(my_list)

#result = np.round(a / b, 2)

print("Final array:", final_array)