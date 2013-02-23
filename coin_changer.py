__author__ = 'Aristide'

from nose.tools import assert_true, assert_equal
from unittest import TestCase




class TestCoinChanger(TestCase):

    def test_coin_changer(self):
        """
        Given:
            If all coins are multiples in order, the GA is optimal
            Otherwise, if greedy algorithm gives optimal solution for 100 + 25 - 1, it will give optimal solution for
            any amount
        """

        coins = [1,5,10,25,100]

        for i in range(1,5):
            if coins[i] % coins[i-1] is 0:
                continue

            else:
                if i is 4:
                    edge = coins[i] + coins[i-1] - 1

                else:
                    edge = coins[i] + 1

                for k in range(coins[i] + 1, edge + 1):
                    change_set_1 = coin_changer(k / 100.0, coins[:(i+1)])
                    change_set_2 = coin_changer(k / 100.0, coins[:i])

                    assert_true(sum(change_set_1.values()) < sum(change_set_2.values()))



def coin_changer(amount, coins):
    amount *= 100

    coins.sort(reverse=True)

    result = {1:0, 5:0, 10:0, 25:0, 100:0}

    i = 0

    while amount > 0:
        if amount >= coins[i]:
            amount -= coins[i]
            result[coins[i]] += 1
        else:
            i += 1

    return result
