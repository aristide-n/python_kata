__author__ = 'Aristide'

from unittest import TestCase

from nose.tools import assert_equal, assert_true

from tdd.potter import price


class TestPotterPrice(TestCase):

    def testBasics(self):
        assert_equal(0, price([]))
        assert_equal(8, price([0]))
        assert_equal(8, price([1]))
        assert_equal(8, price([2]))
        assert_equal(8, price([3]))
        assert_equal(8, price([4]))
        assert_equal(8 * 2, price([0, 0]))
        assert_equal(8 * 3, price([1, 1, 1]))


    def testSimpleDiscounts(self):
        assert_equal(8 * 2 * 0.95, price([0, 1]))
        assert_equal(8 * 3 * 0.9, price([0, 2, 4]))
        assert_equal(8 * 4 * 0.8, price([0, 1, 2, 4]))
        assert_equal(8 * 5 * 0.75, price([0, 1, 2, 3, 4]))


    def testSeveralDiscounts(self):
        assert_equal(8 + (8 * 2 * 0.95), price([0, 0, 1]))
        assert_equal(2 * (8 * 2 * 0.95), price([0, 0, 1, 1]))
        assert_equal((8 * 4 * 0.8) + (8 * 2 * 0.95), price([0, 0, 1, 2, 2, 3]))
        assert_equal(8 + (8 * 5 * 0.75), price([0, 1, 1, 2, 3, 4]))


    def testEdgeCases(self):
        assert_equal(2 * (8 * 4 * 0.8), price([0, 0,
                                               1, 1,
                                               2, 2,
                                               3, 4]))
        assert_equal(3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8),
                     price([0, 0, 0, 0, 0,
                            1, 1, 1, 1, 1,
                            2, 2, 2, 2, 3,
                            3, 3, 3, 3, 4,
                            4, 4, 4]))