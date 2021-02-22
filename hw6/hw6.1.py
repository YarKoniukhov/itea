"""
     1.
     Создать файл file_practice.txt
     Записать в него строку 'Starting practice with files'
     Файл должен заканчиваться пустой строкой
 """

file = open('../file_practice.txt', 'w')
file.write('Starting practice with files\n')
file.close()

"""
     2.
     Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
     Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""

file = open('../file_practice.txt')
data = file.readline(5).upper()
print(data)
data = file.seek(0)
print(file.read())
file.close()

"""
     3.
     Прочесть файл files/text.txt
     В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
     иначе - заменить все буквы 'e' на 'i'
     Полученный текст дописать в файл file_practice.txt
"""

f = open('../files_text.txt', 'w')
f.write('Proin laoreet dui vel libero dapibus vehicula vitae eget turpis.\n'
        'Nam non eros eu elit posuere posuere id ac turpis.\n'
        'Quisque nec orci blandit, lobortis felis non, eleifend felis.\n'
        'Vivamus at odio at lacus viverra luctus et ut mauris.\n'
        'Etiam vehicula nibh eu quam feugiat tempus.\n')
f.close()

f = open('../files_text.txt')
data1 = f.read()
print(data1)

e = i = 0
for let in data1:
    if let == 'i':
        i += 1
    elif let == 'e':
        e += 1
print(e, i)

if i < e:
    data_rep = data1.replace('i', 'e')
    print(data_rep)
else:
    data_rep = data1.replace('e', 'i')
    print(data_rep)

file = open('../file_practice.txt', 'a')
file.write(data_rep)
f.close()
file.close()

"""
     4.
     Если в файле file_practice.txt четное количество элементов
     - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
     Прочесть весь файл и вывести содержимое
"""

with open('../file_practice.txt') as f:
    num = len(f.read())
    with open('../file_practice.txt', 'a') as file:
        if num % 2 != 0:
            file.write('bye')
        else:
            file.write('the end')
f.close()
file.close()

with open('../file_practice.txt') as f:
    print(f.read())
f.close()

"""
     5.
     В средину файла file_practice.txt вставить строку " *some inserted text* "
     (средина - имеется в виду средина текста)
"""


with open('../file_practice.txt', 'r+') as file:
    file.seek(len(file.read()) // 2)
    file.write(' *some inserted text* ')
    file.close()
