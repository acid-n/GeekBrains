# Программа клиент

import sys
import json
import socket
import time
import logging
import logs.config_client_log
from errors import *
from common.variables import *
from common.utils import *

# Инициализация логирования клиента
CLIENT_LOGGER = logging.getLogger('client')


def create_request(account_name='Guest'):
    '''
    Создает запрос о присутсвии клиента
    :param account_name:
    :return:
    '''

    # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def pars_ans(message):
    '''
    Разбор ответа сервера
    :param message:
    :return:
    '''

    CLIENT_LOGGER.debug(f'Разбор ответа сервера {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    '''
    Обрабатываем параметры командной строки
    :return:
    '''

    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        CLIENT_LOGGER.critical(f'Неверно указан порт сервера: {server_port}')
        # print(f'В качестве порта может быть указано число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    CLIENT_LOGGER.info(f'Запущено соединение с сервером {server_address} на порт {server_port}')

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_request()
    send_message(transport, message_to_server)
    try:
        answer = pars_ans(get_message(transport))
        CLIENT_LOGGER.debug(f'Получен ответ от сервера {answer}')
        # print(answer)
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGGER.critical(f'Не удалось декодировать сообщение сервера!')
        # print(f'Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
