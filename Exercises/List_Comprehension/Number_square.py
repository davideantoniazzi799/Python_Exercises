#Crea una lista con i quadrati dei numeri da 1 a 20 usando una list comprehension.

new_list = [pow(number, 2) for number in range(1,21)]
print(new_list)