# -*- coding: utf-8 -*-
import calendar
import json
import logging
from mp_scraper.items import Area, Route, MpItemLoader
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


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

    months = dict((v, k) for k, v in enumerate(calendar.month_name))

    def parse_area(self, response):
        """Extract area data from page

        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the area

        Returns:
            list[Item] -- List of items extracted from the page
        """
        area_loader = MpItemLoader(item=Area(), response=response)
        id = self.extract_id(response.url)

        area_loader.add_value("link", response.url)
        area_loader.add_value("_id", id)
        area_loader.add_value("parent_id", self.extract_parent_id(response))
        area_loader.add_css("name", "title::text",
                            re=r"(?<=[Climbing|Bouldering] in )(.+?)(?:,|$)")

        details_css = "table.description-details td::text"
        coords = response.css(details_css).re(
            r"(-?\d+(?:\.\d+)?),\s(-?\d+(?:\.\d+)?)")
        area_loader.add_value("latitude", coords[0])
        area_loader.add_value("longitude", coords[1])
        area_loader.add_css("elevation", details_css, re=r"(\d+),?(\d+) ft")

        area_loader.add_value(
            "temp_avgs", self.extract_monthly_avg(response, "dataTemps"))
        area_loader.add_value(
            "precip_avgs", self.extract_monthly_avg(response, "dataPrecip"))
        area_loader.add_value(
            "climb_season", self.extract_climb_season(response))

        return area_loader.load_item()

    def parse_route(self, response):
        """Extract route data from page

        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the route

        Returns:
            list[Item] -- List of items extracted from the page
        """
        route_loader = MpItemLoader(item=Route(), response=response)
        id = self.extract_id(response.url)

        route_loader.add_value("link", response.url)
        route_loader.add_value("_id", id)
        route_loader.add_value("parent_id", self.extract_parent_id(response))
        route_loader.add_css("name", "title::text",
                             re=r"(?<=Climb )(.+?)(?:,|$)")
        route_loader.add_css(
            "rating", "#route-star-avg span a span::text", re=r"Avg: (\d(\.\d)?)")

        details_css = "table.description-details td::text"
        route_loader.add_css(
            "types", details_css, re=r"(TR|Trad|Ice|Snow|Alpine|Aid|Boulder|Sport|Mixed)")
        route_loader.add_css("length", details_css, re=r"Grade ([IVX]+)")
        route_loader.add_css("pitches", details_css, re=r"(\d+) pitches")
        route_loader.add_css("height", details_css, re=r"(\d+) ft")
        route_loader.add_value("grades", self.extract_grades(response))

        return route_loader.load_item()

    def extract_id(self, link):
        """Extract the Mountain Project id for a resource from its link

        Arguments:
            link {str} -- Link to extract the ID From

        Returns:
            int -- The Mountain Project ID in the given link
        """
        matches = re.search(r"\.com/(?:area|route)/(\d+)", link)

        # Top level areas won't have a parent
        if matches is not None:
            return int(matches.group(1))

        return None

    def extract_parent_id(self, response):
        parent_link = response.css(
            "div.mb-half.small.text-warm a::attr(href)").extract()[-1]

        return self.extract_id(parent_link)

    def extract_monthly_data(self, response, var_name):
        """Extract the JavaScript arrays containing monthly data

        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the area
            var_name {str} -- Name of the variable to extract

        Returns:
            list -- The 2D list of monthly data
        """
        regex = re.compile(var_name + r" = (\[.+\]);")
        data = response.css("script::text").re_first(regex)

        return json.loads(data)

    def extract_monthly_avg(self, response, var_name):
        """Extract a javascript array containing monthly averages for an area

        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the area
            var_name {str} -- Name of the variable to extract

        Returns:
            list -- The parsed monthly averages extracted from the array (if any, otherwise returns empty list)
        """
        monthly_avg_vals = self.extract_monthly_data(response, var_name)

        if len(monthly_avg_vals) > 0:
            return [
                {
                    "month": self.months[val[0]],
                    "avg_low": float(min(val[1], val[2])),
                    "avg_high": float(max(val[1], val[2]))
                } for val in monthly_avg_vals if len(val) > 0]

        # No temp/precip data for the given area
        return []

    def extract_climb_season(self, response):
        """Extract the climbing season data for an area

        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the area

        Returns:
            list[ClimbSeasonValue] -- The parsed monthly averages extracted from the array (if any, otherwise returns empty list)
        """
        climb_season_vals = self.extract_monthly_data(
            response, "dataClimbSeason")

        if len(climb_season_vals) > 0:
            return [
                {
                    "month": int(self.months[val[0]]),
                    "popularity": float(val[1])
                } for val in climb_season_vals if len(val) > 0]

        # No climb season data for the given area
        return []

    def extract_grades(self, response):
        """Extract grade data from the page and return a dict containing the non-null grades

        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the route

        Returns:
            dict -- A dict of the grades associated with the route
        """
        grade_info = response.css("div.col-md-9 > h2")

        grades = {
            "yds": grade_info.re_first(r"(5\.[\d\w\+\-\?/]{1,5}|3rd|4th|Easy 5th)"),
            "ice": grade_info.re_first(r"[WA]I\d(?:-\d)?[\+-]?"),
            "danger": grade_info.re_first(r" (R|X|PG13)"),
            "aid": grade_info.re_first(r"[CA]\d\+?"),
            "mixed": grade_info.re_first(r"M[\d-]+"),
            "hueco": grade_info.re_first(r"V[\dB-]+[\+-]?\d*(?:easy)?"),
            "snow": grade_info.re_first(r"\w+\.? ?Snow")
        }

        return {k: v for k, v in grades.items() if v is not None}
