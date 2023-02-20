#!/usr/bin/env python3
from brain_games.game_engine import game_run
from brain_games.games import brain_gcd


def main():
    game_run(brain_gcd)


if __name__ == '__main__':
    main()
