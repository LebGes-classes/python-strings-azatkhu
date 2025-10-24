print('Введите текст, состоящий из слов на англ языке и заканчивающийся точкой (символ точка в тексте единственный). Каждое слово состоит из англ букв, длина слова не превышает 20 символов')

text = input()
words = []
word = ''
text_filtered = []
is_sentence_ready = 0
maxx_len_word = 0
alphabet_small = 'abcdefghijklmnopqrstuvwxyz'
alphabet_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text_encrypted = ''
list_encrypted = []


while '.' not in text:
    print('Предложение должно оканчиваться символом "."')
    text = input()

for i in range(len(text)):
    if (text[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,. ') and (is_sentence_ready == 0):
        
        if text[i] != '.':
            
            if text[i] != ' ' and len(word) != 20:
                word += text[i]
            elif text[i] != ' ' and len(word) == 20:
                words += [word] 
                word = text[i]
            elif text[i] == ' ' and len(word) != 0:
                words += [word]
                word = ''

        else:
            is_sentence_ready = 1

if len(word) != 0:
    words += [word]
        
word = ''
list_encrypted = [''] * len(words) 

for i in words:
    for j in i:
        text_filtered += j

for i in range(len(words)):
    if len(words[i]) > maxx_len_word:
        maxx_len_word = len(words[i])

K = maxx_len_word 

for i in range(len(text_filtered)): 
    if text_filtered[i] in alphabet_big:

        for j in range(len(alphabet_big)):
            if text_filtered[i] == alphabet_big[j]:
                res = j

        if res + K > 25: 
            i_replaced = res + K - 26
        else:
            i_replaced = res + K
        text_filtered[i] = alphabet_big[i_replaced]

    elif text_filtered[i] in alphabet_small:

        for j in range(len(alphabet_small)):
            if text_filtered[i] == alphabet_small[j]:
                res = j
                
        if res + K > 25: 
            i_replaced = res + K - 26
        else:
            i_replaced = res + K
        text_filtered[i] = alphabet_small[i_replaced]

count = 0

for i in range(len(words)):
    while len(list_encrypted[i]) != len(words[i]):
        list_encrypted[i] += text_filtered[count]
        count += 1

for i in list_encrypted:
    if i != list_encrypted[-1]:
        text_encrypted += i
        text_encrypted += ' '
    else:
        text_encrypted += i
        text_encrypted += '.'

print(text_encrypted)