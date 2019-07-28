# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy

class IcoParserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    slogan = scrapy.Field()
    description = scrapy.Field()
    categories = scrapy.Field()
    socials = scrapy.Field()
    rating = scrapy.Field()
    about = scrapy.Field()
    team = scrapy.Field()
    advisors = scrapy.Field()
    advisor = scrapy.Field()

class PersonItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    position = scrapy.Field()
    links = scrapy.Field()
    source_page_url = scrapy.Field()
