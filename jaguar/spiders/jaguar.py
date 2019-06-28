
import scrapy
from scrapy_splash import SplashRequest
from scrapy.http import Request,FormRequest
import re
import uuid
import hashlib
import logging
import subprocess
import requests
import csv
import io
from scrapy.spiders import Spider
from datetime import datetime
from scrapy.http import Request,FormRequest
import json
from scrapy.http.headers import Headers
import urllib
from collections import OrderedDict
from jaguar.items import JaguarItem

class MySpider(Spider):
    name = 'jaguar'
    start_urls = ["http://approved.me.jaguar.com/en_qa/used/qatar"]
    urls= ['http://approved.me.jaguar.com/en_qa/used/qatar']
        
    
    def start_requests(self):
        for url in self.urls:
            yield SplashRequest(url,callback=self.parse,args={'wait':'5'},endpoint='render.html')

        

    def parse(self, response):
        print("##################")
        links = response.xpath("//div[contains(@class,'results__vehicle column--nopadding small-12 medium-4 large-3 ')]/a//@href").extract()
        links = list(OrderedDict.fromkeys(links))
        print(links)
        for link in links:
            web= "http://approved.me.jaguar.com"+link
            yield SplashRequest(web,callback=self.getdata,endpoint='render.html', args={'wait':'15'},headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})

    def getdata(self,response):
        item=JaguarItem()
        item["Last_Code_Update_Date"] = "Tuesday,June 25,2019"
        item["Scrapping_Date"] = datetime.today().strftime('%A, %B %d, %Y')
        item["Country"] = "Qatar"
        
        item["Seller_Type"] = "Large Independent Dealers"
        item["Seller_Name"] = "Alfardan Premier Motors"
        item["Car_URL"] = response.url
        name = response.xpath("//hgroup/h1[contains(@class,'section-title')]/text()").get().split()[0]
        arr = response.xpath("//tr/td/text()").extract()
        item["City"] = arr[8]
        item["Car_Name"] = "Jaguar"+ ' ' + name
        item["Year"] = arr[0]
        item["Make"] = "Jaguar"
        item["model"] = name
        item["transmission"] = arr[4]
        item["bodystyle"] = arr[5]
        item["colour_exterior"] = arr[1]
        item["colour_interior"] = arr[2]
        item["fuel_type"] = arr[7]
        item["mileage"] = arr[3].split('Km')[0]
        item['Price_Currency'] = 'QAR'
        item['asking_price_inc_VAT'] = response.xpath("//strong[contains(@class,'price-box')]/text()").get().split('QAR')[-1].strip()
        yield item



