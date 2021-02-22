"""
     Написать функцию, которая будет проверять счастливый билетик или нет.

     Билет счастливый, если сумма одной половины цифр равняется сумме второй.
 """
#ticket_num = 123024


def is_lucky(ticket):
    sum_left = 0
    sum_right = 0
    l = len(str(ticket))
    for i in range(l):
        if i < l // 2:
            sum_right += ticket // 10 ** i % 10
        else:
            sum_left += ticket // 10 ** i % 10
    print(sum_right, sum_left)

    if sum_left == sum_right:
        print('Билет счастливый')
        return True
    else:
        print('Попробуй ещё')
        return False


assert is_lucky(222222) is True


assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

print("All tests passed successfully!")

