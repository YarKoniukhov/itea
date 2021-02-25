"""
     Напишите функцию, которая принимает список чисел
     и возвращает отсортированный список,
     при условии, что все числа -1 остаются на своих местах.

     [in]   [6, 3, -1, 4, 2, -1, 1]
     [out]  [1, 2, -1, 3, 4, -1, 6]
 """
var = [6, 3, -1, 4, 2, -1, 1]

def sort_ascending(x):
    positive = []
    negative = []

    for index, i in enumerate(x):
        if i > 0:
           positive.append(i)
           positive.sort()
        elif i < 0:
            negative.append(index)

    for index in negative:
        if index >= 0:
            positive.insert(index, -1)
    print(positive)
    return positive

sort_ascending(var)

t_1 = [-1, 150, 190, 170, -1, -1, 160, 180]
assert sort_ascending(t_1) == [-1, 150, 160, 170, -1, -1, 180, 190]

t_2 = [-1, -1, -1, -1, -1]
assert sort_ascending(t_2) == [-1, -1, -1, -1, -1]

t_3 = [4, 2, 9, 11, 2, 16]
assert sort_ascending(t_3) == [2, 2, 4, 9, 11, 16]

t_4 = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
assert sort_ascending(t_4) == [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]

t_5 = [-1]
assert sort_ascending(t_5) == [-1]

print("All tests passed successfully!")