# -*- coding: utf-8 -*-

"""
Selenium使用示例

Author: ainoob.cn
Email: 535334234@qq.com
"""

from selenium import webdriver
import time
from lxml import etree

# 定义全局变量
_url = 'https://www.baidu.com/s?wd=AI%E6%95%99%E7%A8%8B&ie=UTF-8'

def open_browser(browser_type = 'Chrome'):
    """
    设置模拟浏览器选项，并打开浏览器。
    """

    # Chromedriver的执行路径
    drive_path = 'D:\Workspaces\chromedriver\chromedriver.exe'

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
    
    # 默认打开浏览器（需要把Chromedriver的执行路径加入到了环境变量的Path中）
    # browser = webdriver.Chrome()
    # 打开默认浏览器
    # browser = webdriver.Chrome(executable_path=drive_path)
    # 使用模拟选项打开浏览器
    browser = webdriver.Chrome(executable_path=drive_path, chrome_options =options)
    
    return browser

def close_browser(browser):
    """
    关闭浏览器
    """

    browser.close() 
    browser = None

def get_page(browser, url=''):
    """
    通过模拟浏览器打开网页Url，取出网页Page内容源码。

    browser.page_source是获取网页的全部html
    
    """

    url = _url if url=='' else url
    # print(browser, url)

    # 等待十秒加载不出来就会抛出异常，10秒内加载出来正常返回
    # browser.implicitly_wait(10)
    # 打开指定URL
    browser.get(url) 

    # 获取网页信息
    print('Url=', browser.current_url)
    print('Title=', browser.title )
    print('Cookies=', browser.get_cookies() )
    
    # 获取网页源代码
    page_html = browser.page_source
    return page_html

def parse_page(page_html, content='keywords'):
    """
    通过Xpath解析并获取页面内容
    """

    try:
        page = etree.HTML(page_html)
        keywords = page.xpath('//div[@id="rs"]//th/a/text()')
        print(keywords)
        return keywords
    except:
        print('页面解析错误')
        return None

def save_page(page_content):
    """
    保持页面内容
    """

def find_element(browser, url=''):
    """
    打开指定url页面，查找页面中的元素。
    常用查找方法：
        browser.find_element_by_name()
        browser.find_element_by_xpath()
        browser.find_element_by_css_selector()
        browser.find_element_by_link_text()
        browser.find_element_by_partial_link_text()
        browser.find_element_by_tag_name()
        browser.find_element_by_class_name()   
    元素的常用方法：
        element.get_attribute() 
        element.send_key()
    """
    url = _url if url=='' else url
    browser.get(url)

    e_link = browser.find_element_by_link_text('资讯')
    print('Link Tag: ', e_link.tag_name )
    print('Link Url: ', e_link.get_attribute('href') )
    print('Link Name: ', e_link.text )

    e_input = browser.find_element_by_name('wd')
    print('Input Id: ',e_input.get_attribute('id'))
    print('Input Name: ',e_input.get_attribute('name'))
    print('Input Text: ',e_input.text)
    

if __name__ == "__main__":
    browser = open_browser()
    
    # page_html = get_page(browser)
    # keywords = parse_page(page_html, 'keywords')

    find_element(browser)

    close_browser(browser)