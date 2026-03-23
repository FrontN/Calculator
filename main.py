from Calculator_art import logo
import time
import os

def clear_screen():
    """
    Clears the screen and prints the logo.

    This function is used to clear the screen and print the logo of the calculator.
    It uses the os module to determine the operating system and then uses the appropriate
    command to clear the screen.
    After clearing the screen, it prints the logo of the calculator.
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

def get_valid_input(prompt, valid_options):
    """
    Prompts the user for input and validates it against a list of valid options.

    Parameters:
    prompt (str): The message to display to the user when asking for input.
    valid_options (list): A list of valid options that the user's input must match.

    Returns:
    str: The valid input entered by the user.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")
            time.sleep(2)
        
def get_valid_number(prompt):
    """
    Prompts the user for a number and validates it against a ValueError exception.
    
    Parameters:
    prompt (str): The message to display to the user when asking for input.
    
    Returns:
    float: The valid number entered by the user.
    """
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")
            time.sleep(2)
            clear_screen()
            continue

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

def int_div(a,b):
    """
    This function takes two numbers and returns their integer division (floor division).

    Parameters:
        a (int): the first number
        b (int): the second number

    Returns:
        int: the integer division of a and b, or "Error: division by zero is not allowed." if b is equal to 0
    """
    if b == 0:
        return "Error: division by zero is not allowed."
    return a // b

def mov(a,b):
    """
    This function takes two numbers and returns their modulus (remainder of division).

    Parameters:
        a (int): the first number
        b (int): the second number

    Returns:
        int: the modulus of a and b
    """
    if b == 0:
        return "Error: modulus by zero is not allowed."
    return a % b

def pow(a,b):
    """
    This function takes two numbers and returns their power.

    Parameters:
        a (int): the first number
        b (int): the second number

    Returns:
        int: the power of a and b
    """
    return a ** b
def operations(operation = None):
    """
    Returns a dictionary of operations where the keys are the operation symbols
    and the values are the corresponding functions.

    If operation is None, returns the entire dictionary.

    Otherwise, returns the function corresponding to the given operation symbol.

    Parameters:
        operation (str): The operation symbol to retrieve the corresponding function.

    Returns:
        dict: A dictionary of operations where the keys are the operation symbols
        and the values are the corresponding functions.
    """
    operations = {
        "+": add,
        "-": subs,
        "*": mult,
        "/": div,
        "//": int_div,
        "%": mov,
        "**": pow
    }
    return operations if not operation else operations[operation]

def main():
    """
    Main function of the calculator program.

    This function will continue to run until the user chooses to exit.

    It will first ask the user if they want to use the previous result, or start a new calculation.
    If the user chooses to use the previous result, it will use the previous result as the first number.
    Otherwise, it will ask the user for the first number.

    Then, it will print out all the available operations and ask the user to pick one.
    After the user picks an operation, it will ask the user for the second number.

    Then, it will print out the result of the operation, and ask the user if they want to continue or exit.

    If the user chooses to continue, it will start over again from the beginning.
    If the user chooses to exit, it will break out of the loop and the program will end.
    """
    keep_going = True
    solution = None
    while keep_going:
        clear_screen()
        if solution != None and get_valid_input("Type 'y' to use the previous result, type 'n' to start a new calculation: ", ['y', 'yes', 'n', 'no']).startswith('y'):
            first_number = solution
        else:
            first_number = get_valid_number("What's the first number? ")
        clear_screen()
        print(first_number)
        print("Operations:")
        for x in operations():
            print(x)
        operation = get_valid_input("Pick an operation: ", list(operations()))
        clear_screen()
        while True:
            print(f"{first_number} {operation}")
            second_number = get_valid_number("What's the next number? ")
            clear_screen()
            solution = operations(operation)(first_number, second_number)
            print(f"{first_number} {operation} {second_number} = {solution}")
            time.sleep(2)
            clear_screen()
            if isinstance(solution, str):
                continue
            break
        keep_going = get_valid_input("Type 'y' to continue, type 'n' to exit: ", ['y', 'yes', 'n', 'no']).startswith('y')

if __name__ == "__main__":
    main()
