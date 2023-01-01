# Задача №25

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

text = input("Enter something: ")
modified = ','.join(text).split(',')
print(modified)
uniques = set(modified)
print(uniques)
counted = list()
for el in uniques:
    counted.append(tuple([el, modified.count(el)]))
print(counted)

for el in uniques:
    count = 0
    for i in range(0, len(modified)):
        if modified[i] == el:
            if count == 0:
                modified[i] = el
                count = 1
            else:
                temp = str(f'{el}_{count}')
                modified[i] = temp
                count += 1

print(modified)
