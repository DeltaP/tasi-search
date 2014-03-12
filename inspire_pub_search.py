#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib, urllib2

n_papers = 5        #max number of papers to return from search (arbitrary)

def scrape_pub(query):
  address   = "http://inspirehep.net/search?ln=en&ln=en&p=find+author%3A%22"+(urllib.quote_plus(query))+"%22&of=hb&action_search=Search&sf=&so=d&rm=&rg=25&sc=0"
  request   = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
  urlfile   = urllib2.urlopen(request)
  page      = urlfile.read()
  soup      = BeautifulSoup(page)
  pub_list  = soup.findAll('a', href=True, text='Detailed record')
  pub_links = ['http://inspirehep.net'+x['href'] for x in pub_list]
  
  return pub_links

def pub_record(pub_link):
  address     = pub_link
  request     = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
  urlfile = urllib2.urlopen(request)
  page        = urlfile.read()
  soup        = BeautifulSoup(page)

  title       = soup.findAll(attrs={"name":"citation_title"})
  author_list = soup.findAll(attrs={"name":"citation_author"})
  authors     = [x['content'].encode('utf-8') for x in author_list]
  date        = soup.findAll(attrs={"name":"citation_publication_date"})

  if (len(title)>0):
    print title[0]['content'].encode('utf-8')
  if (len(authors)>0):
    print authors
  if (len(date)>0):
    print date[0]['content'].encode('utf-8')
  print "\n"
  
if __name__ == '__main__':
  names = open('TASI_1997.csv')
  for name in names:
    print "Searching:  " + name.rstrip()
    print"---------------------------------"
    pub_links = scrape_pub(name)
    for li in pub_links[0:n_papers]:
      pub_record(li)
    print "*\t*\t*\t*\t*\n"
