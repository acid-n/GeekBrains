# Программа клиент

import sys
import json
import socket
import time
import argparse
import logging
import logs.config_client_log
from errors import *
from common.variables import *
from common.utils import *
from decos import log

# Инициализация логирования клиента
LOGGER = logging.getLogger('client')


@log
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
    LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


@log
def pars_ans(message):
    '''
    Разбор ответа сервера
    :param message:
    :return:
    '''

    LOGGER.debug(f'Разбор ответа сервера {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ReqFieldMissingError(RESPONSE)


@log
def create_arg_parser():
    # Создаем парсер аргументов коммандной строки
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    return parser


def main():
    # Обрабатываем параметры командной строки
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port

    # проверим подходящий номер порта
    if not 1023 < server_port < 65536:
        LOGGER.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {server_port}.'
            f'Допустимы адреса с 1024 до 65535. Клиент завершается.')
        sys.exit(1)

    LOGGER.info(f'Запущен клиент с параметрами: адрес сервера: {server_address}, порт: {server_port}')

    # Инициализация сокета и обмена
    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        message_to_server = create_request()
        send_message(transport, message_to_server)
        answer = pars_ans(get_message(transport))
        LOGGER.info(f'Принят ответ от сервера {answer}')
    except json.JSONDecodeError:
        LOGGER.error(f'Не удалось декодировать полученную JSON строку.')
    except ReqFieldMissingError as missing_error:
        LOGGER.error(f'В ответе сервера отсутствует необходимое поле {missing_error.missing_field}')
    except ConnectionRefusedError:
        LOGGER.critical(f'Не удалось подключиться к серверу {server_address}:{server_port},'
                        f' конечный компьютер отверг запрос на подключение.')


if __name__ == '__main__':
    main()
