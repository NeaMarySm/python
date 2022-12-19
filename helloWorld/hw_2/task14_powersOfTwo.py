# Задача 14

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Enter your number: '))
powers = []
for i in range(0, n):
    if 2**i > n:
        break
    powers.append(2**i)

print(powers)
