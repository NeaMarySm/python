import random


def print_field(matrix):
    print(matrix[0], matrix[1], matrix[2])
    print(matrix[3], matrix[4], matrix[5])
    print(matrix[6], matrix[7], matrix[8])


def get_free_cells(matrix):
    return list(filter(lambda x: x != 'X' and x != 'O', matrix))


def user_step(player, matrix):
    number = 0
    free_cells = get_free_cells(matrix)
    while not number in range(1, 10) or not number in free_cells:
        number = int(input(f'Enter number of the cell to put {player}: '))
    make_step(number, matrix, player)


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


def bot_step(matrix, player):
    print(f'Bot puts {player}')
    free = get_free_cells(matrix)
    idx = random.randint(0, len(free)-1)
    make_step(free[idx], matrix, player)
