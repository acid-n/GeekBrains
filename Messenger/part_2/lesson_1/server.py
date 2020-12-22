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
def handler_client_message(message, messages_list, client, clients, names):
    '''
    Обрабатывает сообщения от клиента, принимает словарь - сообщение от клиента
    проверяет корректность, возвращает словарь для ответа клиента
    :param message:
    :return:
    '''

    LOGGER.debug(f'Разбор сообщения от клиента {message}')

    # Если это сообщение о присутствии, принимаем и отвечаем
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message:
        # Если такой пользователь еще не зарегистрирован, регистрируем,
        # иначе, отправляем ответ и завершаем соединение.
        if message[USER][ACCOUNT_NAME] not in names.keys():
            names[message[USER][ACCOUNT_NAME]] = client
            send_message(client, RESPONSE_200)
        else:
            response = RESPONSE_400
            response[ERROR] = 'Имя пользователя уже занято.'
            send_message(client, response)
            clients.remove(client)
            client.close()
        return
    # Если это сообщение, то добавляем его в очередь сообщений. Ответ не требуется.
    elif ACTION in message and message[ACTION] == MESSAGE and DESTINATION in message and TIME in message \
            and SENDER in message and MESSAGE_TEXT in message:
        messages_list.append(message)
        return
    # Если клиент выходит
    elif ACTION in message and message[ACTION] == EXIT and ACCOUNT_NAME in message:
        clients.remove(names[message[ACCOUNT_NAME]])
        names[message[ACCOUNT_NAME]].close()
        del names[message[ACCOUNT_NAME]]
        return
    # Иначе отдаем Bad Request
    else:
        response = RESPONSE_400
        response[ERROR] = 'Запрос некорректен'
        send_message(client, response)
        return


@log
def process_message(message, names, listen_socks):
    """
    Функция адресной отправки сообщения определенному клиенту. Принимает словарь сообщение,
    список зарегистрированных пользователей и слушающие сокеты. Ничего не возвращает.
    """
    if message[DESTINATION] in names and names[message[DESTINATION]] in listen_socks:
        send_message(names[message[DESTINATION]], message)
        LOGGER.info(f'Отправлено сообщение пользователю {message[DESTINATION]} '
                    f'от пользователя {message[SENDER]}.')
    elif message[DESTINATION] in names and names[message[DESTINATION]] not in listen_socks:
        raise ConnectionError
    else:
        LOGGER.info(f'Пользователь {message[DESTINATION]} не зарегистрирован на сервере, '
                    f'отправка сообщения невозможна.')


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
    # очередь сообщений
    messages = []

    # Словарь, содержащий имена пользователей и соответствующие им сокеты
    names = dict()

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

        # принимаем сообщение и если там есть ошибка, исключаем клиента
        if recv_data_lst:
            for client_with_message in recv_data_lst:
                try:
                    handler_client_message(get_message(client_with_message),
                                           messages,
                                           client_with_message,
                                           clients,
                                           names)
                except Exception:
                    # LOGGER.info(f'Клиент {client_with_message.getpeername()} отключился от сервера')
                    clients.remove(client_with_message)

        # если есть сообщения для отправки и ожидающие клиенты, отправляем им сообщение
        for i in messages:
            try:
                process_message(i, names, send_data_lst)
            except Exception:
                LOGGER.info(f'Связь с клиентом {i[DESTINATION]} была потеряна')
                clients.remove(names[i[DESTINATION]])
                del names[i[DESTINATION]]
        messages.clear()


if __name__ == '__main__':
    main()
