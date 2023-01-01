# Задача №19

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 2
# Output:  [4, 5, 1, 2, 3]

# import random

# def generate_random_list(length, min=1, max=100):
#     numbers = list()
#     for i in range(0, length):
#         item = random.randint(min, max)
#         numbers.append(item)
#     return numbers


length = int(input('Enter range length: '))
shift = int(input('Enter shift amount: '))

numbers = list(range(1, length+1))
print(numbers)

result = list()
for i in range(shift, length+shift):

    if i > length-1:
        result.append(numbers[i-length])
    else:
        result.append(numbers[i])
print(result)

# for i in range(0, shift):
#     last = numbers.pop(-1)
#     numbers.insert(0, last)
# print(numbers)


def shiftList(list, shift):
    if shift < 0:
        for i in range(abs(shift)):
            list.append(list.pop(0))
    else:
        list.reverse()
        for i in range(shift):
            list.append(list.pop(0))
        list.reverse()
    return list


print(shiftList(numbers, shift))

# def shiftList(myList, k):
#     t = k
#     if k > 0
#     else -k

# if k > 0:
#     myList.reverse()
# for _ in range(t):
# myList.append(myList.pop(0))
# if k > 0:
#     myList.reverse()
# return myList
