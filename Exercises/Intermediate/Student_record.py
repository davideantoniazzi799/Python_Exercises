#Salva studenti con nome, età e voto in una lista di dizionari.
#Stampa la media dei voti.
from statistics import mean

stud_dict = {}

while True:
    stud_name = input("Insert the student's name (EXIT to stop): ").title()
    if stud_name == "Exit":
        break

    stud_age = int(input("Insert the student's age: "))
    stud_mark = float(input("Insert the student's mark: "))

    stud_dict[stud_name] = {
        "Age": stud_age,
        "Mark": stud_mark
    }

# Estrae tutti i voti in una lista
marks = [info["Mark"] for info in stud_dict.values()]

# Calcola la media solo se ci sono studenti
if marks:
    average_mark = mean(marks)
    print(f"Average mark in the class is {average_mark:.2f}")
else:
    print("No students were added.")