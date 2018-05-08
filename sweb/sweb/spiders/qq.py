# -*- coding: utf-8 -*-
import scrapy
from sweb.items import SwebItem

class QqSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['wxn.qq.com']
    start_urls = ['http://roll.finance.sina.com.cn/finance/zq1/gsjsy/index.shtml']

    def parse(self, response):
        for sel in response.xpath('//ul[@class="list_009"]/li'):
            s = SwebItem()
            t = sel.xpath('a/text()').extract()
            qt = sel.xpath('span/text()').extract()
            qn = sel.xpath('a/@href').extract()

            for title in t:
                s['qqContent'] = title.encode('utf-8')
            for qqTime in qt:
                s['qqTime'] = qqTime.encode('utf-8')
            for qqName in qn:
                s['qqName'] = qqName.encode('utf-8')
            yield s

