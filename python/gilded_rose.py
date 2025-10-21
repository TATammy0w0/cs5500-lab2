# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class UpdateStrategy:
    def update(self, item):
        raise NotImplementedError

    @staticmethod
    def _inc_quality(item, n=1):
        item.quality = min(50, item.quality + n)

    @staticmethod
    def _dec_quality(item, n=1):
        item.quality = max(0, item.quality - n)

class DefaultStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        self._dec_quality(item, 1)
        if item.sell_in < 0:
            self._dec_quality(item, 1)

class AgedBrieStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        self._inc_quality(item, 1)
        if item.sell_in < 0:
            self._inc_quality(item, 1)

class BackstageStrategy(UpdateStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
            return

        if item.sell_in < 5:
            self._inc_quality(item, 3)
        elif item.sell_in < 10:
            self._inc_quality(item, 2)
        else:
            self._inc_quality(item, 1)

class SulfurasStrategy(UpdateStrategy):
    def update(self, item):
        pass

class GildedRose(object):
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    AGED_BRIE = "Aged Brie"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"

    STRATEGIES = {
        AGED_BRIE: AgedBrieStrategy(),
        BACKSTAGE: BackstageStrategy(),
        SULFURAS: SulfurasStrategy(),
    }

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self.STRATEGIES.get(item.name, DefaultStrategy())
            strategy.update(item)