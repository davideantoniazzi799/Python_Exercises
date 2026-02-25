#Crea una classe Student con:
# - attributi: name, surname, grades (lista di voti)
# - metodo add_grade(v) per aggiungere un voto
# - metodo average() che calcoli e ritorni la media
from statistics import mean

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    @property
    def average(self):
        if not self.grades:
            return 0

        return mean(self.grades)

student1 = Student(name = "Luca", surname="Rossi")
student2 = Student(name = "Mario", surname="Verdi")

student1.add_grade(8)
student1.add_grade(9)
student1.add_grade(6)
print(f"{student1.name}'s average is {student1.average:.2f}")