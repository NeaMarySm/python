# Задача 12

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
import math

sum = int(input('Enter the sum of numbers: '))
prod = int(input('Enter the product of numbers: '))

numbers = range(1, 1001)

d = sum**2 - 4*prod
first = (sum - math.sqrt(d))/2
second = (sum + math.sqrt(d))/2

if not first in numbers or not second in numbers:
    print('No solutions in the current range of natural numbers')
else:
    print('First number: ', int(first), '\nSecond number: ', int(second))
