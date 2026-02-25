# ======================
# EXERCISE 1 — Student Management System
# ======================
#
# Create a class StudentManager that:
# - Stores students in a list of dictionaries
#
# Each student should have:
# - name
# - math_score
# - science_score
#
# Methods:
# - add_student(name, math, science)
# - to_dataframe() → returns a Pandas DataFrame
# - add_averages() → uses NumPy to compute average scores
# - passed_students(threshold=75) → returns only students who passed
#
# Then:
# - Create at least 5 students
# - Print the final DataFrame
# - Print only passed students

import pandas as pd
import numpy as np

THRESHOLD = 75

#CREATING CLASS
class StudentManager:
    def __init__(self):
        self.students = []

    #Add student dictionary to the list
    def add_student(self, name, math, science):
        self.students.append(
            {"Name": name, 
             "Math_score": math, 
             "Science_score": science
             })

    #DataFrame
    def to_dataframe(self):
        return pd.DataFrame(self.students)

    #Average scores
    def add_averages(self, data):
        df["Average_score"] = round(np.mean(data[["Math_score", "Science_score"]], axis = 1), 2)
        return data

    #Passed students
    def passed_students(self, data):
        return data[data["Average_score"] >= THRESHOLD]

#Creating students   
studentManager = StudentManager()
studentManager.add_student(name= "Luke", math= 78, science= 98)
studentManager.add_student(name="Lucy", math = 87, science= 76)
studentManager.add_student(name="Andrew", math = 69, science= 74)
studentManager.add_student(name="David", math = 67, science= 91)
studentManager.add_student(name="Jonny", math = 98, science= 93)

#DataFrame
df = studentManager.to_dataframe()
df = studentManager.add_averages(data=df)

#Passed students
passed_students = studentManager.passed_students(data=df)

print("Students data:")
print(df)
print("Students that passed the threshold(75):")
print(passed_students["Name"])