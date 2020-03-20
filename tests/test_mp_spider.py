import unittest
from unittest.mock import MagicMock

from mp_scraper.spiders.mp import MpSpider
from mp_scraper.items import MonthlyTempAvgs, MonthlyPrecipAvgs, ClimbSeasonValue


class TestMpSpider(unittest.TestCase):
    def setUp(self):
        self.spider = MpSpider()

    def test_extract_id(self):
        cases = [
            (".com/route/105717310/stolen-chimney", "105717310"),
            (".com/area/105716859/ancient-art", "105716859"),
            (".com", None),
            (".com/directory/105716859/route-or-area", None)
        ]

        for case in cases:
            with self.subTest(case=case):
                result = self.spider.extract_id(case[0])
                self.assertEqual(result, case[1])

    def test_extract_monthly_avg(self):
        def run_case(var_name, item_type):
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

            self.spider.extract_monthly_data = MagicMock(return_value=data)

            expected = [
                item_type(area_id=area_id, month=1, avg_low=1, avg_high=2),
                item_type(area_id=area_id, month=2, avg_low=3, avg_high=4),
                item_type(area_id=area_id, month=3, avg_low=5, avg_high=6),
                item_type(area_id=area_id, month=4, avg_low=7, avg_high=8),
                item_type(area_id=area_id, month=5, avg_low=9, avg_high=10),
                item_type(area_id=area_id, month=6, avg_low=11, avg_high=12),
                item_type(area_id=area_id, month=7, avg_low=13, avg_high=14),
                item_type(area_id=area_id, month=8, avg_low=15, avg_high=16),
                item_type(area_id=area_id, month=9, avg_low=17, avg_high=18),
                item_type(area_id=area_id, month=10, avg_low=19, avg_high=20),
                item_type(area_id=area_id, month=11, avg_low=21, avg_high=22),
                item_type(area_id=area_id, month=12, avg_low=23, avg_high=24)
            ]

            result = self.spider.extract_monthly_avg(area_id, None, var_name)
            
            self.assertEqual(len(expected), len(result))
            for index, item in enumerate(result):
                self.assertIsInstance(item, item_type)
                self.assertDictEqual(dict(expected[index]), dict(item))

        run_case("dataTemps", MonthlyTempAvgs)
        run_case("dataPrecip", MonthlyPrecipAvgs)

    def test_extract_climb_season(self):
        area_id=67890
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

        self.spider.extract_monthly_data = MagicMock(return_value=data)

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

        result = self.spider.extract_climb_season(area_id, None)

        self.assertEqual(len(expected), len(result))
        for index, item in enumerate(result):
                self.assertIsInstance(item, ClimbSeasonValue)
                self.assertDictEqual(dict(expected[index]), dict(item))

    def test_empty_monthly_vals(self):
        area_id = 12345
        self.spider.extract_monthly_data = MagicMock(return_value=[[]])
        
        temps = self.spider.extract_monthly_avg(area_id, None, "dataTemps")
        precip = self.spider.extract_monthly_avg(area_id, None, "dataPrecip")
        climb_season = self.spider.extract_climb_season(area_id, None)

        self.assertEqual(None, temps)
        self.assertEqual(None, precip)
        self.assertEqual(None, climb_season)



if __name__ == "__main__":
    unittest.main()
