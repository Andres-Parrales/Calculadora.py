#history.py

_history = []  #Lista privada para guardar operaciones

def add_to_history(operation: str, result: float):
    """
    Save a operation in history
    """
    _history.append(f"{operation} = {result}")

def get_history():
    """
    Returns a copy of the history.
    """
    return _history.copy()

def clear_history():
    """
    Clear the all history
    """
    _history.clear()


