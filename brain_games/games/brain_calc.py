#!/usr/bin/env python3
import random



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


def run():
    
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    correct_answer = return_correct_answer(first_number,
                                               second_number, operation)
    question = f'Question: {first_number} {operation} {second_number}'
    
    
    return question, correct_answer
