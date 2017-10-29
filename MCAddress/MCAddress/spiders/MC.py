# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
from MCAddress.items import McaddressItem
class McSpider(scrapy.Spider):
    name = "MC"
    allowed_domains = ["www.4008517517.net/"]
    start_urls = ['http://www.4008517517.net/']
    url="http://www.4008517517.net/maidanglao/fendian/mdl5471.html"
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':'safedog-flow-item=4BAE0CC95B2F77549179F9A606A0E5E3; AJSTAT_ok_pages=1; AJSTAT_ok_times=2; Hm_lvt_44fe0dd5b9e3bf339d71b9cf97456017=1509252670,1509280318; Hm_lpvt_44fe0dd5b9e3bf339d71b9cf97456017=1509280318',
        'Host':'www.4008517517.net',
        'Pragma':'no-cache',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    def start_requests(self):
        yield Request(url=self.url,callback=self.parse,headers=self.headers,dont_filter=True)

    def parse(self, response):
        count=24
        while count<=228:
            item=McaddressItem()
            xpathStr="/html/body/div[4]/div[1]/div[1]/div[4]/div["+str(count)+"]/text()"
            addr=response.xpath(xpathStr).extract_first()
            addr=addr.split('，')[0]
            addr=re.sub('\d+\、','',addr)
            addr=re.sub('\：','',addr)
            item["address"]=addr.strip()
            yield item
            count+=1

