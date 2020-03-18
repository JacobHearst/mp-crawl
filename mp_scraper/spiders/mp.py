# -*- coding: utf-8 -*-
import json
import logging
from mp_scraper.items import Area, Route
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MpSpider(CrawlSpider):
    """Spider for crawling the Mountain Project"""
    name = "mp"
    allowed_domains = ["mountainproject.com"]
    start_urls = ["https://www.mountainproject.com"]

    rules = (
        Rule(LinkExtractor(
            allow=(r"\.com\/area\/\d+/[\w\d-]+$")), callback="parse_area", follow=True),
        Rule(LinkExtractor(
            allow=(r"\.com\/route\/\d+/[\w\d-]+$")), callback="parse_route"),
    )

    def parse_area(self, response):
        """Extract area data from page"""
        area = Area()
        area["area_id"] = self.extract_id(response.url)

        area["parent_id"] = self.extract_parent_id(response)
        area["name"] = response.css("title::text").re_first(r"(?<=[Climbing|Bouldering] in )(.+?)(?:,|$)")
        area["name"] = area["name"].replace("\"", "'")

        coords = response.css(
            "table.description-details td::text").re(r"(\d{1,3}(\.\d+)?),\s(-?\d{1,3}(\.\d+)?)")
        area["latitude"] = coords[0]
        area["longitude"] = coords[2]
        area["elevation"] = "".join(response.css("table.description-details td::text").re(r"(\d+),?(\d+) ft"))
        area["link"] = response.url

        area["temp_avg"] = self.extract_monthly_averages(response, "dataTemps")
        area["precip_avg"] = self.extract_monthly_averages(response, "dataPrecip")
        area["climb_season"] = self.extract_monthly_averages(response, "dataClimbSeason")

        return area


    def parse_route(self, response):
        """Extract route data from page"""
        route = Route()
        route["link"] = response.url

        route["route_id"] = self.extract_id(response.url)
        route["parent_id"] = self.extract_parent_id(response)

        route_name = response.css("title::text").re_first(r"(?<=Climb )(.+?)(?:,|$)")
        route["name"] = route_name.replace("\"", "'")

        route["grades"] = self.extract_grades(response)
        route["rating"] = response.css("#route-star-avg span a span::text").re_first(r"Avg: (\d(\.\d)?)")

        details_table = response.css("table.description-details td::text")
        route["types"] = ", ".join(details_table.re(r"(TR|Trad|Ice|Snow|Alpine|Aid|Boulder|Sport)"))
        route["length"] = details_table.re_first(r"Grade ([IVX]+)")
        route["pitches"] = details_table.re_first(r"(\d+) pitches")
        route["height"] = details_table.re_first(r"(\d+) ft")

        return route

    def extract_id(self, link):
        """Extract the Mountain Project id for a resource from its link and return the int id"""
        matches = re.search(r"\.com/(area|route)/(\d+)", link)
        if matches is not None:
            return int(matches.group(2))

        return None
    
    def extract_parent_id(self, response):
        """Find the parent area and return its id from the url and return the int id"""
        # Get the furthest right element in the breadcrumbs to extract parent id
        parent_link = response.css(
            "div.mb-half.small.text-warm a::attr(href)").extract()[-1]
        
        return self.extract_id(parent_link)

    def extract_monthly_averages(self, response, var_name):
        """Extract the JavaScript arrays containing the monthly average data and return a list"""
        regex = re.compile(var_name + r" = (\[.+\]);")
        rawAvgs = response.css("script::text").re_first(regex)

        # Parse the JavaScript array (in string representation) into a Python array
        return json.loads("{ \"val\": " + rawAvgs + "}")["val"]

    def extract_grades(self, response):
        """Extract any grade data from the page and return a dict of grades"""
        grade_info = response.css("div.col-md-9 > h2")
        
        grades = {
            "yds": grade_info.re_first(r"(5\.\d+[a-z]?\+?|3rd|4th|Easy 5th)"),
            "ice": grade_info.re_first(r"[WA]I\d[-\d]?\+?"),
            "danger": grade_info.re_first(r"(R|X|PG13)"),
            "aid": grade_info.re_first(r"[CA]\d\+?"),
            "m": grade_info.re_first(r"M\d+"),
            "v": grade_info.re_first(r"V\d+\+?|V-easy"),
            "snow": grade_info.re_first(r"\w+\.? ?Snow")
        }

        if all(grade is None for grade in grades.values()):
            logging.error("No grade found on page %s", response.url)

        return grades
