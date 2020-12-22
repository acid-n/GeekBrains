# Программа клиента, передающего серверу сообщения при каждом запросе на соединение
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    s.sendto('Запрос на соединение!', ('', 8888))
# выдает ошибку "a bytes-like object is required, not str
