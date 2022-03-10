# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

chars = 'abcdefghijklmnopqrstuvwxyz'

char_index = int(input('Введите номер буквы английского альфавита'))
char = chars[char_index - 1]
print(f'Буква: {char}')
