import csv
with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)    
    for row in reader:
        if int(row["Grade"]) > 80:
            print(row["Name"])
import json
data = {
    "course": "Python",
    "duration": "3 months",
    "students": ["Ali", "Sara"]
}
with open("course.json", "w") as file:
    json.dump(data, file, indent=4)
with open("course.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data["students"])
import pandas as pd
data = {
    "ID": [1, 2, 3],
    "Name": ["Mohamed", "ziad", "hadi"],
    "Salary": [5000, 6200, 4800]
}
df = pd.DataFrame(data)
df.to_excel("employees.xlsx", index=False)
loaded_df = pd.read_excel("employees.xlsx")
print(loaded_df[["Name", "Salary"]])
import csv
import json
def csv_to_json(csv_file, json_file):
    data = {"people": []}
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["Age"] = int(row["Age"])
            data["people"].append(row)
    with open(json_file, 'w') as f:
        json.dump(data, f)
