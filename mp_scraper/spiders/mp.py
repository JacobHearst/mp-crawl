# -*- coding: utf-8 -*-
import json
import logging
from mp_scraper.items import Area, Route, RouteGrade, ClimbSeasonValue, MonthlyAverage
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
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

    def parse_area(self, response):
        """Extract area data from page
        
        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the area
        
        Returns:
            list[Item] -- List of items extracted from the page
        """
        area_loader = ItemLoader(item=Area(), response=response)
        area_id = self.extract_id(response.url)

        area_loader.add_value("link", response.url)
        area_loader.add_value("area_id", area_id)
        area_loader.add_value("parent_id", self.extract_parent_id(response))
        area_loader.add_css("name", "title::text", re="(?<=[Climbing|Bouldering] in )(.+?)(?:,|$)")

        details_css = "table.description-details td::text"
        coords = response.css(details_css).re(r"(-?\d+(?:\.\d+)?),\s(-?\d+(?:\.\d+)?)")
        area_loader.add_value("latitude", coords[0])
        area_loader.add_value("longitude", coords[1])
        area_loader.add_css("elevation", details_css, re="(\d+),?(\d+) ft")

        return [
            area_loader.load_item(),
            *self.extract_climb_season(area_id, response),
            *self.extract_monthly_avg(area_id, response, "dataTemps"),
            *self.extract_monthly_avg(area_id, response, "dataPrecip")
        ]


    def parse_route(self, response):
        """Extract route data from page
        
        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the route
        
        Returns:
            list[Item] -- List of items extracted from the page
        """
        route_loader = ItemLoader(item=Route(), response=response)
        route_id = self.extract_id(response.url)

        route_loader.add_value("link", response.url)
        route_loader.add_value("route_id", route_id)
        route_loader.add_value("parent_id", self.extract_parent_id(response))
        route_loader.add_css("name", "title::text", re="(?<=Climb )(.+?)(?:,|$)")
        route_loader.add_css("rating", "#route-star-avg span a span::text", re="Avg: (\d(\.\d)?)")

        details_css = "table.description-details td::text"
        route_loader.add_css("types", details_css, re="(TR|Trad|Ice|Snow|Alpine|Aid|Boulder|Sport)")
        route_loader.add_css("length", details_css, re="Grade ([IVX]+)")
        route_loader.add_css("pitches", details_css, re="(\d+) pitches")
        route_loader.add_css("height", details_css, re="(\d+) ft")

        return [
            route_loader.load_item(),
            *self.extract_grades(response, route_id)
        ]        

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
            return matches.group(1)

        return None

    def extract_parent_id(self, response):
        """Find the parent area and return its id from the url
        
        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the resource
        
        Returns:
            int -- The Mountain Project ID in the given link
        """
        # Get the furthest right element in the breadcrumbs to extract parent id
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
        rawAvgs = response.css("script::text").re_first(regex)

        return json.loads(rawAvgs)

    def extract_monthly_avg(self, area_id, response, var_name):
        """Extract a javascript array containing monthly averages for an area
        
        Arguments:
            area_id {int} -- ID of the area that the average belongs to
            response {scrapy.http.Response} -- Scrapy response for the area
            var_name {str} -- Name of the variable to extract
        
        Returns:
            list[MonthlyAverage] -- The parsed monthly averages extracted from the array (if any, otherwise returns None)
        """
        monthly_avg_vals = self.extract_monthly_data(response, var_name)
        table_name = "temp_avg" if var_name == "dataTemps" else "precip_avg"

        if len(monthly_avg_vals[0]) > 0:
            return [
                MonthlyAverage(
                    table_name=table_name,
                    area_id=area_id,
                    month=val[0],
                    avg_low=val[1],
                    avg_high=val[2]
                ) for val in monthly_avg_vals]
        
        # No temp/precip data for the given area
        return None

    def extract_climb_season(self, area_id, response):
        """Extract the climbing season data for an area
        
        Arguments:
            area_id {int} -- ID of the area that the data belongs to
            response {scrapy.http.Response} -- Scrapy response for the area
        
        Returns:
            list[ClimbSeasonValue] -- The parsed monthly averages extracted from the array (if any, otherwise returns None)
        """
        climb_season_vals = self.extract_monthly_data(response, "dataClimbSeason")

        if len(climb_season_vals[0]) > 0:
            return [
                ClimbSeasonValue(
                    area_id=area_id,
                    month=val[0],
                    value=val[1]
                ) for val in climb_season_vals]
        
        # No climb season data for the given area
        return None


    def extract_grades(self, response, route_id):
        """Extract any grade data from the page and return a list of RouteGrade items
        
        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the route
            route_id {int} -- Route ID that the grade(s) belong to
        
        Returns:
            list[RouteGrade] -- A list of the grades associated with the route
        """
        grade_info = response.css("div.col-md-9 > h2")

        grades = [
            RouteGrade(route_id=route_id, grade_system="yds", grade=grade_info.re_first(r"(5\.\d+[a-z]?\+?|3rd|4th|Easy 5th)")),
            RouteGrade(route_id=route_id, grade_system="ice", grade=grade_info.re_first(r"[WA]I\d[-\d]?\+?")),
            RouteGrade(route_id=route_id, grade_system="danger", grade=grade_info.re_first(r"(R|X|PG13)")),
            RouteGrade(route_id=route_id, grade_system="aid", grade=grade_info.re_first(r"[CA]\d\+?")),
            RouteGrade(route_id=route_id, grade_system="m", grade=grade_info.re_first(r"M\d+")),
            RouteGrade(route_id=route_id, grade_system="v", grade=grade_info.re_first(r"V\d+\+?|V-easy")),
            RouteGrade(route_id=route_id, grade_system="snow", grade=grade_info.re_first(r"\w+\.? ?Snow"))
        ]

        # Don't clog up the pipeline with items that are just going to be dropped
        return [grade for grade in grades if grade["grade"] is not None]
