# Crea un array con valori da 1 a 20.
# 
# Poi:
# - crea una copia
#
# - usa un ciclo per:
#   - moltiplicare per -1 tutti i valori dispari
#   - lasciare invariati i pari
# 
# - stampa array originale e modificato

import numpy as np

a = np.arange(1,21)
a_copy = np.copy(a)
print(a_copy)

for i in range(0, np.size(a_copy)):
    if a_copy[i] % 2 != 0:
        a_copy[i] *= -1

print("Original array:", a)
print("Modified array:", a_copy)