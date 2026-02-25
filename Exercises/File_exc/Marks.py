#Scrivi un programma che:
# 1 - Legge il file grade.txt
# 2 - Calcola la media dei voti per ogni studente
# 3 - Salva il risultato in grades_summary.txt

with open("grades.txt") as file_input, open("grades_summary.txt", mode = "w") as file_output:
    stud_grades = {}
    for line in file_input:
        name, grade = line.strip().split(",") #strip deletes \n
        grade = int(grade)
        if name not in stud_grades:
            stud_grades[name] = []

        stud_grades[name].append(grade)

    for (k,v) in stud_grades.items():
        file_output.write(f"{k}: {sum(v)/len(v):.1f}\n")