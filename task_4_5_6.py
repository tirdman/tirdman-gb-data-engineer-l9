"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Storage:

    def __init__(self, name):
        self.name = name
        self.__storage_list = {}
        self.__department = {}

    def receive_equipment(self, eq_list):
        for next_eq in eq_list:

            if next_eq.type_eq() not in self.__storage_list:
                self.__storage_list[next_eq.type_eq()] = []

            if self.check_sn_duplicate(next_eq):
                self.__storage_list[next_eq.type_eq()].append(next_eq)

        return self.__storage_list

    def check_sn_duplicate(self, eq):
        return not any(eq.serial_number == next_eq.serial_number for next_eq in self.__storage_list[eq.type_eq()])


class OfficeEquipment:
    __TYPE_EQUIPMENT = 'НЕ ОПРЕДЕЛЕННО'

    def __init__(self, color, brand, model, serial_number):
        self.brand = brand
        self.model = model
        self.color = color
        self.serial_number = serial_number

    def __str__(self):
        return f"Брэнд: {self.brand}, Модель: {self.model}, Цвет: {self.color}, SN: {self.serial_number}"


class Printer(OfficeEquipment):
    __TYPE_EQUIPMENT = 'Принтер'

    @classmethod
    def type_eq(cls):
        return cls.__TYPE_EQUIPMENT

    def __init__(self, color, brand, model, serial_number, is_color_print):
        self.is_color_print = is_color_print
        super().__init__(color, brand, model, serial_number)

    def __str__(self):
        general = super().__str__()
        specific = f"Цветная печать: {'Да' if self.is_color_print else 'Нет'}"
        return f"Тип устройства: {__class__.__TYPE_EQUIPMENT}, {general}, {specific}"


class Scanner(OfficeEquipment):
    __TYPE_EQUIPMENT = 'Сканер'

    @classmethod
    def type_eq(cls):
        return cls.__TYPE_EQUIPMENT

    def __init__(self, color, brand, model, serial_number, is_many_list_scan):
        self.is_many_list_scan = is_many_list_scan
        super().__init__(color, brand, model, serial_number)

    def __str__(self):
        general = super().__str__()
        specific = f"Многостраничное сканирование: {'Да' if self.is_many_list_scan else 'Нет'}"
        return f"Тип устройства: {__class__.__TYPE_EQUIPMENT}, {general}, {specific}"


class Copier(OfficeEquipment, ):
    __TYPE_EQUIPMENT = 'Ксерокс'

    @classmethod
    def type_eq(cls):
        return cls.__TYPE_EQUIPMENT

    def __init__(self, color, brand, model, serial_number, format_paper_support):
        self.format_paper_support = format_paper_support
        super().__init__(color, brand, model, serial_number)

    def __str__(self):
        general = super().__str__()
        specific = f"Поддерживаемые форматы: {', '.join(self.format_paper_support)}"
        return f"Тип устройства: {__class__.__TYPE_EQUIPMENT}, {general}, {specific}"


printer = Printer('black', 'samsung', '1210', 11111, True)
scanner = Scanner('red', 'lg', '5820', 22222, True)
copier = Copier('white', 'xerox', '4490', 33333, ['A4', 'A3'])

print(printer)
print(scanner)
print(copier)

storage = Storage('Склад 9')

# Приёмка оборудования на склад
print(storage.receive_equipment([printer, printer, printer, scanner, copier]))

# Передача оборудования в отдел
print(storage.receive_equipment([printer, printer, printer, scanner, copier]))
