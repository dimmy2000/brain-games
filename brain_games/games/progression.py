import random


DESCRIPTION = """What number is missing in the progression?"""


def build_progression(start: int, step: int, items: int = 10) -> list:
    progression = []
    item = start
    for index in range(1, items + 1):
        progression.append(str(item))
        item += step
    return progression


def get_expression_and_answer() -> tuple:
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    stop = start + step * 10
    progression = build_progression(start, step)
    correct_answer = str(random.randrange(start, stop, step))
    expression = ' '.join(progression)
    expression = expression.replace(correct_answer, "..")
    return correct_answer, expression
