"""
    Вводится строка.
    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""
string = input('Введите строку: ')

"""
word = ''

for char in string:
    if char.isalpha():
        word = len(char)

print(word)
print(char)
"""

string = string.strip()
var = biggest = 0

var += len(string.split())

for word in string.split():
    if len(word) > biggest:
        biggest = len(word)
        words = word
print('В строке', var, 'слов, \nсамое длиное слово -', words, ',', biggest, 'символов')