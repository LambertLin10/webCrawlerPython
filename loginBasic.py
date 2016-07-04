#coding=utf-8
'''
Created on 2016年6月29日

@author: Lambert
'''
from bs4 import BeautifulSoup as bs
import requests


headers = {
#貼上firefox顯示的所有header
}
rs = requests.session()
res = rs.get('https://github.com/linyt10/Dramaker',headers = headers)
soup = bs(res.text)
print soup