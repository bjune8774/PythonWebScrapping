# -*- coding: cp949 -*-
import urllib2
import bs4

maker = 'bjune.jeong'

def init(url) :
    html = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    print 'URL = ', url
    return soup;

def find(parser, arg1, arg2) :
    if arg2 == '' :
        return parser.find(arg1)
    else :
        return parser.find(arg1, arg2)

def findAll(parser, arg1, arg2) :
    if arg2 == '' :
        return parser.find_all(arg1)
    else :
        return parser.find_all(arg1, arg2)


# Test Code
if __name__ == '__main__':
    print 'Test code from here'
    print maker
    
