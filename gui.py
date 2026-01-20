# Gui.py
import tkinter as tk
from tkinter import messagebox

from calculator_core import calculate
from history import get_history, clear_history, add_to_history
from errors import CalculatorError

# ----------- Configuracion -----------------
OP_SYMBOLS = {
    "add": "+",
    "subtract": "-",
    "multiply": "×",
    "divide": "÷",
    "percent": "%"
}

current_value = ""
stored_value = None
current_operation = None

# ------------- Ventana ----------------------
root = tk.Tk()
root.title("Calculadora")
root.geometry("320x600")
root.resizable(False, False)
root.config(bg="#EAF2FB")

# ------------- Pantalla ---------------------
display = tk.Entry(
    root,
    font=("Segoe UI", 26),
    justify="right",
    bd=0,
    relief="flat",
    bg="#FDFEFE",
    fg="#2C3E50"
)
display.pack(fill="x", padx=15, pady=15)

def update_display(value):
    display.delete(0, tk.END)
    display.insert(tk.END, value)

# ------------ Logica ----------------------
def press_number(num):
    global current_value
    current_value += str(num)
    update_display(current_value)

def press_operation(op):
    global stored_value, current_value, current_operation
    if current_value == "":
        return
    stored_value = float(current_value)
    current_operation = op
    current_value = ""
    update_display("")

def backspace():
    global current_value
    if current_value:
        current_value = current_value[:-1]
        update_display(current_value)

def calculate_result():
    global stored_value, current_operation, current_value
    try:
        if stored_value is None or current_value == "":
            return

        a = stored_value
        b = float(current_value)
        op = current_operation

        result = calculate(op, a, b)

        symbol = OP_SYMBOLS.get(op, op)
        entry = f"{int(a) if a.is_integer() else a} {symbol} {int(b) if b.is_integer() else b} = {int(result) if float(result).is_integer() else result}"
        add_to_history(entry, result)

        update_display(result)
        current_value = str(result)
        stored_value = None
        current_operation = None
        update_history()

    except CalculatorError as e:
        messagebox.showerror("Error", str(e))

def clear_all():
    global current_value, stored_value, current_operation
    current_value = ""
    stored_value = None
    current_operation = None
    update_display("")

# ----------------- Botones ------------------------
frame = tk.Frame(root, bg="#EAF2FB")
frame.pack()

def btn(text, row, col, cmd, bg="#D6E6F5", fg="#2C3E50", colspan=1):
    tk.Button(
        frame,
        text=text,
        width=5,
        height=2,
        font=("Segoe UI", 14),
        bg=bg,
        fg=fg,
        relief="flat",
        activebackground="#AED6F1",
        command=cmd
    ).grid(
        row=row,
        column=col,
        columnspan=colspan,
        padx=6,
        pady=6,
        sticky="nsew"
    )

btn("C", 0, 0, clear_all, bg="#F5B7B1")
btn("%", 0, 1, lambda: press_operation("percent"), bg="#B8D4F1")
btn("÷", 0, 2, lambda: press_operation("divide"), bg="#B8D4F1")
btn("⌫", 0, 3, backspace, bg="#B8D4F1")

btn("7", 1, 0, lambda: press_number(7))
btn("8", 1, 1, lambda: press_number(8))
btn("9", 1, 2, lambda: press_number(9))
btn("×", 1, 3, lambda: press_operation("multiply"), bg="#B8D4F1")

btn("4", 2, 0, lambda: press_number(4))
btn("5", 2, 1, lambda: press_number(5))
btn("6", 2, 2, lambda: press_number(6))
btn("-", 2, 3, lambda: press_operation("subtract"), bg="#B8D4F1")

btn("1", 3, 0, lambda: press_number(1))
btn("2", 3, 1, lambda: press_number(2))
btn("3", 3, 2, lambda: press_number(3))
btn("+", 3, 3, lambda: press_operation("add"), bg="#B8D4F1")

btn("0", 4, 0, lambda: press_number(0), colspan=2)
btn("=", 4, 2, calculate_result, bg="#7FB3D5", fg="white", colspan=2)

# ------------------ Historial ------------------------
tk.Label(
    root,
    text="Historial",
    bg="#EAF2FB",
    fg="#2C3E50",
    font=("Segoe UI", 11, "bold"),
    anchor="w"
).pack(fill="x", padx=18, pady=(10, 2))

# Marco visual del historial (BARRA / BORDE)
history_frame = tk.Frame(
    root,
    bg="#B8D4F1",
    bd=1
)
history_frame.pack(fill="x", padx=15, pady=4)

history_box = tk.Text(
    history_frame,
    height=6,
    state="disabled",
    bg="#FDFEFE",
    fg="#2C3E50",
    bd=0,
    highlightthickness=0
)
history_box.pack(fill="both", padx=6, pady=6)

def update_history():
    history_box.config(state="normal")
    history_box.delete("1.0", tk.END)

    last_line = None

    for item in get_history():
        item = item.strip()
        if not item:
            continue
        if item == last_line:
            continue

        if item.count("=") > 1:
            left, result = item.split("=")[0:2]
            item = f"{left.strip()} = {result.strip()}"

        history_box.insert(tk.END, item + "\n")
        last_line = item

    history_box.config(state="disabled")


tk.Button(
    root,
    text="Limpiar historial",
    command=lambda: (clear_history(), update_history()),
    bg="#AED6F1",
    fg="#2C3E50",
    relief="flat"
).pack(pady=8)

# ------------------- Teclado ----------------------
root.bind("<Return>", lambda e: calculate_result())

# ------------------- Inicio ------------------------
update_history()
root.mainloop()
