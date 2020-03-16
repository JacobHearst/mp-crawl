import logging
from mp_scraper.items import Route, SQLInsertQuery


class RouteMiddleware:
    def process_spider_output(self, response, result, spider):
        for item in result:
            if isinstance(item, Route):
                required_fields = ["route_id",
                                   "parent_id", "name", "link", "types"]
                missing_keys = [field for field in item if item[field]
                                is None and field in required_fields]

                if len(missing_keys) == 0:
                    for query in self.process_route(item):
                        yield query
                else:
                    logging.error('MISSING_KEYS: %s' % (missing_keys))
                    yield None
            else:
                yield item

    def process_route(self, item):
        """Build SQLQuerys to insert route data into the database and returns a list of those queries"""
        fields = ["route_id", "parent_id", "name",
                  "rating", "types", "pitches", "height", "link"]
        data = {field: val for field, val in item.items() if field in fields}

        return [
            SQLInsertQuery(table="route", data=data),
            *self.process_grades(item["route_id"], item["grades"])
        ]

    def process_grades(self, route_id, grades):
        """Build SQLQuerys to insert route grade data into the database and returns a list of those queries"""
        queries = []

        for grade_system in grades:
            if grades[grade_system] is not None:
                data = {
                    "route_id": route_id,
                    "grade": grades[grade_system],
                    "grade_system": grade_system
                }

                queries.append(SQLInsertQuery(table="route_grade", data=data))

        return queries
