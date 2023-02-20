#!/usr/bin/env python3
import prompt
import brain_games.cli
from brain_games.games import game

max_score = 3

def run_game(game):
    name = brain_games.cli.welcome_user()
    print('What is the result of the expression?')
    score = 0
    while score < max_score:
        question, correct_answer = game.run()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct_answer}'.",
            )
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
        score += 1
    
    print(f'Congratulations, {name}!')
