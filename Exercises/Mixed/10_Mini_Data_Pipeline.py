# ==========================================================
# EXERCISE 5 — Mini Data Pipeline (Real World Logic)
# ==========================================================
# Create a class DataPipeline:
#
# Methods:
# - load_from_csv(filename)
# - clean_data()
# - analyze()
# - export_report(filename)
#
# Rules:
# - load_from_csv:
#     loads a Pandas DataFrame
#     handles missing file errors
#
# - clean_data:
#     removes rows with missing values
#     clips numerical columns between 0 and 100
#
# - analyze:
#     returns:
#       min, max, mean for each numeric column
#
# - export_report:
#     writes analysis to a text file
#
# Then:
# - run the full pipeline on a test CSV file
# - print final results

import pandas as pd

class DataPipeline:
    def __init__(self):
        self.df = None

    def load_from_csv(self, filename):
        try:
            self.df = pd.read_csv(filename, sep=",")
        except FileNotFoundError: 
            print(f"Error: {filename} not found.")
    
    #DROPNA and CLIP
    def clean_data(self):
        self.df = self.df.dropna()
        numeric_cols = self.df.select_dtypes(include="number").columns
        self.df[numeric_cols] = self.df[numeric_cols].clip(0, 100)

    def analyze(self):
        numeric_df = self.df.select_dtypes(include="number")
        return numeric_df.min(), numeric_df.max(), numeric_df.mean()
    
    def export_report(self, filename):
        min_data, max_data, mean_data = self.analyze()

        with open(filename, mode="w") as file_output:
            for column in min_data.index:
                file_output.write(f"Column: {column}\n")
                file_output.write(f"Min: {min_data[column]}\n")
                file_output.write(f"Max: {max_data[column]}\n")
                file_output.write(f"Mean: {round(mean_data[column], 2)}\n")
                file_output.write("-" * 30 + "\n")


datapipeline = DataPipeline()
datapipeline.load_from_csv("test_students_pipeline.csv")
datapipeline.clean_data()
datapipeline.export_report("analysis_pipeline.txt")

min_data, max_data, mean_data = datapipeline.analyze()

print("MIN:\n", min_data)
print("MAX:\n", max_data)
print("MEAN:\n", mean_data)