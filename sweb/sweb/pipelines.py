# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sweb.items import SwebItem

class SwebPipeline(object):
    def process_item(self, item, spider):
        swebItem = SwebItem()
        swebItem['qqName'] = item['qqName']
        swebItem['qqContent'] = item['qqContent']
        swebItem['qqTime'] = item['qqTime']
        swebItem['qqCount'] = 12
        swebItem.save()
        # item.save()
        return item
