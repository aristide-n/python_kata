# -*- coding: utf-8 -*-

def update_aged(item):
    item.sell_in -= 1
    if item.quality < 50: item.quality += 1


def update_backstage(item):
    item.sell_in -= 1

    if item.sell_in < 0: item.quality = 0
    elif item.quality < 50:
        item.quality += 1
        if item.quality < 50 and item.sell_in < 10: item.quality += 1
        if item.quality < 50 and item.sell_in < 5: item.quality += 1

def update_conjured(item):
    item.sell_in -= 1
    if item.quality > 0: item.quality -= 2

    if item.sell_in < 0 and item.quality > 0: item.quality -= 2


def update_standard(item):
    item.sell_in -= 1
    if item.quality > 0: item.quality -= 1

    if item.sell_in < 0 and item.quality > 0: item.quality -= 1


def update_quality(items):
    for item in items:
        if item.name == "Aged Brie":
            update_aged(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            update_backstage(item)
        elif item.name == "Conjured bow tie":
            update_conjured(item)
        elif item.name != "Sulfuras, Hand of Ragnaros":
            update_standard(item)
        # Last: Do nothing for sulfuras items

    return items


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
