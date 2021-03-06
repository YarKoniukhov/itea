"""
     1. Реализовать функцию get_country(city), которая принимает название города
     и возвращает страну, которой он принадлежит исходя из словаря data.

     2. Релизовать функцию groupping_data(data), которая принимает словарь data
     и возвращает отформатированные данные в виде списка словарей с ключами
     'country', 'capital' и 'cities'.
     Учитывать, что во входящем словаре data
     ключ - country, первый элемент значения - capital, остальные - cities.
 """

data = {
    "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"]
       }


def get_country(city):
    for k, v in data.items():
        if city in v:
            print(k)
            return k
get_country('Hamburg')

"""
def groupping_data(data):
    data_format = {}
    data_format.setdefault('country', data.keys())

    print(data_format)


groupping_data(data)
"""