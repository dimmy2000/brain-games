#!/usr/bin/env python3
import prompt
import random


def is_even(number: int) -> bool:
    return number % 2 == 0


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    score = 0
    answers = ["no", "yes"]
    while True:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if answer not in answers or answers.index(answer) != is_even(number):
            print(
                f"""'{answer}' is wrong answer ;(. """
                f"""Correct answer was '{answers[is_even(number)]}'.\n"""
                f"""Let's try again, {name}!"""
            )
            break
        elif answers.index(answer) == is_even(number):
            print("Correct!")
            score += 1
        if score == 3:
            print(f"Congratulations, {name}!")
            break


if __name__ == "__main__":
    main()
