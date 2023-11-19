import unittest

from primes_2 import eratosthenes
from eratosthenes import test_eratosthenes


class TestEratosthenes(unittest.TestCase):

    def test_1(self):
        self.assertEqual(eratosthenes(5), test_eratosthenes(5))

    def test_2(self):
        self.assertEqual(eratosthenes(5), test_eratosthenes(5))

    def test_3(self):
        self.assertEqual(eratosthenes(5), test_eratosthenes(5))

    def test_4(self):
        self.assertEqual(eratosthenes(5), test_eratosthenes(5))

    def test_5(self):
        self.assertEqual(eratosthenes(5), test_eratosthenes(5))


if __name__ == '__main__':
    unittest.main()
