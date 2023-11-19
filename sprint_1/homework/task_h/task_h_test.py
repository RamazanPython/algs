import unittest

from task_h import get_sum


class TestGetSum(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(get_sum("0", "0"), "0")

    def test_case_2(self):
        self.assertEqual(get_sum("1", "1"), "10")

    def test_case_3(self):
        self.assertEqual(get_sum("101", "101"), "1010")

    def test_case_4(self):
        self.assertEqual(get_sum("1", "101"), "110")

    def test_case_5(self):
        self.assertEqual(get_sum("1010", "1"), "1011")

    def test_case_6(self):
        self.assertEqual(get_sum("001", "001"), "10")

    def test_case_7(self):
        self.assertEqual(get_sum("00001", "1"), "10")

    def test_case_8(self):
        # Assuming empty string should be treated as "0"
        self.assertEqual(get_sum("", "1"), "1")

    def test_case_9(self):
        self.assertEqual(get_sum("110", "101"), "1011")

    def test_case_10(self):
        self.assertEqual(get_sum("111", "111"), "1110")


if __name__ == "__main__":
    unittest.main()
