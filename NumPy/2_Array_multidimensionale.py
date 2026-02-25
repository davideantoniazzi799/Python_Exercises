#------------CREARE UN ARRAY A DIVERSE DIMENSIONI -----------
import numpy as np

#---- 0 Dimensioni ----
arr = np.array(42)

#---- 1 Dimensione ----
arr1D = np.array([1, 2, 3, 4, 5])
#come se fosse una lista

#---- 2 Dimensioni ----
arr2D = np.array([[1, 2, 3], 
                  [4, 5, 6]])
#come se fosse un array che contiene due array (vedi parentesi quadre viola)

#---- 3 Dimensioni ----
arr3D = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])
#come se fosse un array che contiene degli array che contegono altri array

print(arr3D)

#------------CAPIRE LE DIMENSIONI DI UN ARRAY -----------
print(arr.ndim)      #0 dimensioni

#------------GENERARE ARRAY CON N DIMENSIONI -----------
arr5D = np.array([1, 2, 3, 4, 5], ndmin=5) #5 dimensioni
print(arr5D)
print('Numero di dimensioni:', arr5D.ndim)

#------------ARANGE, ZEROS E ONES -----------
#Arange genera array con valori in un intervallo specificato
arrArange = np.arange(5,50,5) #da 5 a 50 con step di 5, lo step non è obbligatorio

#Zeros genera array di zeri
arrZeros = np.zeros(3) #array di 3 righe con soli zeri
arrZeros2D = np.zeros((3,4)) #array di 3 righe e 4 colonne con soli zeri a due dimensioni
#in pratica la prima dimensione deve avere 3 elementi e la seconda 4

#Ones genera array di uni
arrOnes = np.ones(3) #array di 3 righe con soli uni

print(arrOnes)

#------------MATRICE IDENTITA' -----------
#funzione .eye()
arrIdentita = np.eye(4) #matrice identità 4x4
print(arrIdentita)

#------------MATRICE DIAGONALE -----------
#dobbiamo prima creare un array con i valori che vogliamo sulla diagonale
arrDiagonal = np.array([1, 2, 3, 4])
#poi con la funzione .diag() creiamo la matrice diagonale
matriceDiagonale = np.diag(arrDiagonal)
print(matriceDiagonale)

#Con .diag() possiamo anche estrarre la diagonale di una matrice
print(np.diag(matriceDiagonale)) #estraiamo la diagonale

#------------MATRICE TRIANGOLARE SUPERIORE E INFERIORE -----------
#funzione .triu() e .tril()
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(np.triu(arr)) #matrice triangolare superiore
print(np.tril(arr)) #matrice triangolare inferiore