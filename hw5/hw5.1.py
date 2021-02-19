"""
    Генератор паролей.
    Пользователь выбирает 1 из 3 вариантов:
    1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)
    2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)
    3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
        (для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)
    Для решения использовать:
    - константы строк из модуля string (ascii_letters, digits и т.д.)
    - функцию choice из модуля random (для выборки случайного элемента из последовательности)
    - функцию randint из модуля random (для генерации случайной длины сложного пароля от 8 до 16 символов)
    Дополнительно:
    1. Позволить пользователю выбирать длину пароля, но предупреждать, что
        пароль ненадежный, если длина меньше 8 символов
    2. Добавить еще вариант генерации пароля - 4. Пользовательский пароль:
        - пользователь вводил пул символов, из которых будет генерироваться пароль
        - вводит длину желаемого пароля
        - программа генерирует пароль из нужной длины из введенных символов
        - * игнорируются пробелы
"""  # noqa: E501

from string import digits, ascii_letters, ascii_lowercase, ascii_uppercase, punctuation
from random import randint, choice


def main():
    choice = input(
        "Меню: \n"
        "1. Сгенерировать простой пароль.\n"
        "2. Сгенерировать средний пароль.\n"
        "3. Сгенерировать сложный пароль.\n"
        "4. Выход.\n"
        "Сделайте выбор и нажмите Enter: "
    )
    if choice == "1":
        simple_password()
    elif choice == "2":
        average_password()
    elif choice == "3":
        complex_password()
    elif choice == "4":
        print("Bye!")
        return

    return main()


def simple_password():
    tmp = ascii_lowercase
    parol = ''
    for i in range(8):
        i = choice(tmp)
        parol += i
    print('Ваш пароль сгенерирован:', parol)


def average_password():
    tmp = digits + ascii_letters + ascii_uppercase + ascii_lowercase
    parol = ''
    for i in range(8):
        i = choice(tmp)
        parol += i
    print('Ваш пароль сгенерирован:', parol)


def complex_password():
    tmp = digits + ascii_letters + ascii_uppercase + ascii_lowercase + punctuation
    parol = ''
    password_length = randint(8, 16)
    for i in range(password_length):
        i = choice(tmp)
        parol += i
    print('Ваш пароль сгенерирован:', parol)


if __name__ == '__main__':
    main()



