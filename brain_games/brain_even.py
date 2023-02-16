import prompt
import random
from cli import welcome_user
#----------------------------brain-even--------------------------------------------------
def check_parity(number):
    if number % 2 == 0:
        return True
    return False


def compare_answer_brain_even(parity, answer):
    if parity is True and answer == 'yes':
        return True
    elif parity is False and answer == 'no':
        return True
    return False


def brain_even():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        first_qustion = random.randint(1, 100)
        answer = prompt.string(f'Question: {first_qustion}\nYour answer: ')
        if compare_answer_brain_even(check_parity(first_qustion), answer) is True:
            print('Correct!')
            i += 1
        else:
            i = 4
            print(f"Let's try again, {name}!")
    if i == 3:
        return print(f'Congratulations, {name}!')
#----------------------------------------------------------------------------------------