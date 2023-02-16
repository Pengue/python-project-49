#!/usr/bin/env python3
import prompt
import random
import brain_games.cli
import brain_games.games.brain_even

def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a






def brain_prime():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        qustion = random.randint(1, 100)
        answer = prompt.string(f'Question: {qustion}\nYour answer: ')
        if brain_games.games.brain_even.compare_answer_brain_prime(
                                                                is_prime(qustion), answer
                                                                ) is True:
            print('Correct!')
            i += 1
        else:
            brain_games.cli.lets_try_again(name)
            break
    if i == 3:
        return print(f'Congratulations, {name}!')
