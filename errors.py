# errors.py
class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass

class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""
    pass

class InvalidOperationError(CalculatorError):
    """Raised when an invalid operator is requested."""
    pass

