# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from pymongo import MongoClient
import json


# class UserAgentMiddleware(object):
#     """ 换User-Agent """
#
#     def process_request(self, request, spider):
#         agent = random.choice(agents)
#         request.headers["User-Agent"] = agent
#         request.headers["referer"] = "https://xa.fang.anjuke.com/"


class ProxyMiddleware(object):

    # def __init__(self):
    #     self.clent = MongoClient("localhost", 27017)
    #     db = self.clent['Anjuke']
    #     proxyTable = db['ProxyAll']
    #     collection = proxyTable.find()
    #     self.proxyList = []
    #     for proxy in collection:
    #         self.proxyList.append(proxy)

    def process_request(self, request, spider):
        clent = MongoClient("localhost", 27017)
        db = clent['Anjuke']
        proxyTable = db['ProxyAll']
        collection = proxyTable.find()
        proxyList = []
        for proxy in collection:
            proxyList.append(proxy)

        request.headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
        request.headers["referer"] = "https://www.xicidaili.com"
        request.headers['Host'] = 'www.xicidaili.com'
        proxy = random.choice(proxyList)
        ipProxy = str.lower(str(proxy['type'])) + "://" + str(proxy["host"]) + ":" + str(proxy["port"])
        print(u"当前使用的IP为： " + ipProxy)
        request.meta["proxy"] = ipProxy
    #
    # def close_spider(self, spider):
    #     self.clent.close()
