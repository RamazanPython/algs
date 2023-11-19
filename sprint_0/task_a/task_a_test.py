import unittest

from task_a import solution


class TestProcessList(unittest.TestCase):

    def test_empty_list(self):
        k = 3
        numbers = [4,3,8,1,5,6,3]
        self.assertEqual(solution(numbers, k), [5,4,4.67,4,4.67])

if __name__ == "__main__":
    unittest.main()
