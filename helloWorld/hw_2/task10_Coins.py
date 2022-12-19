# Задача 10

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

import random
n = int(input('Enter number of coins: '))
coins = []

for i in range(0, n):
    num = random.randint(0, 1)
    coins.append(num)

print(coins)

count_zero = 0
count_one = 0

for coin in coins:
    if coin == 0:
        count_zero += 1
    else:
        count_one += 1

min = count_zero
if count_one < count_zero:
    min = count_one

print(f'You need to turn at least {min} coins')
