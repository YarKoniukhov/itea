"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.
    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)
    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))
    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "some string".
        Результат: "some edited string".
    (Использовать форматирование строк f либо метод format)
"""

string = 'Lorem, Ipsum, Is, SImPlY, DuMMy, TEXT, Of, The, Printing, INDUSTRY.'

upp_regist = low_regist = title_regist = 0

for char in string:
    if char.isupper():
        upp_regist += 1
    elif char.islower():
        low_regist += 1

print('Some string:', string)
if upp_regist > low_regist:
    print('Some edited string:', string.upper())
elif low_regist > upp_regist:
    print('Some edited string:', string.lower())
else:
    print('Some edited string:', string.swapcase())

print('Some string:', string)
if string.istitle():
    print('Some edited string: done. ' + string)
else:
    print('Some edited string:', string.replace('Lorem', 'draft: '))

print('Some string:', string)
if len(string) > 20:
    string = string[:20]
    print('Some edited string:', string)
else:
    print('Some edited string:', string.ljust(20, '@'))
