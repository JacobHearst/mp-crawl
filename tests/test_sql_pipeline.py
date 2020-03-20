import unittest
from unittest.mock import MagicMock

from mp_scraper.pipelines import SqlPipeline
from mp_scraper.items import Route, Area, RouteGrade, ClimbSeasonValue, MonthlyPrecipAvgs, MonthlyTempAvgs

import mysql.connector

class TestSqlPipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = SqlPipeline()

    def test_sql_encode(self):
        cases = [
            (1, "1"),
            ("", "NULL"),
            ("String", "\"String\""),
            ("Good 'Ol single quotes", "\"Good 'Ol single quotes\""),
            ("\"Quotes\" - Quotes on quotes", "\"\"Quotes\" - Quotes on quotes\""),
            (0, "0"),
            (None, "NULL"),
            (True, "True")
        ]

        for case in cases:
            with self.subTest(case=case):
                result = self.pipeline.sql_encode(case[0])
                self.assertEqual(case[1], result)
