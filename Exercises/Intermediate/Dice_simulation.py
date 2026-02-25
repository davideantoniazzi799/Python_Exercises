#Simula il lancio di un dado n volte e calcola le percentuali di uscita.
import random

number_count_dict = {}

number_throws = random.randint(5,10)
throw_outcomes = [random.randint(1,6) for i in range(number_throws)]

for number in throw_outcomes:
    if number in number_count_dict:
        number_count_dict[number] += 1
    else:
        number_count_dict[number] = 1

for (number, value) in sorted(number_count_dict.items()):
    print(f"The {number} came out {value} times({value/number_throws * 100:.2f} %).")