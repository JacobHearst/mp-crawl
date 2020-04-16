from mp_scraper.spiders.mp import MpSpider
from mp_scraper.items import Area, Route
import os
from scrapy.http import Request, HtmlResponse
from tests import compare_item_iter
from tests.pages.expected_items import expected_items
import unittest


class TestItemExtraction(unittest.TestCase):
    def test_area_extraction(self):
        spider = MpSpider()
        areas = expected_items["areas"]
        for page in areas:
            with self.subTest(page=page):
                url = areas[page][0]["link"]
                result = spider.parse_area(self.mock_response("areas", page, url))
                compare_item_iter(self, areas[page], result)

    def test_route_extraction(self):
        spider = MpSpider()
        routes = expected_items["routes"]
        for page in routes:
            with self.subTest(page=page):
                url = routes[page][0]["link"]
                result = spider.parse_route(self.mock_response("routes", page, url))
                compare_item_iter(self, routes[page], result)

    def mock_response(self, sub_dir, resource_name, url):
        request = Request(url=url)

        responses_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(responses_dir, "pages", sub_dir, resource_name + ".html")
        file_obj = open(file_path, 'r', encoding="utf-8")

        response = HtmlResponse(url=url, request=request,
                                body=file_obj.read(), encoding="utf-8")
        file_obj.close()

        return response


if __name__ == "__main__":
    unittest.main()

