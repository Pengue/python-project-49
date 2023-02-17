#!/usr/bin/env python3
import prompt
import random
import brain_games.cli


def return_correct_answer(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number


def check_answer(correct_answer, answer):
    if str(correct_answer) == (answer):
        return True
    else:
        return False


def brain_calc():
    name = brain_games.cli.welcome_user()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        operation = random.choice(['+', '-', '*'])
        correct_answer = return_correct_answer(first_number,
                                               second_number, operation)
        answer = prompt.string(f'Question: {first_number} '
                               + f'{operation} {second_number}\nYour answer: ')
        if check_answer(correct_answer, answer) is True:
            print('Correct!')
            i += 1
        else:
            brain_games.cli.game_over(answer, correct_answer, name)
            break
    if i == 3:
        return print(f'Congratulations, {name}!')
    return
