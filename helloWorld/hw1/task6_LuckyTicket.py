# Задача 6

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

def sum_of_digits(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    return sum


def is_lucky(number):
    first = number//1000
    last = number % 1000
    if sum_of_digits(first) == sum_of_digits(last):
        return 'Yes'
    return 'No'


ticket = int(input('Enter ticket number (six digits): '))
result = is_lucky(ticket)
print(result)
