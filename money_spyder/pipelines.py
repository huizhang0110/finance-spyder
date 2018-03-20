# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class JsonPipeline:

    def __init__(self):
        self.fo = open('article.json', 'w')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.fo.write(lines)
        return item


class MoneySpyderPipeline(object):
    def process_item(self, item, spider):
        return item
