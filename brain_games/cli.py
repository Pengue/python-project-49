import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hellow, {name}!')
    return name
