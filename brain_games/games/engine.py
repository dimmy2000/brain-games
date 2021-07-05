import prompt
from brain_games.cli import welcome_user
from typing import Any, Callable, TypeVar

GAME_DURATION = 3

F = TypeVar('F', bound=Callable[..., Any])


def play(game: F) -> None:
    name: str = welcome_user()
    score: int = 0
    print(game.DESCRIPTION)
    while True:
        correct_answer, expression = game.get_expression_and_answer()
        print(f"Question: {expression}")
        answer: str = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(
                f"""'{answer}' is wrong answer ;(. """
                f"""Correct answer was '{correct_answer}'.\n"""
                f"""Let's try again, {name}!"""
            )
            break
        if score == GAME_DURATION:
            print(f"Congratulations, {name}!")
            break
