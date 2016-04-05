# -*- coding: utf-8 -*-
import scrapy
from ttest.items import DuitangItem

class DtSpider(scrapy.Spider):
    name = "cbl"
    allowed_domains = ["duitang.com"]
    page = 1
    start_urls = []
    for page in range(1,100):
        start_urls.append("http://www.duitang.com/search/?page=%s&kw=keyword&type=feed" % page)

    def parse(self, response):
        for sel in response.xpath('//a[@class="a"]/img/@src'):
            item = DuitangItem()
            detaillink = sel.extract().replace('.thumb.224_0', '')
            item['image_urls'] = [detaillink]
            yield item