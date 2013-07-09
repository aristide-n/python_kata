__author__ = 'Aristide'

from nose.tools import assert_true, assert_equal
from unittest import TestCase




class TestCoinChanger(TestCase):

    def test_coin_changer(self):
        """
        Note: The coin set includes the unit value

        Given:
            If all coins are factors in increasing order, the Greedy Algorithm is optimal
            Otherwise, if greedy algorithm gives optimal solution for 100 + 25 - 1, it will give optimal solution for
            any amount
            (See proof at: http://people.cis.ksu.edu/~sathish/coinset.pdf)

        Test:
            Traverse the coin set from index 1: the second lowest coin denomination, to index 4: the highest coin. At
             each index:

             1. If the coin there is a multiple of the coin at the previous index, NO TEST is done, the greedy algorithm
             always works.

             2. Otherwise
                I. if it's the last index
                    A. set the maximum amount to test the greedy algorithm with as 100 + 25 - 1
                    B. For each amount between 1 above the highest coin and the maximum, calculate the change using the
                     full set of coins, and again with the set missing the highest coin. If the result of the former
                      calculation is the lesser, the Greedy algorithm is optimal for the coin set.

                II. If it's any other index in the middle of the set
                    A. set the amount to test the greedy algorithm with as 1 above the value of the coin at the
                    index
                    B. calculate the change using the set of coins up to the index, and again with the previous set
                    missing the coin at the index. If the result of the former calculation is the lesser, the Greedy
                    algorithm is optimal for the coin set up to the index.
        """

        coin_set = [1,5,10,25,100]

        for i in range(1,5):
            if coin_set[i] % coin_set[i-1] is 0:
                continue

            else:
                if i is 4:
                    edge_amount = coin_set[i] + coin_set[i-1] - 1

                else:
                    edge_amount = coin_set[i] + 1

                for k in range(coin_set[i] + 1, edge_amount + 1):
                    change_set_1 = coin_changer(k / 100.0, coin_set[:(i+1)])
                    change_set_2 = coin_changer(k / 100.0, coin_set[:i])

                    assert_true(sum(change_set_1.values()) < sum(change_set_2.values()))



def coin_changer(amount, coin_set):
    """
    Greedy algorithm: http://en.wikipedia.org/wiki/Greedy_algorithm

    For a coin set sorted in increasing order and an amount to give change for:
        1. Convert the amount in cents
        2. Initialize a dictionary that maps each coin denomination to the count of coins of that kind in the change
         for the amount
        3. Initialize a pointer to the end of the coin set which is the slot of the coin with the highest value
        4. Until the whole amount has been converted to change:
            I. If the amount is greater than the coin at the position of the pointer
                A. remove the value of the coin from the amount
                B Add 1 to the count of the coin in the change dictionary
            II. Otherwise, decrement the position of the pointer by 1
    """
    amount *= 100

    result = {1:0, 5:0, 10:0, 25:0, 100:0}

    i = len(coin_set) - 1

    while amount > 0:
        if amount >= coin_set[i]:
            amount -= coin_set[i]
            result[coin_set[i]] += 1
        else:
            i -= 1

    return result
