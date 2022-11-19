import random
from random import randint


game_rule = 'calculator_game'


def get_expression_parts():
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    return num1, num2, operator


# create one simple math expression, calculate the result
# example: '14 + 9', '23 - 7', '5 * 12'
def get_expression_and_result():
    num1, num2, operator = get_expression_parts()
    expression = f'{num1} {operator} {num2}'
    if operator == "+":
        result_int = num1 + num2
    elif operator == "-":
        result_int = num1 - num2
    else:
        result_int = num1 * num2
    return result_int, expression


# generate lists of mathematical expressions and their answers
def get_calc_lists():
    questions_calc_list = []
    results_calc_list = []
    for count in range(3):
        result, expression = get_expression_and_result()
        questions_calc_list.append(expression)
        results_calc_list.append(str(result))
    return questions_calc_list, results_calc_list


# run the create lists function pass its result to the
# variables that the engine imports
calc_questions, calc_results = get_calc_lists()
