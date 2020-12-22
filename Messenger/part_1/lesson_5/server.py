# Программа сервер

import socket
import sys
import json
import argparse
import logging
import logs.config_server_log
from errors import *
from common.variables import *
from common.utils import *

# Инициализация логирования сервера
SERVER_LOGGER = logging.getLogger('server')


def handler_client_message(message):
    '''
    Обрабатывает сообщения от клиента, принимает словарь - сообщение от клиента
    проверяет корректность, возвращает словарь для ответа клиента
    :param message:
    :return:
    '''

    SERVER_LOGGER.debug(f'Разбор сообщения от клиента {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def create_arg_parser():
    """
    Парсер аргументов коммандной строки
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    return parser


def main():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаем значения по умолчанию.
    Сначала обрабатываем порт: server.py -p 8888 -a 192.168.1.1
    :return:
    '''
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p

    # Проверка получения корректного номера порта для работы сервера
    if not 1023 < listen_port < 65536:
        SERVER_LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта {listen_port}')
        sys.exit(1)

    SERVER_LOGGER.info(f'Запущен сервер, порт для подключения {listen_port}, адрес {listen_address}')

    # Готовим сокет
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        SERVER_LOGGER.info(f'Установлено соединение с клиентом {client_address}')
        try:
            message_from_client = get_message(client)
            SERVER_LOGGER.debug(f'Получено сообщение {message_from_client}')
            response = handler_client_message(message_from_client)
            SERVER_LOGGER.info(f'Сформирован ответ клиенту {response}')
            send_message(client, response)
            SERVER_LOGGER.debug(f'Соединение с клиентом {client_address} закрывается')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать JSON строку, полученную от {client_address}')
            client.close()
        except IncorrectDataRecivedError:
            SERVER_LOGGER.error(f'От клиента {client_address} приеняты некорректные данные')
            client.close()


if __name__ == '__main__':
    main()
