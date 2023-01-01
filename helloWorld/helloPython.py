# print('hello Python!')
# a = True
# print(type(a))

# Немного о строках
text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6])  # сеикакл
print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...
print(text)


exit()
list = [1, 2, 3]
print(list)
# in_list = 4 in list  # False
in_list = not 4 in list  # True
print(in_list)
print('**********')
num = 3
is_odd = not num % 2 is 0  # True
print(num, 'is odd ?', is_odd)
print(num + num)
