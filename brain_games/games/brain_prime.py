#!/usr/bin/env python3
import prompt
import random
import brain_games.cli
from brain_games.games.brain_even import compare_answer


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    elif a == 1:
        return 'no'
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    if d * d > a is True:
        return 'yes'
    else: 
        return 'no'


def sules():
    return('Answer "yes" if given number is prime. Otherwise answer "no".')


def run():
    question = random.randint(1, 100)
    correct_answer = compare_answer(is_prime(question))
    return question, correct_answer
    
