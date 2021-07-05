#!/usr/bin/env python3
"""This is the script of brain greatest common divisor game."""
from brain_games.games import gcd
from brain_games.games.engine import play


def main():
    """Play brain greatest common divisor game."""
    play(gcd)


if __name__ == "__main__":
    main()
