import math
import random


RULES = 'Find the greatest common divisor of given numbers.'


def generate_round():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    correct_answer = math.gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return question, correct_answer
