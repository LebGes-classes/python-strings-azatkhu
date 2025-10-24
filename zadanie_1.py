text = input('Введите текст: ')

word = ''
text_mirrored = ''
text_reversed = ''  
list_of_words = []
reversed_list = []

for i in range(len(text)):
    
    if text[i] != ' ':
        word += text[i]
    elif text[i] == ' ' and len(word) != 0:
        list_of_words += [word]
        word = ''

list_of_words += [word]

for i in range(len(list_of_words) - 1, -1,-1):
    text_mirrored += list_of_words[i]
    reversed_list += [list_of_words[i]]
    
    if i != 0:
        text_mirrored += ' '

for i in range(len(reversed_list)):
    for j in range(len(reversed_list[i]) - 1, -1, -1):
        text_reversed += reversed_list[i][j]
        
    if i != reversed_list[-1]:
        text_reversed += ' '

print('Строка в зеркальном и обратном порядке: ', text_reversed)