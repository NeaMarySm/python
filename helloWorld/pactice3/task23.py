# Задача №23

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2

import random


def generate_random_list(length, min=1, max=100):
    numbers = list()
    for i in range(0, length):
        item = random.randint(min, max)
        numbers.append(item)
    return numbers


length = int(input('Enter list length: '))
numbers = generate_random_list(length, -5, 15)
print(numbers)
count = 0
for i in range(1, length):
    if numbers[i] > numbers[i-1]:
        count += 1
print(count)
