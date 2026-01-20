#Gui.py
import tkinter as tk
from tkinter import messagebox

from calculator_core import calculate
from history import get_history, clear_history, add_to_history
from errors import CalculatorError

#-----------Configuracion-----------------
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

#-------------Ventana----------------------
root = tk.Tk()
root.title("Calculadora")
root.geometry("320x520")
root.resizable(False, False)
root.config(bg="#1e1e1e")


#-------------Pantalla---------------------
display = tk.Entry(
    root,
    font=("Segoe UI", 24),
    justify="right",
    bd=10,
    relief="flat",
    bg="#000",
    fg="white"   
)

display.pack(fill="x", padx=10, pady=10)

def update_display(value):
    display.delete(0, tk.END)
    display.insert(tk.END, value)     


#------------Logica----------------------
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
        entry = f"{a} {symbol} {b} = {result}"
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


#-----------------Botones------------------------
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

def btn(text, row, col, cmd, bg="#333", colspan=1):
    tk.Button(
        frame,
        text=text,
        width=5,
        height=2,
        font=("segoe UI", 14),
        bg=bg,
        fg="white",
        relief="flat",
        command=cmd
        ).grid(row=row, column = col, columnspan = colspan, padx=5, pady=5, sticky="nsew")


btn("C", 0, 0, clear_all, bg="#a33")
btn("%", 0, 1, lambda: press_operation("percent"), bg="#555")
btn("÷", 0, 2, lambda: press_operation("divide"), bg="#555")
btn("⌫", 0, 3, backspace, bg="#666")


btn("7", 1, 0, lambda: press_number(7))
btn("8", 1, 1, lambda: press_number(8))
btn("9", 1, 2, lambda: press_number(9))
btn("×", 1, 3, lambda: press_operation("multiply"), bg="#555")

btn("4", 2, 0, lambda: press_number(4))
btn("5", 2, 1, lambda: press_number(5))
btn("6", 2, 2, lambda: press_number(6))
btn("-", 2, 3, lambda: press_operation("subtract"), bg="#555")

btn("1", 3, 0, lambda: press_number(1))
btn("2", 3, 1, lambda: press_number(2))
btn("3", 3, 2, lambda: press_number(3))
btn("+", 3, 3, lambda: press_operation("add"), bg="#555")

btn("0", 4, 0, lambda: press_number(0), colspan=2)
btn("=", 4, 2, calculate_result, bg="#0a84ff", colspan=2)

#------------------Historial------------------------
tk.Label(root, text="Historial", bg="#1e1e1e", fg="white").pack()

history_box = tk.Text(root, height=6, state="disabled", bg="#111", fg="white")
history_box.pack(fill="x", padx=10)

def update_history():
    history_box.config(state="normal")
    history_box.delete(1.0, tk.END)
    for item in get_history():
        history_box.insert(tk.END, item + "\n")
        history_box.config(state="disabled")

tk.Button(
    root,
    text="Limpiar historial",
    command= lambda: (clear_history(), update_history()),
    bg="#444",
    fg="white"
).pack(pady=5)


#-------------------Teclado----------------------
root.bind("<Return>", lambda e: calculate_result())

#-------------------Inicio------------------------
root.mainloop()

