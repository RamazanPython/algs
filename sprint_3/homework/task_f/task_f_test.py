import unittest

from task_f import solution


class TestFindLargestPerimeter(unittest.TestCase):
    def test_empty_array(self):
        result = solution([])
        self.assertEqual(result, 0)  # or whatever the expected result is for an empty array

    def test_single_element_array(self):
        result = solution([5])
        self.assertEqual(result, 0)  # or whatever the expected result is for a single-element array

    def test_valid_triangles(self):
        # Test with valid triangles
        test_cases = [
            ([3, 4, 5], 12),  # Valid right-angled triangle
            ([6, 8, 10], 24),  # Valid right-angled triangle
            ([5, 5, 5], 15),  # Equilateral triangle
            ([10, 15, 20], 45),  # Scalene triangle
        ]

        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                result = solution(nums)
                self.assertEqual(result, expected)

    def test_invalid_triangles(self):
        # Test with invalid triangles
        test_cases = [
            ([1, 1, 3], 0),  # Sum of two sides is less than the third side
            ([1, 2, 1], 0),  # Sum of two sides is less than the third side
            ([5, 10, 25], 0),  # Sum of two sides is less than the third side
        ]

        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                result = solution(nums)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
