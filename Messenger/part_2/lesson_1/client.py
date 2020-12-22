# Программа клиент

import sys
import json
import socket
import time
import argparse
import threading
import logging
import logs.config_client_log
from errors import *
from common.variables import *
from common.utils import *
from decos import log

# Инициализация логирования клиента
LOGGER = logging.getLogger('client')


@log
def create_exit_message(account_name):
    """
    Функция создает словарь с сообщением о выходе
    """
    return {
        ACTION: EXIT,
        TIME: time.time(),
        ACCOUNT_NAME: account_name
    }


@log
def message_from_server(sock, my_username):
    # Обрабатываем сообщения пользователей, поступающих с сервера
    while True:
        try:
            message = get_message(sock)
            if ACTION in message and message[ACTION] == MESSAGE and SENDER in message \
                    and DESTINATION in message and MESSAGE_TEXT in message and message[DESTINATION] == my_username:
                print(f'\nПолучено сообщение от пользвоателя {message[SENDER]}:'
                      f'\n{message[MESSAGE_TEXT]}')
                LOGGER.info(f'Получено сообщени от пользователя {message[SENDER]}:'
                            f'\n{message[MESSAGE_TEXT]}')
            else:
                LOGGER.error(f'Получено некорректное сообщение с сервера {message}')
        except IncorrectDataRecivedError:
            LOGGER.error(f'Не удалось декодировать полуенное сообщение.')
        except (OSError, ConnectionError, ConnectionAbortedError, ConnectionResetError, json.JSONDecodeError):
            LOGGER.critical(f'Потеряно соединение с сервером.')
            break


@log
def create_message(sock, account_name='Guest'):
    """
    Функция запрашивает кому отправить сообщение и сообщение,
    отрпавляет полученный данные на сервер
    """
    to_user = input('Введите получателя сообщения: ')
    message = input('Введите сообщение: ')
    message_dict = {
        ACTION: MESSAGE,
        SENDER: account_name,
        DESTINATION: to_user,
        TIME: time.time(),
        MESSAGE_TEXT: message
    }
    LOGGER.debug(f'Сформирован словарь сообщения: {message_dict}')
    try:
        send_message(sock, message_dict)
        LOGGER.info(f'Отправлено сообщение для пользователя {to_user}')
    except:
        LOGGER.critical(f'Потеряно соединение с сервером.')
        sys.exit(1)


def print_help():
    """
    Функция выводящяя справку по использованию
    """
    print('Поддерживаемые команды: ')
    print('message: отправить сообщение. Кому и текст будут запрошены отдельно.')
    print('help: вывести подсказки по командам')
    print('exit: выход из программы')


@log
def user_interactive(sock, username):
    """
    Функция взаимодействует с пользователем, запрашивает команды, отправляет сообщения
    """
    print_help()
    while True:
        command = input('Введите команду: ')
        if command == 'message':
            create_message(sock, username)
        elif command == 'help':
            print_help()
        elif command == 'exit':
            send_message(sock, create_exit_message(username))
            print('Завершение соединения.')
            LOGGER.info('Завершение работы по команде пользователя.')
            # Задержка необходима, чтобы успели уйти сообщения о выходе
            time.sleep(1)
            break
        else:
            print('Команда не распознана. Введите help, чтобы вывести подсказки.')


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
    parser.add_argument('-n', '--name', default=None, nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_name = namespace.name

    # проверим подходящий номер порта
    if not 1023 < server_port < 65536:
        LOGGER.critical(f'Попытка запуска клиента с неподходящим номером порта: {server_port}.')
        sys.exit(1)

    return server_address, server_port, client_name


def main():
    print('Консольный мессенджер. Клиентский модуль.')

    # Загружаем параметры коммандной строки
    server_address, server_port, client_name = create_arg_parser()

    # Если имя пользователя не было задано, необходимо запросить пользователя
    if not client_name:
        client_name = input('Введите имя пользователя: ')

    LOGGER.info(f'Запущен клиент с параметрами: {server_address}, {server_port}, имя пользователя: {client_name}')

    # Инициализация сокета и обмена
    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        send_message(transport, create_request(client_name))
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
    except (ConnectionRefusedError, ConnectionError):
        LOGGER.critical(f'Не удалось подключиться к серверу {server_address}:{server_port},'
                        f' конечный компьютер отверг запрос на подключение.')
        sys.exit(1)
    else:
        # Если соединение с сервером установлено корректно, запускается клиентский процесс приема сообщений
        receiver = threading.Thread(target=message_from_server, args=(transport, client_name))
        receiver.daemon = True
        receiver.start()

        # Запускаем отправку сообщений и взаимодействие с пользователем
        user_interface = threading.Thread(target=user_interactive, args=(transport, client_name))
        user_interface.daemon = True
        user_interface.start()
        LOGGER.debug('Запущены процессы')

        # Watchdog основной цикл, если один из потоков завершен, то значит или потеряно соединение или
        # пользователь ввел exit. Поскольку все события обрабатываются в потоках, достаточно просто завершить цикл
        while True:
            time.sleep(1)
            if receiver.is_alive() and user_interface.is_alive():
                continue
            break


if __name__ == '__main__':
    main()
