import unittest

from task_h import is_correct_bracket_seq


class TestBrackets(unittest.TestCase):

    def test_1(self):
        brackets = '()'
        self.assertTrue(is_correct_bracket_seq(brackets))

    def test_2(self):
        brackets = '[({})]'
        self.assertTrue(is_correct_bracket_seq(brackets))

    def test_3(self):
        brackets = ''
        self.assertTrue(is_correct_bracket_seq(brackets))

    def test_4(self):
        brackets = '('
        self.assertFalse(is_correct_bracket_seq(brackets))

    def test_5(self):
        brackets = '[{(]})'
        self.assertFalse(is_correct_bracket_seq(brackets))

    def test_6(self):
        brackets = '([]{})'
        self.assertTrue(is_correct_bracket_seq(brackets))

    def test_7(self):
        brackets = '([]'
        self.assertFalse(is_correct_bracket_seq(brackets))

    def test_8(self):
        brackets = '[]]'
        self.assertFalse(is_correct_bracket_seq(brackets))

    def test_9(self):
        brackets = '([)]'
        self.assertFalse(is_correct_bracket_seq(brackets))

    def test_10(self):
        brackets = '((()))'
        self.assertTrue(is_correct_bracket_seq(brackets))

    def test_11(self):
        brackets = '(((((((((())))))))))'
        self.assertTrue(is_correct_bracket_seq(brackets))

    def test_12(self):
        brackets = '{[()]}}'
        self.assertFalse(is_correct_bracket_seq(brackets))

    def test_13(self):
        brackets = '{{{{{{{{{{}}}}}}}}}}'
        self.assertTrue(is_correct_bracket_seq(brackets))

    def test_14(self):
        brackets = '{[}'
        self.assertFalse(is_correct_bracket_seq(brackets))

    def test_15(self):
        brackets = '(((((((((()))))))))'
        self.assertFalse(is_correct_bracket_seq(brackets))

    def test_16(self):
        brackets = '))))'
        self.assertFalse(is_correct_bracket_seq(brackets))

    def test_17(self):
        brackets = ']()'
        self.assertFalse(is_correct_bracket_seq(brackets))

    def test_18(self):
        brackets = '([{)])'
        self.assertFalse(is_correct_bracket_seq(brackets))


if __name__ == '__main__':
    unittest.main()
