import scrapy
from scrapy.loader.processors import Compose, TakeFirst, Join
from scrapy.loader import ItemLoader


to_int = Compose(TakeFirst(), int)
to_float = Compose(TakeFirst(), float)
escape_quotes = Compose(TakeFirst(), lambda val: val.replace("\"", "\\\""))


class MpItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

class Area(scrapy.Item):
    area_id = scrapy.Field(input_processor=to_int)
    parent_id = scrapy.Field(input_processor=to_int)
    name = scrapy.Field(input_processor=escape_quotes)
    latitude = scrapy.Field(input_processor=to_float)
    longitude = scrapy.Field(input_processor=to_float)
    elevation = scrapy.Field(input_processor=Join(""), output_processor=to_int)
    link = scrapy.Field()


class Route(scrapy.Item):
    route_id = scrapy.Field(input_processor=to_int)
    parent_id = scrapy.Field(input_processor=to_int)
    name = scrapy.Field(input_processor=escape_quotes)
    types = scrapy.Field(input_processor=Join(", "))
    rating = scrapy.Field(input_processor=to_float)
    link = scrapy.Field()
    length = scrapy.Field()
    pitches = scrapy.Field(input_processor=to_int)
    height = scrapy.Field(input_processor=to_int)


class MonthlyTempAvg(scrapy.Item):
    area_id = scrapy.Field(input_processor=to_int)
    month = scrapy.Field()
    avg_low = scrapy.Field(input_processor=to_float)
    avg_high = scrapy.Field(input_processor=to_float)


class MonthlyPrecipAvg(scrapy.Item):
    area_id = scrapy.Field(input_processor=to_int)
    month = scrapy.Field()
    avg_low = scrapy.Field(input_processor=to_float)
    avg_high = scrapy.Field(input_processor=to_float)


class ClimbSeasonValue(scrapy.Item):
    area_id = scrapy.Field(input_processor=to_int)
    month = scrapy.Field()
    value = scrapy.Field(input_processor=to_float)



class RouteGrades(scrapy.Item):
    yds = scrapy.Field()
    ice = scrapy.Field()
    danger = scrapy.Field()
    aid = scrapy.Field()
    m = scrapy.Field()
    v = scrapy.Field()
    snow = scrapy.Field()


class RouteGrade(scrapy.Item):
    route_id = scrapy.Field(input_processor=to_int)
    grade = scrapy.Field()
    grade_system = scrapy.Field()
