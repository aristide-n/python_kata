# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, update_quality


class GildedRoseTest(unittest.TestCase):

    def test_standard_update(self):
        items = [Item("foo", 10, 40)]

        # Update lowers quality and sell In days by 1
        update_quality(items)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(39, items[0].quality)

        # Update past the sell date lowers the quality by 2
        for _ in range(10): update_quality(items)
        self.assertEqual(28, items[0].quality)

        # The quality is never negative
        for _ in range(20): update_quality(items)
        self.assertEqual(0, items[0].quality)


    def test_aged_update(self):
        items = [Item("Aged Brie", 10, 40)]

        # Update lowers sell In days by 1 and increases quality by 1
        update_quality(items)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(41, items[0].quality)

        # The quality is never greater than 50
        for _ in range(60): update_quality(items)
        self.assertEqual(50, items[0].quality)


    def test_sulfuras_update(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 40)]

        # Update does nothing to this item
        update_quality(items)
        self.assertEquals(10, items[0].sell_in)
        self.assertEquals(40, items[0].quality)


    def test_backstage_update(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 20)]

        # Update with more than 10 sell in days increases quality by 1 and lowers
        # sell In days by 1
        update_quality(items)
        self.assertEquals(19, items[0].sell_in)
        self.assertEquals(21, items[0].quality)

        # Update with 10 - 6 sell in days increases quality by 2 and lowers
        # sell In days by 1
        for _ in range(10): update_quality(items)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(32, items[0].quality)

        # Update with 5 - 1 sell in days increases quality by 3 and lowers
        # sell In days by 1
        for _ in range(5): update_quality(items)
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(43, items[0].quality)

        # The quality is never greater than 50
        for _ in range(4): update_quality(items)
        self.assertEqual(50, items[0].quality)

        # Update past the concert date date lowers the quality to 0
        update_quality(items)
        self.assertEqual(0, items[0].quality)


    def test_conjured_update(self):
        items = [Item("Conjured bow tie", 10, 40)]

        # Update lowers quality by 2 and sell In days by 1
        update_quality(items)
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(38, items[0].quality)

        # Update past the sell date lowers the quality by 4
        for _ in range(10): update_quality(items)
        self.assertEqual(16, items[0].quality)

        # The quality is never negative
        for _ in range(20): update_quality(items)
        self.assertEqual(0, items[0].quality)

if __name__ == "__main__":
    unittest.main()
