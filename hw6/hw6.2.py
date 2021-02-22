"""
    Обновите генератор паролей из hw5/password_gen.py таким образом, чтобы:
    1. Все сгенерированные пароли записывались в файл.
    2. После генерации пароля, сравнить его с содержимым файла.
        Если в файле уже записан такой пароль,
        то вывести сообщение с предупреждением "Insecure password".
    *3. Программа должна генерировать только уникальные пароли.
        Если в результате пункта 2 пароль уже содержится в файле, то генерируем
        его заново.
    * дополнительно стоит обрабатывать количество попыток генерации,
    так как после того, как будут сгенерированы все возможные комбинации,
    программа зациклится либо уйдет в бесконечную рекурсию и сломается
"""



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


