#Dalla lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] crea una nuova lista che contiene solo i numeri pari.

number_list = [1,2,3,4,5,6,7,8,9,10]
even_list = [number for number in number_list if number % 2 == 0]
print(even_list)