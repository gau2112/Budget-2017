#Created By Gautam 2017-01-20 at 10:40:54
#This is a Testing Python Script
#Lets See What Happens


import urllib2
import urllib
import sys
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

try:
    url = "http://www.firstpost.com/budget-2017/"
    req = urllib.urlopen(url).read()
    soup = BeautifulSoup(req)
    div = soup.find('section',class_='trending section')
    cat = div.find('ul',class_='column three photo-news aspect-fix no-border').findAll('li')
    #print cat
    for k in cat:
            #print type(k),type(cat)
        #continue
        #print k
        #if k is None:
            #continue
        #try:
            cat_title = k.find('span',class_='cat-title')
            featured_news = k.find('div',class_='column-featured')
            other_news = k.find('div',class_='other-news')
            if cat_title != None:
             print '\n\n',cat_title.text


            if featured_news is None:
                "can dp"
            else:
                featured_news = featured_news.findAll('a')
                for l in featured_news:
                    print l.text
            
            
            if other_news is None:
                "can't do"
            else:
                other_news=other_news.findAll('a')
                for v in other_news:
                    print v.text
except:
    print 'Too Many Requests'
                    
        #except:
            #print k
        #print other_news.findAll('a')
            #break
    #except:
        #print 'Issues'

