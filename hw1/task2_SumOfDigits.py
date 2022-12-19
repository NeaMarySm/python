# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


def sum_of_digits(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum


number = int(input('Enter your number: '))
sum = sum_of_digits(number)
print(f'Sum of digits is {sum}')
