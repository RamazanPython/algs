import unittest

from primes_1 import is_prime


class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        # Test prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))

        # Test non-prime numbers
        self.assertFalse(is_prime(1))  # By definition, 1 is not prime
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(16))

        # Test that 0 and negative numbers are not prime
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))


if __name__ == '__main__':
    unittest.main()
