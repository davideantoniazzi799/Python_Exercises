# ==========================================================
# EXERCISE 4 — Advanced Function Logic
# ==========================================================
# Create a function register_student(name, age, *grades, **extra_info)
#
# Rules:
# - Must accept unlimited grades
# - Must accept extra info like:
#     city="Rome"
#     course="Physics"
#
# The function must:
# - Validate:
#     name is string
#     age is int between 18–30
#     all grades are numbers between 0–100
# - Return a dictionary with:
#     {
#       "name": str,
#       "age": int,
#       "grades": list,
#       "extra": dict
#     }
#
# Raise meaningful errors when validation fails

def register_student(name, age, *grades, **extra_info):
    extra_info_dict = {}

    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if not (18<= age <= 30):
        raise ValueError("Age must be between 18 and 30")
        
    for item in grades:
        if not isinstance(item, (int, float)):
            raise TypeError("Grades must be numbers")

        if not (0 <= item <= 100):
            raise ValueError("Grades must be between 0 and 100")

    grades_list = list(grades)

    for k, v in extra_info.items():
        extra_info_dict[k] = v

    student_dict ={
        "name": name,
        "age" : age,
        "grades" : grades_list,
        "extra" : extra_info_dict
    }

    return student_dict

student1_data = register_student("Luca", 
                                 19, 
                                 89, 88, 78, 
                                 city = "Rome",
                                 course = "Physics")

print(student1_data)