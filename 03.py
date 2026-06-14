# 3. Implement a program to store student records (name, roll, marks,contact number) using a
# dictionary.
# a. Provide menu options to add, search, and display students
from tabulate import tabulate

def add_data(student_record:list):
    data = {}
    data["name"] = input("Enter name : ") 
    data["roll"] = int(input("Enter roll number :")) 
    data["marks"] = float(input("Enter marks :")) 
    data["contact"] = input("Enter contact number :") 
    student_record.append(data)

def search_student(student_record:list):
    roll = int(input("Enter roll number of student:"))
    for data in student_record:
        if data['roll'] == roll:
            print(tabulate([data], headers="keys", tablefmt="simple_grid"))
            break


def display_data(student_record:list):
    print(tabulate(student_record, headers="keys", tablefmt="simple_grid"))

student_record = [{
        "name":"pradeep kunwar",
        "roll":1,
        "marks":80.56,
        "contact":9842640145,
    }]

while True:
    print("1. Add Data")
    print("2. Search Student")
    print("3. Display data")
    print("0. Exit")

    choice = int(input("Enter operation to perform :"))   
    if choice not in [1,2,3]:
        break

    match choice:
        case 1:
            add_data(student_record)
        case 2:
            search_student(student_record)
        case 3:
            display_data(student_record)
