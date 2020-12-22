"""Unit-тесты клиента"""

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import *
from client import *


class TestClass(unittest.TestCase):
    """
    Тестируем клиента
    """

    def test_def_presense(self):
        """Тест коректного запроса"""
        test = create_request()
        # время необходмо прировнять принудительно, иначе тест никогда не будет пройден
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректного разбора ответа 200"""
        self.assertEqual(pars_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(pars_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, pars_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
