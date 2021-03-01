"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.
    Напишите несколько тестов для функции.
    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"
"""

text = "hi world, hi python. i am very cool but i am still learning."


def frequent_word(txt):
    data = {}
    word = txt.lower().split()
    for lll in word:
        data[lll] = data.get(lll, 0) + 1

    max_count = max(data.values())
    most_frequent = [k for k, v in data.items() if v == max_count]
    b = sorted(most_frequent)
    print(b[0])
    return b[0]


frequent_word(text)

assert frequent_word(text) == "am"