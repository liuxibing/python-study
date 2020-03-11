# -*- coding: utf-8 -*-

"""
自动访问www.ainoob.cn的最近文章

Author: ainoob.cn
Email: 535334234@qq.com
"""

from selenium import webdriver
import time

# 设置浏览器模拟选项
options = webdriver.ChromeOptions()
# 模拟User Agent
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"')
# 使用无界面浏览器
options.add_argument('--headless')
# 禁止使用gpu
# options.add_argument('--disable-gpu')
# 禁止图片加载
options.add_argument('--disable-images')

# Chromedriver的执行路径
drive_path = 'D:\Workspaces\chromedriver\chromedriver.exe'
# 打开浏览器
browser = webdriver.Chrome(executable_path=drive_path, chrome_options =options)
url = 'http://www.ainoob.cn'
# 打开浏览器预设网址
browser.get(url)  
time.sleep(10)
last_link = browser.find_element_by_xpath('//div[@class="widget widget_recent_entries"]/ul/li[1]/a')
print(last_link.get_attribute('href'))
browser.get(last_link.get_attribute('href'))

for _ in range(100):
    time.sleep(10)
    prev_link = browser.find_element_by_xpath('//span[@class="article-nav-prev"]/a') 
    print(prev_link.get_attribute('href'))
    browser.get(prev_link.get_attribute('href'))

# 关闭浏览器
time.sleep(10)
browser.close() 


