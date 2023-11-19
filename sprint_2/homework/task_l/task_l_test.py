import unittest

from task_l import get_pisano_length


class TestMyQueueSized(unittest.TestCase):

    def test_1(self):
        assert get_pisano_length(0) == 0

    def test_2(self):
        assert get_pisano_length(1) == 1

    def test_3(self):
        assert get_pisano_length(2) == 3

    def test_4(self):
        assert get_pisano_length(3) == 8

    def test_5(self):
        assert get_pisano_length(4) == 6


if __name__ == '__main__':
    unittest.main()
