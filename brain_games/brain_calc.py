import prompt
import random
from brain_games.cli import welcome_user


def return_correct_answer(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number


def check_answer_brain_calc(correct_answer, answer):
    if int(correct_answer) == int(answer):
        return True
    else:
        return False


def brain_calc():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        operation = random.choice(['+', '-', '*'])
        correct_answer = return_correct_answer(first_number, second_number, \
            operation)
        answer = prompt.string(f'Question: {first_number} {operation} \
            {second_number}\nYour answer: ')
        if check_answer_brain_calc(correct_answer, answer) is True:
            print('Correct!')
            i += 1
        else:
            i = 4
            print(f"'{answer}' is wrong answer ;(. Correct answer was \
                '{correct_answer}' .")
            print(f"Let's try again, {name}!")
    if i == 3:
        return print(f'Congratulations, {name}!')
