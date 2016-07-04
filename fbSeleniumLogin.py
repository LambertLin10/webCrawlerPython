#coding=utf-8
'''
Created on 2016年6月30日

@author: Lambert
'''
from bs4 import BeautifulSoup
from selenium import webdriver


browser = webdriver.Firefox()

browser.get('https://zh-tw.facebook.com/login/')
browser.find_element_by_id("email").send_keys("youremail")
browser.find_element_by_id("pass").send_keys("yourpassword")
browser.find_element_by_id("loginbutton").click()
browser.find_element_by_css_selector("a._2s25 > span").click()
soup = BeautifulSoup(browser.page_source)
browser.get(soup.select('._2s25')[0]['href'] + "&sk=about")
soup = BeautifulSoup(browser.page_source)
print soup.select('._c24._50f3')[2].select('div')[1].text
browser.close()