"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

import re


class OnlyNumListErr(Exception):
    def __init__(self, txt):
        self.txt = txt


regex = r"^[+-]?((\d+(\.\d+)?)|(\.\d+))$"
num_list = []

print('Введите список из чисел. Для выхода введите "q"')

while True:

    try:
        next_num = input()
        if next_num == 'q':
            break

        if not re.match(regex, next_num):
            raise OnlyNumListErr('Ошибка. Вы ввели не число.')

        num_list.append(float(next_num))

    except OnlyNumListErr as err:
        print(err)

print(f'Итоговый список: {num_list}')
