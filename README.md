# 🧮 Desktop Calculator – Python & Tkinter

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

A clean, modern desktop calculator application featuring a real calculator-style interface, keyboard support, and modular architecture.



---

## ✨ Features

* **Real Calculator Layout:** Intuitive buttons and responsive display.
* **Keyboard Support:** Full integration (Press `Enter` to calculate).
* **History Management:** Dedicated panel to track previous operations.
* **Modular Design:** Strict separation of concerns (GUI vs Logic).
* **Production Ready:** Unit tests included and Windows `.exe` packaging.

---

## 🧠 Architecture Overview

The application follows a professional layered design to ensure maintainability:

| Module | Responsibility |
| :--- | :--- |
| `gui.py` | Handles user interaction, display updates, and event listeners. |
| `calculator_core.py` | Pure mathematical logic, independent of the UI. |
| `history.py` | Manages data persistence for calculation history. |
| `errors.py` | Custom exception definitions for robust error handling. |

---

## 📂 Project Structure

```text
├── src/
│   ├── gui.py              # Main graphical interface
│   ├── calculator_core.py  # Core calculation logic
│   ├── history.py          # History management
│   └── errors.py           # Custom exceptions
├── tests/
│   └── test_calculator.py  # Unit tests
├── assets/
│   └── icono.ico           # Application icon
├── .gitignore
└── README.md
🚀 Getting Started
Prerequisites
Python 3.10+

Tkinter (usually bundled with Python)

Installation & Run
Clone the repository:

Bash

git clone [https://github.com/Andres-Parrales/desktop-calculator.git](https://github.com/Andres-Parrales/desktop-calculator.git)
Navigate to the source folder and run:

Bash

python src/gui.py
Running Tests
Bash

python -m unittest tests/test_calculator.py
🪟 Windows Executable (.exe)
This project uses PyInstaller for packaging. To build the executable:

Bash

pyinstaller --onefile --windowed --icon=assets/icono.ico src/gui.py
The resulting file will be located in the dist/ folder.

🛠️ Technologies Used
Language: Python

UI Framework: Tkinter

Testing: Unittest

Deployment: PyInstaller

👤 Author
Iván - Junior Software Developer

LinkedIn

Portfolio
