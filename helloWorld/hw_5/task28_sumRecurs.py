# Задача 28:

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

first = int(input("enter first number: "))
second = int(input("enter second number: "))


def sumRecurs(a, b):
    if b == 0:
        return a
    return 1+sumRecurs(a, b-1)


res = sumRecurs(first, second)
print(res)
