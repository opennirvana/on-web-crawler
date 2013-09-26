import urllib2
from bs4 import BeautifulSoup

fish_url = 'http://www.opennirvana.com'

links = []

def get_data(url):
   if fish_url not in url:
      url = fish_url + url
   page = urllib2.urlopen(url)
   html_doc = page.read()
   soup = BeautifulSoup(html_doc)
   return soup

def get_link(url):
   page = urllib2.urlopen(url)
   html_doc = page.read()
   soup = BeautifulSoup(html_doc)
   urllinks = []
   for link in soup.find_all('a'):
      links = link.get('href')
      links = str(links)
      if links.startswith('/') or fish_url in links:
         urllinks.append(links)
   return urllinks

links = get_link(fish_url)

for r in links:
   soup = get_data(r)
   for link in soup.find_all('a'):
      urllink = link.get('href')
      urllink = str(urllink)
      if urllink.startswith('/') or fish_url in links and urllink not in links:
         links.append(urllink)

for w in links:
   print (w)
