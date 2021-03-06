import scrapy
from scrapy.loader.processors import Compose, TakeFirst, Join, Identity
from scrapy.loader import ItemLoader


to_int = Compose(TakeFirst(), int)
to_float = Compose(TakeFirst(), float)
iter_to_float = lambda iter: [float(val) for val in iter]
strip = Compose(TakeFirst(), lambda value: value.strip())


class MpItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class Area(scrapy.Item):
    _id = scrapy.Field()
    ancestors = scrapy.Field(output_processor=Identity())
    name = scrapy.Field(input_processor=strip)
    coords = scrapy.Field()
    elevation = scrapy.Field(input_processor=Join(""), output_processor=to_int)
    link = scrapy.Field()
    temp_avgs = scrapy.Field()
    precip_avgs = scrapy.Field()
    climb_season = scrapy.Field()


class Route(scrapy.Item):
    _id = scrapy.Field()
    ancestors = scrapy.Field(output_processor=Identity())
    name = scrapy.Field(input_processor=strip)
    types = scrapy.Field(output_processor=Identity())
    rating = scrapy.Field(input_processor=to_float)
    link = scrapy.Field()
    length = scrapy.Field()
    pitches = scrapy.Field(input_processor=to_int)
    height = scrapy.Field(input_processor=to_int)
    grades = scrapy.Field()
