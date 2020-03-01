# -*- coding: utf-8 -*-

"""
Selenium使用示例

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
options.add_argument('--disable-gpu')
# 禁止图片加载
options.add_argument('--disable-images')

# Chromedriver的执行路径
drive_path = 'D:\Workspaces\chromedriver\chromedriver.exe'
# 使用模拟选项打开浏览器
# browser = webdriver.Chrome(executable_path=drive_path, chrome_options =options)
# 打开浏览器
browser = webdriver.Chrome(executable_path=drive_path)
# 如果把Chromedriver的执行路径加入到了环境变量的Path中，打开浏览器时可以不指定执行路径
# browser = webdriver.Chrome()
url = 'https://www.baidu.com'
# 打开浏览器预设网址
browser.get(url)   
# 获取网页源代码
page_html = browser.page_source
# 关闭浏览器
time.sleep(10)
browser.close() 
