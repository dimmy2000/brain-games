"""This module contains logic of brain-calc game."""
import random
from operator import mul, add, sub


DESCRIPTION = """What is the result of the expression?"""


def get_expression_and_answer() -> tuple:
    """Creates task expression and correct answer."""
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
    }
    operator = random.choice(list(operators.keys()))
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    correct_answer = str(operators[operator](number_1, number_2))
    expression = f"{number_1} {operator} {number_2}"
    return correct_answer, expression
