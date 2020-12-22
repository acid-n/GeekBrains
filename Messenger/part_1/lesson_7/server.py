# Программа сервер

import socket
import sys
import json
import argparse
import time
import select
import logging
import logs.config_server_log
from errors import *
from common.variables import *
from common.utils import *
from decos import log

# Инициализация логирования сервера
LOGGER = logging.getLogger('server')


@log
def handler_client_message(message, messages_list, client):
    '''
    Обрабатывает сообщения от клиента, принимает словарь - сообщение от клиента
    проверяет корректность, возвращает словарь для ответа клиента
    :param message:
    :return:
    '''

    LOGGER.debug(f'Разбор сообщения от клиента {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        send_message(client, {RESPONSE: 200})
        return
    elif ACTION in message and message[ACTION] == MESSAGE and TIME in message and MESSAGE_TEXT in message:
        messages_list.append((message[ACCOUNT_NAME], message[MESSAGE_TEXT]))
        return
    else:
        send_message(client, {RESPONSE: 400, ERROR: 'Bad Request'})
        return


@log
def create_arg_parser():
    """
    Парсер аргументов коммандной строки
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p

    if not 1023 < listen_port < 65536:
        LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта {listen_port}.')
        sys.exit(1)

    return listen_address, listen_port


def main():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаем значения по умолчанию.
    Сначала обрабатываем порт: server.py -p 8888 -a 192.168.1.1
    :return:
    '''

    listen_address, listen_port = create_arg_parser()

    LOGGER.info(f'Запущен сервер, порт для подключения {listen_port}, адрес {listen_address}')

    # Готовим сокет
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))
    transport.settimeout(0.5)

    # список клиентов
    clients = []
    messages = []

    # Слушаем порт
    transport.listen(MAX_CONNECTIONS)

    while True:
        # Ожидаем подключения, если таймаут вышел, ловим исключение
        try:
            client, client_address = transport.accept()
        except OSError:
            pass
        else:
            LOGGER.info(f'Установлено соединение {client_address}')
            clients.append(client)

        recv_data_lst = []
        send_data_lst = []
        err_lst = []

        # проверяем на наличие ждущих клиентов
        try:
            if clients:
                recv_data_lst, send_data_lst, err_lst = select.select(clients, clients, [], 0)
        except OSError:
            pass

        # принимаем сообщение и если там есть сообщения, кладем в словарь, если ошибка, исключаем клиента
        if recv_data_lst:
            for client_with_message in recv_data_lst:
                try:
                    handler_client_message(get_message(client_with_message), messages, client_with_message)
                except:
                    # LOGGER.info(f'Клиент {client_with_message.getpeername()} отключился от сервера')
                    clients.remove(client_with_message)

        # если есть сообщения для отправки и ожидающие клиенты, отправляем им сообщение
        if messages and send_data_lst:
            message = {
                ACTION: MESSAGE,
                SENDER: messages[0][0],
                TIME: time.time(),
                MESSAGE_TEXT: messages[0][1]
            }
            del messages[0]
            for waiting_client in send_data_lst:
                try:
                    send_message(waiting_client, message)
                except:
                    LOGGER.info(f'Клиент {waiting_client.getpeername()} отключился от сервера.')
                    clients.remove(waiting_client)


if __name__ == '__main__':
    main()
