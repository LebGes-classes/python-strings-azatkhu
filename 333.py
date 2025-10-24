import re

text = input('Введите текст: ')

text_space_fixed = re.sub(r'\s+', ' ', text)
words = re.findall(r'\b\w+\b', text_space_fixed)
alphabet_small = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_big =   'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
text_lower = '' 

for i in text_space_fixed:
    for j in range(len(alphabet_big)):
        if i == alphabet_big[j]:
            i = alphabet_small[j]

    text_lower += i

pattern = re.findall(r'[a-zа-я]+', text_lower)
words_frequency = {}
result = {}
a = []
text_split = pattern

for i in range(len(text_split)):
    if text_split[i] not in words_frequency:
        words_frequency[text_split[i]] = text_split.count(text_split[i])

keys_list = list(words_frequency)

for i in range(len(text_split)):
    if text_split.count(text_split[i]) not in a:
        a += [text_split.count(text_split[i])]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] < a[j]:
            k = a[i]
            a[i] = a[j]
            a[j] = k

k = 0

for i in range(len(a)):
    if k != 5:
        
        for j in keys_list:
            if text_split.count(j) == a[i]:

                print(k + 1, ' место - слово/буква:', j, 'количество в тексте:', a[i])
                
                k += 1
                
                if k == 5:
                    break
