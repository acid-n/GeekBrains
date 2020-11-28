# Программа вывода сообщений на стороне сервера при запросе от клиента
from socket import *

# Определяем UDP-протокол
s = socket(AF_INET, SOCK_DGRAM)

# Несколько приложений может слушать сокет
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Определяем широковещательные пакеты
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

s.bind(('', 8888))

while True:
    msg = s.recv(128)
    print(msg)
