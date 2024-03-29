# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Вывод:
# 2.5 10

import math
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


# def find_farthest_orbit(orbits):
#     ellipses = list(filter(lambda x: x[0] != x[1], orbits))
#     print(ellipses)
#     squares = list(map(lambda s: s[0]*s[1]*math.pi, ellipses))
#     print(squares)
#     return max(squares)

def find_farthest_orbit(orbits):
    # squares = map(lambda s: s[0]*s[1]*math.pi,
    #               filter(lambda x: x[0] != x[1], orbits))

    squares = [math.pi*x[0]*x[1]
               for x in orbits if x[0] != x[1]]  # list comprehension
    max_orbit = list(
        filter(lambda x: math.pi*x[0]*x[1] == max(squares), orbits))
    return max_orbit


print(find_farthest_orbit(orbits))
