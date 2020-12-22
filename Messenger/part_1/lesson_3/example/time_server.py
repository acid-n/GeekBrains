# Программа сервера времени
from socket import *
import time

# Создает сокет TCP
s = socket(AF_INET, SOCK_STREAM)

# Присваиваем порт 8888
s.bind(('', 8888))

# Переходит в режим ожиданитя запросов.
# Одновременно обслуживает не более 5 запросов.
s.listen(5)

while True:
    # Принять запрос на соединение
    client, addr = s.accept()
    print(f'Получен запрос на соединение от {str(addr)}')
    timestr = time.ctime(time.time()) + '\n'
    client.send(timestr.encode('ascii'))
    client.close()
