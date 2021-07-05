#!/usr/bin/env python3
"""This is the script of brain progression game."""
from brain_games.games import progression
from brain_games.games.engine import play


def main():
    """Play brain progression game."""
    play(progression)


if __name__ == "__main__":
    main()
