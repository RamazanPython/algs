import unittest

from task_b import comparator


class TestComparator(unittest.TestCase):

    def test_greater_than(self):
        self.assertFalse(comparator(['alla', 4, 100], ['gena', 6, 1000]))
        self.assertTrue(comparator(['gena', 6, 1000], ['rita', 2, 90]))

    def test_less_than(self):
        self.assertTrue(comparator(['timofey', 4, 80], ['alla', 4, 100]))
        self.assertTrue(comparator(['gosha', 2, 90], ['rita', 2, 100]))

    def test_equal(self):
        self.assertTrue(comparator(['gosha', 2, 90], ['rita', 2, 90]))
        self.assertFalse(comparator(['alla', 4, 100], ['alla', 4, 100]))

    def test_mixed(self):
        self.assertTrue(comparator(['gosha', 2, 90], ['rita', 2, 100]))
        self.assertFalse(comparator(['timofey', 4, 80], ['gena', 6, 1000]))


if __name__ == '__main__':
    unittest.main()
