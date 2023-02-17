#!/usr/bin/env python3
import math
import prompt
import random
import brain_games.cli
from brain_games.games.brain_calc import check_answer


def brain_gcd():
    name = brain_games.cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        correct_answer = math.gcd(first_number, second_number)
        print(f'Question: {first_number} {second_number}')
        answer = prompt.string('\nYour answer: ')
        if check_answer(correct_answer, answer) is True:
            print('Correct!')
            i += 1
        else:
            brain_games.cli.game_over(answer, correct_answer, name)
            break
    if i == 3:
        return print(f'Congratulations, {name}!')
    return
