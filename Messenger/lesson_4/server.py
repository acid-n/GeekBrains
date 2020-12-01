# Программа сервер

import socket
import sys
import json
from common.variables import *
from common.utils import *


def handler_client_message(message):
    '''
    Обрабатывает сообщения от клиента, принимает словарь - сообщение от клиента
    проверяет корректность, возвращает словарь для ответа клиента
    :param message:
    :return:
    '''

    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаем значения по умолчанию.
    Сначала обрабатываем порт: server.py -p 8888 -a 192.168.1.1
    :return:
    '''

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print(f'После параметра "-p" необходимо ууказать номер порта.')
        sys.exit(1)
    except ValueError:
        print(f'В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Загружаем какой адрес слушать
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        print(f'После параметра "-a" необходимо указывать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Создаем сокет
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
            response = handler_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print(f'Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
