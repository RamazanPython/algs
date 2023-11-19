import unittest

from task_b import solution


class TestMyFunction(unittest.TestCase):

    def test_case_1(self):
        input_value = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9]
        k = 4
        expected_output = 1
        self.assertEqual(solution(k, input_value), expected_output)

    def test_case_2(self):
        input_value = [4, 4, 4, 3, 3, 3, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
        k = 3
        expected_output = 4
        self.assertEqual(solution(k, input_value), expected_output)

    def test_case_3(self):
        input_value = [1, 2, 3, 1, 2, 2, 2, 2, 2, 2]
        k = 3
        expected_output = 2
        self.assertEqual(solution(k, input_value), expected_output)

    def test_case_4(self):
        input_value = []
        k = 3
        expected_output = 0
        self.assertEqual(solution(k, input_value), expected_output)


if __name__ == "__main__":
    unittest.main()
