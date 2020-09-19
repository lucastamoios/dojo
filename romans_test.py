import unittest

import romans


class TestRomans(unittest.TestCase):

    def test_one(self):
        result = romans.cast(1)
        self.assertEqual(result, 'I')

    def test_five(self):
        result = romans.cast(5)
        self.assertEqual(result, 'V')

    def test_ten(self):
        result = romans.cast(10)
        self.assertEqual(result, 'X')

    def test_fifty(self):
        result = romans.cast(50)
        self.assertEqual(result, 'L')

    def test_two(self):
        result = romans.cast(2)
        self.assertEqual(result, 'II')

    def test_eleven(self):
        result = romans.cast(11)
        self.assertEqual(result, 'XI')

    def test_twelve(self):
        result = romans.cast(12)
        self.assertEqual(result, 'XII')

    def test_big_number_smaller(self):
        result = romans.biggest_smaller_than([1, 10, 20], 12)
        self.assertEqual(result, 10)
