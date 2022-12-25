from colored import fg, bg, attr
class ColorGenerator():
    def color_get(bg_color = '', fg_color = ''):
        result = ''
        if(bg_color != ''):
            result += bg(bg_color)
        if(fg_color != ''):
            result += fg(fg_color)
        return result
    
    def color_reset():
        return attr('reset')

class PlayerHelper():
    def __init__(self) -> None:
        pass
    def get_number_of_play():
        print (ColorGenerator.color_get(fg_color='green') + 'How many time do you want play?' + ColorGenerator.color_get())
        return input()

    def game_level():
        return input(ColorGenerator.color_get(fg_color='green') + 'What level would you like to play? (advance, hard, medium , easy, s easy) > ' + ColorGenerator.color_reset())
    
    def kind_of_math_operation():
        return input(ColorGenerator.color_get(fg_color='green') + 'What kind of math operation would you like to play? (*, /, %, +, -) > ' + ColorGenerator.color_reset())
    
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

    def get_randomNumber(start, stop):
        return random.randrange(start, stop)
    
    def get_math_problem_byLevel():
        match user_game_level:
            case 's easy':
                first_rnd = PlayerHelper.get_randomNumber(2,10)
                second_rnd = PlayerHelper.get_randomNumber(2,10)
                return {'problem': f'{first_rnd} {math_operation_type} {second_rnd}' , 'solution': f'{PlayerHelper.get_solution(first_rnd, second_rnd)}'}
            case 'easy':
                first_rnd = PlayerHelper.get_randomNumber(2,10)
                second_rnd = PlayerHelper.get_randomNumber(2,12)
                return {'problem': f'{first_rnd} {math_operation_type} {second_rnd}' , 'solution': f'{PlayerHelper.get_solution(first_rnd, second_rnd)}'}
            case 'medium':
                first_rnd = PlayerHelper.get_randomNumber(2,10)
                second_rnd = PlayerHelper.get_randomNumber(2,101)
                return {'problem': f'{first_rnd} {math_operation_type} {second_rnd}' , 'solution': f'{PlayerHelper.get_solution(first_rnd, second_rnd)}'}
            case 'hard':
                first_rnd = PlayerHelper.get_randomNumber(2,101)
                second_rnd = PlayerHelper.get_randomNumber(2,101)
                return {'problem': f'{first_rnd} {math_operation_type} {second_rnd}' , 'solution': f'{PlayerHelper.get_solution(first_rnd, second_rnd)}'}
            case 'advance':
                first_rnd = PlayerHelper.get_randomNumber(101,1001)
                second_rnd = PlayerHelper.get_randomNumber(101,1001)
                return {'problem': f'{first_rnd} {math_operation_type} {second_rnd}' , 'solution': f'{PlayerHelper.get_solution(first_rnd, second_rnd)}'}


    
print ('Hello World !')
print('Welcome to math quiz!')
number_of_play = PlayerHelper.get_number_of_play()
while number_of_play.isnumeric() != True:
    print(ColorGenerator.color_get(fg_color='red') + 'Please enter correct number!' + ColorGenerator.color_reset())
    number_of_play = PlayerHelper.get_number_of_play()


game_levels = ('advance', 'hard', 'medium' , 'easy', 's easy') 
user_game_level = PlayerHelper.game_level()

while user_game_level not in game_levels:
    print(ColorGenerator.color_get(fg_color='red') + 'Please enter correct level!' + ColorGenerator.color_reset())
    print(ColorGenerator.color_get(fg_color='purple_4a') + '(advance, hard, medium , easy, s easy)' + ColorGenerator.color_reset())
    user_game_level = PlayerHelper.game_level()



math_operation_type_tuple = ('*', '/', '%', '+', '-')
math_operation_type = PlayerHelper.kind_of_math_operation()

while math_operation_type not in math_operation_type_tuple:
    print(ColorGenerator.color_get(fg_color='red') + 'Please enter correct math operation!' + ColorGenerator.color_reset())
    print(ColorGenerator.color_get(fg_color='purple_4a') + '(*, /, %, +, -)' + ColorGenerator.color_reset())
    math_operation_type = PlayerHelper.kind_of_math_operation()


        
import random


math_problems = []
for x in range(0, int(number_of_play)):
    math_problems.append(PlayerHelper.get_math_problem_byLevel())

for idx, x in enumerate(math_problems):
    user_solution = input(ColorGenerator.color_get(fg_color='green') + f"your {idx} problem: {x['problem']}="  + ColorGenerator.color_reset())
    
    while user_solution != x['solution']:
        print(ColorGenerator.color_get(fg_color='red') + "your put wrong answer! try again or give up by type 'ies' that instant for 'i eat shit'" + ColorGenerator.color_reset())
        user_solution = input(f"your {idx+1} solution: {x['problem']}= ")
        if(user_solution == 'ies'):
            print(ColorGenerator.color_get(fg_color='purple_4a') + f"the correct answer was {x['solution']}" + ColorGenerator.color_reset())
            break