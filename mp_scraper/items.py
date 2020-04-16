import scrapy
from scrapy.loader.processors import Compose, TakeFirst, Join, Identity
from scrapy.loader import ItemLoader


to_int = Compose(TakeFirst(), int)
to_float = Compose(TakeFirst(), float)


class MpItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class Area(scrapy.Item):
    _id = scrapy.Field()
    parent_id = scrapy.Field()
    name = scrapy.Field()
    latitude = scrapy.Field(input_processor=to_float)
    longitude = scrapy.Field(input_processor=to_float)
    elevation = scrapy.Field(input_processor=Join(""), output_processor=to_int)
    link = scrapy.Field()
    temp_avgs = scrapy.Field(output_processor=Identity())
    precip_avgs = scrapy.Field(output_processor=Identity())
    climb_season = scrapy.Field(output_processor=Identity())


class Route(scrapy.Item):
    _id = scrapy.Field()
    parent_id = scrapy.Field()
    name = scrapy.Field()
    types = scrapy.Field(input_processor=Join(", "))
    rating = scrapy.Field(input_processor=to_float)
    link = scrapy.Field()
    length = scrapy.Field()
    pitches = scrapy.Field(input_processor=to_int)
    height = scrapy.Field(input_processor=to_int)
    grades = scrapy.Field()
