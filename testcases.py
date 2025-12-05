import unittest
from lab_manual_6  import square_number

class TestSquareNumber(unittest.TestCase):

    # Normal cases
    # def test_square_positive(self):
    #     self.assertEqual(square_number(5), 25)
    #
    # def test_square_negative(self):
    #     self.assertEqual(square_number(-4), 16)
    #
    # def test_square_float(self):
    #     self.assertAlmostEqual(square_number(2.5), 6.25)

    # Edge cases
    # def test_square_zero(self):
    #     self.assertEqual(square_number(0), 0)
    #
    # def test_square_large_number(self):
    #     self.assertEqual(square_number(10000), 100000000)

    # Error cases
    def test_square_string_input(self):
        with self.assertRaises(TypeError):
            square_number("abc")

    def test_square_list_input(self):
        with self.assertRaises(TypeError):
            square_number([2, 3])
