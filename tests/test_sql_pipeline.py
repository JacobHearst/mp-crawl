from mp_scraper.pipelines import SqlPipeline
from mp_scraper.items import Route, Area, RouteGrade, ClimbSeasonValue, MonthlyPrecipAvg, MonthlyTempAvg

import mysql.connector
from scrapy.exceptions import DropItem
import unittest
from unittest.mock import MagicMock


class TestSqlPipeline(unittest.TestCase):
    def test_process_item(self):
        pipeline = SqlPipeline()
        item = Area(area_id=111222, name="Area", link="link")

        pipeline.insert_item = MagicMock()

        result = pipeline.process_item(item, None)
        pipeline.insert_item.assert_called_with('area', item)
        self.assertEqual(result, item)

    def test_process_invalid_item(self):
        pipeline = SqlPipeline()
        item = Area(area_id=111222, name="Area", link=None)

        with self.assertRaises(DropItem):
            result = pipeline.process_item(item, None)

    def test_sql_encode(self):
        pipeline = SqlPipeline()
        cases = [
            (1, "1"),
            ("", "NULL"),
            ("String", "\"String\""),
            ("Good 'Ol single quotes", "\"Good 'Ol single quotes\""),
            ("\"Quotes\" - Quotes on quotes", "\"\"Quotes\" - Quotes on quotes\""),
            (0, "0"),
            (True, "True")
        ]

        for case in cases:
            with self.subTest(case=case):
                result = pipeline.sql_encode(case[0])
                self.assertEqual(case[1], result)
