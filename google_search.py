#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib, urllib2
import re

class record:
  name        = ""
  instutution = []
  rank        = []
  start       = []
  end         = []

def google_scrape(query):
    address = "http://www.google.com/search?q=%s&num=100&hl=en&start=0" % (urllib.quote_plus(query))
    request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    urlfile = urllib2.urlopen(request)
    page = urlfile.read()
    soup = BeautifulSoup(page)

    linkdictionary = {}

    for li in soup.findAll('li', attrs={'class':'g'}):
        sLink = li.find('a')
        sSpan = li.find('span', attrs={'class':'st'})
        if p.findall(sLink['href']):
          #print sLink['href']
          #print sSpan
          linkdictionary[sLink['href']]=sSpan
    return linkdictionary

if __name__ == '__main__':
  names = open('name_list.csv')

  p = re.compile('.edu')

  for name in names:
    print "Searching:  " + name
    search = name + " physics"
    result = google_scrape(name)
    for key in result:
      print key
      f=urllib.urlopen(key)
      i=f.info()
      #print i.getheader('date')
      print i.getdate('last-modified')
      print i.getheader('last-modified')
