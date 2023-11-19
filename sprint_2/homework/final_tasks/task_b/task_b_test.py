import unittest

from task_b import solution


class TestMyFunction(unittest.TestCase):

    def test_case_1(self):
        input_value = "10 2 + 9 * 10 -"
        expected_output = 1
        self.assertEqual(solution(input_value.split()), 98)


if __name__ == "__main__":
    unittest.main()
