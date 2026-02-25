# ==========================================================
# EXERCISE 2 — File Processing & Error Control
# ==========================================================
# Create a function save_students_to_file(students, filename)
# that:
# - writes each student's name and average grade to a file
# - format: "Name | Average"
#
# Create a function load_students_from_file(filename)
# that:
# - reads the file
# - returns a list of dictionaries
# - handles:
#     FileNotFoundError
#     ValueError (invalid data format)
#
# Then:
# - reload the data
# - print only students with average >= 75

from statistics import mean

def save_students_to_file(students, filename):
    with open(filename, mode = "w") as file_output:
        for item in students:
            name = item["Name"]
            avg_grades = round(mean(item["Grades"]), 2)
            file_output.write(f"{name} | {avg_grades}\n")

def load_students_from_file(filename):
    students_list = []
    try:
        with open(filename) as file_input:
            for line in file_input:
                try: 
                    name, avg_grade = line.strip().split("|")
                    name = name.strip()
                    avg_grade = float(avg_grade.strip())
                    student_dict = {
                        "Name": name,
                        "Average": avg_grade
                    }
                
                    students_list.append(student_dict)
        
                except ValueError:
                    print(f"Invalid data format in line: {line.strip()}")

            return students_list
        
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []

stud_dict = [
    {"Name" : "Luca", "Grades" : [78, 89, 98]},
    {"Name" : "Sofia", "Grades" : [77, 81, 89]},
    {"Name" : "Marco", "Grades" : [67, 78, 65]},
    {"Name" : "Luigi", "Grades" : [81, 93, 77]}
]

save_students_to_file(students=stud_dict, filename="Student_average_grade.txt")
students75 = load_students_from_file(filename="Student_average_grade.txt")

print("Students with average >= 75:")
for student in students75:
    if student["Average"] >= 75:
        print(student)