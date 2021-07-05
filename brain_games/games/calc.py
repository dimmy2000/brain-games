import random
from operator import mul, add, sub


DESCRIPTION = """What is the result of the expression?"""


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_expression_and_answer() -> tuple:
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
