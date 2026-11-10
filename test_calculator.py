# https://github.com/k8d0r/lab11-KC-JW
# Partner 1: Kieran Cochran
# Partner 2: Jerry Wang

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(2.5, 0.5), 3.0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1,2),2)
        self.assertEqual(mul(2,2),4)
        self.assertEqual(mul(4,4),16)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,4),2)
        self.assertEqual(div(3,9),3)
        self.assertEqual(div(2,26),13)
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    #    fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4), 5)
        self.assertAlmostEqual(hypotenuse(5,12), 13)
        self.assertAlmostEqual(hypotenuse(7,24), 25)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(9),3)
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(16), 4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()