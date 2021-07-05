#!/usr/bin/env python3
"""This is the script of brain prime game."""
from brain_games.games import prime
from brain_games.games.engine import play


def main():
    """Play brain prime game."""
    play(prime)


if __name__ == "__main__":
    main()
