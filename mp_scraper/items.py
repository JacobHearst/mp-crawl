import scrapy
from scrapy.loader.processors import Compose, TakeFirst, Join, Identity
from scrapy.loader import ItemLoader

from enum import Enum


to_int = Compose(TakeFirst(), int)
to_float = Compose(TakeFirst(), float)
iter_to_float = lambda iter: [float(val) for val in iter]
strip = Compose(TakeFirst(), lambda value: value.strip())


class MpItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class Area(scrapy.Item):
    """An area listed on Mountain Project
    Temp/precip_avgs dictionary format: {
        1: {
            "avg_low": int,
            "avg_high": int
        },
        2: {...},
        ...
        12: {...}
        
    }

    Climb_season dictionary format: {
        1: int,
        2: int,
        ...
        12: int
    }
    """
    _id = scrapy.Field()
    parent_id = scrapy.Field()
    name = scrapy.Field(input_processor=strip)
    coords = scrapy.Field() # [Latitude, Longitude]
    elevation = scrapy.Field(input_processor=Join(""), output_processor=to_int) # Elevation in feet
    link = scrapy.Field()
    temp_avgs = scrapy.Field()
    precip_avgs = scrapy.Field()
    climb_season = scrapy.Field()


class Route(scrapy.Item):
    """A route listed on Mountain Project
    Route types: TR, Trad, Ice, Snow, Alpine, Aid, Boulder, Sport, Mixed

    Grades dictionary format: {
        "yds": {
            "grade": string,
            "sort_index": int
        },
        ... // Other grade systems
    }
    """
    _id = scrapy.Field()
    parent_id = scrapy.Field()
    name = scrapy.Field(input_processor=strip)
    types = scrapy.Field(output_processor=Identity()) # Array of the route's types
    rating = scrapy.Field(input_processor=to_float)
    link = scrapy.Field()
    length = scrapy.Field() # Length from I-VII
    pitches = scrapy.Field(input_processor=to_int)
    height = scrapy.Field(input_processor=to_int) # Height in feet
    grades = scrapy.Field()
