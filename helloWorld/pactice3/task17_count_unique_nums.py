# Задача №17

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random


def generate_random_list(length, min=1, max=100):
    numbers = list()
    for i in range(0, length):
        item = random.randint(min, max)
        numbers.append(item)
    return numbers


length = int(input('Enter list length: '))

numbers = generate_random_list(length, 1, 20)
print(numbers)
temp = []
for i in numbers:
    if i in temp:
        continue
    else:
        temp.append(i)
result = len(temp)
print(temp)
print(result)
