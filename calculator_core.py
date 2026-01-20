#calculator_core.py

from errors import DivisionByZeroError, InvalidOperationError
from history import add_to_history

def add(a: float, b: float) -> float:
    """Suma dos numeros"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Resta dos numeros"""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplica dos numeros"""
    return a * b

def percent(a: float, b: float) -> float:
    """saca el porcentaje de los numeros"""
    return (a / 100) * b

def divide(a: float, b: float) -> float:
    """Divide dos numeros"""
    if b == 0:
        raise DivisionByZeroError("No se puede dividir por cero")
    return a / b

def calculate(operation: str, a: float, b: float) -> float:
    """Funcion central que decide que operacion ejecutar"""
    
    if operation == "add":
        result = add(a, b)
    
    elif operation == "subtract":
        result = subtract(a, b)
    
    elif operation == "multiply":
        result = multiply(a, b)
    
    elif operation == "percent":
        result = percent(a, b)
    
    elif operation == "divide":
        result = divide(a, b)
        
    else:
        raise InvalidOperationError("Operacion invalida")
    
    add_to_history(f"{a} {operation} {b}", result)
    return result


