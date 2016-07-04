#coding=utf-8
'''
Created on 2016年6月29日

@author: Lambert
'''
import requests


payload ={
'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
'EndStation':'3301e395-46b8-47aa-aa37-139e15708779',
'SearchDate':'2016/06/29',
'SearchTime':'12:00',
'SearchWay':'DepartureInMandarin'          
}
res = requests.post('https://www.thsrc.com.tw/tw/TimeTable/SearchResult',data = payload)
print res.text