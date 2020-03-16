import calendar
import logging
from mp_scraper.items import Area, SQLInsertQuery


class AreaMiddleware:
    months = dict((v, k) for k, v in enumerate(calendar.month_name))

    def process_spider_output(self, response, result, spider):
        for item in result:
            if isinstance(item, Area):
                required_fields = ["area_id", "name", "link"]
                missing_keys = [field for field in item if item[field]
                                is None and field in required_fields]

                if len(missing_keys) == 0:
                    for query in self.process_area(item):
                        yield query
                else:
                    logging.error('MISSING_KEYS: %s' % (missing_keys))
                    yield None
            else:
                yield item

    def process_area(self, item):
        """Build SQLQuerys to insert area data into the database"""
        fields = ["area_id", "parent_id", "name",
                       "latitude", "longitude", "elevation", "link"]
        data = {field: val for field,
                       val in item.items() if field in fields}

        return [
            SQLInsertQuery(table="area", data=data),
            *self.process_monthly_avg(item["area_id"], "temp_avg", item["temp_avg"]),
            *self.process_monthly_avg(item["area_id"], "precip_avg", item["precip_avg"]),
            *self.process_climb_season(item["area_id"], item["climb_season"]),
        ]

    def process_monthly_avg(self, area_id, table, data):
        """Build SQLQuerys to insert monthly high/low averages into the database"""
        queries = []

        for month in data:
            data = {
                "area_id": area_id,
                "month": self.months[month[0]],
                "avg_high": month[1],
                "avg_low": month[2]
            }
            values = [area_id, self.months[month[0]], month[1], month[2]]

            queries.append(SQLInsertQuery(table=table, data=data))

        return queries

    def process_climb_season(self, area_id, data):
        """Build SQLQuerys to insert single monthly values into the database"""
        queries = []

        if len(data[0]) > 0:
            for month in data:
                data = {
                    "area_id": area_id,
                    "month": self.months[month[0]],
                    "value": month[1]
                }

                queries.append(SQLInsertQuery(table="climb_season", data=data))
        
        return queries
