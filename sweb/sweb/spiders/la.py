# -*- coding: utf-8 -*-
import scrapy
# from sweb.items import SwebItem
from sweb.items import SwebItem
class LaSpider(scrapy.Spider):
    name = 'la'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://news.baidu.com']

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            swebItem = SwebItem()
            laTitle = sel.xpath('a/text()').extract()
            laPosition = sel.xpath('text()').extract()
            laType = sel.xpath('a/@href').extract()
            # swebItem['laTitle'] = laTitle
            # swebItem['laPosition'] = laPosition
            # swebItem['laType'] = laType
            for t in laTitle:
                swebItem['laTitle'] = t.encode('utf-8')
            for t in laPosition:
                swebItem['laPosition'] = t.encode('utf-8')
            for t in laType:
                swebItem['laType'] = t.encode('utf-8')
            yield swebItem