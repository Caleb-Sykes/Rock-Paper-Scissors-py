import random

comp = False
player = False
tie = False

dual_dict = {}

moves = ['rock','paper','scissors']

user_input = input('Enter your Move: ')

comp_input = random.choice(moves)
print('Computers Move: '+comp_input)

if user_input == 'rock':
    dual_dict['player'] = 1
elif user_input == 'paper':
    dual_dict['player'] = 2
elif user_input == 'scissors':
    dual_dict['player'] = 3

if comp_input == 'rock':
    dual_dict['comp'] = 1
elif comp_input == 'paper':
    dual_dict['comp'] = 2
elif comp_input == 'scissors':
    dual_dict['comp'] = 3

#print(dual_dict)

if dual_dict['player'] == dual_dict['comp']:
    print('tie')
elif dual_dict['player'] == 1 and dual_dict['comp'] == 2:
    print('computer wins!!')
elif dual_dict['player'] == 2 and dual_dict['comp'] == 3:
    print('computer wins!!')
elif dual_dict['player'] == 3 and dual_dict['comp'] == 1:
    print('computer wins!!')
else:
    print('player wins!!')
