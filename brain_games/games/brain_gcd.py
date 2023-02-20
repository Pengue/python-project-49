#!/usr/bin/env python3
import math
import random



def rules():
    return 'Find the greatest common divisor of given numbers.'


def run():

    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    correct_answer = math.gcd(first_number, second_number)
    question = f'Question: {first_number} {second_number}'
    return question, correct_answer
    
    
