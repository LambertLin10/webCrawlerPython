#coding=utf-8
'''
Created on 2016年6月29日

@author: Lambert
'''
#import requests
#res = requests.get("https://www.douban.com/")
#print res.text


#from bs4 import BeautifulSoup
"""
html_sample = \
<html> \
  <body> \
    <h1 id = "title">hello</h1>
    <a href = "#" class = "link">This is link</a>
    <a href = "##" class = "link2" >This is link2</a>
  </body>
</html>
"""
#soup = BeautifulSoup(html_sample)
#print soup.text
#print soup.contents
#print soup.select('.link')


from bs4 import BeautifulSoup
import requests


res = requests.get('https://www.douban.com/')
soup = BeautifulSoup(res.text)
for li in soup.select('#anony-nav')[0].select('.anony-nav-links')[0].select('li'):
    print li.select('a')[0].text
    