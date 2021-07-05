#!/usr/bin/env python3
"""This is the script of brain calc game."""
from brain_games.games import calc
from brain_games.games.engine import play


def main():
    """Play brain calc game."""
    play(calc)


if __name__ == "__main__":
    main()
