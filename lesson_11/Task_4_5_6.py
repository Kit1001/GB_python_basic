"""
Начать работу над проектом «Склад оргтехники».
Создать класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над предыдущим заданием.
Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

Продолжить работу над предыдущим заданием.
Реализовать механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

Комментарий:
Класс Warehouse:
  Атрибуты:
    .items_list - список всех предметов "находящихся на складе"
    .departments - словарь, в котором ключи - название отдела, а значение - список предметов "отправленных" в этот отдел
    .inventory - возвращает словарь, где ключи это виды техники, а значения -  ее кол-во на складе
  Методы:
    .get_new_items(Тип техники (Printer, Copier или Scanner), кол-во, свойства техники) - добавляет на склад указанное
        кол-во оргтехники
    .send_to_department(Название отдела, тип техники, кол-во, *свойства которые должны быть у техники) -
        "отправляет" в указанный отдел технику с нужными свойствами (любое количество, указывать необазятально)

Класс OfficeEquipment:
  Атрибуты:
    .brand - брэнд техники
    .color - ее цвет
    .type - тип техники
    .properties - возвращает множество со всеми свойствами техники

Классы Printer, Copier и Scanner:
  Наследуются от класса OfficeEquipment, имеют по одному уникальному дополнительному атрибуту:
    .print_method, .paper_size и .color_capability соответственно
"""


import re
from abc import ABC


class Warehouse:
    def __init__(self):
        self._items_list = []
        self.departments = {}

    def get_new_items(self, item_type, number_of_items, *args):
        """Метод для добавления новых предметов на склад"""

        # проверка, что переданное число - действительно является целым числом
        if type(number_of_items) != int:
            print('Второй аргумент - число предметов, должно быть число типа int')
            return

        # проверка, что такой тип техники есть среди описанных классов (Printer, Copier или Scanner)
        try:
            item_type_ = eval(item_type)
        except NameError:
            print(f'В базе данных нет оргтехники типа {item_type}')
            return

        # Добавляем в список self.items_list указанную технику, вызывая ее класс и передавая туда описанные свойства.
        # При ошибке сообщаем пользователю, если не хватает каких-то аргументов или их наоборот слишком много
        for _ in range(number_of_items):
            try:
                self._items_list.append(item_type_(*args))
            except TypeError as e:
                msg = re.findall(r"'(\w+)'", str(e))
                if msg:
                    print(f'Для добавления на склад предмета типа {item_type}, '
                          f'необходимо указать еще следующие параметры: '
                          f'{", ".join(msg)}')
                else:
                    msg = re.findall(r'(\d+) positional arguments but (\d+)', str(e))
                    if msg:
                        print(f'Было передано {msg[0][1]} аргументов, а для техники типа {item_type}'
                              f' нужно только {msg[0][0]}')
                    else:
                        print(e)
                break

    def send_to_department(self, dpt_name, item_type, number_of_items, *args):
        """Метод 'отправляет' технику со склада в указанный отдел, информация об этом хранится в self.departments"""

        # проверяем, что аргумент с кол-вом техники является целым числом
        if type(number_of_items) != int:
            print('Третий аргумент - число предметов, должно быть число типа int')
            return
        self.departments.setdefault(dpt_name, [])       # если нужного отдела нет в self.departments - создаем

        # проверка, что на складе вообще есть нужное кол-во техники нужного типа
        if self.inventory[item_type] < number_of_items:
            print(f'На складе недостаточно техники типа {item_type}')
            return

        # Проходим по списку всей техники, что есть на складе self.items_list и проверяем каждую, есть ли у нее
        # нужные свойства, если они были указаны в *args, для этого используем флаг condition.
        # Доблавяем технику нужного типа и с нужными свойствами во временный список tmp_list
        tmp_list = []
        for item in self._items_list:
            condition = True
            if item.type == item_type:
                if args:
                    for arg in args:
                        if arg not in item.properties:
                            condition = False
                if condition:
                    tmp_list.append(item)
                    if len(tmp_list) == number_of_items:    # если в списке tmp_list набралось нужное кол-во элементов
                        break                               # прерываем цикл

        # Если набралось нужное кол-во элементов в tmp_list, добавляем их в нужную позицию в словаре self.departments
        # и убираем их из списка self.items_list
        if len(tmp_list) == number_of_items:
            for item in tmp_list:
                idx = self._items_list.index(item)
                self.departments[dpt_name].append(self._items_list.pop(idx))
            print(f'{number_of_items} ед. {item_type} были успешно перемещены в {dpt_name}')

        # Если не набралось нужного кол-ва техники в списке tmp_list сообщаем пользователю, что операция не удалась
        else:
            if len(tmp_list) == 0:
                msg = 'нет'
            else:
                msg = f'есть только {len(tmp_list)} ед.'
            print(f'На складе {msg} указанной техники типа {item_type}'
                  f' со свойствами "{", ".join(args)}", операция не была выполнена')
            if len(self.departments[dpt_name]) == 0:
                self.departments.pop(dpt_name)

    @property
    def inventory(self):
        """Метод возвращает словарь, в котором ключи - это типы техники на складе, а значения - ее кол-во"""
        result = {}
        for item in self._items_list:
            if item.type in result:
                result[item.type] += 1
            else:
                result.setdefault(item.type, 1)
        return result


class OfficeEquipment(ABC):
    def __init__(self, brand, color):
        super().__init__()
        self.brand = brand
        self.color = color
        self.type = self.get_type()
        self.name = "Офисная техника"

    def __repr__(self):
        """Задаем отображение объектов через атрибут self.name"""
        return self.name

    @property
    def properties(self):
        """Метод возвращает свойства объекта в виде множества"""
        properties = []
        for key, val in self.__dict__.items():
            properties.append(val)
        properties = set(properties)
        return properties

    @classmethod
    def get_type(cls):
        """
        С помощью этого метода получаем название класса, это используется в классах-наследниках
        для получения атрибута self.type
        """
        return cls.__name__


class Printer(OfficeEquipment):
    """Атрибут .print_method - обозначает способ печати принтера, например струйный или лазерный"""
    counter = 0

    def __init__(self, brand, color, print_method):
        super().__init__(brand, color)
        self.print_method = print_method
        Printer.counter += 1
        self.name = f'Printer #{Printer.counter}'


class Copier(OfficeEquipment):
    """Атрибут .paper_size - обозначает формат бумаги, с которым работает копир, например A4"""
    counter = 0

    def __init__(self, brand, color, paper_size):
        super().__init__(brand, color)
        self.paper_size = paper_size
        Copier.counter += 1
        self.name = f'Copier #{Copier.counter}'


class Scanner(OfficeEquipment):
    """Атрибут .color_capability - обозначает работает ли сканер в цветном или черно-белом режиме"""
    counter = 0

    def __init__(self, brand, color, color_capability):
        super().__init__(brand, color)
        self.color_capability = color_capability
        Scanner.counter += 1
        self.name = f'Scanner #{Scanner.counter}'


# Шаг №1
# создаем объект класса Warehouse и добавим на него несколько ед. оргтехники
# выведем содержимое ._items_list и .inventory
my_warehouse = Warehouse()
my_warehouse.get_new_items('Printer', 4, 'HP', 'White', 'Laser')
my_warehouse.get_new_items('Copier', 3, 'Xerox', 'Black', 'A4')
my_warehouse.get_new_items('Printer', 3, 'Canon', 'White', 'Ink-jet')
my_warehouse.get_new_items('Scanner', 5, 'Canon', 'Gray', 'Monochrome')

print(f'Шаг №1:\n'
      f'Создаем объект класса Warehouse и добавим в него несколько ед. оргтехники\n'
      f'Содержимое склада (._items_list): ')
# noinspection PyProtectedMember
print(my_warehouse._items_list)
print('Атрибут .inventory: ')
print(my_warehouse.inventory)

# Шаг №2
# попробуем вызвать метод get_new_items неправильно, указав недостаточно свойств техники и передав неправильное кол-во
print(f'\nШаг №2:\nНеправильный вызов метода .get_new_items:')
my_warehouse.get_new_items('Printer', 'Три', 'Canon', 'White', 'Ink-jet')
my_warehouse.get_new_items('Scanner', 5)
my_warehouse.get_new_items('Xerox', 3, 'Xerox', 'Black', 'A4')

# Шаг №3
# Переместим несколько принтеров брэнда "Canon" в отдел "Office" и посмотрим содержимое .departments
# Так же проверим, что кол-во техники на складе уменьшилось
print('\nШаг №3:')
my_warehouse.send_to_department('Office', 'Printer', 3, 'Canon')
print(f'Содержимое my_warehouse.departments:')
print(my_warehouse.departments)
print(f'Кол-во техники на складе уменьшилось (my_warehouse.inventory):\n{my_warehouse.inventory}')

# Шаг №4
# Попробуем вызвать метод .send_to_departments неправильно - указав несуществющие свойства или неправильное кол-во
print(f'\nШаг №4:\nПопробуем вызвать метод .send_to_departments неправильно:')
my_warehouse.send_to_department('Office', 'Printer', 1, 'LG', 'White')
my_warehouse.send_to_department('Office', 'Printer', "Десять", 'Canon')
my_warehouse.send_to_department('Office', 'Printer', 15, 'Canon')
my_warehouse.send_to_department('Office', 'Printer', 4, 'Canon')
