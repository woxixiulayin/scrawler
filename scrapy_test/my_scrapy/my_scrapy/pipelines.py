# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from mongoengine import *  

class Tieba_post_doc(Document):
    url_link = StringField(max_length=300, required=True)  
    rep_num = StringField(max_length=10, required=True)  
    title = StringField(max_length=100, required=True)  
    first_time = StringField(max_length=20, required=True)  
    last_time = StringField(max_length=20, required=True)  
    author = StringField(max_length=30, required=True)  
    # tags = Field()
    body = StringField(required=True)  

def item2doc(item):
	doc = Tieba_post_doc()
	# doc['url_link'] = item.url_link
	# doc['title'] = item.title 
	for (k, v) in item.items():
		doc[k] = item[k]

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = codecs.open('items.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
    	d_item = dict(item)
    	doc = item2doc(item)
        line = json.dumps(d_item) + "\n"
        self.file.write(line.decode('unicode_escape'))
        return item