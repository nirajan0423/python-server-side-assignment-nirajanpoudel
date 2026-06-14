# 4. Create a Python function to calculate factorial of a number using recursion

def calculate_recursion(num):
    if num < 0:
        print("Enter positive number")
        return
    return 1 if num == 0 else num * calculate_recursion(num-1)

number = int(input("Enter number : "))
print(f"Factorial of {number} is ",calculate_recursion(number))
    