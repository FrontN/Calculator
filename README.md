# Calculator
🧮 Advanced Python CLI Calculator  A robust, interactive command-line calculator that supports continuous calculations, error handling, and a clean user interface. Developed with a focus on **modular programming** and **State Machine** logic.
## ✨ Key Features

* **Persistent Memory**: Carry over the result of your last calculation to the next operation seamlessly.
* **Input Validation**: Built-in protection against invalid inputs (non-numeric strings) using `try-except` blocks.
* **Safe Division**: Custom logic to handle division by zero without crashing, utilizing `isinstance()` checks.
* **Modular Architecture**: Operations are mapped via a dictionary, making it incredibly easy to add new functions (e.g., power, square root).
* **UX Focused**: Automatically clears the terminal for a distraction-free experience and uses timed delays for readability.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your machine.

### Installation & Execution
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/FrontN/python-calculator.git](https://github.com/FrontN/python-calculator.git)
   Navigate to the directory:

Bash
cd python-calculator
Run the application:

Bash
python main.py
🛠️ Technical Implementation
The "State Machine" Logic
The program uses a keep_going counter to track the application state.

If keep_going == 0: The app initializes a new calculation.

If keep_going > 0: The app pulls the previous solution and uses it as the first_number.

Dictionary Mapping
Instead of messy if/elif chains, this project uses a dictionary to store function references:

Python
operations = {
    "+": add,
    "-": subs,
    "*": mult,
    "/": div
}
This allows for dynamic function calling: operations[operation](a, b).

📖 Usage Example
Plaintext
What's the first number? 12
Pick an operation: +  -  * /
Selection: *
What's the next number? 2
✅ Result: 12.0 * 2.0 = 24.0

Type 'c' to reset or pick an operation to continue with 24.0.
👨‍💻 Author
Developed as part of a deep dive into Python's functional programming and exception handling.
