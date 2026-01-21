# Gui.py
import tkinter as tk
from tkinter import messagebox

from calculator_core import evaluate_expression
from history import get_history, clear_history, add_to_history
from errors import CalculatorError

# -------- Configuración ----------
expression = ""

# -------- Ventana ----------
root = tk.Tk()
root.title("Calculadora")
root.geometry("320x600")
root.resizable(False, False)
root.config(bg="#EAF2FB")

# -------- Pantalla ----------
display = tk.Entry(
    root,
    font=("Segoe UI", 26),
    justify="right",
    bd=0,
    relief="flat",
    bg="#FDFEFE",
    fg="#B94444"
)
display.pack(fill="x", padx=15, pady=15)

def update_display(value):
    display.delete(0, tk.END)
    display.insert(tk.END, value)

# -------- Lógica ----------
def press(value):
    global expression
    expression += str(value)
    update_display(expression)

def backspace():
    global expression
    if expression:
        expression = expression[:-1]
        update_display(expression)

def clear_all():
    global expression
    expression = ""
    update_display("")

def calculate_result():
    global expression
    if not expression.strip():
        return
    try:
        result = evaluate_expression(expression)
        add_to_history(f"{expression} = {result}", result)
        expression = str(result)
        update_display(expression)
        update_history()
    except CalculatorError as e:
        messagebox.showerror("Error", str(e))

# -------- Botones ----------
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
btn("(", 0, 1, lambda: press("("))
btn(")", 0, 2, lambda: press(")"))
btn("⌫", 0, 3, backspace)

btn("7", 1, 0, lambda: press("7"))
btn("8", 1, 1, lambda: press("8"))
btn("9", 1, 2, lambda: press("9"))
btn("/", 1, 3, lambda: press("/"))

btn("4", 2, 0, lambda: press("4"))
btn("5", 2, 1, lambda: press("5"))
btn("6", 2, 2, lambda: press("6"))
btn("*", 2, 3, lambda: press("*"))

btn("1", 3, 0, lambda: press("1"))
btn("2", 3, 1, lambda: press("2"))
btn("3", 3, 2, lambda: press("3"))
btn("-", 3, 3, lambda: press("-"))

btn("0", 4, 0, lambda: press("0"), colspan=2)
btn("+", 4, 2, lambda: press("+"))
btn("=", 4, 3, calculate_result, bg="#7FB3D5", fg="white")

# -------- Historial ----------
tk.Label(
    root,
    text="Historial",
    bg="#EAF2FB",
    font=("Segoe UI", 11, "bold"),
    anchor="w"
).pack(fill="x", padx=18, pady=(10, 2))

history_frame = tk.Frame(root, bg="#B8D4F1")
history_frame.pack(fill="x", padx=15)

history_box = tk.Text(
    history_frame,
    height=6,
    state="disabled",
    bg="#FDFEFE",
    bd=0
)
history_box.pack(fill="both", padx=6, pady=6)

def update_history():
    history_box.config(state="normal")
    history_box.delete("1.0", tk.END)
    for item in get_history():
        history_box.insert(tk.END, item + "\n")
    history_box.config(state="disabled")

tk.Button(
    root,
    text="Limpiar historial",
    command=lambda: (clear_history(), update_history()),
    bg="#AED6F1",
    relief="flat"
).pack(pady=8)

# -------- Teclado ----------
root.bind("<Return>", lambda e: calculate_result())

# -------- Inicio ----------
update_history()
root.mainloop()
