import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):
    def test_sum(self):
        calc = Calculator(8,2)
        self.assertEqual(calc.get_sum(),10, "The answer was not 10")


    def test_subtraction(self):
        calc = Calculator(8,2)
        self.assertEqual(calc.get_subrtraction(),10, "The answer was not 6")


    def test_multiply(self):
        calc = Calculator(8,2)
        self.assertEqual(calc.get_multiplication(),10, "The answer was not 16")


if __name__ == "__main__":
    unittest.main()