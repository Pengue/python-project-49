#!/usr/bin/env python3
import prompt
import random
import brain_games.cli


def check_parity(number):
    if number % 2 == 0:
        return True
    return False


def compare_answer(parity, answer):
    if parity is True and answer == 'yes':
        return True
    elif parity is False and answer == 'no':
        return True
    return False


def brain_even():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        first_qustion = random.randint(1, 100)
        answer = prompt.string(f'Question: {first_qustion}\nYour answer: ')
        if compare_answer(
                        check_parity(first_qustion),
                        answer
                        ) is True:
            print('Correct!')
            i += 1
        else:
            brain_games.cli.lets_try_again(name)
            break
    if i == 3:
        return print(f'Congratulations, {name}!')
    return