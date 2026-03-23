Python Advanced Calculator 🧮
A robust, console-based calculator implemented in Python featuring modular logic, comprehensive error handling, and persistent result memory.

Features 🎮
Persistent Memory: Seamlessly carry over the previous result as the starting point for your next calculation.

Robust Input Handling: Custom validation loops with try-except blocks ensure the app never crashes on invalid numeric input.

Smart Error Recovery: Specialized logic to handle "Division by Zero" without resetting the entire session.

Modular Design: Clean separation of mathematical operations, input validation, and core application state.

Dynamic Operation Mapping: Uses a dictionary-based dispatch system instead of complex if/else chains.

Cross-Platform UI: Automatic terminal clearing for Windows and Unix-based systems.

Operations 📋
Basic: Addition (+), Subtraction (-), Multiplication (*)

Division Suite:

Standard Division (/): Returns the exact float quozient.

Floor Division (//): Returns the integer quozient.

Modulus (%): Returns the remainder of the division.

Advanced: Exponentiation (**) for calculating powers.

Project Structure 📁
python-calculator/
├── Calculatorworkflow.drawio.pdf
├── algoritmo_Calculator.txt
├── main.py                # Main application logic and entry point
├── Calculator_art.py      # ASCII art logo
└── README.md              # Project documentation
Main Functions Overview:
clear_screen() - Clears console and displays the calculator logo.

get_valid_input() - Validates operation selection against a list of allowed symbols.

get_valid_number() - Safely converts user input to float with error handling.

operations() - Returns the operation dictionary or a specific function mapping.

add(), subs(), mult(), div(), int_div(), mov(), pow() - Core math logic.

main() - The primary state machine managing the calculation loop.

Requirements ✅
Python 3.x

No external dependencies required (pure Python standard library).

Installation & Setup 🚀
Clone the repository:
Bash
git clone https://github.com/FrontN/python-calculator.git
cd python-calculator
How to Play 🎯
Run the application:

Bash
python main.py
Choose your mode:

Type y to use the previous result as the first number.

Type n to start a fresh calculation.

Perform calculations:

Enter the first number (if starting new).

Pick an operation from the displayed list (e.g., *, %, **).

Enter the next number.

Error Correction:

If you attempt to divide by zero, the app will warn you and ask for a new second number immediately, saving your progress.

Game Output Example 📺
12.0
Operations:
+
-
*
/
//
%
**
Pick an operation: *

12.0 * 
What's the next number? 2

12.0 * 2.0 = 24.0
Technical Highlights 💡
State Persistence: Uses None initialization for solution to distinguish between a zero result and a new state.

Recursive Logic: The nested while True loop for second numbers ensures a smooth UX during mathematical errors.

Clean Code: Documented with standard Python Docstrings for every function.

Dry Principle: Reusable validation functions reduce code duplication.

Future Enhancements 🎯
Scientific functions (Square root, Logarithms)

Calculation history log (save to .txt)

Support for multiple numbers in a single string (expression parsing)

Constants support (Pi, e)

Contributing 🤝
Feel free to fork this repository and submit pull requests for any improvements!

Author 👨‍💻
FrontN - Developed as a deep dive into Python's functional programming and exception handling.

Happy calculating! 🔢
