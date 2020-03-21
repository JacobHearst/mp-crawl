import unittest
from unittest.mock import MagicMock

from mp_scraper.spiders.mp import MpSpider
from mp_scraper.items import MonthlyTempAvg, MonthlyPrecipAvg, ClimbSeasonValue

from tests import compare_item_iter


class TestMpSpider(unittest.TestCase):
    def test_extract_id(self):
        spider = MpSpider()
        cases = [
            (".com/route/105717310/stolen-chimney", 105717310),
            (".com/area/105716859/ancient-art", 105716859),
            (".com", None),
            (".com/directory/105716859/route-or-area", None)
        ]

        for case in cases:
            with self.subTest(case=case):
                result = spider.extract_id(case[0])
                self.assertEqual(result, case[1])

    def test_extract_temps(self):
        spider = MpSpider()
        area_id = 12345
        data = [
            ["January", 1, 2],
            ["February", 3, 4],
            ["March", 5, 6],
            ["April", 7, 8],
            ["May", 9, 10],
            ["June", 11, 12],
            ["July", 13, 14],
            ["August", 15, 16],
            ["September", 17, 18],
            ["October", 19, 20],
            ["November", 21, 22],
            ["December", 23, 24]
        ]

        spider.extract_monthly_data = MagicMock(return_value=data)

        expected = [
            MonthlyPrecipAvg(area_id=area_id, month=1, avg_high=1, avg_low=2),
            MonthlyPrecipAvg(area_id=area_id, month=2, avg_high=3, avg_low=4),
            MonthlyPrecipAvg(area_id=area_id, month=3, avg_high=5, avg_low=6),
            MonthlyPrecipAvg(area_id=area_id, month=4, avg_high=7, avg_low=8),
            MonthlyPrecipAvg(area_id=area_id, month=5, avg_high=9, avg_low=10),
            MonthlyPrecipAvg(area_id=area_id, month=6, avg_high=11, avg_low=12),
            MonthlyPrecipAvg(area_id=area_id, month=7, avg_high=13, avg_low=14),
            MonthlyPrecipAvg(area_id=area_id, month=8, avg_high=15, avg_low=16),
            MonthlyPrecipAvg(area_id=area_id, month=9, avg_high=17, avg_low=18),
            MonthlyPrecipAvg(area_id=area_id, month=10, avg_high=19, avg_low=20),
            MonthlyPrecipAvg(area_id=area_id, month=11, avg_high=21, avg_low=22),
            MonthlyPrecipAvg(area_id=area_id, month=12, avg_high=23, avg_low=24)
        ]

        result = spider.extract_monthly_avg(area_id, None, "dataPrecip")
        compare_item_iter(self, expected, result)

    def test_extract_temps(self):
        spider = MpSpider()
        area_id = 12345
        data = [
            ["January", 2, 1],
            ["February", 4, 3],
            ["March", 6, 5],
            ["April", 8, 7],
            ["May", 10, 9],
            ["June", 12, 11],
            ["July", 14, 13],
            ["August", 16, 15],
            ["September", 18, 17],
            ["October", 20, 19],
            ["November", 22, 21],
            ["December", 24, 23]
        ]

        spider.extract_monthly_data = MagicMock(return_value=data)

        expected = [
            MonthlyTempAvg(area_id=area_id, month=1, avg_low=1, avg_high=2),
            MonthlyTempAvg(area_id=area_id, month=2, avg_low=3, avg_high=4),
            MonthlyTempAvg(area_id=area_id, month=3, avg_low=5, avg_high=6),
            MonthlyTempAvg(area_id=area_id, month=4, avg_low=7, avg_high=8),
            MonthlyTempAvg(area_id=area_id, month=5, avg_low=9, avg_high=10),
            MonthlyTempAvg(area_id=area_id, month=6, avg_low=11, avg_high=12),
            MonthlyTempAvg(area_id=area_id, month=7, avg_low=13, avg_high=14),
            MonthlyTempAvg(area_id=area_id, month=8, avg_low=15, avg_high=16),
            MonthlyTempAvg(area_id=area_id, month=9, avg_low=17, avg_high=18),
            MonthlyTempAvg(area_id=area_id, month=10, avg_low=19, avg_high=20),
            MonthlyTempAvg(area_id=area_id, month=11, avg_low=21, avg_high=22),
            MonthlyTempAvg(area_id=area_id, month=12, avg_low=23, avg_high=24)
        ]

        result = spider.extract_monthly_avg(area_id, None, "dataTemps")
        compare_item_iter(self, expected, result)

    def test_extract_climb_season(self):
        spider = MpSpider()
        area_id = 67890
        data = [
            ["October", 19, 20],
            ["March", 5, 6],
            ["April", 7, 8],
            ["July", 13, 14],
            ["January", 1, 2],
            ["June", 11, 12],
            ["February", 3, 4],
            ["December", 23, 24],
            ["May", 9, 10],
            ["August", 15, 16],
            ["November", 21, 22],
            ["September", 17, 18],
        ]

        spider.extract_monthly_data = MagicMock(return_value=data)

        expected = [
            ClimbSeasonValue(area_id=area_id, month=10, value=19),
            ClimbSeasonValue(area_id=area_id, month=3, value=5),
            ClimbSeasonValue(area_id=area_id, month=4, value=7),
            ClimbSeasonValue(area_id=area_id, month=7, value=13),
            ClimbSeasonValue(area_id=area_id, month=1, value=1),
            ClimbSeasonValue(area_id=area_id, month=6, value=11),
            ClimbSeasonValue(area_id=area_id, month=2, value=3),
            ClimbSeasonValue(area_id=area_id, month=12, value=23),
            ClimbSeasonValue(area_id=area_id, month=5, value=9),
            ClimbSeasonValue(area_id=area_id, month=8, value=15),
            ClimbSeasonValue(area_id=area_id, month=11, value=21),
            ClimbSeasonValue(area_id=area_id, month=9, value=17)
        ]

        result = spider.extract_climb_season(area_id, None)
        compare_item_iter(self, expected, result)

    def test_empty_monthly_vals(self):
        spider = MpSpider()
        area_id = 12345
        spider.extract_monthly_data = MagicMock(return_value=[[]])

        temps = spider.extract_monthly_avg(area_id, None, "dataTemps")
        precip = spider.extract_monthly_avg(area_id, None, "dataPrecip")
        climb_season = spider.extract_climb_season(area_id, None)

        self.assertEqual([], temps)
        self.assertEqual([], precip)
        self.assertEqual([], climb_season)


if __name__ == "__main__":
    unittest.main()
