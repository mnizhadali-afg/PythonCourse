import random

def roll_die():
    """Roll two dice and return their face values as a tuple"""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)

def display_dice(dice):
    die1, die2 = dice
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')

die_values = roll_die()
display_dice(die_values)

sum_of_dice = sum(die_values)

if sum_of_dice in (7, 11): #win
    game_status = 'Won'
elif sum_of_dice in (2, 3, 12): #lost
    game_status = 'Lost'
else:
    game_status = 'Continue' #continue rolling
    my_point = sum_of_dice
    print('Point is: ', my_point)

while game_status == 'Continue':
    die_values = roll_die()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point:
        game_status = 'Won'
    elif sum_of_dice == 7:
        game_status = 'Lost'

if game_status == 'Won':
    print('Player WON')
else:
    print('Player Lost')