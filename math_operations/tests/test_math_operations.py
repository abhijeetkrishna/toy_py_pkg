import unittest
from math_operations.operations import addition

class MathOperationsTest(unittest.TestCase):
    def test_addition(self):
        result = addition(2, 3)
        self.assertEqual(result, 5)  # Verify that the result is equal to 5

        result = addition(-10, 5)
        self.assertEqual(result, -5)  # Verify that the result is equal to -5

        result = addition(0, 0)
        self.assertEqual(result, 0)  # Verify that the result is equal to 0

        # Add more test cases to cover different scenarios and edge cases

if __name__ == '__main__':
    unittest.main()
