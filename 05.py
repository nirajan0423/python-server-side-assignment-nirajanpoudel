# 5. Write Python code to read from a CSV file of student marks and calculate average marks.


import csv

total = 0
count = 0

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    
    next(reader)  # Skip header row
    
    for row in reader:
        marks = float(row[1])  # Marks are in the second column
        total += marks
        count += 1

if count > 0:
    average = total / count
    print("Average Marks =", average)
else:
    print("No records found.")
