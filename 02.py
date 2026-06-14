# 2. Create a program that takes a list of student names and stores them in a file. Then, read
# the file and display the contents.

student_names = []

name = input("Enter the name of students separated with comma (,) :")
student_names = [f"{nam.strip()}," for nam in name.split(",")]

with open("02_studentdata.txt", "w+") as file:
    file.writelines(student_names)
    
    file.seek(0)
    print("\n\nStudent names::")
    for name in file.read().split(","):
        print(name)
    
