#NumPy è una libreria fondamentale per il calcolo scientifico in Python.
#Fornisce un potente oggetto array multidimensionale e strumenti per lavorare con questi

import numpy as np

#Questo crea un array NumPy da una lista Python
arr = np.array([1, 2, 3, 4, 5])

#Differenza tra array NumPy e lista Python
#Le liste Python sono flessibili e possono contenere elementi di tipi diversi, ma sono
#meno efficienti per operazioni numeriche rispetto agli array NumPy, che sono ottimizzati per il calcolo scientifico.
lista = [1, 2, 3, 4, 5]
#Esempio di differenza
print(lista*5)
print(arr*5)

print(arr+5)
#print(lista+5) ci da errore perche non si puo sommare un intero ad una lista