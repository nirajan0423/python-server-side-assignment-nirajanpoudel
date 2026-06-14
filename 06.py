# 6. Develop a simple OOP-based Python class Student with attributes like name, roll
# number, and marks. Implement methods to input and display details.

'''

class name -> Student
attributes -> name:string, roll_number:int, marks:float
methods -> input details, display details

not mentioned of use of constrtuctor

'''

class Student:
    def input_details(self):
        self.name = input("Name : ")
        self.roll_number = int(input("Roll number : "))
        self.marks = float(input("Marks : "))

    def display_details(self):
        print("Name = ", self.name)
        print("Roll number = ", self.roll_number)
        print("Marks = ", self.marks)


pradeep =  Student()
pradeep.input_details()
print()
pradeep.display_details()
