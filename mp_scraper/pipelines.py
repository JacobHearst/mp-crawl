import json
import logging

from mp_scraper.items import Area

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        
        # Track how many items scraped are already in the database
        self.area_duplicates = 0
        self.route_duplicates = 0

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE")
        )

    def open_spider(self, spider):
        if self.mongo_uri is None:
            spider.crawler.engine.close_spider(self, reason="No URI provided")

        if self.mongo_db is None:
            spider.crawler.engine.close_spider(self, reason="No database provided")
            

        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        logging.info(f"Skipped {self.area_duplicates} already seen areas")
        logging.info(f"Skipped {self.route_duplicates} already seen routes")

        self.client.close()

    def process_item(self, item, spider):
        collection_name = item.__class__.__name__.lower()
        try:
            self.db[collection_name].insert_one(dict(item))
        except DuplicateKeyError:
            if isinstance(item, Area):
                self.area_duplicates += 1
            else:
                self.route_duplicates += 1

        return item
