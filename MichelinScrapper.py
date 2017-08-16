# -*- coding: cp949 -*-
from RestaurantInfo import *
import HtmlParser

michelin_guide_url = 'https://guide.michelin.co.kr/ko/restaurant/'

htmlParser = HtmlParser.init(michelin_guide_url)
restCount = len(HtmlParser.findAll(htmlParser, 'article', 'restaurant-list-wrap'))

restInfoList = []

for i in range(0, restCount):
    restInfo = RestaurantInfo()
    restInfo.category = HtmlParser.find(htmlParser, 'span', 'restaurant-list-category').text
    restInfo.title = HtmlParser.find(htmlParser, 'h3', '').text
    restInfo.imgUrl = HtmlParser.find(htmlParser, 'img', '')['src']
##    restInfo.grade = ''
    restInfo.addr = HtmlParser.findAll(htmlParser, 'p', 'ellipsis')[0].text
    restInfo.phone = HtmlParser.findAll(htmlParser, 'p', 'ellipsis')[1].text
    restInfo.homepage = HtmlParser.findAll(htmlParser, 'p', 'ellipsis')[2].text
    
    restInfoList.append(restInfo)
    print i
    print restInfoList[i].printInfo()
    
