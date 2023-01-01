# Задача №27

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13
input = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# words = input.split()
# uniques = set(words)
# print(uniques)
# print(len(uniques))

count = 1
result = list()
word = ''
for i in input:
    if i == ' ' or i == '.':
        if not word in result:
            result.append(word)
        word = ''
        count += 1
    else:
        word += i.lower()


print(result)
print(len(result))
