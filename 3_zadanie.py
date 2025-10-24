import re

text = input('Введите текст: ')
text_lower = []
text_space_fixed = re.sub(r'\s+', ' ', text)
words = re.findall(r'\b\w+\b', text_space_fixed)

text_split = []
word = ''
alphabet_small = 'abcdefghijklmnopqrstuvwxyz'
alphabet_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text_lower = ''
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for letter in text_space_fixed:
    for i in range(26, len(letters)):
        if letter == letters[i]:
            letter = letters[i-26]
            print(letter)
            input()
    text_lower += letter
'''
for i in text_space_fixed:
    for j in range(len(alphabet_big)):
        if i == alphabet_big[j]:
            i = alphabet_small[j]
    text_lower += i'''
print(text_lower, '1lower')
pattern = re.findall(r'[a-zа-я]+', text_lower)
print(pattern)

#text_split = text_lower.split()
'''for i in range(len(text_lower)):
    if text_lower[i] != ' ':
        word += text_lower[i]
    else:
        text_split += [word]
        word = ''
if len(word) != 0:
    text_split += [word]
print(text_lower)
input()
print(text_split)
input()'''

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

print(pattern)