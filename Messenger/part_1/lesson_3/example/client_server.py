# Программа клиента, запрашивающиего текущее время
from socket import *

# Создать сокет TCP
s = socket(AF_INET, SOCK_STREAM)

# Соединиться с сервером
s.connect(('localhost', 8888))

# Принять не более 1024 байтов данных
tm = s.recv(1024)

s.close()
print(f'Текущее время: {tm.decode("ascii")}')
