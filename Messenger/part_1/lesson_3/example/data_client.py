# Программа клиента для отправки приветствия серверу и получения ответа
from socket import *

# Создать сокет TCP
s = socket(AF_INET, SOCK_STREAM)

# Соединиться с сервером
s.connect(('localhost', 8888))

msg = 'Привет, сервер!'
s.send(msg.encode('utf-8'))
data = s.recv(1000000)
print(f'Сообщение от сервера: {data.decode("utf-8")}, длиной {len(data)} байт')
s.close()
