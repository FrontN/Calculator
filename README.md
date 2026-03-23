Python Advanced Calculator 🧮
Una calcolatrice da riga di comando (CLI) robusta e interattiva, progettata con un approccio modulare e una gestione avanzata delle eccezioni per un'esperienza utente fluida e senza crash.

✨ Key Features
Persistent Memory: Possibilità di utilizzare il risultato dell'ultimo calcolo come base per l'operazione successiva senza ricominciare da zero.

Advanced Error Handling: Protezione totale contro input non numerici tramite blocchi try-except e validazione continua.

Smart Division & Modulo: Logica personalizzata per prevenire il crash da "Division by Zero" su tre diversi operatori (/, //, %).

Modular Architecture: Le operazioni sono mappate tramite un dizionario, permettendo di estendere facilmente le funzionalità (potenze, moduli, divisioni intere).

UX Optimized: Pulizia automatica del terminale (clear_screen) e ritardi temporizzati (time.sleep) per garantire la massima leggibilità tra i calcoli.

📋 Operations & Logic
Il programma non si limita alle quattro operazioni base, ma scompone la divisione in tre parti logiche:

Standard Division (/): Restituisce il quoziente decimale esatto.

Floor Division (//): Restituisce quante volte il divisore sta interamente nel dividendo.

Modulus (%): Restituisce esclusivamente il resto della divisione.

Exponentiation (**): Calcola la potenza del primo numero elevato al secondo.

🚀 Getting Started
Prerequisites
Python 3.x installato sul sistema.

Installation & Execution
Clona il repository:

Bash
git clone https://github.com/FrontN/python-calculator.git
cd python-calculator
Avvia l'applicazione:

Bash
python main.py
🛠️ Technical Implementation
State Management & Null Logic
A differenza delle versioni base, questa calcolatrice utilizza una gestione dello stato basata su None:

Inizializzazione: solution = None permette di distinguere tra un calcolo non ancora effettuato e un risultato che vale matematicamente 0.

Persistenza: Se solution != None, il sistema chiede all'utente se desidera procedere con il numero precedente o iniziare un nuovo set di calcoli.

Dictionary Mapping vs If/Else
Per evitare catene disordinate di if/elif, il progetto utilizza il Dictionary Dispatch Pattern:

Python
operations = {
    "+": add,
    "-": subs,
    "*": mult,
    "/": div,
    "//": int_div,
    "%": mov,
    "**": pow
}
Questo permette chiamate dinamiche alle funzioni: operations[operation](a, b).

Recursive Input Validation
La gestione del secondo numero avviene in un ciclo while True dedicato:

Se l'operazione restituisce una stringa (messaggio di errore), il sistema visualizza l'errore e richiede solo il secondo numero, mantenendo in memoria il primo numero e l'operatore scelto.

📖 Usage Example
Plaintext
What's the first number? 17
Pick an operation: +  -  * /  //  %  **
Selection: %
What's the next number? 5

✅ Result: 17.0 % 5.0 = 2.0

Type 'y' to continue with 2.0, type 'n' to start a new calculation: 
👨‍💻 Author
FrontN - Sviluppato come approfondimento sulla programmazione funzionale, gestione delle eccezioni e logica degli stati in Python.

Happy calculating! 🔢
