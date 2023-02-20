#!/usr/bin/env python3
import random
from brain_games.games.brain_even import compare_answer


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    elif a == 1:
        return 'no'
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run():
    choice = [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17,
              18, 19, 21, 22, 23, 29, 31, 37, 38, 39, 40, 41,
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 90,
              91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    question = random.choice(choice)
    correct_answer = compare_answer(is_prime(question))
    return question, correct_answer
