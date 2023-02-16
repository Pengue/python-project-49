#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.cli import welcome_user


def brain_progression():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?') 
    a = 0
    while a < 3:
        length_progression = 10
        start = randint(1, 10)
        step = randint(1, 10)
        secret_number = randint(0, length_progression - 1)
        question = ''
        i = 0
        while i < length_progression:
            if question:
                question += ' '
            if i != secret_number:
                question = question + str((start + (step * i)))
                i += 1
            else:
                question += '..'
                correct_answer = str(start + (step * i))
                i += 1
        answer = prompt.string(f'Question: {question}\nYour answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            a += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}' .")
            print(f"Let's try again, {name}!")
            break
    if a == 3:
        return print(f'Congratulations, {name}!')    
