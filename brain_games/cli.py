import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hellow, {name}!')
    return name


def check_parity(number):
    if number % 2 == 0:
        return True
    return False


def compare_answer(parity, answer):
    if parity == True and answer == 'yes':
        return True
    elif parity == False and answer == 'no':
        return True
    return False


def play_strange_game():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        first_qustion = random.randint(1,100)
        answer = prompt.string(f'Question: {first_qustion}\nYour answer: ')
        if compare_answer(check_parity(first_qustion), answer) is True:
            print('Correct!')
            i += 1
        else:
            i = 4
            print(f"Let's try again, {name}!")
    if i == 3:
        return print(f'Congratulations, {name}!')
