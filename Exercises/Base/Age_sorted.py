#Ordina una lista di dizionari (per esempio studenti con età) in base all’età.

students_dict = {
    "Elin": 27,
    "Davide": 27,
    "Luke": 45,
    "Josh": 35,
    "Dobby": 23,
    "Reese": 21,
}

ordered_dict = sorted(students_dict.items(), key=lambda item: item[1])

for student, age in ordered_dict:
    print(f"The student {student} has {age} years")