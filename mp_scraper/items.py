# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Area(scrapy.Item):
    area_id = scrapy.Field()
    parent_id = scrapy.Field()
    name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    elevation = scrapy.Field()
    link = scrapy.Field()
    temp_avg = scrapy.Field()
    precip_avg = scrapy.Field()
    climb_season = scrapy.Field()

class Route(scrapy.Item):
    route_id = scrapy.Field()
    parent_id = scrapy.Field()
    name = scrapy.Field()
    types = scrapy.Field()
    rating = scrapy.Field()
    link = scrapy.Field()
    grades = scrapy.Field()
    grade = scrapy.Field()
    pitches = scrapy.Field()
    height = scrapy.Field()


class SQLInsertQuery(scrapy.Item):
    table = scrapy.Field()
    data = scrapy.Field()
