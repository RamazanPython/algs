import unittest

from task_g import StackMaxEffective


class TestStackMaxEffective(unittest.TestCase):

    def test_1(self):
        stack = StackMaxEffective()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.max == 3

    def test_2(self):
        stack = StackMaxEffective()
        stack.push(1)
        stack.push(2)
        stack.push(100)
        stack.pop()

        print(stack.max)
        assert stack.max == 2


if __name__ == '__main__':
    unittest.main()
