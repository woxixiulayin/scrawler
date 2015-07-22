# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class MyScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class Tieba_post_item(Item):
    url_link = Field()
    rep_num = Field()
    title = Field()
    first_time = Field()
    last_time = Field()
    author = Field()
    tags = Field()
    body = Field()