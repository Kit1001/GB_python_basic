"""
*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
"Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')


Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

Комментарий:
Скрипт выводит 5 случайных записей из списка отпарсеных строк и одну строку с адресом IPv6
Лог скачивается из сети по ссылке
"""


import re
import requests
import random

RE_PARSE_IPV4 = re.compile(r'((?:\d+\.){3}\d+)[^\[]+\[(\d{2}.\w+(?:.\d+){4}\s.\d{4})]'
                           r'\s"(\w+)\s([^\s]+)[^"]+"\s(\d+)\s([^\s]+)')

RE_PARSE_IPV6 = re.compile(r'((?:\w*:){5,6}\w+)[^\[]+\[(\d{2}.\w+(?:.\d+){4}\s.\d{4})]'
                           r'\s"(\w+)\s([^\s]+)[^"]+"\s(\d+)\s([^\s]+)')

# получаем лог файл
log_address = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(log_address, stream=True)
url_encoding = response.encoding
content = response.iter_lines()
result = []

# обрабатываем его построчно, сохраняем отпарсенные строки в список result
for line in content:
    line = line.decode(url_encoding)
    parsed_line = RE_PARSE_IPV4.findall(line)
    if parsed_line:
        result.append(parsed_line[0])
    else:
        parsed_line = RE_PARSE_IPV6.findall(line)
        if parsed_line:
            result.append(parsed_line[0])
            pos = len(result) - 1


# выводим 5 случайных записей из result и последнюю строку с адресом IPv6
for _ in range(5):
    print(random.choice(result))
print(result[pos])

# можно раскоментить и тогда скрипт будет сохранять весь полученный список в файл logs_parsed.txt
# with open('logs_parsed.txt', 'w', encoding='utf-8') as f:
#     for item in result:
#         item = ', '.join(item)
#         f.write(f'{item}\n')
