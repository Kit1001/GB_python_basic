"""Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
 взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

        Например:
#>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]


Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
 (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""

import random


def get_jokes(number, repeat='Нет'):
    """
    Функция формирует шутки, беря по одному случайному слову из 3х списков с помощью функции choice()
    Чтобы исключить повторы слов при неактивном флаге repeat - использованные элементы из списка слов удаляются
    с помощью метода .pop()
    Т.к. в каждом списке слов всего 5, обходим возможную ошибку IndexError с помощью конструкции try except,
    при этом функция выведет на экран количество получившихся шуток
    :param number: количество шуток
    :param repeat: флаг, разрещающий повторы, по умолачнию выкл.
    :return: список шуток
    """
    counter = 0
    joke_list = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    while counter < number:
        try:
            noun = random.choice(nouns)
            adverb = random.choice(adverbs)
            adjective = random.choice(adjectives)
            if repeat == 'Нет':
                joke_list.append(f'{noun} {adverb} {adjective}')
                nouns.pop(nouns.index(noun))
                adverbs.pop(adverbs.index(adverb))
                adjectives.pop(adjectives.index(adjective))
            elif repeat == 'Да':
                joke_list.append(f'{noun} {adverb} {adjective}')
            counter += 1
        except IndexError:
            print(f'К сожалению, получилось всего {counter} шуток')
            break
    return joke_list


# Попытаемся вывести список из 9 шуток, без повторов
print(get_jokes(9))

# Сделаем тоже самое, но разрешим повторы
print(get_jokes(9, repeat='Да'))
