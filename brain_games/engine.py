import prompt


ROUNDS = 3


def get_user_name_and_show_welcome(game_rule):
    print('Welcome to the Brain Games!')
    user_name = prompt.string("May I have your name? ")
    print(f'Hello, {user_name}!')
    print(game_rule)
    return user_name


def get_user_answer_and_show_question(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def start_game(game):
    game_rule = game.game_rule
    user_name = get_user_name_and_show_welcome(game_rule)
    for _ in range(ROUNDS):
        question, right_answer = game.get_question_and_answer()
        user_answer = get_user_answer_and_show_question(question)
        if user_answer == str(right_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')
