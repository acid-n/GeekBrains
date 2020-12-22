"""Unit-тесты сервера"""

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from common.variables import *
from server import *


class TestServer(unittest.TestCase):
    '''
    Тестируем одну функцию сервера
    '''
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200}

    def test_no_action(self):
        """Ошибка если нет действия"""
        self.assertEqual(handler_client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}
        ), self.err_dict)

    def test_wrong_action(self):
        """Ошибка если неизвестное действие"""
        self.assertEqual(handler_client_message(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}
        ), self.err_dict)

    def test_no_time(self):
        """Ошибка, если запрос не содежит штампа времени"""
        self.assertEqual(handler_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}
        ), self.err_dict)

    def test_no_user(self):
        """Ошибка - нет пользователя"""
        self.assertEqual(handler_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}
        ), self.err_dict)

    def test_unknown_user(self):
        """Ошибка - пользователь не Guest"""
        self.assertEqual(handler_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}
        ), self.err_dict)

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(handler_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}
        ), self.ok_dict)


if __name__ == '__main__':
    unittest.main()
