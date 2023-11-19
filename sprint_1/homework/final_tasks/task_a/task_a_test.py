import unittest

from task_a import solution


class TestMyFunction(unittest.TestCase):

    def test_case_1(self):
        input_value = [0, 1, 4, 9, 0]
        expected_output = '0 1 2 1 0'
        self.assertEqual(solution(input_value), expected_output)

    def test_case_2(self):
        input_value = [0, 7, 9, 4, 8, 20]
        expected_output = '0 1 2 3 4 5'
        self.assertEqual(solution(input_value), expected_output)

    def test_case_3(self):
        input_value = [1, 0, 4, 5, 0, 9, 0, 10]
        expected_output = '1 0 1 1 0 1 0 1'
        self.assertEqual(solution(input_value), expected_output)

    def test_case_4(self):
        input_value = [1, 2, 0]
        expected_output = '2 1 0'
        self.assertEqual(solution(input_value), expected_output)

    def test_case_5(self):
        input_value = [1, 2, 3, 4, 5, 0, 5, 4, 3, 2, 1]
        expected_output = '5 4 3 2 1 0 1 2 3 4 5'
        self.assertEqual(solution(input_value), expected_output)

    def test_case_6(self):
        input_value = [0, 0]
        expected_output = '0 0'
        self.assertEqual(solution(input_value), expected_output)

    def test_case_7(self):
        input_value = [99, 0, 100, 72, 43, 49, 0, 51, 19, 61, 93, 31]
        expected_output = '1 0 1 2 2 1 0 1 2 3 4 5'
        self.assertEqual(solution(input_value), expected_output)


if __name__ == "__main__":
    unittest.main()
