import scrapy
from scrapy.loader.processors import Compose, TakeFirst, Join
from scrapy.loader import ItemLoader


to_int = Compose(TakeFirst(), int)
to_float = Compose(TakeFirst(), float)
escape_quotes = Compose(TakeFirst(), lambda val: val.replace("\"", "\""))


class MpItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

class Area(scrapy.Item):
    area_id = scrapy.Field(output_processor=to_int)
    parent_id = scrapy.Field(output_processor=to_int)
    name = scrapy.Field(output_processor=escape_quotes)
    latitude = scrapy.Field(output_processor=to_float)
    longitude = scrapy.Field(output_processor=to_float)
    elevation = scrapy.Field(output_processor=Compose(Join(""), to_int))
    link = scrapy.Field()


class Route(scrapy.Item):
    route_id = scrapy.Field(output_processor=to_int)
    parent_id = scrapy.Field(output_processor=to_int)
    name = scrapy.Field(output_processor=escape_quotes)
    types = scrapy.Field(output_processor=Join(", "))
    rating = scrapy.Field(output_processor=to_float)
    link = scrapy.Field()
    length = scrapy.Field()
    pitches = scrapy.Field(output_processor=to_int)
    height = scrapy.Field(output_processor=to_int)


class MonthlyAverage(scrapy.Item):
    area_id = scrapy.Field(output_processor=to_int)
    month = scrapy.Field()
    avg_low = scrapy.Field(output_processor=to_float)
    avg_high = scrapy.Field(output_processor=to_float)


class MonthlyTempAvgs(MonthlyAverage):
    pass


class MonthlyPrecipAvgs(MonthlyAverage):
    pass


class ClimbSeasonValue(scrapy.Item):
    area_id = scrapy.Field(output_processor=to_int)
    month = scrapy.Field()
    value = scrapy.Field(output_processor=to_float)



class RouteGrades(scrapy.Item):
    yds = scrapy.Field()
    ice = scrapy.Field()
    danger = scrapy.Field()
    aid = scrapy.Field()
    m = scrapy.Field()
    v = scrapy.Field()
    snow = scrapy.Field()


class RouteGrade(scrapy.Item):
    route_id = scrapy.Field(output_processor=to_int)
    grade = scrapy.Field()
    grade_system = scrapy.Field()
