from colored import fg, bg, attr
def color_get(bg_color = '', fg_color = ''):
    result = ''
    if(bg_color != ''):
        result += bg(bg_color)
    if(fg_color != ''):
        result += fg(fg_color)
    return result

def color_reset():
    return attr('reset')

print ('Hello World !')
print('Welcome to math quiz!')

def get_number_of_play():
    print (color_get(fg_color='green') + 'How many time do you want play?' + color_reset())
    return input()

number_of_play = get_number_of_play()

while number_of_play.isnumeric() != True:
    print(color_get(fg_color='red') + 'Please enter correct number!' + color_reset())
    number_of_play = get_number_of_play()

def game_level():
    return input(color_get(fg_color='green') + 'What level would you like to play? (advance, hard, medium , easy, s easy) > ' + color_reset())

game_levels = ('advance', 'hard', 'medium' , 'easy', 's easy') 
user_game_level = game_level()

while user_game_level not in game_levels:
    print(color_get(fg_color='red') + 'Please enter correct level!' + color_reset())
    print(color_get(fg_color='purple_4a') + '(advance, hard, medium , easy, s easy)' + color_reset())
    user_game_level = game_level()

def kind_of_math_operation():
    return input(color_get(fg_color='green') + 'What kind of math operation would you like to play? (*, /, %, +, -) > ' + color_reset())

math_operation_type_tuple = ('*', '/', '%', '+', '-')
math_operation_type = kind_of_math_operation()

while math_operation_type not in math_operation_type_tuple:
    print(color_get(fg_color='red') + 'Please enter correct math operation!' + color_reset())
    print(color_get(fg_color='purple_4a') + '(*, /, %, +, -)' + color_reset())
    math_operation_type = kind_of_math_operation()

def get_solution(first_rnd, second_rnd):
    match math_operation_type:
        case '*':
            return first_rnd * second_rnd
        case '/':
            return first_rnd / second_rnd
        case '%':
            return first_rnd % second_rnd
        case '+':
            return first_rnd + second_rnd
        case '-':
            return first_rnd - second_rnd
        
import random
def get_randomNumber(start, stop):
    return random.randrange(start, stop)
def get_math_problem_byLevel():
    match user_game_level:
        case 's easy':
            first_rnd = get_randomNumber(2,10)
            second_rnd = get_randomNumber(2,10)
            return {'problem': f'{first_rnd} {math_operation_type} {second_rnd}' , 'solution': f'{get_solution(first_rnd, second_rnd)}'}
        case 'easy':
            first_rnd = get_randomNumber(2,10)
            second_rnd = get_randomNumber(2,12)
            return {'problem': f'{first_rnd} {math_operation_type} {second_rnd}' , 'solution': f'{get_solution(first_rnd, second_rnd)}'}
        case 'medium':
            first_rnd = get_randomNumber(2,10)
            second_rnd = get_randomNumber(2,101)
            return {'problem': f'{first_rnd} {math_operation_type} {second_rnd}' , 'solution': f'{get_solution(first_rnd, second_rnd)}'}
        case 'hard':
            first_rnd = get_randomNumber(2,101)
            second_rnd = get_randomNumber(2,101)
            return {'problem': f'{first_rnd} {math_operation_type} {second_rnd}' , 'solution': f'{get_solution(first_rnd, second_rnd)}'}
        case 'advance':
            first_rnd = get_randomNumber(101,1001)
            second_rnd = get_randomNumber(101,1001)
            return {'problem': f'{first_rnd} {math_operation_type} {second_rnd}' , 'solution': f'{get_solution(first_rnd, second_rnd)}'}


math_problems = []
for x in range(0, int(number_of_play)):
    math_problems.append(get_math_problem_byLevel())

for idx, x in enumerate(math_problems):
    user_solution = input(color_get(fg_color='green') + f"your {idx} problem: {x['problem']}="  + color_reset())
    
    while user_solution != x['solution']:
        print(color_get(fg_color='red') + "your put wrong answer! try again or give up by type 'ies' that instant for 'i eat shit'" + color_reset())
        user_solution = input(f"your {idx+1} solution: {x['problem']}= ")
        if(user_solution == 'ies'):
            print(color_get(fg_color='purple_4a') + f"the correct answer was {x['solution']}" + color_reset())
            break