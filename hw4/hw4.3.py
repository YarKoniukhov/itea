"""
    Написать программу, которая принимает номер телефона в любом формате:
    +38 (050) 12-34-567 или 099 123 -45 67 или 80501234567 или 888 050 123 4567
    а выводит в формате: 380501234567.
    Если цифр в номере недостаточно, чтобы описать номер в нужном формате -
        попросить пользователя повторить ввод.
"""

phone = input('Enter phone number: ')

number = ''

for i in phone:
    if i.isdigit():
        number = number + i

if len(number) < 8:
    print('Повторите ввод номера!')
elif len(number) == 9:
    print('380' + number)
elif len(number) == 10:
    print('38' + number)
elif len(number) == 11:
    print('3' + number)

print(number)
