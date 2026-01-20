# history.py

_history = []

def add_to_history(operation: str, result=None):
    """
    Save operation in history without duplicating result
    """
    if result is None:
        _history.append(operation)
    else:
        _history.append(f"{operation}")

def get_history():
    return _history.copy()

def clear_history():
    _history.clear()
