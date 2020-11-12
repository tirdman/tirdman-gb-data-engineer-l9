"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class DateInvalidErr(Exception):
    pass


class CustomDate:
    day_month_year = ''

    def __init__(self, in_date):
        CustomDate.day_month_year = in_date

    @classmethod
    def split_date_to_attributes(cls):
        cls.day, cls.month, cls.year = [int(i) for i in cls.day_month_year.split('-')]

    @staticmethod
    def valid_date(in_date):
        day, month, year = [int(i) for i in in_date.split('-')]

        if month < 1 or month > 12:
            raise DateInvalidErr('Месяц должен быть в диапазоне [1, 12]')
        #
        if year < 1950 or year > 2020:
            raise DateInvalidErr('Год должен быть в диапазоне [1950, 2020]')

        if day < 1 or day > 31:
            raise DateInvalidErr('День должен быть в диапазоне [1, 31]')

        return True


c_date = CustomDate('11-12-2020')
print(CustomDate.day_month_year)

CustomDate.split_date_to_attributes()
print(f'День: {CustomDate.day}, Месяц: {CustomDate.month}, Год: {CustomDate.year}')

CustomDate.valid_date('11-12-2020')
