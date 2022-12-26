# Задача 18:

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random


def find_closest(num, numbers):

    for k in numbers:
        if num != k:
            closest = k
            diff = abs(num-k)
            break
    for i in numbers:
        if i == num:
            continue
        elif abs(num-i) < diff:
            closest = i
            diff = abs(num-i)
        elif abs(num-i) == diff:
            if i < closest:
                closest = i
                diff = abs(num-i)
    return closest


N = int(input('Enter number of elements: '))
X = int(input('What number check? '))

numbers = []

for i in range(0, N):
    num = random.randint(1, N)
    numbers.append(num)

print(numbers)

result = find_closest(X, numbers)
print('Closest number to ', X, 'is', result)
