# Программа клиент

import sys
import json
import socket
import time
from common.variables import *
from common.utils import *


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
        print(f'В качестве порта может быть указано число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_request()
    send_message(transport, message_to_server)
    try:
        answer = pars_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print(f'Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
