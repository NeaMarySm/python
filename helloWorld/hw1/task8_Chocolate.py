# Задача 8

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input('Width: '))
length = int(input('Length: '))
pieces = int(input('Number of pieces: '))

if pieces > 0 and pieces < width * length:
    if pieces % width == 0 or pieces % length == 0:
        print('Yes')
    else:
        print('No')
else:
    print('Wrong number of pieces')
