# -*- coding: utf-8 -*-
import calendar
import json
import logging
from mp_scraper.items import Area, Route, RouteGrade, ClimbSeasonValue, MonthlyTempAvgs, MonthlyPrecipAvgs, MpItemLoader, RouteGrades
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
        route_loader = MpItemLoader(item=Route(), response=response)
        route_id = self.extract_id(response.url)
        parent_link = response.css(
            "div.mb-half.small.text-warm a::attr(href)").extract()[-1]

        route_loader.add_value("link", response.url)
        route_loader.add_value("route_id", route_id)
        route_loader.add_value("parent_id", self.extract_id(parent_link))
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
            str -- The Mountain Project ID in the given link
        """
        matches = re.search(r"\.com/(?:area|route)/(\d+)", link)

        # Top level areas won't have a parent
        if matches is not None:
            return matches.group(1)

        return None

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
        item_type = MonthlyTempAvgs if var_name == "dataTemps" else MonthlyPrecipAvgs

        if len(monthly_avg_vals[0]) > 0:
            return [
                item_type(
                    area_id=area_id,
                    month=self.months[val[0]],
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
                    month=self.months[val[0]],
                    value=val[1]
                ) for val in climb_season_vals]
        
        # No climb season data for the given area
        return None


    def extract_grades(self, response, route_id):
        """Extract grade data from the page and return a list of RouteGrade items
        
        Arguments:
            response {scrapy.http.Response} -- Scrapy response for the route
            route_id {int} -- Route ID that the grade(s) belong to
        
        Returns:
            list[RouteGrade] -- A list of the grades associated with the route
        """
        grade_info_css = "div.col-md-9 > h2"

        grades_loader = MpItemLoader(item=RouteGrades(), response=response)
        grades_loader.add_css("yds", grade_info_css, re="(5\.\d+[a-z]?\+?|3rd|4th|Easy 5th)")
        grades_loader.add_css("ice", grade_info_css, re="[WA]I\d[-\d]?\+?")
        grades_loader.add_css("danger", grade_info_css, re="(R|X|PG13)")
        grades_loader.add_css("aid", grade_info_css, re="[CA]\d\+?")
        grades_loader.add_css("m", grade_info_css, re="M\d+")
        grades_loader.add_css("v", grade_info_css, re="V\d+\+?|V-easy")
        grades_loader.add_css("snow", grade_info_css, re="\w+\.? ?Snow")

        grades = grades_loader.load_item()

        # Convert grades to RouteGrade and filter 
        return [
            RouteGrade(
                route_id=route_id,
                grade=grades[grade],
                grade_system=grade
            ) for grade in grades if grades[grade] is not None]
