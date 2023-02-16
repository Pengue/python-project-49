#!/usr/bin/env python3
import math
import prompt
import random
import brain_games.cli


def check_answer_brain_calc(correct_answer, answer):
    if str(correct_answer) == (answer):
        return True
    else:
        return False


def brain_gcd():
    name = brain_games.cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        correct_answer = math.gcd(first_number, second_number)
        answer = prompt.string(
                            f'Question: {first_number} ' +
                            f'{second_number}\nYour answer: '
                            )
        if check_answer_brain_calc(correct_answer, answer) is True:
            print('Correct!')
            i += 1
        else:
            brain_games.cli.game_over(answer, correct_answer, name)
            break
    if i == 3:
        return print(f'Congratulations, {name}!')
    return
