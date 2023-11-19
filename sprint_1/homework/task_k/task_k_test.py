import unittest

from task_k import get_sum


class TestTwoNumberSum(unittest.TestCase):

    def convert_list_to_number(self, array: list) -> int:
        return int(''.join(map(str, array)))

    def validate_equality(self, input_list, input_number, result):
        correct_result = self.convert_list_to_number(input_list) + input_number
        self.assertEqual(result, " ".join(str(correct_result)))

    def test_1(self):
        input_list = [1, 2, 3, 4, 5]
        input_number = 54321
        result = get_sum(input_list, input_number)

        self.validate_equality(input_list, input_number, result)

    def test_2(self):
        input_list = [1]
        input_number = 100
        result = get_sum(input_list, input_number)

        self.validate_equality(input_list, input_number, result)

    def test_3(self):
        input_list = [0]
        input_number = 0
        result = get_sum(input_list, input_number)

        self.validate_equality(input_list, input_number, result)

    def test_4(self):
        input_list = [1, 2, 0, 0]
        input_number = 34
        result = get_sum(input_list, input_number)

        self.validate_equality(input_list, input_number, result)

    def test_5(self):
        input_list = [9, 9, 9, 9]
        input_number = 1
        result = get_sum(input_list, input_number)

        self.validate_equality(input_list, input_number, result)

    def test_6(self):
        input_list = [1, 1, 1, 1]
        input_number = 9
        result = get_sum(input_list, input_number)

        self.validate_equality(input_list, input_number, result)

    def test_7(self):
        input_list = [9, 8, 1, 2]
        input_number = 9913123893
        result = get_sum(input_list, input_number)

        self.validate_equality(input_list, input_number, result)


if __name__ == '__main__':
    unittest.main()
