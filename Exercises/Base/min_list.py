#Scrivi una funzione che restituisca il valore minore di una lista, senza usare min().
from random import randint

def check_min_list(a):
    """Returns the minimum value in a list of numbers"""
    minimum = a[0]
    for number in a:
        if number < minimum:
            minimum = number

    return minimum

len_list = randint(1,10)
list_numbers = [randint(0,100) for _ in range(len_list)]
print(list_numbers)
print(f"The minimum value in the list is {check_min_list(list_numbers)}")