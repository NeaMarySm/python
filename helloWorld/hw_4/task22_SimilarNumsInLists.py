# Задача 22:

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6

# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6

# 6 12

import random


def generate_random_list(length, min=1, max=100):
    numbers = list()
    for i in range(0, length):
        item = random.randint(min, max)
        numbers.append(item)
    return numbers


n = int(input('Enter first list length: '))
m = int(input('Enter second list length: '))

first_list = generate_random_list(n, 1, 20)
second_list = generate_random_list(m, 1, 20)
print(first_list)
print(second_list)

first_set = set(first_list)
second_set = set(second_list)

result = first_set.intersection(second_set)
# result = list(result)
# result_list.sort() нужно ли снова приводить к списку и сортировать?
print(f'first: {result} ')


def find_similar(first, second):
    result = []
    for i in range(0, len(first)):
        for j in range(0, len(second)):
            if first[i] == second[j]:
                if first[i] in result:
                    continue
                else:
                    result.append(first[i])
    result.sort()
    print(f'second: {result} ')


find_similar(first_list, second_list)
