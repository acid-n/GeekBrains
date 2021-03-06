"""Unit-тесты утилит"""

import sys
import os
import unittest
import json

sys.path.append(os.path.join(os.getcwd(), '..'))

from common.variables import *
from common.utils import *


class TestSocket:
    '''
    Тестируем отправку и получение,
    при создании требует словарь, который будет прогонятся через тестовую функцию
    '''

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.receved_message = None

    def send(self, message_to_send):
        """
        Тестовая функция отправки, корректно кодирует сообщения,
        так-же сохраняет, что должно было отправлено в сокет.
        message_to_send - то, что отправляем в сокет
        :param message_to_send:
        :return:
        """

        json_test_message = json.dumps(self.test_dict)
        # кодируем сообщение
        self.encoded_message = json_test_message.encode(ENCODING)
        # сохраняем что должно было отправлено в сокет
        self.receved_message = message_to_send

    def recv(self, max_len):
        """
        Получаем данные из сокета
        :param max_len:
        :return:
        """
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class Tests(unittest.TestCase):
    '''
    Тестовый класс, выполняющий тестирование
    '''
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 111111.111111,
        USER: {
            ACCOUNT_NAME: 'test_test'
        }
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_send_message(self):
        """
        Тестируем корректность работы функции отправки,
        создадим тестовый сокет и проверим корректность отправки словаря
        :return:
        """
        # экземпляр тестового словаря, хранит тестовый словарь
        test_socket = TestSocket(self.test_dict_send)
        # вызов тестируемой функции, результаты будут сохранены в тестовом сокете
        send_message(test_socket, self.test_dict_send)
        # проверка корректности кодирования словаря
        # сравниваем результат кодирования и результат от тестируемой функции
        self.assertEqual(test_socket.encoded_message, test_socket.receved_message)
        # дополнительно, проверяем генерацию исключения, при не словаре на входе
        with self.assertRaises(Exception):
            send_message(test_socket, test_socket)

    def test_get_message(self):
        """
        Тест функции приема сообщения
        :return:
        """
        test_sock_ok = TestSocket(self.test_dict_recv_ok)
        test_sock_err = TestSocket(self.test_dict_recv_err)
        # тест корректной расшифровки корректного словаря
        self.assertEqual(get_message(test_sock_ok), self.test_dict_recv_ok)
        # тест корректной расшифровки ошибочного словаря
        self.assertEqual(get_message(test_sock_err), self.test_dict_recv_err)


if __name__ == '__main__':
    unittest.main()
