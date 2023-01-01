# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

total_cranes = 1
while total_cranes % 6:
    total_cranes = int(input('Number of cranes(multiple of six)? '))

pete = int(total_cranes / 6)
serj = pete
kate = total_cranes - (pete + serj)
print("Pete's cranes: ", pete)
print("Serj's cranes: ", serj)
print("Kate's cranes: ", kate)
