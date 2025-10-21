# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = items

    @staticmethod
    def _inc_quality(item, by=1):
        item.quality = min(50, item.quality + by)

    @staticmethod
    def _dec_quality(item, by=1):
        item.quality = max(0, item.quality - by)

    @staticmethod
    def _dec_sell_in(item):
        item.sell_in -= 1

    def _update_sulfuras(self, item):
        return

    def _update_aged_brie(self, item):
        self._inc_quality(item, 1)
        self._dec_sell_in(item)
        if item.sell_in < 0:
            self._inc_quality(item, 1)

    def _update_backstage(self, item):
        if item.sell_in > 10:
            self._inc_quality(item, 1)
        elif item.sell_in > 5:
            self._inc_quality(item, 2)
        elif item.sell_in >= 0:
            self._inc_quality(item, 3)

        self._dec_sell_in(item)

        if item.sell_in < 0:
            item.quality = 0

    def _update_default(self, item):
        self._dec_quality(item, 1)
        self._dec_sell_in(item)
        if item.sell_in < 0:
            self._dec_quality(item, 1)

    def update_quality(self):
        for item in self.items:
            if item.name == self.SULFURAS:
                self._update_sulfuras(item)
            elif item.name == self.AGED_BRIE:
                self._update_aged_brie(item)
            elif item.name == self.BACKSTAGE:
                self._update_backstage(item)
            else:
                self._update_default(item)