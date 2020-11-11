"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class CustomDivZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    nom, denom = [int(i) for i in input('Введите числитель и знаменатель через пробел: ').split()]

    if denom == 0:
        raise CustomDivZero('Вы ввели нуль в качестве знаменателя')
except CustomDivZero as err:
    print(err)
except Exception as err:
    print(err)
else:
    print(f'Результат деления: {nom / denom}')
