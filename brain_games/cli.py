import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    return print(f'Hellow, {name}!')

def brain_even():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    first_qustion = random.randint(1,100)
    answer = prompt.string(f'Question: {first_qustion}\nYour answer: ')
    if first_qustion % 2 == True
    