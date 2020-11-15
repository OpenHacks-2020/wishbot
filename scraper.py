# #-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import re

def scrape_link(webpage):
    html_page = urllib2.urlopen(webpage)
    soup = BeautifulSoup(html_page, features='lxml')
    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        if 'listing' in link.get('href'):
            return str(link.get('href'))