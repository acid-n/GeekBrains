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
def message_from_server(message):
    # Обрабатываем сообщения пользователей, поступающих с сервера
    if ACTION in message and message[ACTION] == MESSAGE and SENDER in message and MESSAGE_TEXT in message:
        print(f'Получено сообщение от пользователя {message[SENDER]}:\n {message[MESSAGE_TEXT]}')
        LOGGER.info(f'Получено сообщение от пользователя {message[SENDER]}:\n{message[MESSAGE_TEXT]}')
    else:
        LOGGER.error(f'Получено некорректное сообщение с сервера: {message}')


@log
def create_message(sock, account_name='Guest'):
    # Запрашиваем текст сообщения и возращаем его
    message = input('Введите сообщение или \'!!!\' для завершения работы: ')
    if message == '!!!':
        LOGGER.info('Завершение работы по команде пользователя')
        print(f'Спасибо! Было приятно с вами пообщаться.')
        sys.exit()
        sock.close()
    message_dict = {
        ACTION: MESSAGE,
        TIME: time.time(),
        ACCOUNT_NAME: account_name,
        MESSAGE_TEXT: message
    }
    LOGGER.debug(f'Сформирован словарь сообщения: {message_dict}')
    return message_dict


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
        elif message[RESPONSE] == 400:
            raise ServerError(f'400: {message[ERROR]}')
    raise ReqFieldMissingError(RESPONSE)


@log
def create_arg_parser():
    # Создаем парсер аргументов коммандной строки
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-m', '--mode', default='listen', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_mode = namespace.mode

    # проверим подходящий номер порта
    if not 1023 < server_port < 65536:
        LOGGER.critical(f'Попытка запуска клиента с неподходящим номером порта: {server_port}.')
        sys.exit(1)

    # проверим режим работы клиента
    if client_mode not in ('listen', 'send'):
        LOGGER.critical(f'Указан недопустимый режим работы {client_mode}.')
        sys.exit(1)

    return server_address, server_port, client_mode


def main():

    # Загружаем параметры коммандной строки
    server_address, server_port, client_mode = create_arg_parser()

    LOGGER.info(f'Запущен клиент с параметрами: {server_address}, {server_port}, {client_mode}')

    # Инициализация сокета и обмена
    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        send_message(transport, create_request())
        answer = pars_ans(get_message(transport))
        LOGGER.info(f'Установлено соединение с сервером. Принят ответ от сервера {answer}')
        print(f'Установлено соединение с сервером.')
    except json.JSONDecodeError:
        LOGGER.error(f'Не удалось декодировать полученную JSON строку.')
        sys.exit(1)
    except ServerError as error:
        LOGGER.error(f'При установке соединения сервер вернул ошибку: {error.text}')
        sys.exit(1)
    except ReqFieldMissingError as missing_error:
        LOGGER.error(f'В ответе сервера отсутствует необходимое поле {missing_error.missing_field}')
        sys.exit(1)
    except ConnectionRefusedError:
        LOGGER.critical(f'Не удалось подключиться к серверу {server_address}:{server_port},'
                        f' конечный компьютер отверг запрос на подключение.')
        sys.exit(1)
    else:
        # Если соединение с сервером установлено корректно, начинается обмен, согласно режиму.
        if client_mode == 'send':
            print(f'Режим работы - отправка сообщений.')
        else:
            print(f'Режим работы - прием сообщений.')

        while True:
            # Режим работы - отправка сообщений
            if client_mode == 'send':
                try:
                    send_message(transport, create_message(transport))
                except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                    LOGGER.error(f'Соединение с сервером {server_address} было потеряно.')
                    sys.exit(1)

            # Режим работы - прием
            if client_mode == 'listen':
                try:
                    message_from_server(get_message(transport))
                except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                    LOGGER.error(f'Соединение с сервером {server_address} было потеряно.')
                    sys.exit(1)


if __name__ == '__main__':
    main()
