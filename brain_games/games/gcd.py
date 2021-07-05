import random
from math import gcd


DESCRIPTION = """Find the greatest common divisor of given numbers."""


def calculate_gcd(number_1: int, number_2: int) -> str:
    return str(gcd(number_1, number_2))


def get_expression_and_answer() -> tuple:
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)
    correct_answer = calculate_gcd(number_1, number_2)
    expression = f"{number_1} {number_2}"
    return correct_answer, expression
