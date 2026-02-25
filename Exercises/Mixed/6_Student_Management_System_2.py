# ==========================================================
# EXERCISE 1 — Student Management System
# ==========================================================
# Create a class Student with:
# - attributes: name, age, grades (list)
# - method: average_grade()
#
# Then:
# - store at least 5 students inside a LIST of DICTIONARIES
#   Each dictionary should store:
#     {
#       "student": Student_object,
#       "city": str
#     }
#
# Write functions to:
# 1) Print students with average grade above 80
# 2) Group students by city (dictionary output)
# 3) Raise a ValueError if any student's age is not between 18 and 30

from statistics import mean

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        
        return mean(self.grades)

student1 = Student(name = "Luca", age = 18, grades = [78, 89, 90, 68])
student2 = Student(name = "Stefano", age = 23, grades = [81, 69, 93, 95])
student3 = Student(name = "Maria", age = 25, grades = [67, 69, 87, 78])
student4 = Student(name = "Teresa", age = 23, grades = [89, 89, 90, 98])
student5 = Student(name = "Massimo", age = 28, grades = [76, 98, 87, 71])

stud_list= [
    {"student": student1, "city": "Rome" },
    {"student": student2, "city": "Rome" },
    {"student": student3, "city": "Rome" },
    {"student": student4, "city": "Venice" },
    {"student": student5, "city": "Venice" },
]   

def print_high_achievers(students):
    for item in students:
        student = item["student"]
        if student.average_grade() > 80:
            print(student.name, student.average_grade())

def group_by_city(students):
    grouped = {}

    for item in students:
        city = item["city"]
        student = item["student"]

        if city not in grouped:
            grouped[city] = []

        grouped[city].append(student.name)

    return grouped

def validate_ages(students):
    for item in students:
        student = item["student"]
        if not (18 <= student.age <= 30):
            raise ValueError(f"{student.name} has invalid age: {student.age}")

city_students = group_by_city(students=stud_list)

validate_ages(students=stud_list)

print("Students with average > 80:")
print_high_achievers(students=stud_list)

print("Students by city:")
print(city_students)