# Задача 16:

# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2
import random


def count(num, numbers):
    count = 0
    for i in numbers:
        if i == num:
            count += 1
    return count


N = int(input('Enter number of elements: '))
X = int(input('What number count? '))

numbers = []

for i in range(0, N):
    num = random.randint(1, int(N/2))
    numbers.append(num)

print(numbers)

result = count(X, numbers)
print('Number', num, 'appears ', result, 'times')

# count = numbers.count(X)
# print(count)
