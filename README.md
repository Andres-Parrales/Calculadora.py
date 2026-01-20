Desktop Calculator – Python & Tkinter

A clean, modern desktop calculator application built with Python and Tkinter, featuring a real calculator-style interface, keyboard support, operation history, and Windows executable packaging.

This project was developed with a modular architecture, separating GUI, business logic, error handling, and history management to follow good software engineering practices.

✨ Features

✅ Real calculator layout (buttons & display)

⌨️ Keyboard support (Enter to calculate)

🧠 Modular architecture (clean separation of concerns)

🕒 Operation history panel

🧹 Clear history functionality

🪟 Windows .exe executable

🎨 Custom icon

🧪 Unit tests included

📂 Project Structure
CALCULADORA.PY/
│
├── gui.py                  # Main graphical interface (Tkinter)
├── calculator_core.py      # Core calculation logic
├── history.py              # History management
├── errors.py               # Custom exceptions
├── main.txt                # Optional entry notes
├── test_calculator.py      # Unit tests
│
├── Calculadora.exe         # Windows executable
├── Calculadora.spec        # PyInstaller configuration
├── icono.ico               # Application icon
│
├── build/                  # PyInstaller build files
├── __pycache__/            # Python cache
├── .vscode/                # VS Code settings
│
├── .gitignore
└── README.md

🧠 Architecture Overview

The application follows a simple but professional layered design:

GUI (gui.py)
Handles user interaction, buttons, keyboard input, and display updates.

Core Logic (calculator_core.py)
Contains all mathematical operations, independent from the GUI.

History (history.py)
Stores and manages calculation history.

Errors (errors.py)
Custom exceptions for clean error handling.

This separation makes the project easy to maintain, test, and extend.

🚀 How to Run (Python)
Requirements

Python 3.10+

Tkinter (included with Python on Windows)

Run the application:
python gui.py

🪟 Windows Executable (.exe)

The application is packaged using PyInstaller.

To build it yourself:

pyinstaller --onefile --windowed --icon=icono.ico gui.py


The executable will be generated inside the dist/ folder.

🧪 Running Tests
python test_calculator.py

🛠️ Technologies Used

Python

Tkinter

PyInstaller

Git & GitHub

📌 Learning Goals

This project was created to practice and demonstrate:

Desktop GUI development with Tkinter

Clean code and modular design

Exception handling

Git version control

Packaging Python applications into executables

📄 License

This project is for educational and portfolio purposes.

👤 Author

Iván
Junior Software Developer
Python | Desktop Applications | Clean Architecture
