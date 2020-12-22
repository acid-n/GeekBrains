import unittest


def sum_kv_ij(i, j):
    return i * i + j * j


class TestSumKV(unittest.TestCase):
    def testequal(self):
        self.assertEqual(sum_kv_ij(2, 3), 13)


if __name__ == '__main__':
    unittest.main()
