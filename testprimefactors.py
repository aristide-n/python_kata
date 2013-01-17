__author__ = 'Aristide'

from primefactors import generate
import unittest

class TestPrimeFactors(unittest.TestCase):

    def factlist(self, *factors):
        list = []

        for f in factors:
            list.append(f)

        return  list

    def test_one(self):
        self.assertEqual(self.factlist(), generate(1))


    def test_two(self):
        self.assertEqual(self.factlist(2), generate(2))


    def test_three(self):
        self.assertEqual(self.factlist(3), generate(3))


    def test_four(self):
        self.assertEqual(self.factlist(2,2), generate(4))


    def test_five(self):
        self.assertEqual(self.factlist(2,3), generate(6))


    def test_six(self):
        self.assertEqual(self.factlist(2,2,2), generate(8))


    def test_seven(self):
        self.assertEqual(self.factlist(3,3), generate(9))

if __name__ == '__main__':
    unittest.main()