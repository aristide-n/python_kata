__author__ = 'Aristide'

import unittest

from tdd.fizzbuzz import fb


class TestFB(unittest.TestCase):

    def test_1(self):
        self.assertEqual('1', fb(1))

    def test_2(self):
        self.assertEqual('2', fb(2))

    def test_3(self):
        self.assertEqual('fizz', fb(3))

    def test_4(self):
        self.assertEqual('buzz', fb(5))

    def test_5(self):
        self.assertEqual('fizz', fb(6))

    def test_6(self):
        self.assertEqual('buzz', fb(10))

    def test_7(self):
        self.assertEqual('fizzbuzz', fb(15))

if __name__ == '__main__':
    unittest.main()