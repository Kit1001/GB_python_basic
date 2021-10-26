"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)

Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера.
"""


result = []
# Открываем файл логов, через цикл while разделяем каждую сторку и выделяем нужные нам позиции в отдельные переменные,
# формируем из них кортеж и добавляем в список result.
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        line = line.split()
        remote_addr = line[0]
        request_type = line[5].strip('"')
        requested_resource = line[6]
        result.append((remote_addr, request_type, requested_resource))
# Для проверки, что все сработало, выводим 5 последних позиций в списке result
print("Пять последних кортежей в списке result: ", *result[-5:], "", sep='\n')

# Чтобы вычислить спамера, проходим через список result, сохраняя ip адреса в словарь как ключи, а в качестве значений
# будет количество запросов с данного адреса. Сохраняем пару ключ и значение для максимального количества запросов.
address_dict = {}
max_request_num = 0
spammer_ip = ""
for line in result:
    address_dict.setdefault(line[0], 0)
    address_dict[line[0]] += 1
    if address_dict[line[0]] > max_request_num:
        max_request_num = address_dict[line[0]]
        spammer_ip = line[0]

print(f'Больше всего запросов ({max_request_num}), было отправлено с IP {spammer_ip}')
