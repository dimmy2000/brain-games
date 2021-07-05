"""This module contains logic of brain-progression game."""
import random


DESCRIPTION = """What number is missing in the progression?"""


def build_progression(start: int, step: int, size: int = 10) -> list:
    """Builds arithmetic progression and returns it as a list."""
    progression = []
    item = start
    for index in range(1, size + 1):
        progression.append(str(item))
        item += step
    return progression


def get_expression_and_answer() -> tuple:
    """Creates task expression and correct answer."""
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    stop = start + step * 10
    progression = build_progression(start, step)
    correct_answer = str(random.randrange(start, stop, step))
    expression = ' '.join(progression)
    expression = expression.replace(correct_answer, "..")
    return correct_answer, expression
