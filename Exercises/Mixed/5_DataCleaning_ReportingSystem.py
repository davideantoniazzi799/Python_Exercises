# ======================
# EXERCISE 5 — Data Cleaning & Reporting System
# ======================
#
# Create a class ReportGenerator that:
# - Accepts raw data as a list of dictionaries:
#     {
#       "name": str,
#       "age": int or None,
#       "score": float or None,
#       "city": str
#     }
#
# Methods:
# - clean_data():
#     - Fill missing ages with average age
#     - Fill missing scores with median score
# - add_levels():
#     - Use pd.cut() to assign:
#         Low / Medium / High
# - city_summary():
#     - Returns average score per city
# - export_ready():
#     - Returns final cleaned DataFrame
#
# Print:
# - Cleaned dataset
# - City performance report

import pandas as pd

bins = [0, 59, 79, 100]
lab = ["Low", "Medium", "High"]

class ReportGenerator:
    def __init__(self):
        self.report = []
        self.df = pd.DataFrame(self.report)

    #ADD REPORT
    def add_report(self, name, age, score, city):

        if any(r["name"] == name and r["city"] == city for r in self.report):
            raise KeyError("Duplicate record for this person and city")
        
        if age is not None:
            try:
                age = int(age)
            except (ValueError, TypeError):
                raise TypeError("Age must be a number or None")
    
            if age <= 0:
                raise ValueError("Age must be greater than 0")
            
        if score is not None:
            try:
                score = float(score)
            except (ValueError, TypeError):
                raise TypeError("Score must be a number or None")
            
            if not 0 <= score <= 100:
                raise ValueError("Score must be between 0 and 100")
        
        new_report = {
        "name": name,
        "age": age,
        "score": score,
        "city": city
        }
        
        self.report.append(new_report)
        self.df = pd.DataFrame(self.report)

    #CLEAN DATA
    def clean_data(self):

        if not self.df[["age", "score"]].isna().any().any():
            return "No missing values detected"
        
        self.df["age"].fillna(self.df["age"].mean(), inplace=True)
        self.df["score"].fillna(self.df["score"].median(), inplace=True)
    
    #LEVEL
    def add_levels(self):
        self.df["level"] = pd.cut(self.df["score"], bins=bins, labels=lab, include_lowest=True)

    #CITY SUMMARY
    def city_summary(self):
        return (self.df.groupby("city", as_index=False).agg(Avg_score=("score", "mean")))
    
    #EXPORT DATAFRAME
    def export_ready(self):
        return self.df


report_generator = ReportGenerator()

report_generator.add_report(name="Silvia", age = 18, score = 76, city = "Rome")
report_generator.add_report(name="Marco", age = 19, score = 87, city = "Rome")
report_generator.add_report(name="Andrea", age = 18, score = 67, city = "Milan")
report_generator.add_report(name="Lucia", age = 19, score = 87, city = "Milan")

report_generator.clean_data()
report_generator.add_levels()

city_summary = report_generator.city_summary()
final_df = report_generator.export_ready()

print("Cleaned DataFrame:")
print(final_df)

print("City summary:")
print(city_summary)