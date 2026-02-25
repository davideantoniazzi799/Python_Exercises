#Data una lista con numeri ripetuti, rimuovi i duplicati e stampa la nuova lista.
from random import randint

numbers = []
final_list = []
len_list = randint(0,10)

for i in range(len_list):
    numbers.append(randint(1, 15))

for i in range(len(numbers)):
    if numbers[i] not in final_list:
        final_list.append(numbers[i])

print(*final_list, sep=", ")