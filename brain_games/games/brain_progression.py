from random import randint


RULES = 'What number is missing in the progression?'


def generate_round():
    length_progression = randint(5, 10)
    start = randint(1, 10)
    step = randint(1, 10)
    secret_number = randint(0, length_progression - 1)
    question = ' '
    i = 0
    while i < length_progression:
        if i != secret_number:
            question = question.join((start + (step * i)))
            i += 1
        else:
            question = question.join('..')
            correct_answer = str(start + (step * i))
            i += 1
    return question, correct_answer
