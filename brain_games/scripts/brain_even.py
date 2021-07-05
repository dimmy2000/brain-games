#!/usr/bin/env python3
"""This is the script of brain even game."""
from brain_games.games import even
from brain_games.games.engine import play


def main():
    """Play brain even game."""
    play(even)


if __name__ == "__main__":
    main()
