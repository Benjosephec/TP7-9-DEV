import unittest
from Classdesaad import Fraction

class TestFraction(unittest.TestCase):

    def test_init(self):
        f1 = Fraction(3, 4)
        self.assertEqual(f1.numerator, 3, "Normal test : numerator")
        self.assertEqual(f1.denominator, 4, "Normal test : denominator")

        self.assertRaises(TypeError, Fraction, 3.5, 4)

        f2 = Fraction(4, -3)
        self.assertEqual(f2.numerator, -4, "Test denominator negatif")
        self.assertEqual(f2.denominator, 3, "Test denominator negatif")

        self.assertRaises(ValueError, Fraction, 2, 0)

        f3 = Fraction(0, 1)
        self.assertEqual(f3.numerator, 0)
        self.assertEqual(f3.denominator, 1)

    def test_str(self):
        self.assertEqual(str(Fraction(3, 4)), "3/4")
        self.assertEqual(str(Fraction(2, 1)), "2")

    def test_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        f3 = Fraction(-1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)
        result2 = f1 + f3
        self.assertEqual(result2.numerator, 1)
        self.assertEqual(result2.denominator, 6)

    def test_truediv(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 5)
        result = f1 / f2
        self.assertEqual(result.numerator, 15)
        self.assertEqual(result.denominator, 8)

        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    def test_eq(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertTrue(f1 == f2)
        self.assertFalse(Fraction(1, 2) == Fraction(3, 4))

    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(3, 2).is_integer())

    def test_is_proper(self):
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

    def test_as_mixed_number(self):
        self.assertEqual(Fraction(7, 3).as_mixed_number(), "2 1/3")
        self.assertEqual(Fraction(3, 2).as_mixed_number(), "1 1/2")
        self.assertEqual(Fraction(-10, 4).as_mixed_number(), "-2 1/2")


    def test_is_adjacent_to(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 4)
        f3 = Fraction(4, 4)

        self.assertTrue(f1.is_adjacent_to(f2))
        self.assertTrue(f3.is_adjacent_to(f1))
        self.assertFalse(f1.is_adjacent_to(Fraction(3, 4)))

if __name__ == '__main__':
    unittest.main()