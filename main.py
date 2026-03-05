from Calculator_art import logo
import time
import os

def clear_screen():
    """
    This function clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def add(a,b):
    """
    This function takes two numbers and returns their sum.

    Parameters:
        a (int): the first number
        b (int): the second number

    Returns:
        int: the sum of a and b
    """
    return a + b

def subs(a,b):
    """
    This function takes two numbers and returns their difference.

    Parameters:
        a (int): the first number
        b (int): the second number

    Returns:
        int: the difference of a and b
    """
    return a - b

def mult(a,b):
    """
    This function takes two numbers and returns their product.

    Parameters:
        a (int): the first number
        b (int): the second number

    Returns:
        int: the product of a and b
    """
    return a * b

def div(a,b):
    """
    This function takes two numbers and returns their division.

    Parameters:
        a (int): the first number
        b (int): the second number

    Returns:
        int: the division of a and b, or "Error: division by zero is not allowed." if b is equal to 0
    """
    if b == 0:
        return "Error: division by zero is not allowed."
    return a / b

operations = {
    "+": add,
    "-": subs,
    "*": mult,
    "/": div
}
print(logo)
keep_going = 0
solution = 0
while True:
    if keep_going == 0:
        first_number = float(input("What's the first number? "))
    else:
        print("Type 'c' to start a new calculation")
        first_number = solution
    clear_screen()
    print(logo)
    print(first_number)
    for x in operations:
        print(x)
    operation = input("Pick an operation: ").lower()
    if operation == "c":
        keep_going = 0
        continue
    elif operation in operations:
        clear_screen()
        print(logo)
        print(f"{first_number} {operation}")
        second_number = float(input("What's the next number? "))
        clear_screen()
        print(logo)
        solution = operations[operation](first_number, second_number)
        if isinstance(solution, str):
            print(solution)
            time.sleep(2)
            continue
        else:
            print(f"{first_number} {operation} {second_number} = {solution}")
            keep_going += 1
            time.sleep(2)

    else:
        print("Invalid operation. Please try again.")
        time.sleep(2)
        clear_screen()
        print(logo)
        continue