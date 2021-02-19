string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'
print(string)

# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'

string = string.replace(',', '')
print(string)

# 2. Найти индекс самой последней буквы 's' в строке.
#    Результат: 53

string1 = string.rindex('s')
print(string1)

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6

string2 = string.count('i') + string.count('I')
print(string2)

# 4. Найти и вывести срез строки.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)

print(string.find('si'), string.rindex(' of'))
print(string [15:32])


# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'

print(string[:34].replace(',', '') * 3 + string[34:].replace(',', ''))