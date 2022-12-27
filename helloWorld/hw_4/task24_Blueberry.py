# Задача 24:

# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# Input: 4

# (значения сгенерированы случайным образом
# 4 2 3 1 )
# Output: 9

import random


def generate_random_list(length, min=1, max=100):
    numbers = list()
    for i in range(0, length):
        item = random.randint(min, max)
        numbers.append(item)
    return numbers


length = int(input('Enter number of bushes: '))

berries = generate_random_list(length, 15, 50)
print(f'Berries per bush: {berries}')

sums = []
for i in range(0, len(berries)):
    if i == 0:
        sum = berries[i+1] + berries[i] + berries[len(berries)-1]
    elif i == len(berries)-1:
        sum = berries[i-1] + berries[i] + berries[0]
    else:
        sum = berries[i-1]+berries[i]+berries[i+1]
    sums.append(sum)
result = max(sums)
print(f'Max amount of berries: {result}')
