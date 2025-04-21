# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):


    def test_regular_item_degrades_by_1(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[0].sell_in, 9)

    def test_conjured_item_degrades_by_2(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8)
        self.assertEqual(items[0].sell_in, 4)

    def test_conjured_item_degrades_by_4_after_sell_in(self):
        items = [Item("Conjured Mana Cake", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_item_never_negative(self):
        items = [Item("Conjured Bread", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)
        self.assertEqual(items[0].sell_in, 1)

    def test_backstage_passes_quality_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 22)  # +2
        self.assertEqual(items[0].sell_in, 9)

    def test_backstage_passes_drop_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[0].sell_in, -1)    

        
if __name__ == '__main__':
    unittest.main()
