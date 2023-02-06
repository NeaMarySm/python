import random


def choose_first():
    return random.randint(1, 2)


def take(sweets_left):
    number = 0
    while not number in range(1, 29) or number > sweets_left:
        number = int(input('How many sweets will you take? '))
    return sweets_left - number


def swap_player(current, player_1, player_2):
    if current == player_1:
        current = player_2
    else:
        current = player_1


def bot_turn(sweets_left, max_take):
    if sweets_left % (max_take+1) == 0:
        amount = random.randint(1, max_take)
        print(f'Bot takes {amount} sweets')
        return sweets_left-amount
    else:
        if sweets_left <= max_take:
            print(f'Bot takes {sweets_left} sweets')
            return 0
        else:
            amount = sweets_left % (max_take+1)
            print(f'Bot takes {amount} sweets')
            return sweets_left-amount
