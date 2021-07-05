"""This module contains logic of brain-prime game."""
import random


DESCRIPTION = """Answer "yes" if given number is prime. Otherwise answer "no"."""


def is_prime(number: int) -> bool:
    """Checks if given number is prime."""
    if number > 1:
        for i in range(2, number // 2 + 1):
            if (number % i) == 0:
                return False
        else:
            return True
    return False


def get_expression_and_answer() -> tuple:
    answers = ["no", "yes"]
    number = random.randint(1, 101)
    correct_answer = answers[is_prime(number)]
    expression = str(number)
    return correct_answer, expression
