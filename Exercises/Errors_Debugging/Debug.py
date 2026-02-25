#Questo codice ha un bug:
# numbers = ["10", "20", "zero", "30"]
# total = 0
# for n in numbers:
#    total += int(n)
#print(total)

#Modificalo usando try / except in modo che:
# - il programma non crashi
# - i valori non validi vengano ignorati
# - venga comunque stampata la somma finale

numbers = ["10", "20", "zero", "30"]
total = 0

for n in numbers:
    try:
        total += int(n)
    except ValueError:
        pass

print(total)