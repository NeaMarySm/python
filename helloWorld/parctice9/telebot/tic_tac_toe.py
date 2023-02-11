import random


def print_field(matrix):
    return f'{matrix[0]} | {matrix[1]} | {matrix[2]}\n{matrix[3]} | {matrix[4]} | {matrix[5]}\n{matrix[6]} | {matrix[7]} | {matrix[8]}'
    print(matrix[0], matrix[1], matrix[2])
    print(matrix[3], matrix[4], matrix[5])
    print(matrix[6], matrix[7], matrix[8])


def get_free_cells(matrix):
    return list(filter(lambda x: x != 'X' and x != 'O', matrix))


# def user_step(player, matrix):
#     number = 0
#     free_cells = get_free_cells(matrix)
#     while not number in range(1, 10) or not number in free_cells:
#         number = int(input(f'Enter number of the cell to put {player}: '))
#     make_step(number, matrix, player)


def number_check(num, matrix):
    if not num in range(1, 10) or not num in get_free_cells(matrix):
        return False
    else:
        return True


def is_playing(matrix):
    if (matrix[0] == matrix[1] == matrix[2]) or \
        (matrix[3] == matrix[4] == matrix[5]) or \
        (matrix[6] == matrix[7] == matrix[8]) or \
        (matrix[0] == matrix[3] == matrix[6]) or \
        (matrix[1] == matrix[4] == matrix[7]) or \
        (matrix[2] == matrix[5] == matrix[8]) or \
        (matrix[0] == matrix[4] == matrix[8]) or \
            (matrix[2] == matrix[4] == matrix[6]):
        return False
    else:
        return True


def make_step(cell, matrix, player):
    matrix[cell-1] = player


def bot_cell(matrix):
    # print(f'Bot puts {player}')
    free = get_free_cells(matrix)
    idx = random.randint(0, len(free)-1)
    return free[idx]


def change_player(current, pl1, pl2):
    if current == pl1:
        return pl2
    else:
        return pl1
