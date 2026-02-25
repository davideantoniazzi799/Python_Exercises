#Data una lista di numeri (scritta da te), somma solo i pari.
from random import randint

len_list = randint(1,10)
list_numbers = []
sum_even = 0

for _ in range(len_list):
    list_numbers.append(randint(1,100))

for number in list_numbers:
    if number % 2 == 0:
        sum_even += number

print(list_numbers)
print(f"The sum of the even numbers in the list is {sum_even}")