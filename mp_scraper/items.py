import calendar
import re

import scrapy
from scrapy.loader.processors import Compose, TakeFirst, Join
from scrapy.loader import ItemLoader


months = dict((v, k) for k, v in enumerate(calendar.month_name))

to_int = Compose(TakeFirst(), int)
to_float = Compose(TakeFirst(), float)
swap_quotes = Compose(TakeFirst(), lambda val: val.replace("\"", "'"))
month_to_int = lambda month: months[month]


class SqlObject(scrapy.Item):
    table_name = scrapy.Field()
    required_fields = scrapy.Field()


class Area(SqlObject):
    table_name = "area"
    required_fields = ["area_id", "name", "link"]

    area_id = scrapy.Field(input_processor=to_int)
    parent_id = scrapy.Field(input_processor=to_int)
    name = scrapy.Field(input_processor=swap_quotes)
    latitude = scrapy.Field(input_processor=TakeFirst())
    longitude = scrapy.Field(input_processor=to_float)
    elevation = scrapy.Field(input_processor=Compose(Join(""), to_int))
    link = scrapy.Field()


class Route(SqlObject):
    table_name = "route"
    required_fields = ["route_id", "parent_id", "name", "link"]

    route_id = scrapy.Field(input_processor=to_int)
    parent_id = scrapy.Field(input_processor=to_int)
    name = scrapy.Field(input_processor=swap_quotes)
    types = scrapy.Field(input_processor=Join(", "))
    rating = scrapy.Field(input_processor=to_float)
    link = scrapy.Field()
    length = scrapy.Field()
    pitches = scrapy.Field(input_processor=to_int)
    height = scrapy.Field(input_processor=to_int)


class MonthlyAverage(SqlObject):
    required_fields = ["area_id", "month", "avg_low", "avg_high"]

    area_id = scrapy.Field(input_processor=to_int)
    month = scrapy.Field(input_processor=month_to_int)
    avg_low = scrapy.Field(input_processor=to_float)
    avg_high = scrapy.Field(input_processor=to_float)


class ClimbSeasonValue(SqlObject):
    table_name = "climb_season"
    required_fields = ["area_id", "month", "value"]

    area_id = scrapy.Field(input_processor=to_int)
    month = scrapy.Field(input_processor=month_to_int)
    value = scrapy.Field(input_processor=to_float)


class RouteGrade(SqlObject):
    table_name = "route_grade"
    required_fields = ["route_id", "grade", "grade_system"]

    route_id = scrapy.Field(input_processor=to_int)
    grade = scrapy.Field()
    grade_system = scrapy.Field()
