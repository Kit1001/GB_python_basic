import random

# Первым шагом создаем список из 20 случайных целых и вещественных чисел, с округлением до двух знаков после запятой
price_list = []
for i in range(10):
    random_price = random.uniform(1, 100)
    random_price = round(random_price, 2)
    price_list.append(random_price)
    random_price = random.randint(1, 100)
    price_list.append(random_price)
print('Изначальный список цен:', price_list, sep="\n")

# Позадание А: выводим цены на экран в формате <r> руб <kk> коп в одну строку через запятую
print('\n', 'Подзадание A: ', sep="")
print('Список цен в формате <r> руб <kk> коп:')
counter = 0
while counter < len(price_list):
    price = price_list[counter]
    price = int(price * 100)
    roubles = price // 100
    pennies = price % 100
    add_zero = "0" if pennies < 10 else ""
    price = f'{roubles} руб {add_zero}{pennies} коп'
    print(price, end='')
    print(", " if counter + 1 < len(price_list) else "\n", end='')
    counter += 1

# Позадание B: выводим список цен, отсортированный по возрастанию, не создавая при этом новый.
# Так же необходимо доказать, что объект списка остался тем же самым
print('\n', 'Подзадание B: ', sep="")
object_id_old = id(price_list)
price_list.sort()
object_id_new = id(price_list)
print('Список, отсортированный по возрастанию:', price_list, sep="\n")
if object_id_old == object_id_new:
    print(f'ID списка до сортировки {object_id_old} совпадает с ID списка после сортировки {object_id_new}')
else:
    print('Произошло волшебство и метод .sort() создал новый объект')

# Подзадание C: Создаем новый список, отсортированный по убыванию
print('\n', 'Подзадание С: ', sep="")
price_list_reversed = price_list[:]         # создаем копию списка с помощью среза
price_list_reversed.sort(reverse=True)
print('Список, отсортированный по убыванию:', price_list_reversed, sep="\n")

# Подзадание D: выводим цены пяти самых дорогих товаров по возрастанию
print('\n', 'Подзадание D: ', sep="")
print('Цены 5 самых дорогих товаров по возрастанию:\n', price_list[-6:-1], sep="")
