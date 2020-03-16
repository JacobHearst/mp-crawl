from collections.abc import Sequence, Collection
import json
import logging
import mysql.connector
from mp_scraper.items import SQLInsertQuery
from scrapy.exceptions import DropItem

class SqlPipeline(object):
    """Pipeline to execute sql queries on the database"""
    def open_spider(self, spider):
        """Open a database connection and create a cursor"""
        with open("db_config.json", "r") as json_file:
            db_config = json.load(json_file)

            self.db = mysql.connector.connect(
                host=db_config["host"],
                user=db_config["user"],
                passwd=db_config["passwd"],
                database=db_config["database"]
            )

        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        """Commit data and close database connection"""
        # self.db.commit()
        self.db.close()

    def process_item(self, item, spider):
        """Process an SQL query and execute it"""
        sql = None
        if isinstance(item, SQLInsertQuery):
            sql = self.build_insert(item)

        if sql is not None:
            self.cursor.execute(sql)
        else:
            logging.info(type(item))

        return item

    def build_insert(self, item):
        """Build an SQL INSERT query string and return it"""
        encoded_vals = [self.sql_encode(val) for val in item["data"].values()]
        return "INSERT INTO %s (%s) VALUES (%s)" % (
            item["table"],
            ", ".join(item["data"].keys()),
            ", ".join(encoded_vals)
        )


    def sql_encode(self, value):
        """Encode provided value and return a valid SQL value"""
        encoded_val = ""
        is_empty = False

        if isinstance(value, str):
            is_empty = len(value) == 0

        encoded_val = "NULL" if is_empty or value is None else value

        if isinstance(encoded_val, str) and encoded_val is not "NULL":
            encoded_val = "\"%s\"" % encoded_val

        return str(encoded_val)
