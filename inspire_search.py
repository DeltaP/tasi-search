#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib, urllib2

def scrape_table(query):
  address = "http://www.inspirehep.net/search?ln=en&cc=HepNames&ln=en&cc=HepNames&p=find+author+"+(urllib.quote_plus(query))+"&action_search=Search&sf=&so=d&rm=&rg=25&sc=0&of=hd"
  request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
  urlfile = urllib2.urlopen(request)
  page    = urlfile.read()
  soup    = BeautifulSoup(page)
  tables  = soup.findAll('table',cellpadding=5)
  return tables

if __name__ == '__main__':
  names = open('TASI_1997.csv')
  for name in names:
    print "Searching:  " + name.rstrip()
    print"---------------------------------"
    tables = scrape_table(name)
    for table in tables:
      print
      rows = table.findAll('tr')
      for row in rows[2:]:
        cols        = row.findAll('td')
        institution = cols[0].find('a').text
        position    = cols[1].text
        start       = cols[2].text
        end         = cols[3].text
        print institution,position,start,end
    print "*\t*\t*\t*\t*\n"
