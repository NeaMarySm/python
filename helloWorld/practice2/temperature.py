# Задача №13
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2

import random

n = 10
m = []
for num in range(0, n):
    random_number = random.randint(-10, 50)
    m.append(random_number)

print(n)
print(m)

max = 0
count = 0

for i in m:
    if i > 0:
        count += 1
        if count > max:
            max = count
    else:
        count = 0
print(max)

# def sinoptik(N):
#     days=[]
#     for _ in range(N):
#         days.append(round(random.uniform(-10,50),0))
#     print(days)
#     maxPeriod = maxPeriodResult = 0
#     i = 0
#     while i<N-1:
#         if days[i]>0:
#             while days[i]>0 and i<N-1:
#                 maxPeriod+=1
#                 i+=1
#             if maxPeriodResult<maxPeriod: maxPeriodResult=maxPeriod
#         maxPeriod=0
#         i+=1
#     return maxPeriodResult
