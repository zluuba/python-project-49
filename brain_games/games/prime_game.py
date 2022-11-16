from random import randint
from brain_games.body import welcome_user, question, is_correct, lose, win


def prime_rule():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime_welcome():
    welcome_user()
    prime_rule()


def calculations():
    global expression
    expression = randint(2, 100)
    divider = 2
    while divider <= expression / 2:
        if expression % divider == 0:
            return 'no'
        divider += 1
    return 'yes'


def prime_game():
    count = 0
    while count < 3:
        result = calculations()
        answer = question(expression)
        correct = is_correct(answer, result)
        if correct:
            count += 1
            continue
        else:
            lose()
            break
    else:
        win()
