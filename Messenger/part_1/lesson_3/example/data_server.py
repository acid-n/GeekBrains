# Программа сервера для получения приветствия от клиента и отправка ответа
from socket import *
import time

# Создает сокет TCP
s = socket(AF_INET, SOCK_STREAM)

# Присваивает порт 8888
s.bind(('', 8888))

# Переходит в режим ожидания запросов.
# Одновременно обслуживает не более 5 запросов.
s.listen(5)

while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    print(f'Сообщение: {data.decode("utf-8")}, было отправлено клиентом: {addr}')
    msg = 'Привет, клиент!'
    client.send(msg.encode('utf-8'))
    client.close()
