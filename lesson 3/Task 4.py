"""
Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
#>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

Как поступить, если потребуется сортировка по ключам?
"""


def thesaurus_adv(*names):
    """
    Функция принимает строки, состоящие из имени и фамилии и формирует из них словарь, ключами которого
    являются первые буквы фамилий, а значениями - словари, в которых ключи - это первые буквы имени, а значения -
    списки имен людей, чье имя и фамилия начинается с соответствующей буквы
    :param names: Имена и фамилии
    :return: словарь, содержащий имена и фамилии
    """
    list_of_people = {}
    for full_name in names:
        full_name = full_name.split(' ')
        name = full_name[0]
        surname = full_name[1]
        first_letter_surname = surname[0]
        first_letter_name = name[0]
        # С помощью условных операторов проверяем, есть ли нужный ключ в словаре и если есть просто добавляем
        # нужные имя и фамилию в список по соотвествующим ключам, иначе создаем новую пару ключ: значение в словаре.
        # Делаем это для словаря с буквами фамилий и для соответствующего вложенного словаря с буквами имен
        if first_letter_surname in list_of_people:
            if first_letter_name in list_of_people[first_letter_surname]:
                list_of_people[first_letter_surname][first_letter_name].append(f'{name} {surname}')
            else:
                list_of_people[first_letter_surname][first_letter_name] = [f'{name} {surname}']
        else:
            list_of_people[first_letter_surname] = {first_letter_name: [f'{name} {surname}']}
    return list_of_people


# Задаем некоторый список имен и выведем результат работы функции
some_names = "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"
print('Список имен в виде словаря: \n', thesaurus_adv(*some_names), sep='')

# Здесь выполняется сортировка словаря по ключам с помощью комбинации метода .items() и функции sorted()
list_of_people_sorted = dict(sorted(thesaurus_adv(*some_names).items()))

# Чтобы отсортировать так же вложенные словари и элементы списокв, применяем ту же комбинацию .items() и sorted()
# для каждого вложенного словаря, а затем сортируем элементы каждого списка имен и фамилий.
for key, val in list_of_people_sorted.items():
    list_of_people_sorted[key] = dict(sorted(val.items()))
    for key2, val2 in list_of_people_sorted[key].items():
        list_of_people_sorted[key][key2].sort()

print('Полностью отсортированный словарь: \n', list_of_people_sorted, sep='')