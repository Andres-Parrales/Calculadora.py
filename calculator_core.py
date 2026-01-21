# calculator_core.py
import ast
import operator

from errors import CalculatorError, DivisionByZeroError, InvalidOperationError

# Operadores permitidos
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}

def evaluate_expression(expression: str) -> float:
    try:
        tree = ast.parse(expression, mode="eval")
        return _eval(tree.body)
    except ZeroDivisionError:
        raise DivisionByZeroError("No se puede dividir por cero")
    except Exception:
        raise InvalidOperationError("Expresión inválida")

def _eval(node):
    if isinstance(node, ast.Constant):  # números
        return node.value

    if isinstance(node, ast.BinOp):  # operaciones binarias
        left = _eval(node.left)
        right = _eval(node.right)
        op_type = type(node.op)

        if op_type not in OPERATORS:
            raise InvalidOperationError("Operador no permitido")

        return OPERATORS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):  # negativos
        operand = _eval(node.operand)
        op_type = type(node.op)

        if op_type not in OPERATORS:
            raise InvalidOperationError("Operador no permitido")

        return OPERATORS[op_type](operand)

    raise InvalidOperationError("Expresión inválida")
