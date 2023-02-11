# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import functions as fn


initial_amount = 90
max_per_round = 28
player_1 = 'user'
player_2 = 'bot'

if fn.choose_first() == 1:
    current_player = player_1
else:
    current_player = player_2

sweets_left = initial_amount

while sweets_left != 0:
    print('Sweets left: ', sweets_left)
    print(f'Player_{current_player}')
    if current_player == 'user':
        sweets_left = fn.take(sweets_left)
        current_player = 'bot'
    else:
        sweets_left = fn.bot_turn(sweets_left, max_per_round)
        current_player = 'user'

if current_player == 'user':
    print('Bot has won')
else:
    print('User has won')
