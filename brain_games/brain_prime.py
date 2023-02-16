#!/usr/bin/env python3
import prompt
import random
from brain_games.cli import welcome_user


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def compare_answer_brain_prime(parity, answer):
    if parity is True and answer == 'yes':
        return True
    elif parity is False and answer == 'no':
        return True
    return False


def brain_prime():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        qustion = random.randint(1, 100)
        answer = prompt.string(f'Question: {qustion}\nYour answer: ')
        if compare_answer_brain_prime(is_prime(qustion), answer) is True:
                print('Correct!')
                i += 1
        else:
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        return print(f'Congratulations, {name}!')
